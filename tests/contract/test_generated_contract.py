# This test table comes from spec 3 section 4.2 of the v4 public API specification.
# This file is hand-written and listed in .fernignore.
from __future__ import annotations

import asyncio
import importlib
import importlib.metadata
import inspect
import pkgutil
import re
import types
import typing
import uuid
from enum import Enum

import httpx
import pytest

import zep_cloud
from zep_cloud import AsyncZep, Zep
from zep_cloud.core.pagination import AsyncPager, SyncPager

# Source: spec 3 section 4.2 (endpoint map). Columns: SDK method, HTTP method,
# path, paginated (P), POST read (spec 3 section 2.9).
SECTION_4_2_OPERATIONS: list[tuple[str, str, str, bool, bool]] = [
    ("project.get", "GET", "/project", False, False),
    ("project.update", "PATCH", "/project", False, False),
    ("project.get_content_policy", "GET", "/project/content-policy", False, False),
    ("project.set_content_policy", "PUT", "/project/content-policy", False, False),
    ("project.list_content_policy_revisions", "GET", "/project/content-policy/revisions", True, False),
    ("project.get_content_policy_revision", "GET", "/project/content-policy/revisions/{revision_uuid}", False, False),
    ("project.get_instructions", "GET", "/project/instructions", False, False),
    ("project.set_instructions", "PUT", "/project/instructions", False, False),
    ("project.get_observation_steering", "GET", "/project/observation-steering", False, False),
    ("project.set_observation_steering", "PUT", "/project/observation-steering", False, False),
    ("project.get_ontology", "GET", "/project/ontology", False, False),
    ("project.set_ontology", "PUT", "/project/ontology", False, False),
    ("project.get_user_summary_instructions", "GET", "/project/user-summary-instructions", False, False),
    ("project.set_user_summary_instructions", "PUT", "/project/user-summary-instructions", False, False),
    ("context.create_template", "POST", "/context-templates", False, False),
    ("context.list_templates", "POST", "/context-templates/list", True, True),
    ("context.delete_template", "DELETE", "/context-templates/{template_uuid}", False, False),
    ("context.get_template", "GET", "/context-templates/{template_uuid}", False, False),
    ("context.update_template", "PUT", "/context-templates/{template_uuid}", False, False),
    ("agent.create", "POST", "/agents", False, False),
    ("agent.list", "POST", "/agents/list", True, True),
    ("agent.delete", "DELETE", "/agents/{agent_uuid}", False, False),
    ("agent.get", "GET", "/agents/{agent_uuid}", False, False),
    ("agent.update", "PATCH", "/agents/{agent_uuid}", False, False),
    ("agent.declare_breaking_change", "POST", "/agents/{agent_uuid}/breaking-changes", False, False),
    ("agent.get_context", "POST", "/agents/{agent_uuid}/context", False, True),
    ("agent.split.plan", "POST", "/agents/{agent_uuid}/split-plan", False, False),
    ("agent.literal_policy.get", "GET", "/agents/{agent_uuid}/literal-policy", False, False),
    ("agent.literal_policy.update", "PUT", "/agents/{agent_uuid}/literal-policy", False, False),
    ("agent.skill.candidate.list", "GET", "/agents/{agent_uuid}/skill-candidates", True, False),
    ("agent.skill.candidate.get", "GET", "/agents/{agent_uuid}/skill-candidates/{review_uuid}", False, False),
    (
        "agent.skill.evaluation.create_for_candidate",
        "POST",
        "/agents/{agent_uuid}/skill-candidates/{review_uuid}/candidates/{candidate_uuid}/evaluations",
        False,
        False,
    ),
    ("agent.learning.get", "GET", "/agents/{agent_uuid}/learning", True, False),
    ("agent.learning.list_runs", "GET", "/agents/{agent_uuid}/learning-runs", True, False),
    ("agent.skill.create", "POST", "/agents/{agent_uuid}/skills", False, False),
    ("agent.skill.import_package", "POST", "/agents/{agent_uuid}/skills/import", False, False),
    ("agent.skill.list", "POST", "/agents/{agent_uuid}/skills/list", True, True),
    ("agent.skill.search", "POST", "/agents/{agent_uuid}/skills/search", True, True),
    ("agent.skill.get", "GET", "/agents/{agent_uuid}/skills/{skill_uuid}", False, False),
    ("agent.skill.publication.get", "GET", "/agents/{agent_uuid}/skills/{skill_uuid}/publication", False, False),
    ("agent.skill.publication.lookup", "GET", "/agents/{agent_uuid}/skill-publications", False, False),
    ("agent.skill.use.create", "POST", "/agents/{agent_uuid}/skills/{skill_uuid}/uses", False, False),
    (
        "agent.skill.use.add_outcome",
        "POST",
        "/agents/{agent_uuid}/skills/{skill_uuid}/uses/{use_uuid}/outcome",
        False,
        False,
    ),
    ("agent.skill.approve", "POST", "/agents/{agent_uuid}/skills/{skill_uuid}/approve", False, False),
    ("agent.skill.evaluation.create", "POST", "/agents/{agent_uuid}/skills/{skill_uuid}/evaluations", False, False),
    ("agent.skill.evidence.list", "GET", "/agents/{agent_uuid}/skills/{skill_uuid}/evidence", True, False),
    ("agent.skill.relation.list", "GET", "/agents/{agent_uuid}/skills/{skill_uuid}/relations", True, False),
    (
        "agent.skill.version.restore_version",
        "POST",
        "/agents/{agent_uuid}/skills/{skill_uuid}/restore-version",
        False,
        False,
    ),
    ("agent.skill.retire", "POST", "/agents/{agent_uuid}/skills/{skill_uuid}/retire", False, False),
    ("agent.skill.version.list", "GET", "/agents/{agent_uuid}/skills/{skill_uuid}/versions", True, False),
    ("agent.skill.create_version", "POST", "/agents/{agent_uuid}/skills/{skill_uuid}/versions", False, False),
    ("agent.skill.version.compare", "POST", "/agents/{agent_uuid}/skills/{skill_uuid}/versions/compare", False, True),
    ("agent.skill.version.get", "GET", "/agents/{agent_uuid}/skills/{skill_uuid}/versions/{version}", False, False),
    (
        "agent.skill.export.create",
        "POST",
        "/agents/{agent_uuid}/skills/{skill_uuid}/versions/{version}/export",
        False,
        False,
    ),
    (
        "agent.skill.export.get",
        "GET",
        "/agents/{agent_uuid}/skills/{skill_uuid}/versions/{version}/export/{task_uuid}",
        False,
        False,
    ),
    ("agent.trajectory.create", "POST", "/agents/{agent_uuid}/trajectories", False, False),
    ("agent.trajectory.list", "POST", "/agents/{agent_uuid}/trajectories/list", True, True),
    ("agent.trajectory.get", "GET", "/agents/{agent_uuid}/trajectories/{trajectory_uuid}", False, False),
    ("agent.trajectory.update", "PATCH", "/agents/{agent_uuid}/trajectories/{trajectory_uuid}", False, False),
    ("agent.trajectory.delete", "DELETE", "/agents/{agent_uuid}/trajectories/{trajectory_uuid}", False, False),
    ("agent.trajectory.abandon", "POST", "/agents/{agent_uuid}/trajectories/{trajectory_uuid}/abandon", False, False),
    ("agent.trajectory.close", "POST", "/agents/{agent_uuid}/trajectories/{trajectory_uuid}/close", False, False),
    (
        "agent.trajectory.correct_task_family",
        "POST",
        "/agents/{agent_uuid}/trajectories/{trajectory_uuid}/correct-task-family",
        False,
        False,
    ),
    ("agent.trajectory.list_events", "GET", "/agents/{agent_uuid}/trajectories/{trajectory_uuid}/events", True, False),
    (
        "agent.trajectory.append_event",
        "POST",
        "/agents/{agent_uuid}/trajectories/{trajectory_uuid}/events",
        False,
        False,
    ),
    (
        "agent.trajectory.delete_event",
        "DELETE",
        "/agents/{agent_uuid}/trajectories/{trajectory_uuid}/events/{event_uuid}",
        False,
        False,
    ),
    ("agent.trajectory.reopen", "POST", "/agents/{agent_uuid}/trajectories/{trajectory_uuid}/reopen", False, False),
    (
        "agent.trajectory.get_summary",
        "GET",
        "/agents/{agent_uuid}/trajectories/{trajectory_uuid}/summary",
        False,
        False,
    ),
    (
        "agent.trajectory.list_summary_versions",
        "GET",
        "/agents/{agent_uuid}/trajectories/{trajectory_uuid}/summary/versions",
        True,
        False,
    ),
    ("agent.verifier.list", "POST", "/agents/{agent_uuid}/verifiers/list", True, True),
    ("agent.verifier.get", "GET", "/agents/{agent_uuid}/verifiers/{verifier_uuid}", False, False),
    ("agent.verifier.update", "PATCH", "/agents/{agent_uuid}/verifiers/{verifier_uuid}", False, False),
    (
        "agent.verifier.invalidate_evidence",
        "POST",
        "/agents/{agent_uuid}/verifiers/{verifier_uuid}/invalidate-evidence",
        False,
        False,
    ),
    ("agent.verifier.revoke", "POST", "/agents/{agent_uuid}/verifiers/{verifier_uuid}/revoke", False, False),
    ("user.create", "POST", "/users", False, False),
    ("user.list", "POST", "/users/list", True, True),
    ("user.lookup", "POST", "/users/lookup", False, True),
    ("user.delete", "DELETE", "/users/{user_uuid}", False, False),
    ("user.get", "GET", "/users/{user_uuid}", False, False),
    ("user.update", "PATCH", "/users/{user_uuid}", False, False),
    ("user.get_node", "GET", "/users/{user_uuid}/node", False, False),
    ("user.get_summary_instructions", "GET", "/users/{user_uuid}/summary-instructions", False, False),
    ("user.set_summary_instructions", "PUT", "/users/{user_uuid}/summary-instructions", False, False),
    ("user_group.list_for_user", "GET", "/users/{user_uuid}/user-groups", True, False),
    ("thread.list", "GET", "/threads", True, False),
    ("thread.create", "POST", "/threads", False, False),
    ("thread.lookup", "POST", "/threads/lookup", False, True),
    ("thread.delete", "DELETE", "/threads/{thread_uuid}", False, False),
    ("thread.get", "GET", "/threads/{thread_uuid}", False, False),
    ("thread.get_context", "GET", "/threads/{thread_uuid}/context", False, False),
    ("thread.list_episodes", "GET", "/threads/{thread_uuid}/episodes", True, False),
    ("thread.list_messages", "GET", "/threads/{thread_uuid}/messages", True, False),
    ("thread.add_messages", "POST", "/threads/{thread_uuid}/messages", False, False),
    ("thread.message.get", "GET", "/threads/{thread_uuid}/messages/{message_uuid}", False, False),
    ("thread.message.update", "PATCH", "/threads/{thread_uuid}/messages/{message_uuid}", False, False),
    ("thread.get_summary", "GET", "/threads/{thread_uuid}/summary", False, False),
    ("graph.create", "POST", "/graphs", False, False),
    ("graph.list", "POST", "/graphs/list", True, True),
    ("graph.lookup", "POST", "/graphs/lookup", False, True),
    ("graph.delete", "DELETE", "/graphs/{graph_uuid}", False, False),
    ("graph.get", "GET", "/graphs/{graph_uuid}", False, False),
    ("graph.update", "PATCH", "/graphs/{graph_uuid}", False, False),
    ("graph.clone", "POST", "/graphs/{graph_uuid}/clone", False, False),
    ("graph.get_context", "POST", "/graphs/{graph_uuid}/context", False, True),
    ("graph.get_content_policy", "GET", "/graphs/{graph_uuid}/content-policy", False, False),
    ("graph.list_content_policy_events", "POST", "/graphs/{graph_uuid}/content-policy/events/list", True, True),
    ("graph.document_summary.list", "POST", "/graphs/{graph_uuid}/document-summaries/list", True, True),
    ("graph.episode.list_for_document", "GET", "/graphs/{graph_uuid}/documents/{document_id}/episodes", True, False),
    ("graph.edge.add", "POST", "/graphs/{graph_uuid}/edges", False, False),
    ("graph.edge.list", "POST", "/graphs/{graph_uuid}/edges/list", True, True),
    ("graph.edge.delete", "DELETE", "/graphs/{graph_uuid}/edges/{edge_uuid}", False, False),
    ("graph.edge.get", "GET", "/graphs/{graph_uuid}/edges/{edge_uuid}", False, False),
    ("graph.edge.update", "PATCH", "/graphs/{graph_uuid}/edges/{edge_uuid}", False, False),
    ("graph.episode.add", "POST", "/graphs/{graph_uuid}/episodes", False, False),
    ("graph.episode.list", "POST", "/graphs/{graph_uuid}/episodes/list", True, True),
    ("graph.episode.delete", "DELETE", "/graphs/{graph_uuid}/episodes/{episode_uuid}", False, False),
    ("graph.episode.get", "GET", "/graphs/{graph_uuid}/episodes/{episode_uuid}", False, False),
    ("graph.episode.update", "PATCH", "/graphs/{graph_uuid}/episodes/{episode_uuid}", False, False),
    ("graph.hyperedge.add", "POST", "/graphs/{graph_uuid}/hyperedges", False, False),
    ("graph.hyperedge.list", "POST", "/graphs/{graph_uuid}/hyperedges/list", True, True),
    ("graph.hyperedge.delete", "DELETE", "/graphs/{graph_uuid}/hyperedges/{hyperedge_uuid}", False, False),
    ("graph.hyperedge.get", "GET", "/graphs/{graph_uuid}/hyperedges/{hyperedge_uuid}", False, False),
    ("graph.hyperedge.update", "PATCH", "/graphs/{graph_uuid}/hyperedges/{hyperedge_uuid}", False, False),
    ("graph.hyperedge.create_edge", "POST", "/graphs/{graph_uuid}/hyperedges/{hyperedge_uuid}/edges", False, False),
    (
        "graph.hyperedge.delete_edge",
        "DELETE",
        "/graphs/{graph_uuid}/hyperedges/{hyperedge_uuid}/edges/{edge_uuid}",
        False,
        False,
    ),
    ("graph.get_instructions", "GET", "/graphs/{graph_uuid}/instructions", False, False),
    ("graph.set_instructions", "PUT", "/graphs/{graph_uuid}/instructions", False, False),
    ("graph.node.add", "POST", "/graphs/{graph_uuid}/nodes", False, False),
    ("graph.node.list", "POST", "/graphs/{graph_uuid}/nodes/list", True, True),
    ("graph.node.delete", "DELETE", "/graphs/{graph_uuid}/nodes/{node_uuid}", False, False),
    ("graph.node.get", "GET", "/graphs/{graph_uuid}/nodes/{node_uuid}", False, False),
    ("graph.node.update", "PATCH", "/graphs/{graph_uuid}/nodes/{node_uuid}", False, False),
    ("graph.node.list_neighbors", "POST", "/graphs/{graph_uuid}/nodes/{node_uuid}/neighbors", True, True),
    ("graph.get_observation_steering", "GET", "/graphs/{graph_uuid}/observation-steering", False, False),
    ("graph.set_observation_steering", "PUT", "/graphs/{graph_uuid}/observation-steering", False, False),
    ("graph.observation.list", "POST", "/graphs/{graph_uuid}/observations/list", True, True),
    ("graph.observation.get", "GET", "/graphs/{graph_uuid}/observations/{observation_uuid}", False, False),
    ("graph.get_ontology", "GET", "/graphs/{graph_uuid}/ontology", False, False),
    ("graph.set_ontology", "PUT", "/graphs/{graph_uuid}/ontology", False, False),
    ("graph.search_edges", "POST", "/graphs/{graph_uuid}/search/edges", True, True),
    ("graph.search_episodes", "POST", "/graphs/{graph_uuid}/search/episodes", True, True),
    ("graph.search_nodes", "POST", "/graphs/{graph_uuid}/search/nodes", True, True),
    ("graph.search_observations", "POST", "/graphs/{graph_uuid}/search/observations", True, True),
    ("graph.search_thread_summaries", "POST", "/graphs/{graph_uuid}/search/thread-summaries", True, True),
    ("graph.get_subgraph", "POST", "/graphs/{graph_uuid}/subgraph", False, True),
    ("graph.thread_summary.list", "POST", "/graphs/{graph_uuid}/thread-summaries/list", True, True),
    ("graph.warm", "POST", "/graphs/{graph_uuid}/warm", False, False),
    ("batch.list", "GET", "/batches", True, False),
    ("batch.create", "POST", "/batches", False, False),
    ("batch.delete", "DELETE", "/batches/{batch_uuid}", False, False),
    ("batch.get", "GET", "/batches/{batch_uuid}", False, False),
    ("batch.list_items", "GET", "/batches/{batch_uuid}/items", True, False),
    ("batch.add_items", "POST", "/batches/{batch_uuid}/items", False, False),
    ("batch.process", "POST", "/batches/{batch_uuid}/process", False, False),
    ("task.list", "GET", "/tasks", True, False),
    ("task.get", "GET", "/tasks/{task_uuid}", False, False),
    ("user_group.create", "POST", "/user-groups", False, False),
    ("user_group.list", "POST", "/user-groups/list", True, True),
    ("user_group.delete", "DELETE", "/user-groups/{group_uuid}", False, False),
    ("user_group.get", "GET", "/user-groups/{group_uuid}", False, False),
    ("user_group.update", "PATCH", "/user-groups/{group_uuid}", False, False),
    ("user_group.list_member_candidates", "POST", "/user-groups/{group_uuid}/member-candidates/list", True, True),
    ("user_group.add_members", "POST", "/user-groups/{group_uuid}/members", False, False),
    ("user_group.list_members", "POST", "/user-groups/{group_uuid}/members/list", True, True),
    ("user_group.remove_members", "POST", "/user-groups/{group_uuid}/members/remove", False, False),
    ("user_group.remove_member", "DELETE", "/user-groups/{group_uuid}/members/{user_uuid}", False, False),
    ("lookup.batch", "POST", "/lookup", False, True),
]

