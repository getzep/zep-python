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
    agent_id="payments-agent",
    name="Refund a duplicate charge",
    security_domain="customer:support",
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[AgentListRequestOrderBy]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[AgentListRequestOrder]` — asc or desc
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filters to the exact developer-assigned Agent identifier.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — The developer supplies filters to the exact deployment identifier.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Filters to Agents whose metadata contains these key-value pairs.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 

The developer supplies filters to Agents whose name, Agent identifier, deployment identifier,
or deployment version contains this text. Matching is case-insensitive.
    
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

**memory_settings:** `typing.Optional[AgentMemorySettings]` — Replacement Agent Skills settings. Set to null to restore defaults.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Declare a breaking Agent deployment change. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.declare_breaking_change(
    agent_uuid="agent_uuid",
    expected_revision=1,
    version="2026.09.01",
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

The developer supplies the current Agent revision for optimistic concurrency.
It must be at least 1.
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — The developer supplies the new deployment version. It must differ from the current version.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Agent context. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**environments:** `typing.Optional[typing.List[AgentContextResource]]` — The developer supplies environment names used by the Skill. At most 32.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[str]` — The developer supplies a Skill kind. At most 64.
    
</dd>
</dl>

<dl>
<dd>

**max_characters:** `typing.Optional[int]` — The developer sets the maximum number of characters in the context response.
    
</dd>
</dl>

<dl>
<dd>

**models:** `typing.Optional[typing.List[AgentContextResource]]` — The developer supplies models used for this evaluation. At most 32.
    
</dd>
</dl>

<dl>
<dd>

**objective:** `typing.Optional[str]` — The developer supplies the task-instance objective. At most 512.
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` — The developer supplies the task-family slug. At most 128.
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[AgentContextResource]]` — The developer supplies tool names used by the Skill. At most 32.
    
</dd>
</dl>

<dl>
<dd>

**trace_uuid:** `typing.Optional[str]` — The developer supplies the UUID of the source Trace.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">query_stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Experimental. Retrieves the graph records for a natural-language question about a graph with a read-only retrieval loop. By default, the response has the retrieved records and no answer. Set `generate_answer` to `true` to also get an answer that a model writes from the records, with the cited graph items. Set `stream` to `true` to get the retrieval calls as server-sent events. The default mode is fast. fast: A decision model selects the types of search for each round and stops when it has enough context. The query runs at most 3 search rounds. deep: A model plans its own searches. It can page through complete lists and read more records before it answers. A project with a BYOM configuration supports only deep. A BYOC deployment supports only deep. The operation is experimental and in closed release. Zep enables the operation only for select accounts. The request, the response, the events, and the modes of the operation can change. A request from an account without access returns `404 not_found`. To get access, contact support@getzep.com.
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

