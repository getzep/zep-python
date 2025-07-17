from datetime import datetime
from typing import List

from zep_cloud import EntityEdge, EntityNode

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

TEMPLATE_STRING = """
FACTS and ENTITIES represent relevant context to the current conversation.

# These are the most relevant facts and their valid date ranges
# format: FACT (Date range: from - to)
<FACTS>
%s
</FACTS>

# These are the most relevant entities
# ENTITY_NAME: entity summary
<ENTITIES>
%s
</ENTITIES>
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
        valid_at = datetime.fromisoformat(edge.valid_at).strftime(DATE_FORMAT)
    if edge.invalid_at is not None:
        invalid_at = datetime.fromisoformat(edge.invalid_at).strftime(DATE_FORMAT)

    return f"{valid_at} - {invalid_at}"


def compose_context_string(edges: List[EntityEdge], nodes: List[EntityNode]) -> str:
    """
    Compose a search context from entity edges and nodes.
    
    Args:
        edges: List of entity edges.
        nodes: List of entity nodes.
        
    Returns:
        A formatted string containing facts and entities.
    """
    facts = []
    for edge in edges:
        fact = f"  - {edge.fact} ({format_edge_date_range(edge)})"
        facts.append(fact)

    entities = []
    for node in nodes:
        entity = f"  - {node.name}: {node.summary}"
        entities.append(entity)

    facts_str = "\n".join(facts)
    entities_str = "\n".join(entities)

    return TEMPLATE_STRING % (facts_str, entities_str)