# Reference
## Document
<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">list_collections</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all DocumentCollections.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.list_collections()

```
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

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">get_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a DocumentCollection if it exists.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.get_collection(
    collection_name="collectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">add_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If a collection with the same name already exists, an error will be returned.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.add_collection(
    collection_name="collectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">delete_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

If a collection with the same name already exists, it will be overwritten.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.delete_collection(
    collection_name="collectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">update_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a DocumentCollection
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.update_collection(
    collection_name="collectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">add_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates Documents in a specified DocumentCollection and returns their UUIDs.
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
from zep_cloud import CreateDocumentRequest
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.add_documents(
    collection_name="collectionName",
    request=[
        CreateDocumentRequest(
            content="content",
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

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[CreateDocumentRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">batch_delete_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes specified Documents from a DocumentCollection.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.batch_delete_documents(
    collection_name="collectionName",
    request=["string"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">batch_get_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns Documents from a DocumentCollection specified by UUID or ID.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.batch_get_documents(
    collection_name="collectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**document_ids:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**uuids:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">batch_update_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates Documents in a specified DocumentCollection.
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
from zep_cloud import UpdateDocumentListRequest
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.batch_update_documents(
    collection_name="collectionName",
    request=[
        UpdateDocumentListRequest(
            uuid_="uuid",
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

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[UpdateDocumentListRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">gets_a_document_from_a_document_collection_by_uuid</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns specified Document from a DocumentCollection.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.gets_a_document_from_a_document_collection_by_uuid(
    collection_name="collectionName",
    document_uuid="documentUUID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**document_uuid:** `str` — UUID of the Document to be updated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">delete_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete specified Document from a DocumentCollection.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.delete_document(
    collection_name="collectionName",
    document_uuid="documentUUID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**document_uuid:** `str` — UUID of the Document to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">updates_a_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Document in a DocumentCollection by UUID
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.updates_a_document(
    collection_name="collectionName",
    document_uuid="documentUUID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**document_uuid:** `str` — UUID of the Document to be updated
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document.<a href="src/zep_cloud/document/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches over documents in a collection based on provided search criteria. One of text or metadata must be provided. Returns an empty list if no documents are found.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.document.search(
    collection_name="collectionName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_name:** `str` — Name of the Document Collection
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of returned documents
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Document metadata to filter on.
    
</dd>
</dl>

<dl>
<dd>

**min_score:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` — The lambda parameter for the MMR Reranking Algorithm.
    
</dd>
</dl>

<dl>
<dd>

**search_type:** `typing.Optional[SearchType]` — The type of search to perform. Defaults to "similarity". Must be one of "similarity" or "mmr".
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — The search text.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">list_entity_types</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all entity types for a project.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.list_entity_types()

```
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

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">set_entity_types_internal</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the entity types for a project, replacing any existing ones.
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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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

**group_id:** `typing.Optional[str]` — Deprecated: Use graph_id instead
    
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
from zep_cloud import EpisodeData
from zep_cloud.client import Zep

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

**group_id:** `typing.Optional[str]` — Deprecated: Use graph_id instead
    
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.add_fact_triple(
    fact="fact",
    fact_name="fact_name",
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

**group_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**invalid_at:** `typing.Optional[str]` — The time (if any) at which the fact stops being true
    
</dd>
</dl>

<dl>
<dd>

**source_node_name:** `typing.Optional[str]` — The name of the source node to add
    
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
from zep_cloud.client import Zep

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

**source_graph_id:** `typing.Optional[str]` — source_graph_id is the ID of the graph to be cloned. Required if user_id is not provided
    
</dd>
</dl>

<dl>
<dd>

**source_group_id:** `typing.Optional[str]` — Deprecated: Use source_graph_id instead
    
</dd>
</dl>

<dl>
<dd>

**source_user_id:** `typing.Optional[str]` — user_id of the user whose graph is being cloned. Required if graph_id is not provided
    
</dd>
</dl>

<dl>
<dd>

**target_graph_id:** `typing.Optional[str]` — target_graph_id is the ID to be set on the cloned graph. Must not point to an existing graph. Required if user_id is not provided.
    
</dd>
</dl>

<dl>
<dd>

**target_group_id:** `typing.Optional[str]` — Deprecated: Use target_graph_id instead
    
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
from zep_cloud.client import Zep

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

**group_id:** `typing.Optional[str]` — Deprecated: Use graph_id instead
    
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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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

## Memory
<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">get_fact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated API: get fact by uuid
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.get_fact(
    fact_uuid="factUUID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fact_uuid:** `str` — Fact UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">delete_fact</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated API: delete a fact
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.delete_fact(
    fact_uuid="factUUID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fact_uuid:** `str` — Fact UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">add_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Creates a new session. Use thread.create instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.add_session(
    session_id="session_id",
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

**session_id:** `str` — The unique identifier of the session.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — The unique identifier of the user associated with the session
    
</dd>
</dl>

<dl>
<dd>

**fact_rating_instruction:** `typing.Optional[FactRatingInstruction]` — Deprecated
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Deprecated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">list_sessions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Returns all sessions. Use GET /threads instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.list_sessions()

```
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