client.graph.query_stream(
    graph_uuids=[
        "graph_uuids"
    ],
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

**graph_uuids:** `typing.List[str]` — The graph UUIDs to query. The current release accepts one UUID.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The natural-language question about the graph.
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Literal` — When true, return the retrieval calls as server-sent events.
    
</dd>
</dl>

<dl>
<dd>

**generate_answer:** `typing.Optional[bool]` 

When true, a model also writes an answer from the retrieved records.
The default is false: the response has the records and no answer.
    
</dd>
</dl>

<dl>
<dd>

**guidance:** `typing.Optional[str]` — Optional caller guidance for the answer. The agent treats it as untrusted text.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[GraphQueryRequestMode]` — The retrieval mode. The default is fast. fast: A decision model selects the types of search for each round and stops when it has enough context. The query runs at most 3 search rounds. deep: A model plans its own searches. It can page through complete lists and read more records before it answers. A project with a BYOM configuration supports only deep. A BYOC deployment supports only deep.
    
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

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">query</a>(...) -> GraphQueryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Experimental. Retrieves the graph records for a natural-language question about a graph with a read-only retrieval loop. By default, the response has the retrieved records and no answer. Set `generate_answer` to `true` to also get an answer that a model writes from the records, with the cited graph items. Set `stream` to `true` to get the retrieval calls as server-sent events. The default mode is fast. fast: A decision model selects the types of search for each round and stops when it has enough context. The query runs at most 3 search rounds. deep: A model plans its own searches. It can page through complete lists and read more records before it answers. A project with a BYOM configuration supports only deep. A BYOC deployment supports only deep. The operation is experimental and in closed release. Zep enables the operation only for select accounts. The request, the response, the events, and the modes of the operation can change. A request from an account without access returns `404 not_found`. To get access, contact support@getzep.com.
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

client.graph.query_stream(
    graph_uuids=[
        "graph_uuids"
    ],
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

**graph_uuids:** `typing.List[str]` — The graph UUIDs to query. The current release accepts one UUID.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The natural-language question about the graph.
    
</dd>
</dl>

<dl>
<dd>

**stream:** `typing.Literal` — When true, return the retrieval calls as server-sent events.
    
</dd>
</dl>

<dl>
<dd>

**generate_answer:** `typing.Optional[bool]` 

When true, a model also writes an answer from the retrieved records.
The default is false: the response has the records and no answer.
    
</dd>
</dl>

<dl>
<dd>

**guidance:** `typing.Optional[str]` — Optional caller guidance for the answer. The agent treats it as untrusted text.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[GraphQueryRequestMode]` — The retrieval mode. The default is fast. fast: A decision model selects the types of search for each round and stops when it has enough context. The query runs at most 3 search rounds. deep: A model plans its own searches. It can page through complete lists and read more records before it answers. A project with a BYOM configuration supports only deep. A BYOC deployment supports only deep.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[ContentPolicyEventListFilters]` — Exact-match filters that limit the events in the list.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edge search does not support node_labels, exclude_node_labels, or content_policy_violated. content_policy_violated is supported on episode search only. An edge has two nodes, so a node label filter is not defined for edge search. To filter edges by node label, use graph.edge.list, graph.node.list_neighbors, or graph.get_subgraph. To search the edges of nodes that have a label, do these two steps. First, call graph.search_nodes with node_labels. Then, call graph.search_edges with connected_node_uuids set to the UUIDs of the returned nodes.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages. Search ranks a limited set of results, so iteration ends after that set. To get the top N results, set `page_size` to N and read the first page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**bfs_origin_node_uuids:** `typing.Optional[typing.List[str]]` — Nodes used as BFS origins for graph-distance-aware retrieval.
    
</dd>
</dl>

<dl>
<dd>

**center_node_uuid:** `typing.Optional[str]` 

The node to rank results by distance from. Required when reranker is
node_distance.
    
</dd>
</dl>

<dl>
<dd>

**filter_low_quality_results:** `typing.Optional[bool]` 

The default is false. When true, Zep removes low-quality results at the knee of the
cross-encoder score curve. The filter never removes a result with a score
of 0.9 or more. It keeps at least 5 results, or all results when fewer
than 5 are available. The filter only removes results, so a page still
returns up to page_size results. Use this field only with reranker
cross_encoder. It is not supported for episode search. Invalid
combinations return a 400 error. The cutoff is approximate, not guaranteed.
When the cross-encoder does not score the results, for example after a
timeout, Zep returns the results without the filter.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[EdgeSearchFilters]` — Filters constraining which items are returned.
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` 

The diversity weighting used for maximal marginal relevance reranking.
Required when reranker is mmr.
    
</dd>
</dl>

<dl>
<dd>

**reranker:** `typing.Optional[SearchEdgesRequestReranker]` — The reranking strategy applied to retrieved results. Defaults to rrf.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Episode search supports only the metadata_filters and content_policy_violated filters. Every other filter returns unsupported_filter.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages. Search ranks a limited set of results, so iteration ends after that set. To get the top N results, set `page_size` to N and read the first page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**bfs_origin_node_uuids:** `typing.Optional[typing.List[str]]` — Nodes used as BFS origins for graph-distance-aware retrieval.
    
</dd>
</dl>

<dl>
<dd>

**center_node_uuid:** `typing.Optional[str]` 

The node to rank results by distance from. Required when reranker is
node_distance.
    
</dd>
</dl>

<dl>
<dd>

**filter_low_quality_results:** `typing.Optional[bool]` 

The default is false. When true, Zep removes low-quality results at the knee of the
cross-encoder score curve. The filter never removes a result with a score
of 0.9 or more. It keeps at least 5 results, or all results when fewer
than 5 are available. The filter only removes results, so a page still
returns up to page_size results. Use this field only with reranker
cross_encoder. It is not supported for episode search. Invalid
combinations return a 400 error. The cutoff is approximate, not guaranteed.
When the cross-encoder does not score the results, for example after a
timeout, Zep returns the results without the filter.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[EpisodeSearchFilters]` — Filters constraining which items are returned.
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` 

The diversity weighting used for maximal marginal relevance reranking.
Required when reranker is mmr.
    
</dd>
</dl>

<dl>
<dd>

**reranker:** `typing.Optional[SearchEpisodesRequestReranker]` — The reranking strategy applied to retrieved results. Defaults to rrf.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Node search does not support edge_types, exclude_edge_types, edge_uuids, connected_node_uuids, source_node_uuids, target_node_uuids, date_filters, or content_policy_violated. content_policy_violated is supported on episode search only. The edge filters select edges. To get the nodes that an edge connects, use graph.search_edges or graph.node.list_neighbors. To filter nodes by created_at, use graph.node.list.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages. Search ranks a limited set of results, so iteration ends after that set. To get the top N results, set `page_size` to N and read the first page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**bfs_origin_node_uuids:** `typing.Optional[typing.List[str]]` — Nodes used as BFS origins for graph-distance-aware retrieval.
    
</dd>
</dl>

<dl>
<dd>

**center_node_uuid:** `typing.Optional[str]` 

The node to rank results by distance from. Required when reranker is
node_distance.
    
</dd>
</dl>

<dl>
<dd>

**filter_low_quality_results:** `typing.Optional[bool]` 

The default is false. When true, Zep removes low-quality results at the knee of the
cross-encoder score curve. The filter never removes a result with a score
of 0.9 or more. It keeps at least 5 results, or all results when fewer
than 5 are available. The filter only removes results, so a page still
returns up to page_size results. Use this field only with reranker
cross_encoder. It is not supported for episode search. Invalid
combinations return a 400 error. The cutoff is approximate, not guaranteed.
When the cross-encoder does not score the results, for example after a
timeout, Zep returns the results without the filter.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[NodeSearchFilters]` — Filters constraining which items are returned.
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` 

The diversity weighting used for maximal marginal relevance reranking.
Required when reranker is mmr.
    
</dd>
</dl>

<dl>
<dd>

**reranker:** `typing.Optional[SearchNodesRequestReranker]` — The reranking strategy applied to retrieved results. Defaults to rrf.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Observation search supports no filters. Every filter returns unsupported_filter.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages. Search ranks a limited set of results, so iteration ends after that set. To get the top N results, set `page_size` to N and read the first page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**bfs_origin_node_uuids:** `typing.Optional[typing.List[str]]` — Nodes used as BFS origins for graph-distance-aware retrieval.
    
</dd>
</dl>

<dl>
<dd>

**center_node_uuid:** `typing.Optional[str]` 

The node to rank results by distance from. Required when reranker is
node_distance.
    
</dd>
</dl>

<dl>
<dd>

**filter_low_quality_results:** `typing.Optional[bool]` 

The default is false. When true, Zep removes low-quality results at the knee of the
cross-encoder score curve. The filter never removes a result with a score
of 0.9 or more. It keeps at least 5 results, or all results when fewer
than 5 are available. The filter only removes results, so a page still
returns up to page_size results. Use this field only with reranker
cross_encoder. It is not supported for episode search. Invalid
combinations return a 400 error. The cutoff is approximate, not guaranteed.
When the cross-encoder does not score the results, for example after a
timeout, Zep returns the results without the filter.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[ObservationSearchFilters]` — Filters constraining which items are returned.
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` 

The diversity weighting used for maximal marginal relevance reranking.
Required when reranker is mmr.
    
</dd>
</dl>

<dl>
<dd>

**reranker:** `typing.Optional[SearchObservationsRequestReranker]` — The reranking strategy applied to retrieved results. Defaults to rrf.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Thread-summary search supports only the metadata_filters filter, which matches the metadata of the thread episodes. Every other filter returns unsupported_filter.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**query:** `str` — The search query.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages. Search ranks a limited set of results, so iteration ends after that set. To get the top N results, set `page_size` to N and read the first page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**bfs_origin_node_uuids:** `typing.Optional[typing.List[str]]` — Nodes used as BFS origins for graph-distance-aware retrieval.
    
</dd>
</dl>

<dl>
<dd>

**center_node_uuid:** `typing.Optional[str]` 

The node to rank results by distance from. Required when reranker is
node_distance.
    
</dd>
</dl>

<dl>
<dd>

**filter_low_quality_results:** `typing.Optional[bool]` 

The default is false. When true, Zep removes low-quality results at the knee of the
cross-encoder score curve. The filter never removes a result with a score
of 0.9 or more. It keeps at least 5 results, or all results when fewer
than 5 are available. The filter only removes results, so a page still
returns up to page_size results. Use this field only with reranker
cross_encoder. It is not supported for episode search. Invalid
combinations return a 400 error. The cutoff is approximate, not guaranteed.
When the cross-encoder does not score the results, for example after a
timeout, Zep returns the results without the filter.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[ThreadSummarySearchFilters]` — Filters constraining which items are returned.
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` 

The diversity weighting used for maximal marginal relevance reranking.
Required when reranker is mmr.
    
</dd>
</dl>

<dl>
<dd>

**reranker:** `typing.Optional[SearchThreadSummariesRequestReranker]` — The reranking strategy applied to retrieved results. Defaults to rrf.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set `hyperedges_enabled` to `true` to enable extraction. A member needs the `project.edit` permission. Project API keys receive `403 permission_denied`.
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

**hyperedges_enabled:** `typing.Optional[bool]` 

Set to true to enable hyperedge extraction. This setting cannot be disabled.
A member needs project.edit. Project API keys receive 403 permission_denied.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TaskListRequestStatus]` — Return only the tasks with this status
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[TaskListRequestType]` — Return only the tasks of this type
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

Verify a provider credential before Zep stores it. Both providers accept 1 to 60 requests per minute and an optional retention window. Example requests: `{"name":"Support traces","provider":"braintrust","credential":"secret","requests_per_minute":60,"retention_days":30}` and `{"name":"Support traces","provider":"langsmith","credential":"secret","requests_per_minute":60,"retention_days":30}`.
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

**provider:** `typing.Optional[CreateTraceConnectionRequestProvider]` — Provider is the Braintrust or LangSmith provider.
    
</dd>
</dl>

<dl>
<dd>

**requests_per_minute:** `typing.Optional[int]` — RequestsPerMinute is the request rate limit from 1 to 60 per minute.
    
</dd>
</dl>

<dl>
<dd>

**retention_days:** `typing.Optional[int]` — RetentionDays is an optional retention window in days.
    
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

Delete a trace connection that no active trace import uses.
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

Verify changed settings before Zep stores them. Both providers accept 1 to 60 requests per minute and an optional retention window. Example request: `{"requests_per_minute":60,"retention_days":30}`.
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

**requests_per_minute:** `typing.Optional[int]` — RequestsPerMinute is the new request rate limit, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**retention_days:** `typing.Optional[int]` — RetentionDays is the new retention window in days, when supplied.
    
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

Requires attribute-based access control to be enabled for your account.
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

Requires attribute-based access control to be enabled for your account.
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

Requires attribute-based access control to be enabled for your account.
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

Requires attribute-based access control to be enabled for your account.
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

Requires attribute-based access control to be enabled for your account.
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

Requires attribute-based access control to be enabled for your account.
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

Requires attribute-based access control to be enabled for your account.
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

Requires attribute-based access control to be enabled for your account.
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

Requires attribute-based access control to be enabled for your account.
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

Requires attribute-based access control to be enabled for your account.
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

Requires attribute-based access control to be enabled for your account.
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**user_id:** `typing.Optional[str]` 

An optional external identity identifier, such as an identity-provider
subject claim. Zep uses it to match an identity-provider sign-in to this
user. It is not an address; use uuid to address the user in v4. It is
unique within the project, can contain at most 500 characters, and
cannot be changed after creation.
    
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Agent Learning State. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List durable learning-run outcomes for an Agent. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Agent Literal Policy. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Agent Literal Policy. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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
            "environment_name"
        ],
        tools=[
            "command_name"
        ],
    ),
    allowlisted_values=AgentLiteralPolicyValues(
        environments=[
            "production"
        ],
        tools=[
            "refund_payment"
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Agent Skill. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**definition:** `SkillDefinition` — The developer supplies the structured content of the Skill.
    
</dd>
</dl>

<dl>
<dd>

**skill_id:** `typing.Optional[str]` 

The developer can set a stable ID for the Skill. If omitted, the service
assigns one.
    
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

Submit a portable Skill archive. The completed Task returns `{"result":{"skill_uuid":"<uuid>"}}`. Approve that Skill before retrieval. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Agent Skills. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**environments:** `typing.Optional[typing.List[str]]` — The developer filters results by environment names.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[str]` — The developer supplies a Skill kind.
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` — The developer supplies the task-family slug.
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[str]]` — The developer supplies tool names used by the Skill.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search Agent Skills. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.skill.search(
    agent_uuid="agent_uuid",
    query="How do I refund a duplicate charge?",
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

**query:** `str` — The developer supplies a search query for Skills.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**environments:** `typing.Optional[typing.List[str]]` — The developer supplies environment names used by the Skill.
    
</dd>
</dl>

<dl>
<dd>

**include_markdown:** `typing.Optional[bool]` — The developer sets this to true to include the Skill instructions in Markdown.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[str]` — The developer supplies a Skill kind.
    
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

**task_family:** `typing.Optional[str]` — The developer supplies the task-family slug.
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.List[str]]` — The developer supplies tool names used by the Skill.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Agent Skill. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve Agent Skill. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` — The developer supplies the current Skill version to protect against concurrent edits.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retire Agent Skill. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` — The developer supplies the current Skill version to protect against concurrent edits.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Agent Skill Version. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**definition:** `SkillDefinition` — The developer supplies the structured content for the new Skill version.
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` — The developer supplies the current Skill version to protect against concurrent edits.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Plan an Agent split. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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
                agent_id="payments-agent",
                name="Refund a duplicate charge",
                security_domain="customer:support",
            ),
            skills=[
                AgentSplitPlanSkillSelectionRequest(
                    skill_uuid="6a906e70-50ca-4e43-a874-5fcae02a71fa",
                    skill_version_uuid="6a906e70-50ca-4e43-a874-5fcae02a71fa",
                    version=1,
                )
            ],
        )
    ],
    expected_revision=1,
    rationale="Keep payment refunds separate from charge disputes.",
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

