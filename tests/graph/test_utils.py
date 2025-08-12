from datetime import datetime
from typing import Any, Dict, Optional

import pytest

from zep_cloud import EntityEdge, EntityNode, Episode
from zep_cloud.graph.utils import compose_context_string, format_edge_date_range


class TestFormatEdgeDateRange:
    def test_format_edge_date_range_with_valid_dates(self):
        edge = EntityEdge(
            fact="Test fact",
            name="test_edge",
            uuid_="edge-123",
            created_at="2024-01-01T09:00:00Z",
            source_node_uuid="source-123",
            target_node_uuid="target-123",
            valid_at="2024-01-01T10:00:00Z",
            invalid_at="2024-01-02T10:00:00Z"
        )
        result = format_edge_date_range(edge)
        assert result == "2024-01-01 10:00:00 - 2024-01-02 10:00:00"

    def test_format_edge_date_range_with_none_dates(self):
        edge = EntityEdge(
            fact="Test fact",
            name="test_edge", 
            uuid_="edge-123",
            created_at="2024-01-01T09:00:00Z",
            source_node_uuid="source-123",
            target_node_uuid="target-123",
            valid_at=None, 
            invalid_at=None
        )
        result = format_edge_date_range(edge)
        assert result == "date unknown - present"

    def test_format_edge_date_range_with_partial_dates(self):
        edge = EntityEdge(
            fact="Test fact",
            name="test_edge",
            uuid_="edge-123",
            created_at="2024-01-01T09:00:00Z",
            source_node_uuid="source-123",
            target_node_uuid="target-123",
            valid_at="2024-01-01T10:00:00Z",
            invalid_at=None
        )
        result = format_edge_date_range(edge)
        assert result == "2024-01-01 10:00:00 - present"


