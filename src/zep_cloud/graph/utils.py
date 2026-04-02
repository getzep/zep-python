from datetime import datetime
from typing import List, Optional

from dateutil import parser as dateutil_parser
from zep_cloud import EntityEdge, EntityNode, Episode

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def parse_iso_datetime(iso_string: str) -> Optional[datetime]:
    """Parse ISO datetime string using dateutil parser."""
    if not iso_string:
        return None
    
    try:
        return dateutil_parser.isoparse(iso_string)
    except (ValueError, TypeError):
        return None

TEMPLATE_STRING = """
FACTS and ENTITIES{episodes_header} represent relevant context to the current conversation.

# These are the most relevant facts and their valid date ranges
# format: FACT (Date range: from - to)
<FACTS>
{facts}
</FACTS>

# These are the most relevant entities
# Name: ENTITY_NAME
# Label: entity_label (if present)
# Attributes: (if present)
#   attr_name: attr_value
# Summary: entity summary
<ENTITIES>
{entities}
</ENTITIES>
{episodes_section}
"""


def format_edge_date_range(edge: EntityEdge) -> str:
    """
    Format the date range of an entity edge.
    
    Args:
        edge: The entity edge to format.
        
    Returns:
        A string representation of the date range.
    """
    valid_at = "date unknown"
    invalid_at = "present"

    if edge.valid_at is not None:
        parsed_valid_at = parse_iso_datetime(edge.valid_at)
        if parsed_valid_at is not None:
            valid_at = parsed_valid_at.strftime(DATE_FORMAT)
    if edge.invalid_at is not None:
        parsed_invalid_at = parse_iso_datetime(edge.invalid_at)
        if parsed_invalid_at is not None:
            invalid_at = parsed_invalid_at.strftime(DATE_FORMAT)

    return f"{valid_at} - {invalid_at}"


def compose_context_string(edges: List[EntityEdge], nodes: List[EntityNode], episodes: List[Episode]) -> str:
    """
    Compose a search context from entity edges, nodes, and episodes.
    
    Args:
        edges: List of entity edges.
        nodes: List of entity nodes.
        episodes: List of episodes.
        
    Returns:
        A formatted string containing facts, entities, and episodes.
    """
    facts = []
    for edge in edges:
        fact = f"  - {edge.fact} (Date range: {format_edge_date_range(edge)})"
        facts.append(fact)

    entities = []
    for node in nodes:
        entity_parts = [f"Name: {node.name}"]
        
        if hasattr(node, 'labels') and node.labels:
            labels = list(node.labels)  # Create a copy to avoid modifying original
            if 'Entity' in labels:
                labels.remove('Entity')
            if labels:  # Only add label if there are remaining labels after removing 'Entity'
                entity_parts.append(f"Label: {labels[0]}")
        
        if hasattr(node, 'attributes') and node.attributes:
            # Filter out 'labels' from attributes as it's redundant with the Label field
            filtered_attributes = {k: v for k, v in node.attributes.items() if k != 'labels'}
            if filtered_attributes:  # Only add attributes section if there are non-label attributes
                entity_parts.append("Attributes:")
                for attr_name, attr_value in filtered_attributes.items():
                    entity_parts.append(f"  {attr_name}: {attr_value}")
        
        if node.summary:
            entity_parts.append(f"Summary: {node.summary}")
        
        entity = "\n".join(entity_parts)
        entities.append(entity)

    # Format episodes
    episodes_list = []
    if episodes:
        for episode in episodes:
            role_prefix = ""
            if hasattr(episode, 'role') and episode.role:
                if hasattr(episode, 'role_type') and episode.role_type:
                    role_prefix = f"{episode.role} ({episode.role_type}): "
                else:
                    role_prefix = f"{episode.role}: "
            elif hasattr(episode, 'role_type') and episode.role_type:
                role_prefix = f"({episode.role_type}): "

            parsed_timestamp = parse_iso_datetime(episode.created_at)
            timestamp = parsed_timestamp.strftime(DATE_FORMAT) if parsed_timestamp is not None else "date unknown"
            
            episode_str = f"  - {role_prefix}{episode.content} ({timestamp})"
            episodes_list.append(episode_str)

    facts_str = "\n".join(facts) if facts else ""
    entities_str = "\n".join(entities) if entities else ""
    episodes_str = "\n".join(episodes_list) if episodes_list else ""
    
    # Determine if episodes section should be included
    episodes_header = ", and EPISODES" if episodes else ""
    episodes_section = f"\n# These are the most relevant episodes\n<EPISODES>\n{episodes_str}\n</EPISODES>" if episodes else ""
    
    return TEMPLATE_STRING.format(
        episodes_header=episodes_header,
        facts=facts_str,
        entities=entities_str,
        episodes_section=episodes_section
    )