# Section 4.2 rows that spec 3 section 14.1 keeps out of the generated SDKs.
EXCLUDED_FROM_SDK: set[str] = {
    "user_group.list_policy_sets",  # docs audience
    "user_group.attach_policy_set",  # docs audience
    "user_group.detach_policy_set",  # docs audience
    "abac.list_api_keys",  # /abac administrative plane (zepctl only)
    "abac.list_api_key_policy_sets",  # /abac administrative plane (zepctl only)
    "abac.attach_api_key_policy_set",  # /abac administrative plane (zepctl only)
    "abac.detach_api_key_policy_set",  # /abac administrative plane (zepctl only)
    "abac.get_api_key_settings",  # /abac administrative plane (zepctl only)
    "abac.set_api_key_settings",  # /abac administrative plane (zepctl only)
    "abac.evaluate_policy",  # /abac administrative plane (zepctl only)
    "abac.explain_policy",  # /abac administrative plane (zepctl only)
    "abac.list_policy_sets",  # /abac administrative plane (zepctl only)
    "abac.create_policy_set",  # /abac administrative plane (zepctl only)
    "abac.validate_policy_set",  # /abac administrative plane (zepctl only)
    "abac.delete_policy_set",  # /abac administrative plane (zepctl only)
    "abac.get_policy_set",  # /abac administrative plane (zepctl only)
    "abac.update_policy_set",  # /abac administrative plane (zepctl only)
    "abac.detach_retention_target",  # /abac administrative plane (zepctl only)
    "abac.list_retention_targets",  # /abac administrative plane (zepctl only)
    "abac.attach_retention_target",  # /abac administrative plane (zepctl only)
}

