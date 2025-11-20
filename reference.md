# Reference
## Context
<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">list_context_templates</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all context templates.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.context.list_context_templates()

```
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

<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">create_context_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new context template.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.context.create_context_template(
    template="template",
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template:** `str` — The template content (max 1200 characters).
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `str` — Unique identifier for the template (max 100 characters).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">get_context_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a context template by template_id.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.context.get_context_template(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` — Template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">update_context_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing context template by template_id.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.context.update_context_template(
    template_id="template_id",
    template="template",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` — Template ID
    
</dd>
</dl>

<dl>
<dd>

**template:** `str` — The template content (max 1200 characters).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.context.<a href="src/zep_cloud/context/client.py">delete_context_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a context template by template_id.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.context.delete_context_template(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` — Template ID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">list_entity_types</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all entity types for a project, user, or graph.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.list_entity_types(
    user_id="user_id",
    graph_id="graph_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — User ID to get user-specific entity types
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — Graph ID to get graph-specific entity types
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">set_entity_types_internal</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the entity types for multiple users and graphs, replacing any existing ones.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.set_entity_types_internal()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**edge_types:** `typing.Optional[typing.Sequence[EdgeType]]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_types:** `typing.Optional[typing.Sequence[EntityType]]` 
    
</dd>
</dl>

<dl>
<dd>