**page_size:** `typing.Optional[int]` — Number of sessions to retrieve per page.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to order the results by: created_at, updated_at, user_id, session_id.
    
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

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">end_sessions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated API: End multiple sessions by their IDs.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.end_sessions(
    session_ids=["session_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_ids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**instruction:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">search_sessions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated API: Search sessions for the specified query.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.search_sessions(
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text:** `str` — The search text.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of search results to return. Defaults to None (no limit).
    
</dd>
</dl>

<dl>
<dd>

**min_fact_rating:** `typing.Optional[float]` — The minimum fact rating to filter on.
    
</dd>
</dl>

<dl>
<dd>

**min_score:** `typing.Optional[float]` — The minimum score for search results.
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` — The lambda parameter for the MMR Reranking Algorithm.
    
</dd>
</dl>

<dl>
<dd>

**record_filter:** `typing.Optional[typing.Dict[str, typing.Any]]` — Record filter on the metadata.
    
</dd>
</dl>

<dl>
<dd>

**search_scope:** `typing.Optional[SearchScope]` — Search scope.
    
</dd>
</dl>

<dl>
<dd>

**search_type:** `typing.Optional[SearchType]` — Search type.
    
</dd>
</dl>

<dl>
<dd>

**session_ids:** `typing.Optional[typing.Sequence[str]]` — the session ids to search
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — User ID used to determine which sessions to search.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">get_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a session. Deprecated: use thread.get instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.get_session(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The unique identifier of the session.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">update_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update Session Metadata. Deprecated: This endpoint is no longer supported and will be removed in a future release.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.update_session(
    session_id="sessionId",
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

**session_id:** `str` — The unique identifier of the session.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Dict[str, typing.Any]` — Deprecated
    
</dd>
</dl>

<dl>
<dd>

**fact_rating_instruction:** `typing.Optional[FactRatingInstruction]` 

Optional instruction to use for fact rating.
Fact rating instructions can not be unset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">classify_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Classifies a session.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.classify_session(
    session_id="sessionId",
    classes=["classes"],
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

**session_id:** `str` — Session ID
    
</dd>
</dl>

<dl>
<dd>

**classes:** `typing.Sequence[str]` — The classes to use for classification.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the classifier.
    
</dd>
</dl>

<dl>
<dd>

**instruction:** `typing.Optional[str]` — Custom instruction to use for classification.
    
</dd>
</dl>

<dl>
<dd>

**last_n:** `typing.Optional[int]` — The number of session messages to consider for classification. Defaults to 4.
    
</dd>
</dl>

<dl>
<dd>

**persist:** `typing.Optional[bool]` — Deprecated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">end_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated API: End a session by ID.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.end_session(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID
    
</dd>
</dl>

<dl>
<dd>

**classify:** `typing.Optional[ClassifySessionRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**instruction:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">extract_data</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: extract data from a session by session id
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.extract_data(
    session_id="sessionId",
    last_n=1,
    model_schema="model_schema",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID
    
</dd>
</dl>

<dl>
<dd>

**last_n:** `int` — The number of messages in the chat history from which to extract data
    
</dd>
</dl>

<dl>
<dd>

**model_schema:** `str` — The schema describing the data to be extracted. See Zep's SDKs for more details.
    
</dd>
</dl>

<dl>
<dd>

**current_date_time:** `typing.Optional[str]` — Your current date and time in ISO 8601 format including timezone. This is used for determining relative dates.
    
</dd>
</dl>

<dl>
<dd>

**validate:** `typing.Optional[bool]` 

Validate that the extracted data is present in the dialog and correct per the field description.
Mitigates hallucination, but is slower and may result in false negatives.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">get_session_facts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated API: get facts for a session
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.get_session_facts(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID
    
</dd>
</dl>

<dl>
<dd>

**min_rating:** `typing.Optional[float]` — Minimum rating by which to filter facts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">add_session_facts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated API: Adds facts to a session
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
from zep_cloud import NewFact
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.add_session_facts(
    session_id="sessionId",
    facts=[
        NewFact(
            fact="fact",
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

**session_id:** `str` — Session ID
    
</dd>
</dl>

<dl>
<dd>

**facts:** `typing.Sequence[NewFact]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Returns a memory for a given session. Use thread.get_user_context instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.get(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The ID of the session for which to retrieve memory.
    
</dd>
</dl>

<dl>
<dd>

**lastn:** `typing.Optional[int]` — The number of most recent memory entries to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**min_rating:** `typing.Optional[float]` — The minimum rating by which to filter relevant facts.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Add memory to the specified session. Use thread.add_messages instead.
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
from zep_cloud import Message
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.add(
    session_id="sessionId",
    messages=[
        Message(
            content="content",
            role_type="norole",
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

**session_id:** `str` — The ID of the session to which memory should be added.
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[Message]` — A list of message objects, where each message contains a role and content.
    
</dd>
</dl>

<dl>
<dd>

**fact_instruction:** `typing.Optional[str]` — Deprecated
    
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

**return_context:** `typing.Optional[bool]` — Optionally return memory context relevant to the most recent messages.
    
</dd>
</dl>

<dl>
<dd>

**summary_instruction:** `typing.Optional[str]` — Deprecated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Deletes a session. Use thread.delete instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.delete(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The ID of the session for which memory should be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">get_session_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Returns messages for a session. Use thread.get instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.get_session_messages(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">get_session_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Use graph.episodes.get instead. Returns a specific message from a session.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.get_session_message(
    session_id="sessionId",
    message_uuid="messageUUID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Soon to be deprecated as this is not needed.
    
</dd>
</dl>

<dl>
<dd>

**message_uuid:** `str` — The UUID of the message.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">update_message_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the metadata of a message.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.update_message_metadata(
    session_id="sessionId",
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

**session_id:** `str` — The ID of the session.
    
</dd>
</dl>

<dl>
<dd>

**message_uuid:** `str` — The UUID of the message.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Dict[str, typing.Any]` — Deprecated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.search(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The ID of the session for which memory should be searched.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of search results to return. Defaults to None (no limit).
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Metadata Filter
    
</dd>
</dl>

<dl>
<dd>

**min_fact_rating:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**min_score:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**search_scope:** `typing.Optional[SearchScope]` 
    
</dd>
</dl>

<dl>
<dd>

**search_type:** `typing.Optional[SearchType]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">get_summaries</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated API: Get session summaries by ID
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.get_summaries(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — Session ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.memory.<a href="src/zep_cloud/memory/client.py">synthesize_question</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated API: Synthesize a question from the last N messages in the chat history.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.memory.synthesize_question(
    session_id="sessionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The ID of the session.
    
</dd>
</dl>

<dl>
<dd>

**last_n_messages:** `typing.Optional[int]` — The number of messages to use for question synthesis.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Group
<details><summary><code>client.group.<a href="src/zep_cloud/group/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new group. Deprecated, use graph.create instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.group.add(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` 
    
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

<details><summary><code>client.group.<a href="src/zep_cloud/group/client.py">get_all_groups</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all groups.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.group.get_all_groups()

```
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

**page_size:** `typing.Optional[int]` — Number of groups to retrieve per page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.group.<a href="src/zep_cloud/group/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a group. Deprecated - use graph.get instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.group.get(
    group_id="groupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — The group_id of the group to get.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.group.<a href="src/zep_cloud/group/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a group. Deprecated - use graph.delete instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.group.delete(
    group_id="groupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — Group ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.group.<a href="src/zep_cloud/group/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates information about a group. Deprecated.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.group.update(
    group_id="groupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — Group ID
    
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

<details><summary><code>client.group.<a href="src/zep_cloud/group/client.py">get_facts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Use Get Group Edges instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.group.get_facts(
    group_id="groupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — The group_id of the group to get.
    
</dd>
</dl>

<dl>
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.list_all()

```
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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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

Returns most relevant context for a given thread.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.get_user_context(
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

**thread_id:** `str` — The ID of the thread for which to retrieve context.
    
</dd>
</dl>

<dl>
<dd>

**lastn:** `typing.Optional[int]` — The number of most recent memory entries to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**min_rating:** `typing.Optional[float]` — The minimum rating by which to filter relevant facts.
    
</dd>
</dl>

<dl>
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.get(
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
from zep_cloud import Message
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.thread.add_messages(
    thread_id="threadId",
    messages=[
        Message(
            content="content",
            role_type="norole",
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

**return_context:** `typing.Optional[bool]` — Optionally return memory context relevant to the most recent messages.
    
</dd>
</dl>

<dl>
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
from zep_cloud.client import Zep

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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — The metadata associated with the user.
    
</dd>
</dl>

<dl>
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.list_ordered()

```
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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — The metadata to update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">get_facts</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated: Use Get User Edges instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.get_facts(
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
from zep_cloud.client import Zep

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

<details><summary><code>client.user.<a href="src/zep_cloud/user/client.py">get_sessions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all sessions for a user.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.user.get_sessions(
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
from zep_cloud.client import Zep

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

<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">get_by_group_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all edges for a group. Deprecated, please use graph.edge.get_by_graph_id instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.edge.get_by_group_id(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — Group ID
    
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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.episode.get_by_graph_id(
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

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">get_by_group_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns episodes by group id. Deprecated, please use graph.episode.get_by_graph_id instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.episode.get_by_group_id(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — Group ID
    
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.episode.get_by_user_id(
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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">get_by_group_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all nodes for a group. Deprecated, please use graph.node.get_by_graph_id instead.
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
from zep_cloud.client import Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.node.get_by_group_id(
    group_id="group_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_id:** `str` — Group ID
    
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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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
from zep_cloud.client import Zep

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