MISSING_FROM_ALPHA5 = {
    "project.get_content_policy",
    "project.set_content_policy",
    "project.list_content_policy_revisions",
    "project.get_content_policy_revision",
    "agent.create",
    "agent.list",
    "agent.delete",
    "agent.get",
    "agent.update",
    "agent.declare_breaking_change",
    "agent.get_context",
    "agent.split.plan",
    "agent.literal_policy.get",
    "agent.literal_policy.update",
    "agent.skill.candidate.list",
    "agent.skill.candidate.get",
    "agent.skill.evaluation.create_for_candidate",
    "agent.learning.get",
    "agent.learning.list_runs",
    "agent.skill.create",
    "agent.skill.import_package",
    "agent.skill.list",
    "agent.skill.search",
    "agent.skill.get",
    "agent.skill.publication.get",
    "agent.skill.publication.lookup",
    "agent.skill.use.create",
    "agent.skill.use.add_outcome",
    "agent.skill.approve",
    "agent.skill.evaluation.create",
    "agent.skill.evidence.list",
    "agent.skill.relation.list",
    "agent.skill.version.restore_version",
    "agent.skill.retire",
    "agent.skill.version.list",
    "agent.skill.create_version",
    "agent.skill.version.compare",
    "agent.skill.version.get",
    "agent.skill.export.create",
    "agent.skill.export.get",
    "agent.trajectory.create",
    "agent.trajectory.list",
    "agent.trajectory.get",
    "agent.trajectory.update",
    "agent.trajectory.delete",
    "agent.trajectory.abandon",
    "agent.trajectory.close",
    "agent.trajectory.correct_task_family",
    "agent.trajectory.list_events",
    "agent.trajectory.append_event",
    "agent.trajectory.delete_event",
    "agent.trajectory.reopen",
    "agent.trajectory.get_summary",
    "agent.trajectory.list_summary_versions",
    "agent.verifier.list",
    "agent.verifier.get",
    "agent.verifier.update",
    "agent.verifier.invalidate_evidence",
    "agent.verifier.revoke",
    "graph.get_content_policy",
    "graph.list_content_policy_events",
    "graph.hyperedge.add",
    "graph.hyperedge.list",
    "graph.hyperedge.delete",
    "graph.hyperedge.get",
    "graph.hyperedge.update",
    "graph.hyperedge.create_edge",
    "graph.hyperedge.delete_edge",
}

