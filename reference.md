# Reference
## Agent
<details><summary><code>client.agent.<a href="src/zep_cloud/agent/client.py">create</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.create(
    agent_id="agent_id",
    name="name",
    security_domain="security_domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateAgentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zep_cloud/agent/client.py">list</a>(...) -> AgentPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filters to the exact developer-assigned Agent identifier.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — Filters to the exact deployment identifier.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Filters to Agents whose metadata contains these key-value pairs.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AgentStatus]` — Filters to lifecycle status. Omit to include every status.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Filters to the exact deployment version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zep_cloud/agent/client.py">get</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.get(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zep_cloud/agent/client.py">delete</a>(...) -> AgentDeleteResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.delete(
    agent_uuid="agent_uuid",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current Agent revision used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zep_cloud/agent/client.py">update</a>(...) -> Agent</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.update(
    agent_uuid="agent_uuid",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current Agent revision used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — The customer deployment this Agent represents. Set to null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A human-readable description of the Agent. Set to null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**memory_settings:** `typing.Optional[AgentMemorySettings]` — Replacement Agent Memory settings. Set to null to restore defaults.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Replacement developer metadata. Set to null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The Agent's display name.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — The customer deployment version this Agent represents. Set to null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zep_cloud/agent/client.py">declare_breaking_change</a>(...) -> AgentBreakingChange</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.declare_breaking_change(
    agent_uuid="agent_uuid",
    expected_revision=1,
    version="version",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zep_cloud/agent/client.py">get_context</a>(...) -> AgentContext</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.get_context(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**environments:** `typing.Optional[typing.List[AgentContextResource]]` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**max_characters:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**models:** `typing.Optional[typing.List[AgentContextResource]]` 
    
</dd>
</dl>

<dl>
<dd>

**objective:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[AgentContextResource]]` 
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Batch
<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">list</a>(...) -> BatchPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.batch.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[BatchListRequestStatus]` — Batch status filter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">create</a>(...) -> Batch</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.batch.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ignore_roles:** `typing.Optional[typing.List[str]]` 

Message roles to skip during graph extraction for thread message items in
this batch.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to store on the batch.
    
</dd>
</dl>

<dl>
<dd>

**strict_ontology:** `typing.Optional[bool]` 