**graph_ids:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add data to the graph.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.add(
    data="data",
    type="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `GraphDataType` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — graph_id is the ID of the graph to which the data will be added. If adding to the user graph, please use user_id field instead.
    
</dd>
</dl>

<dl>
<dd>

**source_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — User ID is the ID of the user to which the data will be added. If not adding to a user graph, please use graph_id field instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">add_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add data to the graph in batch mode, processing episodes concurrently. Use only for data that is insensitive to processing order.
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
from zep_cloud import EpisodeData, Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.add_batch(
    episodes=[
        EpisodeData(
            data="data",
            type="text",
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

**episodes:** `typing.Sequence[EpisodeData]` 
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — graph_id is the ID of the graph to which the data will be added. If adding to the user graph, please use user_id field instead.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — User ID is the ID of the user to which the data will be added. If not adding to a user graph, please use graph_id field instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">add_fact_triple</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a fact triple for a user or group
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.add_fact_triple(
    fact="fact",
    fact_name="fact_name",
    source_node_name="source_node_name",
    target_node_name="target_node_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fact:** `str` — The fact relating the two nodes that this edge represents
    
</dd>
</dl>

<dl>
<dd>

**fact_name:** `str` — The name of the edge to add. Should be all caps using snake case (eg RELATES_TO)
    
</dd>
</dl>

<dl>
<dd>

**source_node_name:** `str` — The name of the source node to add
    
</dd>
</dl>

<dl>
<dd>

**target_node_name:** `str` — The name of the target node to add
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[str]` — The timestamp of the message
    
</dd>
</dl>

<dl>
<dd>

**expired_at:** `typing.Optional[str]` — The time (if any) at which the edge expires
    
</dd>
</dl>

<dl>
<dd>

**fact_uuid:** `typing.Optional[str]` — The uuid of the edge to add
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**invalid_at:** `typing.Optional[str]` — The time (if any) at which the fact stops being true
    
</dd>
</dl>

<dl>
<dd>

**source_node_summary:** `typing.Optional[str]` — The summary of the source node to add
    
</dd>
</dl>

<dl>
<dd>

**source_node_uuid:** `typing.Optional[str]` — The source node uuid
    
</dd>
</dl>

<dl>
<dd>

**target_node_summary:** `typing.Optional[str]` — The summary of the target node to add
    
</dd>
</dl>

<dl>
<dd>

**target_node_uuid:** `typing.Optional[str]` — The target node uuid
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**valid_at:** `typing.Optional[str]` — The time at which the fact becomes true
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">clone</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clone a user or group graph.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.clone()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_graph_id:** `typing.Optional[str]` — source_graph_id is the ID of the graph to be cloned. Required if source_user_id is not provided
    
</dd>
</dl>

<dl>
<dd>

**source_user_id:** `typing.Optional[str]` — user_id of the user whose graph is being cloned. Required if source_graph_id is not provided
    
</dd>
</dl>

<dl>
<dd>

**target_graph_id:** `typing.Optional[str]` — target_graph_id is the ID to be set on the cloned graph. Must not point to an existing graph. Required if target_user_id is not provided.
    
</dd>
</dl>

<dl>
<dd>

**target_user_id:** `typing.Optional[str]` — user_id to be set on the cloned user. Must not point to an existing user. Required if target_graph_id is not provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new graph.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.create(
    graph_id="graph_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fact_rating_instruction:** `typing.Optional[FactRatingInstruction]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">list_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all graphs. In order to list users, use user.list_ordered instead
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.list_all(
    page_number=1,
    page_size=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Page number for pagination, starting from 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of graphs to retrieve per page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a graph search query.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.search(
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

**query:** `str` — The string to search for (required)
    
</dd>
</dl>

<dl>
<dd>

**bfs_origin_node_uuids:** `typing.Optional[typing.Sequence[str]]` — Nodes that are the origins of the BFS searches
    
</dd>
</dl>

<dl>
<dd>

**center_node_uuid:** `typing.Optional[str]` — Node to rerank around for node distance reranking
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — The graph_id to search in. When searching user graph, please use user_id instead.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of facts to retrieve. Defaults to 10. Limited to 50.
    
</dd>
</dl>

<dl>
<dd>

**min_fact_rating:** `typing.Optional[float]` — The minimum rating by which to filter relevant facts
    
</dd>
</dl>

<dl>
<dd>

**min_score:** `typing.Optional[float]` — Deprecated
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` — weighting for maximal marginal relevance
    
</dd>
</dl>

<dl>
<dd>

**reranker:** `typing.Optional[Reranker]` — Defaults to RRF
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[GraphSearchScope]` — Defaults to Edges. Communities will be added in the future.
    
</dd>
</dl>

<dl>
<dd>

**search_filters:** `typing.Optional[SearchFilters]` — Search filters to apply to the search
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — The user_id when searching user graph. If not searching user graph, please use graph_id instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a graph.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.get(
    graph_id="graphId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_id:** `str` — The graph_id of the graph to get.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a graph. If you would like to delete a user graph, make sure to use user.delete instead.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.delete(
    graph_id="graphId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_id:** `str` — Graph ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates information about a graph.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.update(
    graph_id="graphId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_id:** `str` — Graph ID
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fact_rating_instruction:** `typing.Optional[FactRatingInstruction]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve project info based on the provided api key.
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

client = Zep(
    api_key="YOUR_API_KEY",
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

## Task
<details><summary><code>client.task.<a href="src/zep_cloud/task/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a task by its ID
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.task.get(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — Task ID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">list_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all threads.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.list_all(
    page_number=1,
    page_size=1,
    order_by="order_by",
    asc=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Page number for pagination, starting from 1
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of threads to retrieve per page.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by: created_at, updated_at, user_id, thread_id.
    
</dd>
</dl>

<dl>
<dd>

**asc:** `typing.Optional[bool]` — Order direction: true for ascending, false for descending.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a new thread.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.create(
    thread_id="thread_id",
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str` — The unique identifier of the thread.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user associated with the thread
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a thread.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.delete(
    thread_id="threadId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str` — The ID of the thread for which memory should be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">get_user_context</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns most relevant context from the user graph (including memory from any/all past threads) based on the content of the past few messages of the given thread.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.get_user_context(
    thread_id="threadId",
    min_rating=1.1,
    template_id="template_id",
    mode="basic",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str` — The ID of the current thread (for which context is being retrieved).
    
</dd>
</dl>

<dl>
<dd>

**min_rating:** `typing.Optional[float]` — The minimum rating by which to filter relevant facts.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Optional template ID to use for custom context rendering.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ThreadGetUserContextRequestMode]` — Deprecated, this field will be removed in a future release. Defaults to summary mode. Use basic for lower latency
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns messages for a thread.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.get(
    thread_id="threadId",
    limit=1,
    cursor=1,
    lastn=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**thread_id:** `str` — Thread ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of results returned
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[int]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**lastn:** `typing.Optional[int]` — Number of most recent messages to return (overrides limit and cursor)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">add_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add messages to a thread.
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
from zep_cloud import Message, Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.add_messages(
    thread_id="threadId",
    messages=[
        Message(
            content="content",
            role="norole",
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

**thread_id:** `str` — The ID of the thread to which messages should be added.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[Message]` — A list of message objects, where each message contains a role and content.
    
</dd>
</dl>

<dl>
<dd>

**ignore_roles:** `typing.Optional[typing.Sequence[RoleType]]` 

Optional list of role types to ignore when adding messages to graph memory.
The message itself will still be added, retained and used as context for messages
that are added to a user's graph.
    
</dd>
</dl>

<dl>
<dd>

**return_context:** `typing.Optional[bool]` — Optionally return context block relevant to the most recent messages.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">add_messages_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add messages to a thread in batch mode. This will process messages concurrently, which is useful for data migrations.
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
from zep_cloud import Message, Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.add_messages_batch(
    thread_id="threadId",
    messages=[
        Message(
            content="content",
            role="norole",
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

**thread_id:** `str` — The ID of the thread to which messages should be added.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[Message]` — A list of message objects, where each message contains a role and content.
    
</dd>
</dl>

<dl>
<dd>

**ignore_roles:** `typing.Optional[typing.Sequence[RoleType]]` 

Optional list of role types to ignore when adding messages to graph memory.
The message itself will still be added, retained and used as context for messages
that are added to a user's graph.
    
</dd>
</dl>

<dl>
<dd>

**return_context:** `typing.Optional[bool]` — Optionally return context block relevant to the most recent messages.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">list_user_summary_instructions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all user summary instructions for a project, user.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.list_user_summary_instructions(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — User ID to get user-specific instructions
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">add_user_summary_instructions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds new summary instructions for users graphs without removing existing ones. If user_ids is empty, adds to project-wide default instructions.
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
from zep_cloud import UserInstruction, Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.add_user_summary_instructions(
    instructions=[
        UserInstruction(
            name="name",
            text="text",
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

**instructions:** `typing.Sequence[UserInstruction]` — Instructions to add to the user summary generation.
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.Sequence[str]]` — User IDs to add the instructions to. If empty, the instructions are added to the project-wide default.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">delete_user_summary_instructions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes user summary/instructions for users or project wide defaults.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.delete_user_summary_instructions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**instruction_names:** `typing.Optional[typing.Sequence[str]]` — Unique identifier for the instructions to be deleted. If empty deletes all instructions.
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.Sequence[str]]` — Determines which users will have their custom instructions deleted. If no users are provided, the project-wide custom instructions will be effected.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a user.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.add(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**disable_default_ontology:** `typing.Optional[bool]` — When true, disables the use of default/fallback ontology for the user's graph.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The email address of the user.
    
</dd>
</dl>

<dl>
<dd>

**fact_rating_instruction:** `typing.Optional[FactRatingInstruction]` — Optional instruction to use for fact rating.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of the user.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name of the user.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The metadata associated with the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">list_ordered</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all users.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.list_ordered(
    page_number=1,
    page_size=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_number:** `typing.Optional[int]` — Page number for pagination, starting from 1
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of users to retrieve per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a user.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.get(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user_id of the user to get.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a user.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.delete(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a user.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.update(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**disable_default_ontology:** `typing.Optional[bool]` — When true, disables the use of default/fallback ontology for the user's graph.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The email address of the user.
    
</dd>
</dl>

<dl>
<dd>

**fact_rating_instruction:** `typing.Optional[FactRatingInstruction]` — Optional instruction to use for fact rating.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of the user.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name of the user.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The metadata to update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">get_node</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a user's node.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.get_node(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — The user_id of the user to get the node for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">get_threads</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all threads for a user.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.get_threads(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">warm</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Hints Zep to warm a user's graph for low-latency search
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.warm(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">get_by_graph_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all edges for a graph.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.edge.get_by_graph_id(
    graph_id="graph_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_id:** `str` — Graph ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` — UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">get_by_user_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all edges for a user.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.edge.get_by_user_id(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` — UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific edge by its UUID.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.edge.get(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` — Edge UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an edge by UUID.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.edge.delete(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` — Edge UUID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">get_by_graph_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns episodes by graph id.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.episode.get_by_graph_id(
    graph_id="graph_id",
    lastn=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_id:** `str` — Graph ID
    
</dd>
</dl>

<dl>
<dd>

**lastn:** `typing.Optional[int]` — The number of most recent episodes to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">get_by_user_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns episodes by user id.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.episode.get_by_user_id(
    user_id="user_id",
    lastn=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**lastn:** `typing.Optional[int]` — The number of most recent episodes entries to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns episodes by UUID
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.episode.get(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` — Episode UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an episode by its UUID.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.episode.delete(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` — Episode UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">get_nodes_and_edges</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns nodes and edges mentioned in an episode
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.episode.get_nodes_and_edges(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` — Episode uuid
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">get_by_graph_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all nodes for a graph.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.node.get_by_graph_id(
    graph_id="graph_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_id:** `str` — Graph ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` — UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">get_by_user_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all nodes for a user
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.node.get_by_user_id(
    user_id="user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — User ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` — UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">get_edges</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all edges for a node
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.node.get_edges(
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

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">get_episodes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all episodes that mentioned a given node
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.node.get_episodes(
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

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific node by its UUID.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.node.get(
    uuid_="uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**uuid_:** `str` — Node UUID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.thread.message.<a href="src/zep_cloud/thread/message/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a message.
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

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.message.update(
    message_uuid="messageUUID",
    metadata={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**message_uuid:** `str` — The UUID of the message.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