ALPHA5_POST_READ_EXPOSES_IDEMPOTENCY = {
    "context.list_templates",
    "user.list",
    "user.lookup",
    "thread.lookup",
    "graph.list",
    "graph.lookup",
    "graph.get_context",
    "graph.document_summary.list",
    "graph.edge.list",
    "graph.episode.list",
    "graph.node.list",
    "graph.node.list_neighbors",
    "graph.observation.list",
    "graph.search_edges",
    "graph.search_episodes",
    "graph.search_nodes",
    "graph.search_observations",
    "graph.search_thread_summaries",
    "graph.get_subgraph",
    "graph.thread_summary.list",
    "user_group.list",
    "user_group.list_member_candidates",
    "user_group.list_members",
    "lookup.batch",
}

D1_REASON = (
    "The generator configuration does not enable automatic Idempotency-Key generation "
    "(spec 3 section 14.6), so a state-changing call without a caller key sends no Idempotency-Key."
)
D3_REASON = (
    "The v4 contract declares only the Api-Key security scheme (spec 3 sections 2.2 and 14.1 "
    "require the bearer scheme too), so the generated client requires api_key and overwrites "
    "the Authorization header."
)
D5_REASON = (
    "Spec 3 section 4.2 marks agent.learning.get as paginated, but the v4 contract returns one "
    "AgentLearningState with no cursor, so the generated method returns no pager."
)
CALLER_KEY = "contract-caller-key"
PROJECT_UUID = "00000000-0000-4000-8000-000000000001"
BASE_URL = "https://contract.test"
_ALPHA5 = importlib.metadata.version("zep-cloud") == "4.0.0a5"
_CLIENT_TYPES = (Zep, AsyncZep)