When true, prevents extraction of generic entity nodes that do not match
the configured ontology for episodes in this batch.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">get</a>(...) -> Batch</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.batch.get(
    batch_uuid="batch_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_uuid:** `str` — Batch UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.batch.delete(
    batch_uuid="batch_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_uuid:** `str` — Batch UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">list_items</a>(...) -> BatchItemPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.batch.list_items(
    batch_uuid="batch_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_uuid:** `str` — Batch UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">add_items</a>(...) -> BatchItemsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, BatchItemInput
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.batch.add_items(
    batch_uuid="batch_uuid",
    items=[
        BatchItemInput(
            type="graph_episode",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_uuid:** `str` — Batch UUID
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.List[BatchItemInput]` — The batch items to append, each identified by its type field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">process</a>(...) -> ProcessBatchResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.batch.process(
    batch_uuid="batch_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_uuid:** `str` — Batch UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Context
<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">create_template</a>(...) -> ContextTemplate</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.context.create_template()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateContextTemplateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">list_templates</a>(...) -> ContextTemplatePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.context.list_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filters results to the context template with this exact name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">get_template</a>(...) -> ContextTemplate</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.context.get_template(
    template_uuid="template_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_uuid:** `str` — Template UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">update_template</a>(...) -> ContextTemplate</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.context.update_template(
    template_uuid="template_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_uuid:** `str` — Template UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateContextTemplateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">delete_template</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.context.delete_template(
    template_uuid="template_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_uuid:** `str` — Template UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DebugLog
<details><summary><code>client.debug_log.<a href="src/zep_cloud/debug_log/client.py">enable</a>() -> DebugLoggingEnablement</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enables debug logging for the project for one hour, or for 24 hours on the Enterprise plan. Episodes ingested while debug logging is enabled have a debug log (see `graph.episode.get_debug_logs`). On the Flex, Flex Plus, and Enterprise plans, the operation also enables ingestion tracing (see `graph.episode.list_ingestion_traces`); `ingestion_trace_enabled` reports the result. A repeated call starts the duration again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.debug_log.enable()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Graph
<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">create</a>(...) -> Graph</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content_policy:** `typing.Optional[GraphContentPolicyRequest]` 

Content policy additions for the graph. The graph binds the current
project content policy plus these additions, and the binding does not
change after creation.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the graph.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — A display name for the graph.
    
</dd>
</dl>

<dl>
<dd>

**time_zone:** `typing.Optional[str]` — The graph's IANA time zone.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">list</a>(...) -> GraphPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[GraphListRequestOrderBy]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GraphListRequestOrder]` — asc or desc
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 

Filters results to graphs whose name, description, or graph ID contains
this text.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">lookup</a>(...) -> Graph</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.lookup()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `LookupRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">get</a>(...) -> Graph</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.get(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">delete</a>(...) -> GraphDeleteResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.delete(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">update</a>(...) -> Graph</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.update(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the graph.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The graph's display name.
    
</dd>
</dl>

<dl>
<dd>

**time_zone:** `typing.Optional[str]` — The graph's IANA time zone.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">clone</a>(...) -> CloneGraphResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.clone(
    graph_uuid="graph_uuid",
    request={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `CloneGraphRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">get_content_policy</a>(...) -> GraphContentPolicy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the content policy the graph bound at creation. The policy of a graph does not change after creation. A graph without a content policy returns revision 0 with no categories and no rules.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.get_content_policy(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">list_content_policy_events</a>(...) -> ContentPolicyEventPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the content policy decisions recorded for a graph, newest first. Each event carries identifiers only. A graph without a content policy returns an empty list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.list_content_policy_events(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Exact-match filters. Supported keys: episode_uuid and drop_reason.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">get_context</a>(...) -> GraphContextResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.get_context(
    graph_uuid="graph_uuid",
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query used to assemble the context block.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` 

Filters constraining which graph data can be selected for the context
block.
    
</dd>
</dl>

<dl>
<dd>

**include_results:** `typing.Optional[bool]` — When true, includes the raw graph results selected for the context block.
    
</dd>
</dl>

<dl>
<dd>

**max_characters:** `typing.Optional[int]` — The maximum number of characters in the assembled context block.
    
</dd>
</dl>

<dl>
<dd>

**recency_bias:** `typing.Optional[GraphContextRequestRecencyBias]` — Adjusts result selection to favor more recent graph data.
    
</dd>
</dl>

<dl>
<dd>

**template_uuid:** `typing.Optional[str]` — The UUID of a context template used to render the context block.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">get_instructions</a>(...) -> Instructions</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.get_instructions(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">set_instructions</a>(...) -> Instructions</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.set_instructions(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `Instructions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">get_observation_steering</a>(...) -> ObservationSteering</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.get_observation_steering(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">set_observation_steering</a>(...) -> ObservationSteering</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.set_observation_steering(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ObservationSteering` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">get_ontology</a>(...) -> Ontology</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.get_ontology(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">set_ontology</a>(...) -> Ontology</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.set_ontology(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `Ontology` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">search_edges</a>(...) -> EdgePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.search_edges(
    graph_uuid="graph_uuid",
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">search_episodes</a>(...) -> EpisodePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.search_episodes(
    graph_uuid="graph_uuid",
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">search_nodes</a>(...) -> NodePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.search_nodes(
    graph_uuid="graph_uuid",
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">search_observations</a>(...) -> ObservationPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.search_observations(
    graph_uuid="graph_uuid",
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">search_thread_summaries</a>(...) -> ThreadSummaryPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.search_thread_summaries(
    graph_uuid="graph_uuid",
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">get_subgraph</a>(...) -> SubgraphResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.get_subgraph(
    graph_uuid="graph_uuid",
    seed_node_uuids=[
        "seed_node_uuids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**seed_node_uuids:** `typing.List[str]` — The node UUIDs to expand from, in traversal-priority order.
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` — The maximum traversal depth from the seed nodes. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[SubgraphRequestDirection]` 

The edge orientation to follow during expansion: in, out, or both.
Defaults to both.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Filters constraining the traversed edges and included nodes.
    
</dd>
</dl>

<dl>
<dd>

**max_edges:** `typing.Optional[int]` — The maximum number of edges in the response. Defaults to 200.
    
</dd>
</dl>

<dl>
<dd>

**max_nodes:** `typing.Optional[int]` — The maximum number of nodes in the response. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">warm</a>(...) -> AsyncResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.warm(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Lookup
<details><summary><code>client.lookup.<a href="src/zep_cloud/lookup/client.py">batch</a>(...) -> LookupBatchResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.lookup.batch()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graphs:** `typing.Optional[typing.List[str]]` — Developer-assigned graph IDs to resolve to UUIDs.
    
</dd>
</dl>

<dl>
<dd>

**threads:** `typing.Optional[typing.List[str]]` — Developer-assigned thread IDs to resolve to UUIDs.
    
</dd>
</dl>

<dl>
<dd>

**users:** `typing.Optional[typing.List[str]]` — Developer-assigned user IDs to resolve to UUIDs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Project
<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">get</a>() -> Project</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">update</a>(...) -> Project</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**default_time_zone:** `typing.Optional[str]` 

The project's IANA fallback time zone. Set to null to clear the existing
value.
    
</dd>
</dl>

<dl>
<dd>

**include_policy_violating_episodes:** `typing.Optional[bool]` 

When true, episode reads on graphs with a content policy include the
episodes that violated the policy.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">get_content_policy</a>() -> ContentPolicy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current content policy revision of the project. A new graph binds this revision at creation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.get_content_policy()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">set_content_policy</a>(...) -> ContentPolicy</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the project content policy and creates a new immutable revision. Graphs that already exist keep the revision they bound. An empty policy (no categories and no rules) removes the content policy for new graphs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.set_content_policy()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**categories:** `typing.Optional[typing.List[ContentPolicyCategoryRequest]]` 

The categories of the policy. Maximum 16. An empty list with no rules
means no content policy.
    
</dd>
</dl>

<dl>
<dd>

**rules:** `typing.Optional[typing.List[ContentPolicyRuleRequest]]` — The rules of the policy. Maximum 32.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">list_content_policy_revisions</a>(...) -> ContentPolicyRevisionPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists every revision of the project content policy, newest first, including revision 0.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.list_content_policy_revisions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">get_content_policy_revision</a>(...) -> ContentPolicy</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.get_content_policy_revision(
    revision_uuid="revision_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**revision_uuid:** `str` — Revision UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">get_instructions</a>() -> Instructions</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.get_instructions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">set_instructions</a>(...) -> Instructions</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.set_instructions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Instructions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">get_observation_steering</a>() -> ObservationSteering</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.get_observation_steering()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">set_observation_steering</a>(...) -> ObservationSteering</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.set_observation_steering()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ObservationSteering` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">get_ontology</a>() -> Ontology</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.get_ontology()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">set_ontology</a>(...) -> Ontology</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the entity types and the edge types that the project uses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.set_ontology()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Ontology` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">get_user_summary_instructions</a>() -> UserSummaryInstructions</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.get_user_summary_instructions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">set_user_summary_instructions</a>(...) -> UserSummaryInstructions</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.project.set_user_summary_instructions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UserSummaryInstructions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Task
<details><summary><code>client.task.<a href="src/zep_cloud/task/client.py">list</a>(...) -> TaskPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.task.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.task.<a href="src/zep_cloud/task/client.py">get</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.task.get(
    task_uuid="task_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_uuid:** `str` — Task UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Thread
<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">list</a>(...) -> ThreadPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ThreadListRequestOrderBy]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ThreadListRequestOrder]` — asc or desc
    
</dd>
</dl>

<dl>
<dd>

**user_uuid:** `typing.Optional[str]` — Filter by user UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">create</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.create(
    user_uuid="user_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_uuid:** `str` — The UUID of the user this thread belongs to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">lookup</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.lookup()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `LookupRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">get</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.get(
    thread_uuid="thread_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_uuid:** `str` — Thread UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">delete</a>(...) -> ThreadDeleteResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.delete(
    thread_uuid="thread_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_uuid:** `str` — Thread UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">get_context</a>(...) -> ThreadContextResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.get_context(
    thread_uuid="thread_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_uuid:** `str` — Thread UUID
    
</dd>
</dl>

<dl>
<dd>

**template_uuid:** `typing.Optional[str]` — Context template UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">list_episodes</a>(...) -> EpisodePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.list_episodes(
    thread_uuid="thread_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_uuid:** `str` — Thread UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">list_messages</a>(...) -> MessagePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.list_messages(
    thread_uuid="thread_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_uuid:** `str` — Thread UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ThreadListMessagesRequestOrder]` — Sort direction: asc or desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">add_messages</a>(...) -> AddMessagesResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, AddMessage
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.add_messages(
    thread_uuid="thread_uuid",
    messages=[
        AddMessage()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_uuid:** `str` — Thread UUID
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.List[AddMessage]` — The messages to add to the thread.
    
</dd>
</dl>

<dl>
<dd>

**ignore_roles:** `typing.Optional[typing.List[str]]` 

Message roles to skip during graph extraction; the messages are still
stored.
    
</dd>
</dl>

<dl>
<dd>

**return_context:** `typing.Optional[bool]` 

When true, returns the context block for the thread's most recent
messages.
    
</dd>
</dl>

<dl>
<dd>

**strict_ontology:** `typing.Optional[bool]` 

When true, prevents extraction of generic entity nodes that do not match
the configured ontology.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">get_summary</a>(...) -> ThreadSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.get_summary(
    thread_uuid="thread_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_uuid:** `str` — Thread UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TraceConnection
<details><summary><code>client.trace_connection.<a href="src/zep_cloud/trace_connection/client.py">list</a>(...) -> TraceConnectionPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List trace connections in the current Zep project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.trace_connection.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trace_connection.<a href="src/zep_cloud/trace_connection/client.py">create</a>(...) -> TraceConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify the provider credential before Zep stores it. Example request: `{"name":"Support traces","provider":"braintrust","credential":"secret","requests_per_minute":10}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.trace_connection.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_url:** `typing.Optional[str]` — APIURL is an optional custom provider endpoint.
    
</dd>
</dl>

<dl>
<dd>

**credential:** `typing.Optional[str]` — Credential is the write-only provider credential.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name is the connection name.
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Provider is the provider name.
    
</dd>
</dl>

<dl>
<dd>

**requests_per_minute:** `typing.Optional[int]` — RequestsPerMinute is the provider request rate limit.
    
</dd>
</dl>

<dl>
<dd>

**retention_days:** `typing.Optional[int]` — RetentionDays is an optional provider retention window.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trace_connection.<a href="src/zep_cloud/trace_connection/client.py">get</a>(...) -> TraceConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one trace connection. The response includes a credential hint and never includes the credential.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.trace_connection.get(
    connection_uuid="connection_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_uuid:** `str` — Trace connection UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trace_connection.<a href="src/zep_cloud/trace_connection/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a trace connection that no active trajectory import uses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.trace_connection.delete(
    connection_uuid="connection_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_uuid:** `str` — Trace connection UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trace_connection.<a href="src/zep_cloud/trace_connection/client.py">update</a>(...) -> TraceConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify changed provider settings before Zep stores them. Example request: `{"credential":"new-secret","requests_per_minute":20}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.trace_connection.update(
    connection_uuid="connection_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_uuid:** `str` — Trace connection UUID
    
</dd>
</dl>

<dl>
<dd>

**api_url:** `typing.Optional[str]` — APIURL is the new custom provider endpoint, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**credential:** `typing.Optional[str]` — Credential is the new write-only provider credential, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name is the new connection name, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**requests_per_minute:** `typing.Optional[int]` — RequestsPerMinute is the new provider request rate limit, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**retention_days:** `typing.Optional[int]` — RetentionDays is the new provider retention window, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trace_connection.<a href="src/zep_cloud/trace_connection/client.py">verify</a>(...) -> TraceConnection</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the provider credential and update the connection status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.trace_connection.verify(
    connection_uuid="connection_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_uuid:** `str` — Trace connection UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## UserGroup
<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">create</a>(...) -> UserGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the user group.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the user group.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">list</a>(...) -> UserGroupPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SearchListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">get</a>(...) -> UserGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.get(
    group_uuid="group_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — User group UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.delete(
    group_uuid="group_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — User group UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">update</a>(...) -> UserGroup</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.update(
    group_uuid="group_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — User group UUID
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the user group.
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `typing.Optional[int]` — The user group's current version, used to detect concurrent updates.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the user group.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">list_member_candidates</a>(...) -> UserPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.list_member_candidates(
    group_uuid="group_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — User group UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">add_members</a>(...) -> MembershipMutationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.add_members(
    group_uuid="group_uuid",
    user_uuids=[
        "user_uuids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — User group UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutateMembersRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">list_members</a>(...) -> UserPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.list_members(
    group_uuid="group_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — User group UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `SearchListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">remove_members</a>(...) -> MembershipMutationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.remove_members(
    group_uuid="group_uuid",
    user_uuids=[
        "user_uuids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — User group UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `MutateMembersRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">remove_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.remove_member(
    group_uuid="group_uuid",
    user_uuid="user_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — User group UUID
    
</dd>
</dl>

<dl>
<dd>

**user_uuid:** `str` — User UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">list_for_user</a>(...) -> UserGroupPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requires a project API key, or an account-admin bearer token with the X-Zep-Project header. The account must be entitled to attribute-based access control.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user_group.list_for_user(
    user_uuid="user_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_uuid:** `str` — User UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## User
<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">create</a>(...) -> User</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**content_policy:** `typing.Optional[GraphContentPolicyRequest]` 

Content policy additions for the user's graph. The graph binds the
current project content policy plus these additions, and the binding
does not change after creation.
    
</dd>
</dl>

<dl>
<dd>

**disable_default_ontology:** `typing.Optional[bool]` — When true, disables the default ontology for the user's graph.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The email address of the user.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The user's first name.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The user's last name.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to store on the user.
    
</dd>
</dl>

<dl>
<dd>

**time_zone:** `typing.Optional[str]` — The user's IANA time zone.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">list</a>(...) -> UserPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[UserListRequestOrderBy]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[UserListRequestOrder]` — asc or desc
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Filters results to users whose user ID, email, or name contains this text.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">lookup</a>(...) -> User</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user.lookup()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `LookupRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">get</a>(...) -> User</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user.get(
    user_uuid="user_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_uuid:** `str` — User UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">delete</a>(...) -> UserDeleteResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user.delete(
    user_uuid="user_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_uuid:** `str` — User UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">update</a>(...) -> User</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user.update(
    user_uuid="user_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_uuid:** `str` — User UUID
    
</dd>
</dl>

<dl>
<dd>

**disable_default_ontology:** `typing.Optional[bool]` — When true, disables the default ontology for the user's graph.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The email address of the user.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The user's first name.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The user's last name.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to merge onto the user; a key set to null is removed.
    
</dd>
</dl>

<dl>
<dd>

**time_zone:** `typing.Optional[str]` — The user's IANA time zone.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">get_node</a>(...) -> Node</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user.get_node(
    user_uuid="user_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_uuid:** `str` — User UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">get_summary_instructions</a>(...) -> UserSummaryInstructions</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user.get_summary_instructions(
    user_uuid="user_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_uuid:** `str` — User UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">set_summary_instructions</a>(...) -> UserSummaryInstructions</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.user.set_summary_instructions(
    user_uuid="user_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_uuid:** `str` — User UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `UserSummaryInstructions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Learning
<details><summary><code>client.agent.learning.<a href="src/zep_cloud/agent/learning/client.py">get</a>(...) -> AgentLearningState</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.learning.get(
    agent_uuid="agent_uuid",
    task_family="task_family",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `str` — Task family
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.learning.<a href="src/zep_cloud/agent/learning/client.py">list_runs</a>(...) -> Pagev4AgentSkillCompilationOutcome</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.learning.list_runs(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` — Task family
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent LiteralPolicy
<details><summary><code>client.agent.literal_policy.<a href="src/zep_cloud/agent/literal_policy/client.py">get</a>(...) -> AgentLiteralPolicy</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.literal_policy.get(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.literal_policy.<a href="src/zep_cloud/agent/literal_policy/client.py">update</a>(...) -> AgentLiteralPolicy</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, AgentLiteralPolicyClasses, AgentLiteralPolicyValues
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.literal_policy.update(
    agent_uuid="agent_uuid",
    allowlisted_classes=AgentLiteralPolicyClasses(
        environments=[
            "environments"
        ],
        tools=[
            "tools"
        ],
    ),
    allowlisted_values=AgentLiteralPolicyValues(
        environments=[
            "environments"
        ],
        tools=[
            "tools"
        ],
    ),
    default="parameterize",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**allowlisted_classes:** `AgentLiteralPolicyClasses` — Typed reusable literal classes.
    
</dd>
</dl>

<dl>
<dd>

**allowlisted_values:** `AgentLiteralPolicyValues` — Exact reusable values scoped by tools and environments.
    
</dd>
</dl>

<dl>
<dd>

**default:** `UpdateAgentLiteralPolicyRequestDefault` — The remediation for literals that are not explicitly allowed.
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `typing.Optional[int]` — The current literal-policy revision used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Skill
<details><summary><code>client.agent.skill.<a href="src/zep_cloud/agent/skill/client.py">create</a>(...) -> AgentSkill</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, SkillDefinition
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.create(
    agent_uuid="agent_uuid",
    definition=SkillDefinition(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**definition:** `SkillDefinition` 
    
</dd>
</dl>

<dl>
<dd>

**skill_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.<a href="src/zep_cloud/agent/skill/client.py">import_package</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a portable Skill archive. The completed Task returns `{"result":{"skill_uuid":"<uuid>"}}`. Approve that Skill before retrieval.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.agent.skill.import_package(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]` — Portable Skill ZIP archive
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.<a href="src/zep_cloud/agent/skill/client.py">list</a>(...) -> Pagev4AgentSkillSearchHit</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.list(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 20)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**environments:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.<a href="src/zep_cloud/agent/skill/client.py">search</a>(...) -> AgentSkillSearchResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.search(
    agent_uuid="agent_uuid",
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 20)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**environments:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**include_markdown:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**markdown_format:** `typing.Optional[AgentSkillSearchRequestMarkdownFormat]` 

MarkdownFormat selects the form of inline `markdown`. `agent` (the
default) returns the Skill text that an Agent needs: no evidence
markers, the description only in the frontmatter, and no empty
sections. `full` returns the stored SKILL.md with its evidence markers.
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.<a href="src/zep_cloud/agent/skill/client.py">get</a>(...) -> AgentSkill</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.get(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.<a href="src/zep_cloud/agent/skill/client.py">approve</a>(...) -> AgentSkillAdmissionDecision</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.approve(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    expected_version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.<a href="src/zep_cloud/agent/skill/client.py">retire</a>(...) -> AgentSkill</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.retire(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    expected_version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.<a href="src/zep_cloud/agent/skill/client.py">create_version</a>(...) -> AgentSkillVersion</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, SkillDefinition
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.create_version(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    definition=SkillDefinition(),
    expected_version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**definition:** `SkillDefinition` 
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Split
<details><summary><code>client.agent.split.<a href="src/zep_cloud/agent/split/client.py">plan</a>(...) -> AgentSplitPlan</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, AgentSplitPlanDestinationRequest, CreateAgentRequest, AgentSplitPlanSkillSelectionRequest
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.split.plan(
    agent_uuid="agent_uuid",
    destinations=[
        AgentSplitPlanDestinationRequest(
            agent=CreateAgentRequest(
                agent_id="agent_id",
                name="name",
                security_domain="security_domain",
            ),
            skills=[
                AgentSplitPlanSkillSelectionRequest(
                    skill_uuid="skill_uuid",
                    skill_version_uuid="skill_version_uuid",
                    version=1,
                )
            ],
        )
    ],
    expected_revision=1,
    rationale="rationale",
    review_acknowledged=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Source Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**destinations:** `typing.List[AgentSplitPlanDestinationRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**rationale:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**review_acknowledged:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Trajectory
<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">create</a>(...) -> AgentTrajectory</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.create(
    agent_uuid="agent_uuid",
    objective="objective",
    task_family="task_family",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**objective:** `str` — The task-instance objective captured for this attempt.
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `str` — The task-family slug.
    
</dd>
</dl>

<dl>
<dd>

**learn_from:** `typing.Optional[bool]` — Whether eligible evidence may participate in learning. Defaults to true.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Developer metadata used to organize and filter Trajectories.
    
</dd>
</dl>

<dl>
<dd>

**parent_trajectory_uuid:** `typing.Optional[str]` — The parent Trajectory UUID when this attempt retries an earlier attempt.
    
</dd>
</dl>

<dl>
<dd>

**trajectory_id:** `typing.Optional[str]` — The optional customer-assigned identifier, unique within the Agent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">list</a>(...) -> AgentTrajectoryPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.list(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `typing.Optional[str]` — Filter by owning Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**source_kind:** `typing.Optional[TrajectoryListRequestSourceKind]` — Source kind
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Filters to Trajectories whose metadata contains these key-value pairs.
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[AgentTrajectoryOutcome]` — Filters to one reported outcome.
    
</dd>
</dl>

<dl>
<dd>

**parent_trajectory_uuid:** `typing.Optional[str]` — Filters to direct retries of this parent Trajectory.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AgentTrajectoryLifecycle]` — Filters to one lifecycle state.
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` — Filters to an exact task-family slug.
    
</dd>
</dl>

<dl>
<dd>

**verification:** `typing.Optional[AgentTrajectoryVerification]` — Filters to one verification strength.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">get</a>(...) -> AgentTrajectory</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.get(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">delete</a>(...) -> AgentTrajectorySourceDeletionResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.delete(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `DeleteAgentTrajectoryRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">update</a>(...) -> AgentTrajectory</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.update(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current Trajectory revision used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` — Replacement task-family slug. Set to null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">abandon</a>(...) -> AgentTrajectoryFinalizationResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.abandon(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
    highest_accepted_sequence=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**highest_accepted_sequence:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**assertion_uuid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**missing_sequence_ranges:** `typing.Optional[typing.List[AgentTrajectorySequenceRange]]` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**verification:** `typing.Optional[AgentTrajectoryVerification]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">close</a>(...) -> AgentTrajectoryFinalizationResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.close(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**closing_sequence:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**missing_sequence_ranges:** `typing.Optional[typing.List[AgentTrajectorySequenceRange]]` 
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[AgentTrajectoryOutcome]` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**verification:** `typing.Optional[AgentTrajectoryVerification]` 
    
</dd>
</dl>

<dl>
<dd>

**verifier:** `typing.Optional[AgentTrajectoryCloseVerifier]` 
    
</dd>
</dl>

<dl>
<dd>

**verifier_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">correct_task_family</a>(...) -> AgentTrajectoryFinalizationResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.correct_task_family(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
    expected_revision=1,
    reason="reason",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current Trajectory revision used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — Why the terminal Trajectory classification is being corrected.
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` — Replacement task-family slug. Set to null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">list_events</a>(...) -> AgentTrajectoryEventPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.list_events(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">append_event</a>(...) -> AgentTrajectoryEvent</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.append_event(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
    event_type="input_reference",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `AgentTrajectoryEventType` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[AgentTrajectoryEventContext]` 
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**occurred_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sequence:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[typing.List[AgentTrajectoryEventSource]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">delete_event</a>(...) -> AgentTrajectorySourceDeletionResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.delete_event(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
    event_uuid="event_uuid",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**event_uuid:** `str` — Event UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `DeleteAgentTrajectoryRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">reopen</a>(...) -> AgentTrajectory</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.reopen(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current Trajectory revision used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">get_summary</a>(...) -> AgentTrajectorySummaryVersion</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.get_summary(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory.<a href="src/zep_cloud/agent/trajectory/client.py">list_summary_versions</a>(...) -> AgentTrajectorySummaryPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory.list_summary_versions(
    agent_uuid="agent_uuid",
    trajectory_uuid="trajectory_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` — Trajectory UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent TrajectoryImport
<details><summary><code>client.agent.trajectory_import.<a href="src/zep_cloud/agent/trajectory_import/client.py">list</a>(...) -> TrajectoryImportPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List trajectory imports that belong to this Agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.list(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory_import.<a href="src/zep_cloud/agent/trajectory_import/client.py">create</a>(...) -> TrajectoryImport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a scheduled import or queue a one-time import. Example request: `{"connection_uuid":"8c78a85e-eac2-4f57-b5f5-59a68a1e77a1","provider_project_id":"project-123","name":"Support traces","selection":{"trace_ids":["trace-123"]},"mapping":{"task_family":{"source":"fixed","value":"support"}}}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.create(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**connection_uuid:** `typing.Optional[str]` — ConnectionUUID identifies the project trace connection.
    
</dd>
</dl>

<dl>
<dd>

**learn_from:** `typing.Optional[bool]` — LearnFrom controls whether imported evidence can support Skills.
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Optional[TrajectoryMapping]` — Mapping defines how source traces become Trajectories. Example: {"task_family":{"source":"fixed","value":"support"}}.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name is the import display name.
    
</dd>
</dl>

<dl>
<dd>

**on_source_change:** `typing.Optional[str]` — OnSourceChange defines how changed source traces are handled.
    
</dd>
</dl>

<dl>
<dd>

**provider_project_id:** `typing.Optional[str]` — ProviderProjectID is the source provider project identifier.
    
</dd>
</dl>

<dl>
<dd>

**require_review:** `typing.Optional[bool]` — RequireReview requires review for candidates backed by this import.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[TrajectoryImportSchedule]` — Schedule enables recurring imports when supplied. Example: {"interval_hours":4,"start_from":"24h","settle_minutes":5,"max_open_hours":24}.
    
</dd>
</dl>

<dl>
<dd>

**selection:** `typing.Optional[TrajectoryImportSelection]` — Selection defines the traces to import. Example: {"trace_ids":["trace_123"]}.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory_import.<a href="src/zep_cloud/agent/trajectory_import/client.py">get</a>(...) -> TrajectoryImport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one trajectory import. The response does not include its source cursor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.get(
    agent_uuid="agent_uuid",
    import_uuid="import_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `str` — Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory_import.<a href="src/zep_cloud/agent/trajectory_import/client.py">delete</a>(...) -> typing.Optional[Task]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set `trajectories=delete` to queue asynchronous Trajectory deletion. The default keeps Trajectories. Example query: `?trajectories=delete`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.delete(
    agent_uuid="agent_uuid",
    import_uuid="import_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `str` — Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**trajectories:** `typing.Optional[TrajectoryImportDeleteRequestTrajectories]` — Whether to delete imported Trajectories
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory_import.<a href="src/zep_cloud/agent/trajectory_import/client.py">update</a>(...) -> TrajectoryImport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use `expected_revision` to reject a stale update. Example request: `{"expected_revision":1,"name":"Updated support traces"}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.update(
    agent_uuid="agent_uuid",
    import_uuid="import_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `str` — Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `typing.Optional[int]` — ExpectedRevision is the current import revision.
    
</dd>
</dl>

<dl>
<dd>

**learn_from:** `typing.Optional[bool]` — LearnFrom is the new learning setting, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Optional[TrajectoryMapping]` — Mapping is the new mapping, when supplied. Example: {"task_family":{"source":"fixed","value":"support"}}.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name is the new import name, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**on_source_change:** `typing.Optional[str]` — OnSourceChange is the new change policy, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**require_review:** `typing.Optional[bool]` — RequireReview is the new review setting, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[TrajectoryImportSchedule]` — Schedule is the new schedule, when supplied. Example: {"interval_hours":4,"start_from":"24h","settle_minutes":5,"max_open_hours":24}.
    
</dd>
</dl>

<dl>
<dd>

**selection:** `typing.Optional[TrajectoryImportSelection]` — Selection is the new selection, when supplied. Example: {"trace_ids":["trace_123"]}.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory_import.<a href="src/zep_cloud/agent/trajectory_import/client.py">pause</a>(...) -> TrajectoryImport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pause a scheduled trajectory import. One-time imports cannot be paused.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.pause(
    agent_uuid="agent_uuid",
    import_uuid="import_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `str` — Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory_import.<a href="src/zep_cloud/agent/trajectory_import/client.py">resume</a>(...) -> TrajectoryImport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resume a scheduled trajectory import. Zep verifies credentials first when they caused the pause.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.resume(
    agent_uuid="agent_uuid",
    import_uuid="import_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `str` — Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Verifier
<details><summary><code>client.agent.verifier.<a href="src/zep_cloud/agent/verifier/client.py">list</a>(...) -> Pagev4AgentVerifier</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.verifier.list(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Page cursor
    
</dd>
</dl>

<dl>
<dd>

**class:** `typing.Optional[str]` — Filters to an exact immutable verifier class.
    
</dd>
</dl>

<dl>
<dd>

**principal_id:** `typing.Optional[str]` — Filters to registrations bound to this exact principal identifier.
    
</dd>
</dl>

<dl>
<dd>

**principal_type:** `typing.Optional[str]` — Filters to registrations bound to this principal type.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AgentVerifierStatus]` — Filters to active or revoked registrations. Omit to include both.
    
</dd>
</dl>

<dl>
<dd>

**verifier_id:** `typing.Optional[str]` — Filters to an exact developer-assigned verifier identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.verifier.<a href="src/zep_cloud/agent/verifier/client.py">get</a>(...) -> AgentVerifier</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.verifier.get(
    agent_uuid="agent_uuid",
    verifier_uuid="verifier_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**verifier_uuid:** `str` — Verifier UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.verifier.<a href="src/zep_cloud/agent/verifier/client.py">update</a>(...) -> AgentVerifier</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.verifier.update(
    agent_uuid="agent_uuid",
    verifier_uuid="verifier_uuid",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**verifier_uuid:** `str` — Verifier UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current verifier revision used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**capabilities:** `typing.Optional[typing.Dict[str, typing.Any]]` — Replacement capabilities. Set to null to clear them.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Replacement metadata. Set to null to clear it.
    
</dd>
</dl>

<dl>
<dd>

**permitted_strengths:** `typing.Optional[typing.List[AgentVerificationStrength]]` — Replacement permitted strengths. The list cannot be empty or null.
    
</dd>
</dl>

<dl>
<dd>

**principal_bindings:** `typing.Optional[typing.List[AgentVerifierPrincipalBindingInput]]` — Replacement exact principal bindings. The list cannot be empty or null.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.verifier.<a href="src/zep_cloud/agent/verifier/client.py">invalidate_evidence</a>(...) -> AgentVerifierEvidenceInvalidationResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.verifier.invalidate_evidence(
    agent_uuid="agent_uuid",
    verifier_uuid="verifier_uuid",
    reason="reason",
    verifier_revisions=[
        1
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**verifier_uuid:** `str` — Verifier UUID
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — Why evidence from these verifier revisions is invalid.
    
</dd>
</dl>

<dl>
<dd>

**verifier_revisions:** `typing.List[int]` — Verifier revisions whose accepted evidence is no longer valid.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.verifier.<a href="src/zep_cloud/agent/verifier/client.py">revoke</a>(...) -> AgentVerifier</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.verifier.revoke(
    agent_uuid="agent_uuid",
    verifier_uuid="verifier_uuid",
    expected_revision=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**verifier_uuid:** `str` — Verifier UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current verifier revision used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Skill Candidate
<details><summary><code>client.agent.skill.candidate.<a href="src/zep_cloud/agent/skill/candidate/client.py">list</a>(...) -> Pagev4AgentSkillCandidateReviewSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.candidate.list(
    agent_uuid="agent_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.candidate.<a href="src/zep_cloud/agent/skill/candidate/client.py">get</a>(...) -> AgentSkillCandidateReview</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.candidate.get(
    agent_uuid="agent_uuid",
    review_uuid="review_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**review_uuid:** `str` — Candidate review UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Skill Evaluation
<details><summary><code>client.agent.skill.evaluation.<a href="src/zep_cloud/agent/skill/evaluation/client.py">create_for_candidate</a>(...) -> AgentSkillCandidateEvaluation</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.evaluation.create_for_candidate(
    agent_uuid="agent_uuid",
    review_uuid="review_uuid",
    candidate_uuid="candidate_uuid",
    evaluated_by="customer",
    evaluator_version="evaluator_version",
    expected_revision=1,
    verdict="succeeded",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**review_uuid:** `str` — Candidate review UUID
    
</dd>
</dl>

<dl>
<dd>

**candidate_uuid:** `str` — Candidate UUID
    
</dd>
</dl>

<dl>
<dd>

**evaluated_by:** `CreateAgentSkillCandidateEvaluationRequestEvaluatedBy` 
    
</dd>
</dl>

<dl>
<dd>

**evaluator_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**verdict:** `CreateAgentSkillCandidateEvaluationRequestVerdict` 
    
</dd>
</dl>

<dl>
<dd>

**controlled_test:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**evidence_reference:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Dict[str, float]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.evaluation.<a href="src/zep_cloud/agent/skill/evaluation/client.py">create</a>(...) -> AgentSkillEvaluation</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.evaluation.create(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    evaluated_by="customer",
    evaluator_version="evaluator_version",
    skill_version=1,
    verdict="succeeded",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**evaluated_by:** `CreateAgentSkillEvaluationRequestEvaluatedBy` 
    
</dd>
</dl>

<dl>
<dd>

**evaluator_version:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**skill_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**verdict:** `CreateAgentSkillEvaluationRequestVerdict` 
    
</dd>
</dl>

<dl>
<dd>

**controlled_test:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**evidence_reference:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Dict[str, float]]` 
    
</dd>
</dl>

<dl>
<dd>

**use_uuid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Skill Publication
<details><summary><code>client.agent.skill.publication.<a href="src/zep_cloud/agent/skill/publication/client.py">lookup</a>(...) -> AgentSkillPublicationLineage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find a destination Skill by its source Agent, Skill, and version. The endpoint returns 404 until an automatic publication is ready or after it is invalidated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.publication.lookup(
    agent_uuid="agent_uuid",
    source_agent_uuid="source_agent_uuid",
    source_skill_uuid="source_skill_uuid",
    source_version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Destination Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**source_agent_uuid:** `str` — Source Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**source_skill_uuid:** `str` — Source Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**source_version:** `int` — Source version number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.publication.<a href="src/zep_cloud/agent/skill/publication/client.py">get</a>(...) -> AgentSkillPublicationLineage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the publication that created a destination Skill. Use its source version and policy identity to verify a copied Skill. The endpoint returns 404 for unpublished and invalidated Skills.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.publication.get(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Destination Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Destination Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Skill Evidence
<details><summary><code>client.agent.skill.evidence.<a href="src/zep_cloud/agent/skill/evidence/client.py">list</a>(...) -> Pagev4AgentSkillEvidence</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.evidence.list(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Skill Relation
<details><summary><code>client.agent.skill.relation.<a href="src/zep_cloud/agent/skill/relation/client.py">list</a>(...) -> Pagev4AgentSkillRelationship</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.relation.list(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[typing.Union[RelationListRequestKindItem, typing.Sequence[RelationListRequestKindItem]]]` — Relationship kinds
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Skill Version
<details><summary><code>client.agent.skill.version.<a href="src/zep_cloud/agent/skill/version/client.py">restore_version</a>(...) -> AgentSkillVersion</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.version.restore_version(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    expected_version=1,
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.version.<a href="src/zep_cloud/agent/skill/version/client.py">list</a>(...) -> Pagev4AgentSkillVersion</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.version.list(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (maximum 100)
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**markdown_format:** `typing.Optional[VersionListRequestMarkdownFormat]` — Markdown form: agent (default) or full
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.version.<a href="src/zep_cloud/agent/skill/version/client.py">compare</a>(...) -> AgentSkillVersionComparison</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.version.compare(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    from_version=1,
    to_version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**from_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**to_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.version.<a href="src/zep_cloud/agent/skill/version/client.py">get</a>(...) -> AgentSkillVersion</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.version.get(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` — Skill version
    
</dd>
</dl>

<dl>
<dd>

**markdown_format:** `typing.Optional[VersionGetRequestMarkdownFormat]` — Markdown form: agent (default) or full
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Skill Use
<details><summary><code>client.agent.skill.use.<a href="src/zep_cloud/agent/skill/use/client.py">create</a>(...) -> AgentSkillUse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.use.create(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    search_id="search_id",
    trajectory_uuid="trajectory_uuid",
    usage="selected",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**search_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**trajectory_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**usage:** `CreateAgentSkillUseRequestUsage` 
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[AddAgentSkillUseOutcomeRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**reason_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.use.<a href="src/zep_cloud/agent/skill/use/client.py">add_outcome</a>(...) -> AgentSkillUseOutcome</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.use.add_outcome(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    use_uuid="use_uuid",
    outcome="succeeded",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**use_uuid:** `str` — Skill use UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddAgentSkillUseOutcomeRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Skill Export
<details><summary><code>client.agent.skill.export.<a href="src/zep_cloud/agent/skill/export/client.py">create</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.export.create(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    version=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` — Skill version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.skill.export.<a href="src/zep_cloud/agent/skill/export/client.py">get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.skill.export.get(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    version=1,
    task_uuid="task_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**skill_uuid:** `str` — Skill UUID
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` — Skill version
    
</dd>
</dl>

<dl>
<dd>

**task_uuid:** `str` — Export Task UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent TrajectoryImport Run
<details><summary><code>client.agent.trajectory_import.run.<a href="src/zep_cloud/agent/trajectory_import/run/client.py">list</a>(...) -> TrajectoryImportRunPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List runs that belong to this trajectory import.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.run.list(
    agent_uuid="agent_uuid",
    import_uuid="import_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `str` — Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory_import.run.<a href="src/zep_cloud/agent/trajectory_import/run/client.py">create</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a pending run and its Task. This operation does not start the run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.run.create(
    agent_uuid="agent_uuid",
    import_uuid="import_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `str` — Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.trajectory_import.run.<a href="src/zep_cloud/agent/trajectory_import/run/client.py">get</a>(...) -> TrajectoryImportRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one run that belongs to this trajectory import.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.run.get(
    agent_uuid="agent_uuid",
    import_uuid="import_uuid",
    run_uuid="run_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `str` — Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**run_uuid:** `str` — Run UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent TrajectoryImport Run Item
<details><summary><code>client.agent.trajectory_import.run.item.<a href="src/zep_cloud/agent/trajectory_import/run/item/client.py">list</a>(...) -> TrajectoryImportRunItemPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List trace results for this run. Run items do not include source payload.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.agent.trajectory_import.run.item.list(
    agent_uuid="agent_uuid",
    import_uuid="import_uuid",
    run_uuid="run_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_uuid:** `str` — Agent UUID
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `str` — Trajectory import UUID
    
</dd>
</dl>

<dl>
<dd>

**run_uuid:** `str` — Run UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Graph DocumentSummary
<details><summary><code>client.graph.document_summary.<a href="src/zep_cloud/graph/document_summary/client.py">list</a>(...) -> DocumentSummaryPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.document_summary.list(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ArtifactListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Graph Episode
<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">list_for_document</a>(...) -> EpisodePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.episode.list_for_document(
    graph_uuid="graph_uuid",
    document_id="document_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Document ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">add</a>(...) -> AddEpisodeResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.episode.add(
    graph_uuid="graph_uuid",
    data="data",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**data:** `str` — The episode content to add to the graph.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 

The episode's reference time, used for temporal reasoning rather than
ingestion time.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — Groups this episode as a chunk of a document on the graph.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to store on the episode. Max 10 keys. Values must be strings, numbers, booleans, or arrays of scalars.
    
</dd>
</dl>

<dl>
<dd>

**source_description:** `typing.Optional[str]` — A description of the source of this episode.
    
</dd>
</dl>

<dl>
<dd>

**strict_ontology:** `typing.Optional[bool]` 

When true, prevents extraction of generic entity nodes that do not match
the configured ontology.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[AddEpisodeRequestType]` — The data format of the episode: text, json, or message. Defaults to text.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">list</a>(...) -> EpisodePage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the episodes of a graph. `filters.mentioned_node_uuids` restricts
the results to episodes that mention any of the listed node UUIDs. The
list can also contain episode UUIDs: an episode UUID matches that episode,
so one request can return a known set of episodes. At most 256 entries.
`filters.metadata_filters` restricts the results to episodes whose stored
metadata matches the predicate.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.episode.list(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ArtifactListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[EpisodeListRequestOrderBy]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[EpisodeListRequestOrder]` — Sort direction: asc or desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">get</a>(...) -> Episode</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.episode.get(
    graph_uuid="graph_uuid",
    episode_uuid="episode_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**episode_uuid:** `str` — Episode UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">delete</a>(...) -> AsyncResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.episode.delete(
    graph_uuid="graph_uuid",
    episode_uuid="episode_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**episode_uuid:** `str` — Episode UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">update</a>(...) -> Episode</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.episode.update(
    graph_uuid="graph_uuid",
    episode_uuid="episode_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**episode_uuid:** `str` — Episode UUID
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to merge onto the episode; a key set to null is removed. Max 10 keys after the merge. Values must be strings, numbers, booleans, or arrays of scalars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">get_debug_logs</a>(...) -> EpisodeDebugLog</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the ingestion workflow log of an episode. The log exists only when debug logging was enabled for the project when the episode was ingested (see `debug_log.enable`). The log holds episode content, so an API key with an ABAC policy needs an explicit grant of this action; the `readonly` macro does not grant it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.episode.get_debug_logs(
    graph_uuid="graph_uuid",
    episode_uuid="episode_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**episode_uuid:** `str` — Episode UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">list_ingestion_traces</a>(...) -> IngestionTracePage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the ingestion traces of an episode, oldest first. Each trace records the input and the output of one ingestion step, with an explanation on each output entry that has one. Traces exist only when ingestion tracing was enabled for the project when the episode was ingested (see `debug_log.enable`). An episode with no traces returns a page with an empty `items` array. Traces hold episode content, prompt input, and model output, so an API key with an ABAC policy needs an explicit grant of this action; the `readonly` macro does not grant it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.episode.list_ingestion_traces(
    graph_uuid="graph_uuid",
    episode_uuid="episode_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**episode_uuid:** `str` — Episode UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Graph Edge
<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">add</a>(...) -> AddEdgesResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds 1 to 100 edges. A name creates a node when deduplicate is false. When deduplicate is true, Zep matches a node by name first.
Example: {"edges":[{"fact":"Ada works at Acme Corp","fact_name":"WORKS_AT","source_node":{"uuid":"f47ac10b-58cc-4372-a567-0e02b2c3d479"},"target_node":{"uuid":"f47ac10b-58cc-4372-a567-0e02b2c3d480"}},{"fact":"Ada leads a team","fact_name":"LEADS","source_node":{"name":"Ada Lovelace","labels":["Person"]},"target_node":{"name":"Engineering","labels":["Department"]}}],"deduplicate":false}
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, EdgeInput, EdgeNodeRef
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.edge.add(
    graph_uuid="graph_uuid",
    edges=[
        EdgeInput(
            fact="Ada works at Acme Corp",
            fact_name="WORKS_AT",
            source_node=EdgeNodeRef(),
            target_node=EdgeNodeRef(),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**edges:** `typing.List[EdgeInput]` — The edges to add to the graph. The request accepts 1 to 100 edges.
    
</dd>
</dl>

<dl>
<dd>

**deduplicate:** `typing.Optional[bool]` 

When true, Zep compares each edge with graph edges and can merge a
duplicate or invalidate a contradicted edge. This adds an LLM call per
edge. The default is false.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">list</a>(...) -> EdgePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.edge.list(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ArtifactListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">get</a>(...) -> Edge</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.edge.get(
    graph_uuid="graph_uuid",
    edge_uuid="edge_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**edge_uuid:** `str` — Edge UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">delete</a>(...) -> AsyncResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.edge.delete(
    graph_uuid="graph_uuid",
    edge_uuid="edge_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**edge_uuid:** `str` — Edge UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">update</a>(...) -> Edge</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one edge. When the edge belongs to a hyperedge, changing fact
rewrites it on every member of that hyperedge in one all-or-nothing
write, because the members share it. Attribute-only edits touch this
edge alone.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.edge.update(
    graph_uuid="graph_uuid",
    edge_uuid="edge_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**edge_uuid:** `str` — Edge UUID
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, typing.Any]]` 

Additional attributes to merge onto the edge; a key set to null is
removed.
    
</dd>
</dl>

<dl>
<dd>

**fact:** `typing.Optional[str]` 

The fact text describing the relationship between the source and target
nodes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Graph Hyperedge
<details><summary><code>client.graph.hyperedge.<a href="src/zep_cloud/graph/hyperedge/client.py">add</a>(...) -> AddHyperedgeResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates one hyperedge: a fact that relates more than two nodes, written
onto one member edge per node pair. The member edges must span at least
three distinct nodes, since two nodes are a pair of edges rather than a
hyperedge; a single pair uses graph.edge.add. Zep assigns the hyperedge
identifier and every member edge identifier at accept time, and the
members become readable when the task completes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, HyperedgeInput, EdgeNodeRef
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.hyperedge.add(
    graph_uuid="graph_uuid",
    edges=[
        HyperedgeInput(
            name="name",
            source_node=EdgeNodeRef(),
            target_node=EdgeNodeRef(),
        )
    ],
    fact="fact",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**edges:** `typing.List[HyperedgeInput]` 

The member edges to create. Each pair becomes one edge carrying the
shared fact.
    
</dd>
</dl>

<dl>
<dd>

**fact:** `str` — The natural-language fact, written onto every member edge.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, typing.Any]]` — Additional attributes to store on every member edge.
    
</dd>
</dl>

<dl>
<dd>

**expired_at:** `typing.Optional[str]` — The time at which the fact was superseded or invalidated.
    
</dd>
</dl>

<dl>
<dd>

**invalid_at:** `typing.Optional[str]` — The time at which the fact stopped being true.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata attached to the episode created for this hyperedge.
    
</dd>
</dl>

<dl>
<dd>

**valid_at:** `typing.Optional[str]` — The time at which the fact became true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.hyperedge.<a href="src/zep_cloud/graph/hyperedge/client.py">list</a>(...) -> HyperedgePage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the graph's hyperedges. A hyperedge is listed while it has at
least one member edge. Supported filters are node_uuids, edge_uuids and
episode_uuids: a hyperedge matches a list when any of its members does,
and must match every list supplied.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.hyperedge.list(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ArtifactListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[HyperedgeListRequestOrderBy]` — Sort key: uuid or created_at
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[HyperedgeListRequestOrder]` — Sort direction: asc or desc
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.hyperedge.<a href="src/zep_cloud/graph/hyperedge/client.py">get</a>(...) -> Hyperedge</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one hyperedge assembled from its member edges. The fact and the
validity timestamps are shared by every member and are reported on the
hyperedge; each member reports only its own name and endpoints.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.hyperedge.get(
    graph_uuid="graph_uuid",
    hyperedge_uuid="hyperedge_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**hyperedge_uuid:** `str` — Hyperedge UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.hyperedge.<a href="src/zep_cloud/graph/hyperedge/client.py">delete</a>(...) -> AsyncResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes every member edge of the hyperedge. After the task completes the
hyperedge and each of its members are gone.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.hyperedge.delete(
    graph_uuid="graph_uuid",
    hyperedge_uuid="hyperedge_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**hyperedge_uuid:** `str` — Hyperedge UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.hyperedge.<a href="src/zep_cloud/graph/hyperedge/client.py">update</a>(...) -> Hyperedge</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the shared fact and writes it onto every member edge in one
all-or-nothing write: either every member carries the new fact or none
does. Only fact is accepted, because it is the only field the members
share. name belongs to each member edge, and membership changes use
create_edge and delete_edge. Updating fact on one member through
graph.edge.update cascades the same way.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.hyperedge.update(
    graph_uuid="graph_uuid",
    hyperedge_uuid="hyperedge_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**hyperedge_uuid:** `str` — Hyperedge UUID
    
</dd>
</dl>

<dl>
<dd>

**fact:** `typing.Optional[str]` — The natural-language fact, rewritten onto every member edge.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.hyperedge.<a href="src/zep_cloud/graph/hyperedge/client.py">create_edge</a>(...) -> AddHyperedgeEdgeResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds one member edge to an existing hyperedge. The new member inherits the
hyperedge's fact and timestamps and joins its episodes, so only its own
name and node pair are supplied.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, EdgeNodeRef
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.hyperedge.create_edge(
    graph_uuid="graph_uuid",
    hyperedge_uuid="hyperedge_uuid",
    name="name",
    source_node=EdgeNodeRef(),
    target_node=EdgeNodeRef(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**hyperedge_uuid:** `str` — Hyperedge UUID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the new member edge, in upper snake case.
    
</dd>
</dl>

<dl>
<dd>

**source_node:** `EdgeNodeRef` — The source node of the new member.
    
</dd>
</dl>

<dl>
<dd>

**target_node:** `EdgeNodeRef` — The target node of the new member.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.hyperedge.<a href="src/zep_cloud/graph/hyperedge/client.py">delete_edge</a>(...) -> AsyncResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes one member edge from the hyperedge. The remaining members stay in
the hyperedge, and deleting the last member removes the hyperedge itself.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.hyperedge.delete_edge(
    graph_uuid="graph_uuid",
    hyperedge_uuid="hyperedge_uuid",
    edge_uuid="edge_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**hyperedge_uuid:** `str` — Hyperedge UUID
    
</dd>
</dl>

<dl>
<dd>

**edge_uuid:** `str` — Edge UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Graph Node
<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">add</a>(...) -> AddNodesResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep, NodeInput
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.node.add(
    graph_uuid="graph_uuid",
    nodes=[
        NodeInput(
            name="name",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**nodes:** `typing.List[NodeInput]` — The nodes to add to the graph.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">list</a>(...) -> NodePage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.node.list(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ArtifactListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[NodeListRequestOrderBy]` — Sort key: uuid (default) or degree
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[NodeListRequestOrder]` — Sort direction: asc or desc (default desc)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">get</a>(...) -> Node</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.node.get(
    graph_uuid="graph_uuid",
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**node_uuid:** `str` — Node UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">delete</a>(...) -> AsyncResult</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.node.delete(
    graph_uuid="graph_uuid",
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**node_uuid:** `str` — Node UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">update</a>(...) -> Node</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.node.update(
    graph_uuid="graph_uuid",
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**node_uuid:** `str` — Node UUID
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, typing.Any]]` 

Additional attributes to merge onto the node; a key set to null is
removed.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The node's name.
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[str]` — A summary of the node.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">list_neighbors</a>(...) -> NeighborPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.node.list_neighbors(
    graph_uuid="graph_uuid",
    node_uuid="node_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**node_uuid:** `str` — Node UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[NodeListNeighborsRequestOrderBy]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[NodeListNeighborsRequestOrder]` — Sort direction: asc or desc
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[NeighborsRequestDirection]` — The edge orientation to follow from the node: in, out, or both.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Filters constraining the connecting edges and the neighbor nodes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Graph Observation
<details><summary><code>client.graph.observation.<a href="src/zep_cloud/graph/observation/client.py">list</a>(...) -> ObservationPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.observation.list(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ArtifactListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.observation.<a href="src/zep_cloud/graph/observation/client.py">get</a>(...) -> Observation</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.observation.get(
    graph_uuid="graph_uuid",
    observation_uuid="observation_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**observation_uuid:** `str` — Observation UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Graph ThreadSummary
<details><summary><code>client.graph.thread_summary.<a href="src/zep_cloud/graph/thread_summary/client.py">list</a>(...) -> ThreadSummaryPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.graph.thread_summary.list(
    graph_uuid="graph_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_uuid:** `str` — Graph UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `ArtifactListRequest` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Thread Message
<details><summary><code>client.thread.message.<a href="src/zep_cloud/thread/message/client.py">get</a>(...) -> Message</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.message.get(
    thread_uuid="thread_uuid",
    message_uuid="message_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_uuid:** `str` — Thread UUID
    
</dd>
</dl>

<dl>
<dd>

**message_uuid:** `str` — Message UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.message.<a href="src/zep_cloud/thread/message/client.py">update</a>(...) -> Message</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.thread.message.update(
    thread_uuid="thread_uuid",
    message_uuid="message_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_uuid:** `str` — Thread UUID
    
</dd>
</dl>

<dl>
<dd>

**message_uuid:** `str` — Message UUID
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to merge onto the message; a key set to null is removed. Max 10 keys after the merge. Values must be strings, numbers, booleans, or arrays of scalars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TraceConnection Project
<details><summary><code>client.trace_connection.project.<a href="src/zep_cloud/trace_connection/project/client.py">list</a>(...) -> TraceProviderProjectPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List provider projects with the `limit` and `cursor` query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.trace_connection.project.list(
    connection_uuid="connection_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_uuid:** `str` — Trace connection UUID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size from 1 to 100; default 50
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Provider page cursor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TraceConnection Trace
<details><summary><code>client.trace_connection.trace.<a href="src/zep_cloud/trace_connection/trace/client.py">get</a>(...) -> SourceTraceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one trace and optionally preview a mapping. Example body: `{"provider_project_id":"project_123","trace_id":"trace-123","mapping":{"task_family":{"source":"fixed","value":"support"}}}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.trace_connection.trace.get(
    connection_uuid="connection_uuid",
    provider_project_id="project_123",
    trace_id="trace_123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_uuid:** `str` — Trace connection UUID
    
</dd>
</dl>

<dl>
<dd>

**provider_project_id:** `str` — ProviderProjectID is the provider project identifier.
    
</dd>
</dl>

<dl>
<dd>

**trace_id:** `str` — TraceID is the provider trace identifier.
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Optional[TrajectoryMapping]` — Mapping is an optional mapping preview configuration. Example: {"task_family":{"source":"fixed","value":"support"}}.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trace_connection.trace.<a href="src/zep_cloud/trace_connection/trace/client.py">list</a>(...) -> SourceTracePage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Filter provider traces. Example body: `{"provider_project_id":"project_123","filter":{"started_after":"2026-01-01T00:00:00Z"}}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import Zep
from zep_cloud.environment import ZepEnvironment

client = Zep(
    api_key="<value>",
    environment=ZepEnvironment.DEFAULT,
)

client.trace_connection.trace.list(
    connection_uuid="connection_uuid",
    provider_project_id="project_123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_uuid:** `str` — Trace connection UUID
    
</dd>
</dl>

<dl>
<dd>

**provider_project_id:** `str` — ProviderProjectID is the provider project identifier.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size from 1 to 100; default 25
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**filter:** `typing.Optional[TraceFilter]` — Filter contains provider trace filters. Example: {"started_after":"2026-01-01T00:00:00Z"}.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

