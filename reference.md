# Reference
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

client.batch.list(
    limit=1,
    cursor="cursor",
    status="status",
)

```
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

**status:** `typing.Optional[str]` — Batch status filter
    
</dd>
</dl>

<dl>
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
    limit=1,
    cursor="cursor",
)

```
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

client.context.list_templates(
    limit=1,
    cursor="cursor",
)

```
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

**description:** `typing.Optional[str]` — A description of the graph.
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — An optional developer-assigned identifier for the graph.
    
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

client.graph.list(
    limit=1,
    cursor="cursor",
    order_by="order_by",
    order="order",
)

```
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

**order_by:** `typing.Optional[str]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — asc or desc
    
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
)

```
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

**target_graph_id:** `typing.Optional[str]` — An optional name for the cloned graph.
    
</dd>
</dl>

<dl>
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

**recency_bias:** `typing.Optional[V4GraphContextRequestRecencyBias]` — Adjusts result selection to favor more recent graph data.
    
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
    limit=1,
    cursor="cursor",
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
    limit=1,
    cursor="cursor",
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
    limit=1,
    cursor="cursor",
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
    limit=1,
    cursor="cursor",
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
    limit=1,
    cursor="cursor",
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

**direction:** `typing.Optional[V4SubgraphRequestDirection]` 

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

#### 🔌 Usage

<dl>
<dd>

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

client.task.list(
    limit=1,
    cursor="cursor",
)

```
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

client.thread.list(
    limit=1,
    cursor="cursor",
    order_by="order_by",
    order="order",
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

**order_by:** `typing.Optional[str]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — asc or desc
    
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

**thread_id:** `typing.Optional[str]` — An optional developer-assigned identifier for the thread.
    
</dd>
</dl>

<dl>
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
    limit=1,
    cursor="cursor",
)

```
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
    limit=1,
    cursor="cursor",
)

```
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

client.user_group.list(
    limit=1,
    cursor="cursor",
)

```
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
    limit=1,
    cursor="cursor",
)

```
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
    limit=1,
    cursor="cursor",
)

```
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
    limit=1,
    cursor="cursor",
)

```
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

**user_id:** `typing.Optional[str]` — An optional developer-assigned identifier for the user.
    
</dd>
</dl>

<dl>
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

client.user.list(
    limit=1,
    cursor="cursor",
    order_by="order_by",
    order="order",
)

```
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

**order_by:** `typing.Optional[str]` — Sort field
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — asc or desc
    
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
    limit=1,
    cursor="cursor",
)

```
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
    limit=1,
    cursor="cursor",
)

```
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to store on the episode.
    
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

**type:** `typing.Optional[V4AddEpisodeRequestType]` — The data format of the episode: text, json, or message. Defaults to text.
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

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
    limit=1,
    cursor="cursor",
)

```
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to merge onto the episode; a key set to null is removed.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">add</a>(...) -> AddEdgeResult</code></summary>
<dl>
<dd>

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

client.graph.edge.add(
    graph_uuid="graph_uuid",
    fact="fact",
    fact_name="fact_name",
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

**fact:** `str` 

The fact text describing the relationship between the source and target
nodes.
    
</dd>
</dl>

<dl>
<dd>

**fact_name:** `str` — The name of the edge, in upper snake case, for example RELATES_TO.
    
</dd>
</dl>

<dl>
<dd>

**source_node:** `EdgeNodeRef` 

The source node of the edge, referenced by uuid or created or matched by
name.
    
</dd>
</dl>

<dl>
<dd>

**target_node:** `EdgeNodeRef` 

The target node of the edge, referenced by uuid or created or matched by
name.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[typing.Dict[str, typing.Any]]` — Additional attributes to store on the edge.
    
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata attached to the episode created for this edge.
    
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
    limit=1,
    cursor="cursor",
)

```
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

#### 🔌 Usage

<dl>
<dd>

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
    limit=1,
    cursor="cursor",
)

```
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
    limit=1,
    cursor="cursor",
)

```
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

**direction:** `typing.Optional[V4NeighborsRequestDirection]` — The edge orientation to follow from the node: in, out, or both.
    
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
    limit=1,
    cursor="cursor",
)

```
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
    limit=1,
    cursor="cursor",
)

```
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata to merge onto the message; a key set to null is removed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