def _gap_reason(operation: str, is_post_read: bool = False) -> str | None:
    if not _ALPHA5:
        return None
    missing_reason = _missing_operation_reason(operation)
    if missing_reason is not None:
        return missing_reason
    if is_post_read and operation in ALPHA5_POST_READ_EXPOSES_IDEMPOTENCY:
        return f"{operation}: POST read; the 4.0.0-alpha.5 contract marks it idempotent"
    return None


def _missing_operation_reason(operation: str) -> str | None:
    if _ALPHA5 and operation in MISSING_FROM_ALPHA5:
        return f"{operation}: absent from the 4.0.0-alpha.5 generated code; present in the current spec 3 contract"
    return None


def _operation_params(include_post_read_gaps: bool = True) -> list[typing.Any]:
    params = []
    for operation, method, path, paginated, post_read in SECTION_4_2_OPERATIONS:
        reason = _gap_reason(operation, post_read) if include_post_read_gaps else _missing_operation_reason(operation)
        marks = pytest.mark.xfail(strict=True, reason=reason) if reason else ()
        params.append(
            pytest.param(
                operation,
                method,
                path,
                paginated,
                post_read,
                marks=marks,
                id=operation,
            )
        )
    return params


def _resolve_method(client: object, operation: str) -> typing.Any:
    parts = operation.split(".")
    target = client
    for part in parts:
        target = getattr(target, part)
    return target