**destinations:** `typing.List[AgentSplitPlanDestinationRequest]` — The developer lists 1 to 100 destination Agents.
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The developer supplies the current revision used for optimistic concurrency. At least 1.
    
</dd>
</dl>

<dl>
<dd>

**rationale:** `str` 

The developer explains the requested change. The limit is 2,000
characters.
    
</dd>
</dl>

<dl>
<dd>

**review_acknowledged:** `bool` — The developer sets this to true to confirm that the review is complete.
    
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

## Agent TaskFamily
<details><summary><code>client.agent.task_family.<a href="src/zep_cloud/agent/task_family/client.py">list</a>(...) -> AgentTaskFamilyDescriptorPage</code></summary>
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

client.agent.task_family.list(
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

<details><summary><code>client.agent.task_family.<a href="src/zep_cloud/agent/task_family/client.py">rename</a>(...) -> RenameAgentTaskFamilyResponse</code></summary>
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

client.agent.task_family.rename(
    agent_uuid="agent_uuid",
    from_slug="support/refund",
    to_slug="support/refund",
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

**from_slug:** `str` — The current slug of the live descriptor.
    
</dd>
</dl>

<dl>
<dd>

**to_slug:** `str` — The new slug, or the slug of the live descriptor to merge into.
    
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

## Agent TraceImport
<details><summary><code>client.agent.trace_import.<a href="src/zep_cloud/agent/trace_import/client.py">list</a>(...) -> TraceImportPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List trace imports that belong to this Agent. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.list(
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

<details><summary><code>client.agent.trace_import.<a href="src/zep_cloud/agent/trace_import/client.py">create</a>(...) -> TraceImportCreateResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a scheduled import or queue a one-time import. A scheduled import returns HTTP 201 with `import`. A one-time import returns HTTP 202 with `import`, `run`, and `task`. Example request: `{"connection_uuid":"8c78a85e-eac2-4f57-b5f5-59a68a1e77a1","provider_project_id":"project-123","name":"Support traces","selection":{"trace_ids":["trace-123"]},"mapping":{"task_family":{"source":"fixed","value":"support"}}}`. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.create(
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

**connection_uuid:** `typing.Optional[str]` — The developer selects the configured provider connection.
    
</dd>
</dl>

<dl>
<dd>

**learn_from:** `typing.Optional[bool]` — LearnFrom controls whether imported evidence can support Skills.
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Optional[TraceMapping]` — Mapping defines how source traces become Traces. Example: {"task_family":{"source":"fixed","value":"support"}}.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name is the import display name.
    
</dd>
</dl>

<dl>
<dd>

**on_source_change:** `typing.Optional[TraceImportOnSourceChange]` — OnSourceChange defines how changed source traces are handled.
    
</dd>
</dl>

<dl>
<dd>

**provider_project_id:** `typing.Optional[str]` — The developer selects the project to import from the provider.
    
</dd>
</dl>

<dl>
<dd>

**require_review:** `typing.Optional[bool]` — RequireReview requires review for candidates backed by this import.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[TraceImportSchedule]` — Schedule enables recurring imports when supplied. Example: {"interval_hours":4,"start_from":"now","settle_minutes":5,"max_open_hours":24}.
    
</dd>
</dl>

<dl>
<dd>

**selection:** `typing.Optional[TraceImportSelection]` — Selection defines the traces to import. Example: {"trace_ids":["trace_123"]}.
    
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

<details><summary><code>client.agent.trace_import.<a href="src/zep_cloud/agent/trace_import/client.py">get</a>(...) -> TraceImport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one trace import. The response does not include its source cursor. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.get(
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

**import_uuid:** `str` — Trace import UUID
    
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

<details><summary><code>client.agent.trace_import.<a href="src/zep_cloud/agent/trace_import/client.py">delete</a>(...) -> typing.Optional[Task]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set `traces=delete` to queue asynchronous Trace deletion. The default keeps Traces. Example query: `?traces=delete`. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.delete(
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

**import_uuid:** `str` — Trace import UUID
    
</dd>
</dl>

<dl>
<dd>

**traces:** `typing.Optional[TraceImportDeleteRequestTraces]` — Whether to delete imported Traces
    
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

<details><summary><code>client.agent.trace_import.<a href="src/zep_cloud/agent/trace_import/client.py">update</a>(...) -> TraceImport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Use `expected_revision` to reject a stale update. Example request: `{"expected_revision":1,"name":"Updated support traces"}`. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.update(
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

**import_uuid:** `str` — Trace import UUID
    
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

**mapping:** `typing.Optional[TraceMapping]` — Mapping is the new mapping, when supplied. Example: {"task_family":{"source":"fixed","value":"support"}}.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name is the new import name, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**on_source_change:** `typing.Optional[UpdateTraceImportRequestOnSourceChange]` — OnSourceChange is the new change policy, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**require_review:** `typing.Optional[bool]` — RequireReview is the new review setting, when supplied.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[TraceImportSchedule]` — Schedule is the new schedule, when supplied. Example: {"interval_hours":4,"start_from":"now","settle_minutes":5,"max_open_hours":24}.
    
</dd>
</dl>

<dl>
<dd>

**selection:** `typing.Optional[TraceImportSelection]` — Selection is the new selection, when supplied. Example: {"trace_ids":["trace_123"]}.
    
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

<details><summary><code>client.agent.trace_import.<a href="src/zep_cloud/agent/trace_import/client.py">pause</a>(...) -> TraceImport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pause a scheduled trace import. One-time imports cannot be paused. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.pause(
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

**import_uuid:** `str` — Trace import UUID
    
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

<details><summary><code>client.agent.trace_import.<a href="src/zep_cloud/agent/trace_import/client.py">resume</a>(...) -> TraceImport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resume a scheduled trace import. Zep verifies credentials first when they caused the pause. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.resume(
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

**import_uuid:** `str` — Trace import UUID
    
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

## Agent Trace
<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">create</a>(...) -> AgentTrace</code></summary>
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

client.agent.trace.create(
    agent_uuid="agent_uuid",
    objective="Refund a duplicate charge.",
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

**objective:** `str` 

The developer describes the task instance. The create request requires a non-empty value but
does not check its size. An AppendAgentTraceEventRequest returns 400 if the Trace objective
exceeds 8 KiB (8,192 bytes).
    
</dd>
</dl>

<dl>
<dd>

**learn_from:** `typing.Optional[bool]` 

The developer supplies whether eligible evidence may participate in learning. Defaults to
true.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Developer metadata used to organize and filter Traces.
    
</dd>
</dl>

<dl>
<dd>

**parent_trace_uuid:** `typing.Optional[str]` — The developer supplies the parent Trace UUID when this attempt retries an earlier attempt.
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` 

The developer may set a task-family slug. If the developer omits it, Agent Skills assigns the
Trace to a task family automatically. If Agent Skills cannot assign a task family, the
`task_family_inference` field of the Trace is `unassigned`. A BYOM configuration requires `task_family`. A
strict-residency deployment requires `task_family`. Without task_family in either case, the
API returns 400 `invalid_request` with the message `task_family is required`. The slug must
contain 1 to 128 lowercase letters, digits, `.`, `_`, `/`, or `-`. It must start with a
lowercase letter or digit.
    
</dd>
</dl>

<dl>
<dd>

**trace_id:** `typing.Optional[str]` 

The developer may set an identifier that is unique within the Agent. A retry with the same
create parameters returns 200 and the existing Trace. Different parameters return 409.
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">list</a>(...) -> AgentTracePage</code></summary>
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

client.agent.trace.list(
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[TraceListRequestOrderBy]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[TraceListRequestOrder]` — asc or desc
    
</dd>
</dl>

<dl>
<dd>

**import_uuid:** `typing.Optional[str]` — Filter by owning Trace import UUID
    
</dd>
</dl>

<dl>
<dd>

**source_kind:** `typing.Optional[TraceListRequestSourceKind]` — Source kind
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Filters to Traces whose metadata contains these key-value pairs.
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[AgentTraceOutcome]` 

The developer supplies filters to one reported outcome. Valid values are succeeded, failed,
partial, abandoned, unknown.
    
</dd>
</dl>

<dl>
<dd>

**parent_trace_uuid:** `typing.Optional[str]` — Filters to direct retries of this parent Trace.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[AgentTraceLifecycle]` — Filters to one lifecycle state.
    
</dd>
</dl>

<dl>
<dd>

**task_family:** `typing.Optional[str]` — Filters to an exact task-family slug.
    
</dd>
</dl>

<dl>
<dd>

**verification:** `typing.Optional[AgentTraceVerification]` — Filters to one verification strength.
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">get</a>(...) -> AgentTrace</code></summary>
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

client.agent.trace.get(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">delete</a>(...) -> AgentTraceSourceDeletionResult</code></summary>
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

client.agent.trace.delete(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `DeleteAgentTraceRequest` 
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">update</a>(...) -> AgentTrace</code></summary>
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

client.agent.trace.update(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
    expected_revision=1,
    task_family="support/refund",
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

**trace_uuid:** `str` — Trace UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current Trace revision used for optimistic concurrency.
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">abandon</a>(...) -> AgentTraceFinalizationResult</code></summary>
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

client.agent.trace.abandon(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
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

**missing_sequence_ranges:** `typing.Optional[typing.List[AgentTraceSequenceRange]]` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**verification:** `typing.Optional[AgentTraceVerification]` 
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">close</a>(...) -> AgentTraceFinalizationResult</code></summary>
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

client.agent.trace.close(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
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

**missing_sequence_ranges:** `typing.Optional[typing.List[AgentTraceSequenceRange]]` 
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[AgentTraceOutcome]` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**verification:** `typing.Optional[AgentTraceVerification]` 
    
</dd>
</dl>

<dl>
<dd>

**verifier:** `typing.Optional[AgentTraceCloseVerifier]` 
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">correct_task_family</a>(...) -> AgentTraceFinalizationResult</code></summary>
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

client.agent.trace.correct_task_family(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
    expected_revision=1,
    reason="acknowledged_gap",
    task_family="support/refund",
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

**trace_uuid:** `str` — Trace UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current Trace revision used for optimistic concurrency.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — Why the terminal Trace classification is being corrected.
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">list_events</a>(...) -> AgentTraceEventPage</code></summary>
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

client.agent.trace.list_events(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">append_event</a>(...) -> AgentTraceEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A tool call and its result can share a tool_call_id. For example, append {"event_type":"tool_call","tool_call_id":"call_8f2b","content":"Search orders","context":{"tools":[{"name":"search_orders"}]}} and {"event_type":"tool_result","tool_call_id":"call_8f2b","content":"Order results","context":{"tools":[{"name":"search_orders"}]}}.
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

client.agent.trace.append_event(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `AgentTraceEventType` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[AgentTraceEventContext]` 

Context gives the model, the tools, and the environments of the event. context.tools is the tool
that the event calls or returns, and Skills learning reads it. A tool event can omit the tool name.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata is developer data. Skills learning does not read it.
    
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

**sources:** `typing.Optional[typing.List[AgentTraceEventSource]]` 
    
</dd>
</dl>

<dl>
<dd>

**tool_call_id:** `typing.Optional[str]` 

ToolCallID is the ID that the agent framework gives a tool call. Use the same ID on
the tool_call and tool_result events. It is valid only on these event types. A result
without a matching call is valid. OpenAI uses tool_calls[].id, Anthropic uses the
tool_use block id, and LangChain uses ToolMessage.tool_call_id.
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">delete_event</a>(...) -> AgentTraceSourceDeletionResult</code></summary>
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

client.agent.trace.delete_event(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
</dd>
</dl>

<dl>
<dd>

**event_uuid:** `str` — Event UUID
    
</dd>
</dl>

<dl>
<dd>

**request:** `DeleteAgentTraceRequest` 
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">reopen</a>(...) -> AgentTrace</code></summary>
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

client.agent.trace.reopen(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The current Trace revision used for optimistic concurrency.
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">get_summary</a>(...) -> AgentTraceSummaryVersion</code></summary>
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

client.agent.trace.get_summary(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
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

<details><summary><code>client.agent.trace.<a href="src/zep_cloud/agent/trace/client.py">list_summary_versions</a>(...) -> AgentTraceSummaryPage</code></summary>
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

client.agent.trace.list_summary_versions(
    agent_uuid="agent_uuid",
    trace_uuid="trace_uuid",
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

**trace_uuid:** `str` — Trace UUID
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

## Agent Verifier
<details><summary><code>client.agent.verifier.<a href="src/zep_cloud/agent/verifier/client.py">list</a>(...) -> Pagev4AgentVerifier</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Agent Verifiers. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Agent Verifier. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Agent Verifier. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidate Agent Verifier Evidence. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.verifier.invalidate_evidence(
    agent_uuid="agent_uuid",
    verifier_uuid="verifier_uuid",
    reason="acknowledged_gap",
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

**reason:** `str` — The developer supplies why evidence from these verifier revisions is invalid.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke Agent Verifier. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Agent Skill Candidate Reviews. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Agent Skill Candidate Review. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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
    evaluator_version="v1.0.0",
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

The developer selects the evaluation source. Valid values are customer, tool,
offline_corpus, policy.
    
</dd>
</dl>

<dl>
<dd>

**evaluator_version:** `str` — The developer supplies the version of the evaluation rule.
    
</dd>
</dl>

<dl>
<dd>

**expected_revision:** `int` — The developer supplies the current revision used for optimistic concurrency. At least 1.
    
</dd>
</dl>

<dl>
<dd>

**verdict:** `CreateAgentSkillCandidateEvaluationRequestVerdict` 

The developer supplies evaluation verdict. Valid values are succeeded, failed, partial,
unknown.
    
</dd>
</dl>

<dl>
<dd>

**controlled_test:** `typing.Optional[bool]` — The developer sets this to true when a controlled test produced the result.
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` — The developer supplies the environment for this evaluation.
    
</dd>
</dl>

<dl>
<dd>

**evidence_reference:** `typing.Optional[str]` — The developer links this evaluation to an evidence record.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Dict[str, float]]` — The developer supplies evaluation metrics.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Record Agent Skill Evaluation. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.skill.evaluation.create(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    evaluated_by="customer",
    evaluator_version="v1.0.0",
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**evaluated_by:** `CreateAgentSkillEvaluationRequestEvaluatedBy` 

The developer selects the evaluation source. Valid values are customer, tool,
offline_corpus, policy.
    
</dd>
</dl>

<dl>
<dd>

**evaluator_version:** `str` — The developer supplies the evaluation rule version. It can contain up to 255 characters.
    
</dd>
</dl>

<dl>
<dd>

**skill_version:** `int` — The developer supplies the Skill version to evaluate. It must be at least 1.
    
</dd>
</dl>

<dl>
<dd>

**verdict:** `CreateAgentSkillEvaluationRequestVerdict` 

The developer supplies evaluation verdict. Valid values are succeeded, failed, partial,
unknown.
    
</dd>
</dl>

<dl>
<dd>

**controlled_test:** `typing.Optional[bool]` — The developer sets this to true when a controlled test produced the result.
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` — The developer supplies the environment for this evaluation. At most 1024.
    
</dd>
</dl>

<dl>
<dd>

**evidence_reference:** `typing.Optional[str]` — The developer links this evaluation to an evidence record.
    
</dd>
</dl>

<dl>
<dd>

**metrics:** `typing.Optional[typing.Dict[str, float]]` — The developer supplies evaluation metrics.
    
</dd>
</dl>

<dl>
<dd>

**use_uuid:** `typing.Optional[str]` — The developer can link this evaluation to a recorded Skill use.
    
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

Find a destination Skill by its source Agent, Skill, and version. The endpoint returns 404 until an automatic publication is ready or after it is invalidated. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

Get the publication that created a destination Skill. Use its source version and policy identity to verify a copied Skill. The endpoint returns 404 for unpublished and invalidated Skills. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Agent Skill Evidence. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Agent Skill Relationships. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[typing.Union[RelationListRequestKindItem, typing.Sequence[RelationListRequestKindItem]]]` — Relationship kinds
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore Agent Skill Version. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` — The developer supplies the current Skill version to protect against concurrent edits.
    
</dd>
</dl>

<dl>
<dd>

**version:** `int` — The developer supplies the Skill version to restore.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List Agent Skill Versions. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compare Agent Skill Versions. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**from_version:** `int` — The developer supplies the source version to compare. It must be at least 1.
    
</dd>
</dl>

<dl>
<dd>

**to_version:** `int` — The developer supplies the destination version to compare. It must be at least 1.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Agent Skill Version. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
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

**include:** `typing.Optional[typing.Literal]` — Optional field to add to the response: contract
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create Agent Skill Use. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.skill.use.create(
    agent_uuid="agent_uuid",
    skill_uuid="skill_uuid",
    search_id="eyJ2IjoxLCJyZXF1ZXN0X2lkIjoiNmE5MDZlNzAtNTBjYS00ZTQzLWE4NzQtNWZjYWUwMmE3MWZhIn0.signature",
    trace_uuid="6a906e70-50ca-4e43-a874-5fcae02a71fa",
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
</dd>
</dl>

<dl>
<dd>

**search_id:** `str` — The developer supplies the signed search token returned by Skill search.
    
</dd>
</dl>

<dl>
<dd>

**trace_uuid:** `str` — The developer supplies the UUID of the source Trace.
    
</dd>
</dl>

<dl>
<dd>

**usage:** `CreateAgentSkillUseRequestUsage` 

The developer supplies how the Skill was used. Valid values are selected, used,
partially_used, ignored, inapplicable.
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[AddAgentSkillUseOutcomeRequest]` 

The developer records the outcome of the attempt. Valid values are
succeeded, failed, partial, abandoned, and unknown.
    
</dd>
</dl>

<dl>
<dd>

**reason_code:** `typing.Optional[str]` — The developer supplies a reason code for this outcome. It can contain up to 255 characters.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Record Agent Skill Feedback. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export an Agent Skill version. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download an Agent Skill export. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

**skill_uuid:** `str` — Skill UUID, or the 8-character short_id
    
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

## Agent TraceImport Run
<details><summary><code>client.agent.trace_import.run.<a href="src/zep_cloud/agent/trace_import/run/client.py">list</a>(...) -> TraceImportRunPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List runs that belong to this trace import. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.run.list(
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

**import_uuid:** `str` — Trace import UUID
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

<details><summary><code>client.agent.trace_import.run.<a href="src/zep_cloud/agent/trace_import/run/client.py">create</a>(...) -> Task</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a pending run and its Task. This operation does not start the run. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.run.create(
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

**import_uuid:** `str` — Trace import UUID
    
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

<details><summary><code>client.agent.trace_import.run.<a href="src/zep_cloud/agent/trace_import/run/client.py">get</a>(...) -> TraceImportRun</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read one run that belongs to this trace import. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.run.get(
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

**import_uuid:** `str` — Trace import UUID
    
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

## Agent TraceImport Run Item
<details><summary><code>client.agent.trace_import.run.item.<a href="src/zep_cloud/agent/trace_import/run/item/client.py">list</a>(...) -> TraceImportRunItemPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List trace results for this run. Run items do not include source payload. Agent Skills is in closed release. Zep enables Agent Skills only for select accounts. A request from an account without access returns `403 permission_denied`. To get access, contact support@getzep.com.
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

client.agent.trace_import.run.item.list(
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

**import_uuid:** `str` — Trace import UUID
    
</dd>
</dl>

<dl>
<dd>

**run_uuid:** `str` — Run UUID
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the document summaries of a graph and returns one page of results. The default `page_size` is 50, and the maximum `page_size` is 100.
You can sort by `uuid` or `created_at`. The default sort is `uuid` in descending order.
You cannot use these `filters` fields: `node_labels`, `exclude_node_labels`, `edge_types`, `exclude_edge_types`, `edge_uuids`, `episode_uuids`, `connected_node_uuids`, `source_node_uuids`, `target_node_uuids`, and `content_policy_violated`.
`date_filters` supports only the `created_at` field.
If the request has an unsupported or unknown filter field, the API returns an `unsupported_filter` error.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[DocumentSummaryListRequestOrderBy]` — Sort key: uuid (default) or created_at
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[DocumentSummaryListRequestOrder]` — Sort direction: asc or desc (default desc)
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[DocumentSummaryListFilters]` 

Filters that limit the items in the list. The operation description
names the filter fields that the operation does not support.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Document ID
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**data:** `str` — The episode content to add to the graph.
    
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

**reference_time:** `typing.Optional[str]` 

The episode's reference time, used for temporal reasoning rather than
ingestion time. Defaults to the ingestion time.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**filters:** `typing.Optional[EpisodeListFilters]` — Filters that limit the episodes in the list.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**episode_uuid:** `str` — Episode UUID
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the edges of a graph and returns one page of results. The default `page_size` is 50, and the maximum `page_size` is 100.
You can sort by `uuid`, `created_at`, or `valid_at`. The default sort is `uuid` in descending order. An edge with no `valid_at` sorts as if its `valid_at` is 1970-01-01T00:00:00Z. Thus it comes before an edge with a later `valid_at` in ascending order, and after an edge with an earlier `valid_at`.
You can use all `filters` fields except `content_policy_violated`.
If the request has an unsupported or unknown filter field, the API returns an `unsupported_filter` error.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[EdgeListRequestOrderBy]` — Sort key: uuid (default), created_at, or valid_at
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[EdgeListRequestOrder]` — Sort direction: asc or desc (default desc)
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[EdgeListFilters]` 

Filters that limit the items in the list. The operation description
names the filter fields that the operation does not support.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**filters:** `typing.Optional[HyperedgeListFilters]` — Filters that limit the hyperedges in the list.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the nodes of a graph and returns one page of results. The default `page_size` is 50, and the maximum `page_size` is 100.
You can sort by `uuid`, `created_at`, or `degree`. The default sort is `uuid` in descending order.
You cannot use these `filters` fields: `connected_node_uuids`, `source_node_uuids`, `target_node_uuids`, and `content_policy_violated`.
If the request has an unsupported or unknown filter field, the API returns an `unsupported_filter` error.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[NodeListRequestOrderBy]` — Sort key: uuid (default), created_at, or degree
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[NodeListRequestOrder]` — Sort direction: asc or desc (default desc)
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[NodeListFilters]` 

Filters that limit the items in the list. The operation description
names the filter fields that the operation does not support.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**node_uuid:** `str` — Node UUID
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the observations of a graph and returns one page of results. The default `page_size` is 50, and the maximum `page_size` is 100.
You can sort by `uuid` or `created_at`. The default sort is `uuid` in descending order.
You cannot use these `filters` fields: `node_labels`, `exclude_node_labels`, `edge_types`, `exclude_edge_types`, `edge_uuids`, `episode_uuids`, `connected_node_uuids`, `source_node_uuids`, `target_node_uuids`, `metadata_filters`, and `content_policy_violated`.
`date_filters` supports only the `created_at` field.
If the request has an unsupported or unknown filter field, the API returns an `unsupported_filter` error.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ObservationListRequestOrderBy]` — Sort key: uuid (default) or created_at
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ObservationListRequestOrder]` — Sort direction: asc or desc (default desc)
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[ObservationListFilters]` 

Filters that limit the items in the list. The operation description
names the filter fields that the operation does not support.
    
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the thread summaries of a graph and returns one page of results. The default `page_size` is 50, and the maximum `page_size` is 100.
You can sort by `uuid` or `created_at`. The default sort is `uuid` in descending order.
You cannot use these `filters` fields: `node_labels`, `exclude_node_labels`, `edge_types`, `exclude_edge_types`, `edge_uuids`, `episode_uuids`, `connected_node_uuids`, `source_node_uuids`, `target_node_uuids`, and `content_policy_violated`.
`date_filters` supports only the `created_at` field.
If the request has an unsupported or unknown filter field, the API returns an `unsupported_filter` error.
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

**graph_uuid:** `str` — The UUID of the graph. For a user graph, you can also use the UUID of the user.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque page cursor
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[ThreadSummaryListRequestOrderBy]` — Sort key: uuid (default) or created_at
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ThreadSummaryListRequestOrder]` — Sort direction: asc or desc (default desc)
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[ThreadSummaryListFilters]` 

Filters that limit the items in the list. The operation description
names the filter fields that the operation does not support.
    
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

List provider projects with the `page_size` and `cursor` query parameters.
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

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

**provider_project_id:** `str` — The developer supplies the project ID from the selected provider.
    
</dd>
</dl>

<dl>
<dd>

**trace_id:** `str` — TraceID is the provider trace identifier.
    
</dd>
</dl>

<dl>
<dd>

**mapping:** `typing.Optional[TraceMapping]` — Mapping is an optional mapping preview configuration. Example: {"task_family":{"source":"fixed","value":"support"}}.
    
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

**provider_project_id:** `str` — The developer supplies the project ID from the selected provider.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — The maximum number of items in one page. The SDK method returns a pager. In Python, `.items` holds only the first page. In TypeScript, `.data` holds only the first page. To read every page, iterate the pager: use `for` or `list(...)` in Python, or `for await` in TypeScript. In Go, the method returns one page, and `Iterator()` reads all pages.
    
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