class TestComposeContextString:
    def test_empty_inputs(self):
        result = compose_context_string([], [], [])
        assert "FACTS and ENTITIES represent relevant context" in result
        assert "<FACTS>" in result
        assert "<ENTITIES>" in result
        assert "EPISODES" not in result

    def test_facts_only(self):
        edge = EntityEdge(
            fact="User likes pizza",
            name="likes",
            uuid_="edge-123",
            created_at="2024-01-01T09:00:00Z",
            source_node_uuid="user-123",
            target_node_uuid="pizza-123",
            valid_at="2024-01-01T10:00:00Z",
            invalid_at="2024-01-02T10:00:00Z"
        )
        result = compose_context_string([edge], [], [])
        
        assert "User likes pizza (Date range: 2024-01-01 10:00:00 - 2024-01-02 10:00:00)" in result
        assert "<FACTS>" in result
        assert "<ENTITIES>" in result
        assert "EPISODES" not in result

    def test_entities_basic(self):
        node = EntityNode(
            name="John",
            summary="A user",
            uuid_="node-123",
            created_at="2024-01-01T09:00:00Z"
        )
        result = compose_context_string([], [node], [])
        
        assert "Name: John" in result
        assert "Summary: A user" in result
        assert "<ENTITIES>" in result

    def test_entities_with_label_and_attributes(self):
        node = EntityNode(
            name="John",
            summary="A user",
            uuid_="node-123",
            created_at="2024-01-01T09:00:00Z",
            labels=["Person"],
            attributes={"age": "30", "city": "New York"}
        )
        result = compose_context_string([], [node], [])
        
        assert "Name: John" in result
        assert "Label: Person" in result
        assert "Attributes:" in result
        assert "age: 30" in result
        assert "city: New York" in result
        assert "Summary: A user" in result

    def test_entities_with_entity_label_removed(self):
        node = EntityNode(
            name="Alice",
            summary="A customer",
            uuid_="node-456",
            created_at="2024-01-01T09:00:00Z",
            labels=["Entity", "Customer"]
        )
        result = compose_context_string([], [node], [])
        
        assert "Name: Alice" in result
        assert "Label: Customer" in result  # Should show Customer, not Entity
        assert "Label: Entity" not in result  # Should not show Entity
        assert "Summary: A customer" in result

    def test_entities_with_only_entity_label(self):
        node = EntityNode(
            name="Bob",
            summary="A person",
            uuid_="node-789",
            created_at="2024-01-01T09:00:00Z",
            labels=["Entity"]
        )
        result = compose_context_string([], [node], [])
        
        assert "Name: Bob" in result
        # Check that the entities section doesn't contain "Label: " (with space after colon)
        entities_section = result[result.find("<ENTITIES>"):result.find("</ENTITIES>")]
        assert "Label: " not in entities_section  # Should not show any label since only Entity was present
        assert "Summary: A person" in result

    def test_entities_with_labels_attribute_filtered(self):
        node = EntityNode(
            name="stores",
            summary="Physical locations for shopping",
            uuid_="node-123",
            created_at="2024-01-01T09:00:00Z",
            labels=["Location", "Entity"],
            attributes={"labels": ["Location", "Entity"], "location_type": "physical"}
        )
        result = compose_context_string([], [node], [])
        
        assert "Name: stores" in result
        assert "Label: Location" in result  # Should show Location (first non-Entity label)
        assert "Attributes:" in result
        assert "location_type: physical" in result
        assert "labels:" not in result  # Should not show labels in attributes
        assert "Summary: Physical locations for shopping" in result

    def test_episodes_basic(self):
        episode = Episode(
            content="Hello there!",
            created_at="2024-01-01T10:00:00Z",
            uuid_="episode-123"
        )
        result = compose_context_string([], [], [episode])
        
        assert "FACTS and ENTITIES, and EPISODES represent" in result
        assert "<EPISODES>" in result
        assert "Hello there! (2024-01-01 10:00:00)" in result

    def test_episodes_with_role(self):
        episode = Episode(
            content="Hello there!",
            created_at="2024-01-01T10:00:00Z",
            uuid_="episode-123",
            role="user"
        )
        result = compose_context_string([], [], [episode])
        
        assert "user: Hello there! (2024-01-01 10:00:00)" in result

    def test_episodes_with_role_and_type(self):
        # Create a mock episode with role_type since Episode model uses enum
        class MockEpisode:
            def __init__(self):
                self.content = "Hello there!"
                self.created_at = "2024-01-01T10:00:00Z"
                self.role = "assistant"
                self.role_type = "ai"
                self.provided_created_at = None
        
        episode = MockEpisode()
        result = compose_context_string([], [], [episode])
        
        assert "assistant (ai): Hello there! (2024-01-01 10:00:00)" in result

    def test_episodes_with_role_type_only(self):
        class MockEpisode:
            def __init__(self):
                self.content = "Hello there!"
                self.created_at = "2024-01-01T10:00:00Z"
                self.role = None
                self.role_type = "system"
                self.provided_created_at = None
        
        episode = MockEpisode()
        result = compose_context_string([], [], [episode])
        
        assert "(system): Hello there! (2024-01-01 10:00:00)" in result

    def test_episodes_with_provided_created_at(self):
        class MockEpisode:
            def __init__(self):
                self.content = "Hello there!"
                self.created_at = "2024-01-01T10:00:00Z"
                self.role = "user"
                self.role_type = None
                self.provided_created_at = "2024-01-02T15:30:00Z"
        
        episode = MockEpisode()
        result = compose_context_string([], [], [episode])
        
        assert "user: Hello there! (2024-01-02 15:30:00)" in result

    def test_complete_context_with_all_elements(self):
        edge = EntityEdge(
            fact="User prefers coffee",
            name="prefers",
            uuid_="edge-123",
            created_at="2024-01-01T07:00:00Z",
            source_node_uuid="user-123",
            target_node_uuid="coffee-123",
            valid_at="2024-01-01T08:00:00Z",
            invalid_at=None
        )
        
        node = EntityNode(
            name="Alice",
            summary="Regular customer",
            uuid_="node-123",
            created_at="2024-01-01T07:00:00Z",
            labels=["Customer"],
            attributes={"tier": "gold", "visits": "25"}
        )
        
        class MockEpisode:
            def __init__(self):
                self.content = "I'd like my usual coffee"
                self.created_at = "2024-01-01T09:00:00Z"
                self.role = "user"
                self.role_type = "customer"
                self.provided_created_at = None
        
        episode = MockEpisode()
        
        result = compose_context_string([edge], [node], [episode])
        
        # Check for all sections
        assert "FACTS and ENTITIES, and EPISODES represent" in result
        assert "<FACTS>" in result
        assert "<ENTITIES>" in result
        assert "<EPISODES>" in result
        
        # Check content
        assert "User prefers coffee" in result
        assert "Name: Alice" in result
        assert "tier: gold" in result
        assert "Summary: Regular customer" in result
        assert "user (customer): I'd like my usual coffee" in result

    def test_multiple_items(self):
        edges = [
            EntityEdge(
                fact="Fact 1",
                name="edge1",
                uuid_="edge-1",
                created_at="2024-01-01T09:00:00Z",
                source_node_uuid="source-1",
                target_node_uuid="target-1",
                valid_at="2024-01-01T10:00:00Z"
            ),
            EntityEdge(
                fact="Fact 2",
                name="edge2", 
                uuid_="edge-2",
                created_at="2024-01-02T09:00:00Z",
                source_node_uuid="source-2",
                target_node_uuid="target-2",
                valid_at="2024-01-02T10:00:00Z"
            )
        ]
        
        nodes = [
            EntityNode(
                name="Node1",
                summary="Summary 1",
                uuid_="node-1",
                created_at="2024-01-01T09:00:00Z"
            ),
            EntityNode(
                name="Node2",
                summary="Summary 2",
                uuid_="node-2", 
                created_at="2024-01-01T09:00:00Z"
            )
        ]
        
        episodes = [
            Episode(
                content="Message 1",
                created_at="2024-01-01T10:00:00Z",
                uuid_="episode-1"
            ),
            Episode(
                content="Message 2",
                created_at="2024-01-01T11:00:00Z",
                uuid_="episode-2"
            )
        ]
        
        result = compose_context_string(edges, nodes, episodes)
        
        assert "Fact 1" in result
        assert "Fact 2" in result
        assert "Node1" in result
        assert "Node2" in result
        assert "Message 1" in result
        assert "Message 2" in result