def _generated_client_methods(client: object, prefix: str = "") -> set[str]:
    methods: set[str] = set()
    visited: set[int] = set()

    def visit(target: object, path: str) -> None:
        if id(target) in visited:
            return
        visited.add(id(target))
        for name in dir(target):
            if name.startswith("_"):
                continue
            value = getattr(target, name)
            if callable(value):
                methods.add(f"{path}{name}")
            elif value is not None:
                module_name = type(value).__module__
                if module_name.startswith("zep_cloud.") and module_name.endswith(".client"):
                    visit(value, f"{path}{name}.")

    visit(client, prefix)
    return methods


@pytest.fixture(scope="module")
def clients() -> typing.Iterator[tuple[Zep, AsyncZep]]:
    sync = Zep(api_key="contract-test", base_url=BASE_URL)
    async_client = AsyncZep(api_key="contract-test", base_url=BASE_URL)
    yield sync, async_client
    sync._client_wrapper.httpx_client.httpx_client.close()
    asyncio.run(async_client._client_wrapper.httpx_client.httpx_client.aclose())


@pytest.mark.parametrize("client_type", _CLIENT_TYPES, ids=["sync", "async"])
@pytest.mark.parametrize(
    ("operation", "method", "path", "paginated", "post_read"),
    _operation_params(include_post_read_gaps=False),
)
def test_client_methods_match_section_4_2(
    clients: tuple[Zep, AsyncZep],
    client_type: type[Zep] | type[AsyncZep],
    operation: str,
    method: str,
    path: str,
    paginated: bool,
    post_read: bool,
) -> None:
    sync, async_client = clients
    client = sync if client_type is Zep else async_client
    assert callable(_resolve_method(client, operation))


def test_client_exposes_no_method_outside_section_4_2(
    clients: tuple[Zep, AsyncZep],
) -> None:
    expected = {operation for operation, *_ in SECTION_4_2_OPERATIONS}
    sync, async_client = clients
    actual = _generated_client_methods(sync) | _generated_client_methods(async_client)
    assert actual - expected == set()
    assert actual.isdisjoint(EXCLUDED_FROM_SDK)


@pytest.mark.parametrize("client_type", _CLIENT_TYPES, ids=["sync", "async"])
@pytest.mark.parametrize(
    ("operation", "method", "path", "paginated", "post_read"),
    [
        pytest.param(*row, marks=pytest.mark.xfail(strict=True, reason=reason), id=row[0])
        if (reason := _missing_operation_reason(row[0]) or (D5_REASON if row[0] == "agent.learning.get" else None))
        else pytest.param(*row, id=row[0])
        for row in SECTION_4_2_OPERATIONS
        if row[3]
    ],
)
def test_paginated_operations_return_pagers(
    clients: tuple[Zep, AsyncZep],
    client_type: type[Zep] | type[AsyncZep],
    operation: str,
    method: str,
    path: str,
    paginated: bool,
    post_read: bool,
) -> None:
    sync, async_client = clients
    client = sync if client_type is Zep else async_client
    result_type = typing.get_type_hints(_resolve_method(client, operation))["return"]
    expected_type = SyncPager if client_type is Zep else AsyncPager
    assert typing.get_origin(result_type) is expected_type


def _page_response(prefix: str, page_number: int) -> dict[str, object]:
    start = 1 if page_number == 1 else 3
    response: dict[str, object] = {
        "items": [{"uuid": f"{prefix}-{index}"} for index in range(start, start + 2)],
    }
    if page_number == 1:
        response["next_cursor"] = "c1"
    return response


def _item_ids(items: typing.Iterable[typing.Any]) -> list[str | None]:
    return [item.uuid_ for item in items]


@pytest.mark.parametrize("operation", ["batch.list", "user.list"])
def test_sync_pager_traverses_two_pages_and_stops_without_next_cursor(
    operation: str,
) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        page_number = 1 if request.url.params.get("cursor") is None else 2
        return httpx.Response(200, json=_page_response(operation, page_number))

    with httpx.Client(transport=httpx.MockTransport(handler)) as httpx_client:
        client = Zep(api_key="contract-test", base_url=BASE_URL, httpx_client=httpx_client)
        resource, method_name = operation.split(".")
        pager = getattr(getattr(client, resource), method_name)(limit=2)
        items = list(pager)

    assert len(requests) == 2
    assert requests[1].url.params.get("cursor") == "c1"
    assert _item_ids(items) == [f"{operation}-1", f"{operation}-2", f"{operation}-3", f"{operation}-4"]
    assert len(set(_item_ids(items))) == 4


@pytest.mark.parametrize("operation", ["batch.list", "user.list"])
@pytest.mark.asyncio
async def test_async_pager_traverses_two_pages_and_stops_without_next_cursor(
    operation: str,
) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        page_number = 1 if request.url.params.get("cursor") is None else 2
        return httpx.Response(200, json=_page_response(operation, page_number))

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as httpx_client:
        client = AsyncZep(
            api_key="contract-test",
            base_url=BASE_URL,
            httpx_client=httpx_client,
        )
        resource, method_name = operation.split(".")
        pager = await getattr(getattr(client, resource), method_name)(limit=2)
        items = [item async for item in pager]

    assert len(requests) == 2
    assert requests[1].url.params.get("cursor") == "c1"
    assert _item_ids(items) == [f"{operation}-1", f"{operation}-2", f"{operation}-3", f"{operation}-4"]
    assert len(set(_item_ids(items))) == 4


@pytest.mark.parametrize("client_type", _CLIENT_TYPES, ids=["sync", "async"])
@pytest.mark.parametrize(
    ("operation", "method", "path", "paginated", "post_read"),
    _operation_params(),
)
def test_only_state_changing_methods_expose_idempotency_key(
    clients: tuple[Zep, AsyncZep],
    client_type: type[Zep] | type[AsyncZep],
    operation: str,
    method: str,
    path: str,
    paginated: bool,
    post_read: bool,
) -> None:
    sync, async_client = clients
    client = sync if client_type is Zep else async_client
    parameters = inspect.signature(_resolve_method(client, operation)).parameters
    state_changing = method != "GET" and not post_read
    assert ("idempotency_key" in parameters) is state_changing


def _uuid4_header(headers: httpx.Headers) -> uuid.UUID:
    key = headers.get("Idempotency-Key")
    assert key is not None
    parsed = uuid.UUID(key)
    assert parsed.version == 4
    assert parsed.variant == uuid.RFC_4122
    return parsed


@pytest.mark.xfail(strict=True, reason=D1_REASON)
def test_call_without_key_sends_uuid4_idempotency_key() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={})

    with httpx.Client(transport=httpx.MockTransport(handler)) as httpx_client:
        client = Zep(api_key="contract-test", base_url=BASE_URL, httpx_client=httpx_client)
        client.user.create()
    _uuid4_header(requests[0].headers)


def test_caller_idempotency_key_is_sent_unchanged() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={})

    with httpx.Client(transport=httpx.MockTransport(handler)) as httpx_client:
        client = Zep(api_key="contract-test", base_url=BASE_URL, httpx_client=httpx_client)
        client.user.create(idempotency_key=CALLER_KEY)
    assert requests[0].headers.get("Idempotency-Key") == CALLER_KEY


@pytest.mark.xfail(strict=True, reason=D1_REASON)
def test_retry_reuses_generated_idempotency_key() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(503, headers={"Retry-After": "1"})
        return httpx.Response(200, json={})

    with httpx.Client(transport=httpx.MockTransport(handler)) as httpx_client:
        client = Zep(api_key="contract-test", base_url=BASE_URL, httpx_client=httpx_client)
        client.user.create(request_options={"max_retries": 1})

    assert len(requests) == 2
    first = _uuid4_header(requests[0].headers)
    second = _uuid4_header(requests[1].headers)
    assert first == second


def test_retry_reuses_caller_idempotency_key() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(503, headers={"Retry-After": "1"})
        return httpx.Response(200, json={})

    with httpx.Client(transport=httpx.MockTransport(handler)) as httpx_client:
        client = Zep(api_key="contract-test", base_url=BASE_URL, httpx_client=httpx_client)
        client.user.create(
            idempotency_key=CALLER_KEY,
            request_options={"max_retries": 1},
        )

    assert len(requests) == 2
    assert [request.headers.get("Idempotency-Key") for request in requests] == [
        CALLER_KEY,
        CALLER_KEY,
    ]


@pytest.mark.parametrize(
    "operation",
    [pytest.param(operation, id=operation) for operation in ("project.get", "user.list")],
)
def test_get_and_post_read_send_no_idempotency_header(operation: str) -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"items": [], "next_cursor": None})

    with httpx.Client(transport=httpx.MockTransport(handler)) as httpx_client:
        client = Zep(api_key="contract-test", base_url=BASE_URL, httpx_client=httpx_client)
        resource, method_name = operation.split(".")
        method = getattr(getattr(client, resource), method_name)
        method()
    assert len(requests) == 1
    assert requests[0].headers.get("Idempotency-Key") is None


def test_client_sends_project_api_key() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={})

    with httpx.Client(transport=httpx.MockTransport(handler)) as httpx_client:
        client = Zep(api_key="contract-api-key", base_url=BASE_URL, httpx_client=httpx_client)
        client.project.get()
    assert requests[0].headers.get("Authorization") == "Api-Key contract-api-key"
    assert requests[0].headers.get("X-Zep-Project") is None


@pytest.mark.xfail(strict=True, reason=D3_REASON)
def test_client_sends_admin_bearer_with_project_header(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("ZEP_API_KEY", raising=False)
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={})

    with httpx.Client(transport=httpx.MockTransport(handler)) as httpx_client:
        client = Zep(
            api_key=None,
            headers={
                "Authorization": "Bearer contract-token",
                "X-Zep-Project": PROJECT_UUID,
            },
            base_url=BASE_URL,
            httpx_client=httpx_client,
        )
        client.project.get()
    assert requests[0].headers.get("Authorization") == "Bearer contract-token"
    assert requests[0].headers.get("X-Zep-Project") == PROJECT_UUID
    assert requests[0].headers.get("Api-Key") is None


def _string_enum_values(annotation: object) -> set[str]:
    union_origin = getattr(types, "UnionType", typing.Union)
    if typing.get_origin(annotation) in (typing.Union, union_origin):
        return set().union(
            *(
                _string_enum_values(argument)
                for argument in typing.get_args(annotation)
                if argument is not type(None) and argument is not typing.Any
            )
        )
    if inspect.isclass(annotation) and issubclass(annotation, Enum):
        assert issubclass(annotation, str)
        return {str(member.value) for member in annotation}
    if typing.get_origin(annotation) is typing.Literal:
        values = typing.get_args(annotation)
        assert all(isinstance(value, str) for value in values)
        return set(values)
    raise AssertionError(f"{annotation!r} is not a string enum")


def test_graph_context_recency_bias_is_off_mild_strong_string_enum(
    clients: tuple[Zep, AsyncZep],
) -> None:
    sync, async_client = clients
    for client in (sync, async_client):
        annotation = typing.get_type_hints(client.graph.get_context)["recency_bias"]
        assert _string_enum_values(annotation) == {"off", "mild", "strong"}


def test_thread_context_recency_bias_is_not_an_object(
    clients: tuple[Zep, AsyncZep],
) -> None:
    sync, async_client = clients
    for client in (sync, async_client):
        hints = typing.get_type_hints(client.thread.get_context)
        if "recency_bias" in hints:
            assert _string_enum_values(hints["recency_bias"]) == {"off", "mild", "strong"}


def _name_words(name: str) -> list[str]:
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name)
    return [word.lower() for word in re.split(r"[^A-Za-z0-9]+", name) if word]


def test_generated_names_contain_no_v3_only_concepts() -> None:
    offenders: list[str] = []
    modules = pkgutil.walk_packages(zep_cloud.__path__, f"{zep_cloud.__name__}.")
    for module_info in modules:
        module_name = module_info.name
        if module_name.startswith("zep_cloud.core") or module_name == "zep_cloud.ontology":
            continue
        module = importlib.import_module(module_name)
        for class_name, class_value in vars(module).items():
            if not inspect.isclass(class_value) or class_name.startswith("_") or class_value.__module__ != module_name:
                continue
            location = f"{module_name}.{class_name}"
            class_words = _name_words(class_name)
            if (
                "lastn" in class_words
                or "scope" in class_words
                or any(
                    class_words[index : index + 2] in (["uuid", "cursor"], ["group", "id"])
                    for index in range(len(class_words) - 1)
                )
            ):
                offenders.append(location)
            for method_name, method_value in inspect.getmembers(class_value, inspect.isfunction):
                if method_name.startswith("_") or method_value.__module__ != module_name:
                    continue
                words = _name_words(method_name)
                if (
                    "lastn" in words
                    or "scope" in words
                    or any(
                        words[index : index + 2] in (["uuid", "cursor"], ["group", "id"])
                        for index in range(len(words) - 1)
                    )
                ):
                    offenders.append(f"{location}.{method_name}")
    assert offenders == []
