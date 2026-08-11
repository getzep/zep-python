# Reference
## UserGroup
<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">list_policy_sets</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.list_policy_sets(
    group_uuid="groupUUID",
    project_id="projectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">attach_policy_set</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.attach_policy_set(
    group_uuid="groupUUID",
    project_id="projectId",
    policy_set_uuid="policy_set_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**policy_set_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">detach_policy_set</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.detach_policy_set(
    group_uuid="groupUUID",
    policy_set_uuid="policySetUUID",
    project_id="projectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**policy_set_uuid:** `str` — Policy set UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">list</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.list(
    project_id="projectId",
    page_number=1,
    page_size=1,
    search="search",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` — Page number
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `int` — Page size
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Name search
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">create</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.create(
    project_id="projectId",
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

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">list_for_user</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.list_for_user(
    user_uuid="userUUID",
    project_id="projectId",
)

```
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

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">get</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.get(
    group_uuid="groupUUID",
    project_id="projectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
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
client.user_group.delete(
    group_uuid="groupUUID",
    project_id="projectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">update</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.update(
    group_uuid="groupUUID",
    project_id="projectId",
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

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**expected_version:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">list_members</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.list_members(
    group_uuid="groupUUID",
    project_id="projectId",
    page_number=1,
    page_size=1,
    search="search",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` — Page number
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `int` — Page size
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — User search
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">add_members</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.add_members(
    group_uuid="groupUUID",
    project_id="projectId",
    user_uuids=["user_uuids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**user_uuids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">remove_members</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.remove_members(
    group_uuid="groupUUID",
    project_id="projectId",
    user_uuids=["user_uuids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**user_uuids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.user_group.<a href="src/zep_cloud/user_group/client.py">list_member_candidates</a>(...)</code></summary>
<dl>
<dd>

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
client.user_group.list_member_candidates(
    group_uuid="groupUUID",
    project_id="projectId",
    page_number=1,
    page_size=1,
    search="search",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `int` — Page number
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `int` — Page size
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — User search
    
</dd>
</dl>

<dl>
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
client.user_group.remove_member(
    group_uuid="groupUUID",
    user_uuid="userUUID",
    project_id="projectId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**group_uuid:** `str` — UserGroup UUID
    
</dd>
</dl>

<dl>
<dd>

**user_uuid:** `str` — User UUID
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `str` — Project UUID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List batches for the current project, optionally filtered by batch status.
</dd>
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
client.batch.list(
    limit=1,
    cursor=1,
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

**limit:** `typing.Optional[int]` — Maximum number of batches to return.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[int]` — Pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Batch status filter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a draft batch that can be filled with graph episodes and thread messages.
</dd>
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

**ignore_roles:** `typing.Optional[typing.Sequence[RoleType]]` 

Optional list of message role types to skip during graph ingestion for
thread_message items in this batch. The messages are still stored and
retained as context, but no graph extraction is performed for them.
Has no effect on graph_episode items.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a batch summary, including runtime progress when the batch has been processed.
</dd>
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
client.batch.get(
    batch_id="batchId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `str` — The batch ID.
    
</dd>
</dl>

<dl>
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a draft or invalid unprocessed batch. Processed batches cannot be deleted.
</dd>
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
client.batch.delete(
    batch_id="batchId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `str` — The batch ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">list_items</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List items in a batch, including derived runtime status when the batch has been processed.
</dd>
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
client.batch.list_items(
    batch_id="batchId",
    limit=1,
    cursor=1,
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

**batch_id:** `str` — The batch ID.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of batch items to return.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[int]` — Pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Batch item status filter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add graph episodes and thread messages to a draft batch. Items are appended in request order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import BatchAddItem, Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.batch.add(
    batch_id="batchId",
    items=[
        BatchAddItem(
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

**batch_id:** `str` — The batch ID.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Sequence[BatchAddItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/zep_cloud/batch/client.py">process</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start processing a filled batch. Repeated calls return a conflict.
</dd>
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
client.batch.process(
    batch_id="batchId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `str` — The batch ID.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">list_custom_instructions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all custom instructions for a project, user, or graph.
</dd>
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
client.graph.list_custom_instructions(
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

**user_id:** `typing.Optional[str]` — User ID to get user-specific instructions
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — Graph ID to get graph-specific instructions
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">add_custom_instructions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds new custom instructions for graphs without removing existing ones. If user_ids or graph_ids is empty, adds to project-wide default instructions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import CustomInstruction, Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.add_custom_instructions(
    instructions=[
        CustomInstruction(
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

**instructions:** `typing.Sequence[CustomInstruction]` — Instructions to add to the graph.
    
</dd>
</dl>

<dl>
<dd>

**graph_ids:** `typing.Optional[typing.Sequence[str]]` — Graph IDs to add the instructions to. If empty, the instructions are added to the project-wide default.
    
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

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">delete_custom_instructions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes custom instructions for graphs or project wide defaults.
</dd>
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
client.graph.delete_custom_instructions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**graph_ids:** `typing.Optional[typing.Sequence[str]]` — Determines which group graphs will have their custom instructions deleted. If no graphs are provided, the project-wide custom instructions will be affected.
    
</dd>
</dl>

<dl>
<dd>

**instruction_names:** `typing.Optional[typing.Sequence[str]]` — Unique identifier for the instructions to be deleted. If empty deletes all instructions.
    
</dd>
</dl>

<dl>
<dd>

**user_ids:** `typing.Optional[typing.Sequence[str]]` — Determines which user graphs will have their custom instructions deleted. If no users are provided, the project-wide custom instructions will be affected.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

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

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional metadata key-value pairs. Max 10 keys. Values must be strings, numbers, booleans, or arrays of scalars.
    
</dd>
</dl>

<dl>
<dd>

**source_description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**strict_ontology:** `typing.Optional[bool]` — When true, prevents extraction of generic Entity nodes that do not match the configured ontology.
    
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

Deprecated. Use the [Batch API](/adding-batch-data) (`client.batch.*`) instead.

Adds data to the graph in batch mode, processing episodes concurrently.
</dd>
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

**strict_ontology:** `typing.Optional[bool]` — When true, prevents extraction of generic Entity nodes that do not match the configured ontology.
    
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
)

```
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

**created_at:** `typing.Optional[str]` — The timestamp of the message
    
</dd>
</dl>

<dl>
<dd>

**edge_attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

Additional attributes of the edge. Values must be scalar types (string, number, boolean, or null).
Nested objects and arrays are not allowed.
    
</dd>
</dl>

<dl>
<dd>

**expired_at:** `typing.Optional[str]` — The time (if any) at which the edge expires
    
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

Optional metadata key-value pairs for the shadow episode created for this fact triple.
Max 10 keys. Values must be strings, numbers, or booleans.
    
</dd>
</dl>

<dl>
<dd>

**source_node_attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

Additional attributes of the source node. Values must be scalar types (string, number, boolean, or null).
Nested objects and arrays are not allowed.
    
</dd>
</dl>

<dl>
<dd>

**source_node_labels:** `typing.Optional[typing.Sequence[str]]` 

The labels for the source node. At most one entity-type label may be
provided so that manually-added triples remain consistent with automatic
episode extraction, which assigns one best-match entity type per node.
The base "Entity" label is added implicitly by the graph layer on save
and does not need to be supplied here.
    
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

**target_node_attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

Additional attributes of the target node. Values must be scalar types (string, number, boolean, or null).
Nested objects and arrays are not allowed.
    
</dd>
</dl>

<dl>
<dd>

**target_node_labels:** `typing.Optional[typing.Sequence[str]]` 

The labels for the target node. At most one entity-type label may be
provided so that manually-added triples remain consistent with automatic
episode extraction, which assigns one best-match entity type per node.
The base "Entity" label is added implicitly by the graph layer on save
and does not need to be supplied here.
    
</dd>
</dl>

<dl>
<dd>

**target_node_name:** `typing.Optional[str]` — The name of the target node to add
    
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

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**time_zone:** `typing.Optional[str]` — The graph's IANA time zone. Stored on its group-backed subject.
    
</dd>
</dl>

<dl>
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
    search="search",
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

**page_number:** `typing.Optional[int]` — Page number for pagination, starting from 1.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of graphs to retrieve per page (default 50, range 1-100; explicit 0 is invalid).
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search term for filtering graphs by graph_id, name, or description. Queries longer than 200 Unicode code points after whitespace normalization are invalid.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Column to sort by (created_at, graph_id, name).
    
</dd>
</dl>

<dl>
<dd>

**asc:** `typing.Optional[bool]` — Sort in ascending order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">add_nodes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add entity nodes to a user or graph directly, without episode ingestion. Up to 100 nodes per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zep_cloud import AddNodeItem, Zep

client = Zep(
    api_key="YOUR_API_KEY",
)
client.graph.add_nodes(
    nodes=[
        AddNodeItem(
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

**nodes:** `typing.Sequence[AddNodeItem]` — The nodes to add. 1 to 100 items.
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">detect_patterns</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detects structural patterns in a knowledge graph including relationship frequencies,
multi-hop paths, co-occurrences, hubs, and clusters.
When a query is provided, uses hybrid search to discover seed nodes,
detects triple-frequency patterns, and returns resolved edges ranked by relevance.
</dd>
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
client.graph.detect_patterns()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**detect:** `typing.Optional[DetectConfig]` 

Which pattern types to detect with type-specific configuration.
Omit to detect all types with defaults. Ignored when query is set.
    
</dd>
</dl>

<dl>
<dd>

**edge_limit:** `typing.Optional[int]` — Max resolved edges per pattern. Default: 10, Max: 100. Only used with query.
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — Graph ID when detecting patterns on a named graph
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max patterns to return. Default: 50, Max: 200
    
</dd>
</dl>

<dl>
<dd>

**min_occurrences:** `typing.Optional[int]` — Minimum occurrence count to report a pattern. Default: 2
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` 

Search query for discovering seed nodes via hybrid search.
When set, forces triple-frequency detection only and enables edge resolution
with cross-encoder reranking. Mutually exclusive with seeds.
    
</dd>
</dl>

<dl>
<dd>

**query_limit:** `typing.Optional[int]` — Max seed nodes from search. Default: 10, Max: 50. Only used with query.
    
</dd>
</dl>

<dl>
<dd>

**recency_weight:** `typing.Optional[RecencyWeight]` 

Exponential half-life decay applied to edge created_at timestamps.
Valid values: none, 7_days, 30_days, 90_days. Default: none
    
</dd>
</dl>

<dl>
<dd>

**search_filters:** `typing.Optional[SearchFilters]` 

Filters which edges/nodes participate in pattern detection.
Reuses the same filter format as /graph/search.
    
</dd>
</dl>

<dl>
<dd>

**seeds:** `typing.Optional[PatternSeeds]` — Seed selection. If omitted, analyzes the entire graph. Mutually exclusive with query.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — User ID when detecting patterns on a user graph
    
</dd>
</dl>

<dl>
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

**limit:** `typing.Optional[int]` — The maximum number of facts to retrieve for non-auto scopes. Defaults to 10. Limited to 50. Ignored when scope=auto.
    
</dd>
</dl>

<dl>
<dd>

**max_characters:** `typing.Optional[int]` — Maximum total characters across all selected results when scope=auto. Defaults to 2500. Limited to 50000.
    
</dd>
</dl>

<dl>
<dd>

**mmr_lambda:** `typing.Optional[float]` — weighting for maximal marginal relevance
    
</dd>
</dl>

<dl>
<dd>

**reranker:** `typing.Optional[Reranker]` 

Defaults to RRF. Ignored when scope=auto except node_distance and episode_mentions are rejected;
auto search always uses RRF retrieval and applies its own internal rerank after retrieval.
episode_mentions ranks edge candidates by how many of the episodes listed
in search_filters.episode_uuids mention them; without episode_uuids it has
no effect and results are ranked as if no reranker were specified.
    
</dd>
</dl>

<dl>
<dd>

**return_raw_results:** `typing.Optional[bool]` 

When scope=auto, include the selected raw graph results alongside the materialized context block.
For graph-service-backed auto mode, selected raw results may include episodes,
edges, nodes, observations, and thread_summaries.
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[GraphSearchScope]` — Defaults to Edges.
    
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

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">get_subgraph</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the bounded neighborhood of a set of seed nodes as a single {nodes, edges} payload: breadth-first expansion up to a caller-specified depth, subject to explicit budgets, with explicit truncation reporting.
</dd>
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
client.graph.get_subgraph(
    seed_node_uuids=["seed_node_uuids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**seed_node_uuids:** `typing.Sequence[str]` 

Seed node UUIDs to expand from, in traversal-priority order: seeds are
admitted before any expansion, in this order, and count toward
max_nodes first. 1-20 entries, required. Seeds that do not exist in
the target graph are ignored, not an error.
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` — Maximum traversal depth from the seeds. 1-3. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` 

Edge orientation followed during expansion, relative to each frontier
node: "in" | "out" | "both". Defaults to "both".
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` 

graph_id identifies the target named graph. Exactly one of user_id or
graph_id is required.
    
</dd>
</dl>

<dl>
<dd>

**max_edges:** `typing.Optional[int]` — Maximum number of edges in the response. 1-1000. Defaults to 200.
    
</dd>
</dl>

<dl>
<dd>

**max_nodes:** `typing.Optional[int]` 

Maximum number of nodes in the response, including admitted seeds.
1-500. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**search_filters:** `typing.Optional[SearchFilters]` 

Filters constraining traversed edges and included nodes. Reuses the
graph.search filter type. search_filters.episode_metadata_filters is
rejected: it cannot be enforced during graph traversal (spec-2 §9.4).
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 

user_id identifies the target user graph. Exactly one of user_id or
graph_id is required.
    
</dd>
</dl>

<dl>
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

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**time_zone:** `typing.Optional[str]` — The graph's IANA time zone. Stored on its group-backed subject.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.<a href="src/zep_cloud/graph/client.py">warm</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Hints Zep to warm a graph for low-latency search
</dd>
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
client.graph.warm(
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

**graph_id:** `str` — The graph_id of the graph to warm.
    
</dd>
</dl>

<dl>
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

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets or clears the project-level fallback time zone for the API key's project.
</dd>
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

**default_time_zone:** `typing.Optional[str]` — The project's IANA fallback time zone. Null clears the existing value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">get_observation_steering</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns project steering or the effective user/graph steering with project fallback. This API is experimental and may change in future releases.
</dd>
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
client.project.get_observation_steering(
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

**user_id:** `typing.Optional[str]` — User ID for user-specific steering
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — Graph ID for graph-specific steering
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.project.<a href="src/zep_cloud/project/client.py">set_observation_steering</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces project, user, or graph steering. An empty configuration clears the project default or removes the user/graph override. Changes affect later materializer runs only. This API is experimental and may change in future releases.
</dd>
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
client.project.set_observation_steering(
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

**user_id:** `typing.Optional[str]` — User ID for user-specific steering
    
</dd>
</dl>

<dl>
<dd>

**graph_id:** `typing.Optional[str]` — Graph ID for graph-specific steering
    
</dd>
</dl>

<dl>
<dd>

**instruction:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[typing.Sequence[ObservationType]]` 
    
</dd>
</dl>

<dl>
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

**thread_id:** `str` — The ID of the current thread (for which context is being retrieved).
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Optional template ID to use for custom context rendering.
    
</dd>
</dl>

<dl>
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

**strict_ontology:** `typing.Optional[bool]` — When true, prevents extraction of generic Entity nodes that do not match the configured ontology.
    
</dd>
</dl>

<dl>
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

Deprecated. Use the [Batch API](/adding-batch-data) (`client.batch.*` with `type: "thread_message"`) instead.

Adds messages to a thread in batch mode, processing messages concurrently.
</dd>
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

**strict_ontology:** `typing.Optional[bool]` — When true, prevents extraction of generic Entity nodes that do not match the configured ontology.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.thread.<a href="src/zep_cloud/thread/client.py">get_summary</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the incremental summary generated from messages in the thread. Returns 404 if no summary exists for the thread.
</dd>
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
client.thread.get_summary(
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

**thread_id:** `str` — The thread ID.
    
</dd>
</dl>

<dl>
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

**time_zone:** `typing.Optional[str]` — The user's IANA time zone. Null or omission leaves it unset at creation.
    
</dd>
</dl>

<dl>
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
    search="search",
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

**page_size:** `typing.Optional[int]` — Number of users to retrieve per page
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search term for filtering users by user_id, name, or email
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Column to sort by (created_at, user_id, email)
    
</dd>
</dl>

<dl>
<dd>

**asc:** `typing.Optional[bool]` — Sort in ascending order
    
</dd>
</dl>

<dl>
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

**time_zone:** `typing.Optional[str]` — The user's IANA time zone. Null clears the existing value.
    
</dd>
</dl>

<dl>
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor response header
of the previous page. Encodes the sort field, direction, and continuation position.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc" (default "desc").
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Optional filters applied to the listed artifacts. Reuses the graph.search filter type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "created_at", "valid_at", or "uuid" (default "uuid").
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` 

UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page.

Deprecated: prefer Cursor, the opaque cursor returned via the Zep-Next-Cursor response header.
    
</dd>
</dl>

<dl>
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor response header
of the previous page. Encodes the sort field, direction, and continuation position.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc" (default "desc").
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Optional filters applied to the listed artifacts. Reuses the graph.search filter type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "created_at", "valid_at", or "uuid" (default "uuid").
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` 

UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page.

Deprecated: prefer Cursor, the opaque cursor returned via the Zep-Next-Cursor response header.
    
</dd>
</dl>

<dl>
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

<details><summary><code>client.graph.edge.<a href="src/zep_cloud/graph/edge/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an entity edge by UUID.
</dd>
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
client.graph.edge.update(
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

**attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Updated attributes. Merged with existing attributes. Set a key to null to delete it.
    
</dd>
</dl>

<dl>
<dd>

**expired_at:** `typing.Optional[str]` — Updated time at which the edge expires
    
</dd>
</dl>

<dl>
<dd>

**fact:** `typing.Optional[str]` — Updated fact for the edge
    
</dd>
</dl>

<dl>
<dd>

**invalid_at:** `typing.Optional[str]` — Updated time at which the fact stopped being true
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Updated name (relationship type) for the edge
    
</dd>
</dl>

<dl>
<dd>

**valid_at:** `typing.Optional[str]` — Updated time at which the fact becomes true
    
</dd>
</dl>

<dl>
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

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">list_by_graph_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated, filterable list of episodes for a graph.
</dd>
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
client.graph.episode.list_by_graph_id(
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor
response header of the previous page.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc". Defaults to "desc".
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Maximum number of episodes to return. An explicit value is clamped to
50; when omitted, the default page size (100) applies.
    
</dd>
</dl>

<dl>
<dd>

**mentioned_node_uuids:** `typing.Optional[typing.Sequence[str]]` 

Restricts results to episodes that mention any of the listed node
UUIDs. At most 256 entries; each must be a syntactically valid UUID.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "uuid" or "created_at". Defaults to "uuid".
    
</dd>
</dl>

<dl>
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

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">list_by_user_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated, filterable list of episodes for a user's graph.
</dd>
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
client.graph.episode.list_by_user_id(
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor
response header of the previous page.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc". Defaults to "desc".
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Maximum number of episodes to return. An explicit value is clamped to
50; when omitted, the default page size (100) applies.
    
</dd>
</dl>

<dl>
<dd>

**mentioned_node_uuids:** `typing.Optional[typing.Sequence[str]]` 

Restricts results to episodes that mention any of the listed node
UUIDs. At most 256 entries; each must be a syntactically valid UUID.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "uuid" or "created_at". Defaults to "uuid".
    
</dd>
</dl>

<dl>
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

<details><summary><code>client.graph.episode.<a href="src/zep_cloud/graph/episode/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update episode metadata with merge semantics. Supplied keys overwrite or add to existing metadata; keys set to null are removed.
</dd>
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
client.graph.episode.update(
    uuid_="uuid",
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

**uuid_:** `str` — Episode UUID
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Dict[str, typing.Optional[typing.Any]]` — Updated metadata. Merged with existing metadata: supplied keys overwrite/add, keys set to null are removed. Maximum 10 keys. Values must be scalars (string, number, boolean, null) or arrays of scalars.
    
</dd>
</dl>

<dl>
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

Deprecated. Use edge and node listing with `filters.episode_uuids` instead. Returns nodes and edges mentioned in an episode, subject to an internal cap; responses reduced by that cap set the Zep-Truncated header.
</dd>
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor response header
of the previous page. Encodes the sort field, direction, and continuation position.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc" (default "desc").
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Optional filters applied to the listed artifacts. Reuses the graph.search filter type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "created_at", "valid_at", or "uuid" (default "uuid").
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` 

UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page.

Deprecated: prefer Cursor, the opaque cursor returned via the Zep-Next-Cursor response header.
    
</dd>
</dl>

<dl>
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor response header
of the previous page. Encodes the sort field, direction, and continuation position.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc" (default "desc").
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Optional filters applied to the listed artifacts. Reuses the graph.search filter type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "created_at", "valid_at", or "uuid" (default "uuid").
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` 

UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page.

Deprecated: prefer Cursor, the opaque cursor returned via the Zep-Next-Cursor response header.
    
</dd>
</dl>

<dl>
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

Deprecated. Use edge listing with `filters.connected_node_uuids`, or the neighbors endpoint (`POST /graph/node/{node_uuid}/neighbors`), instead. Returns all edges for a node, subject to an internal cap; responses reduced by that cap set the Zep-Truncated header.
</dd>
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

Deprecated. Use episode listing with `mentioned_node_uuids` (`POST /graph/episodes/graph/{graph_id}` or `POST /graph/episodes/user/{user_id}`) instead. Returns episodes that mentioned a given node, subject to an internal cap; responses reduced by that cap set the Zep-Truncated header.
</dd>
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

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">get_neighbors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enumerates the distinct entity nodes directly connected to a node, together with the edges connecting each to it.
</dd>
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
client.graph.node.get_neighbors(
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor
response header of the previous page.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` 

Orientation of the connecting edge relative to the anchor node: "out"
(anchor is the edge's source), "in" (anchor is the edge's target), or
"both" (either). Defaults to "both".
    
</dd>
</dl>

<dl>
<dd>

**direction_sort:** `typing.Optional[str]` 

Sort direction for order_by. One of "asc" or "desc". Defaults to
"desc". Named direction_sort to avoid clashing with the traversal
Direction field above.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` 

Filters constraining the connecting edges (edge types, dates, and the
section-3 node-/episode-anchored fields) and the neighbor nodes
(node_labels/exclude_node_labels). Reuses the graph.search filter
type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

Maximum number of neighbor nodes to return. An explicit value is
clamped to 50; when omitted, the default page size (100) applies.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` 

Field to sort neighbor nodes by. One of "uuid" or "created_at".
Defaults to "uuid".
    
</dd>
</dl>

<dl>
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

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a node by UUID.
</dd>
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
client.graph.node.delete(
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

<details><summary><code>client.graph.node.<a href="src/zep_cloud/graph/node/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an entity node by UUID.
</dd>
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
client.graph.node.update(
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

**attributes:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Updated attributes. Merged with existing attributes. Set a key to null to delete it.
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` — Updated labels for the node
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Updated name for the node
    
</dd>
</dl>

<dl>
<dd>

**summary:** `typing.Optional[str]` — Updated summary for the node
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.graph.observation.<a href="src/zep_cloud/graph/observation/client.py">get_by_graph_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns read-only observation nodes for a graph.
</dd>
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
client.graph.observation.get_by_graph_id(
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor response header
of the previous page. Encodes the sort field, direction, and continuation position.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc" (default "desc").
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Optional filters applied to the listed artifacts. Reuses the graph.search filter type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "created_at", "valid_at", or "uuid" (default "uuid").
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` 

UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page.

Deprecated: prefer Cursor, the opaque cursor returned via the Zep-Next-Cursor response header.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.observation.<a href="src/zep_cloud/graph/observation/client.py">get_by_user_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns read-only observation nodes for a user's graph.
</dd>
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
client.graph.observation.get_by_user_id(
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor response header
of the previous page. Encodes the sort field, direction, and continuation position.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc" (default "desc").
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Optional filters applied to the listed artifacts. Reuses the graph.search filter type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "created_at", "valid_at", or "uuid" (default "uuid").
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` 

UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page.

Deprecated: prefer Cursor, the opaque cursor returned via the Zep-Next-Cursor response header.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.observation.<a href="src/zep_cloud/graph/observation/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a specific observation node by UUID. Observation nodes are read-only.
</dd>
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
client.graph.observation.get(
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

**uuid_:** `str` — Observation UUID
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.graph.thread_summary.<a href="src/zep_cloud/graph/thread_summary/client.py">get_by_graph_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns incremental thread summaries associated with the graph.
</dd>
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
client.graph.thread_summary.get_by_graph_id(
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor response header
of the previous page. Encodes the sort field, direction, and continuation position.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc" (default "desc").
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Optional filters applied to the listed artifacts. Reuses the graph.search filter type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "created_at", "valid_at", or "uuid" (default "uuid").
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` 

UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page.

Deprecated: prefer Cursor, the opaque cursor returned via the Zep-Next-Cursor response header.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.graph.thread_summary.<a href="src/zep_cloud/graph/thread_summary/client.py">get_by_user_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns incremental thread summaries generated from messages in each thread associated with the user's graph.
</dd>
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
client.graph.thread_summary.get_by_user_id(
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

**cursor:** `typing.Optional[str]` 

Opaque cursor for pagination, obtained from the Zep-Next-Cursor response header
of the previous page. Encodes the sort field, direction, and continuation position.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[str]` — Sort direction. One of "asc" or "desc" (default "desc").
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[SearchFilters]` — Optional filters applied to the listed artifacts. Reuses the graph.search filter type.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[str]` — Field to sort by. One of "created_at", "valid_at", or "uuid" (default "uuid").
    
</dd>
</dl>

<dl>
<dd>

**uuid_cursor:** `typing.Optional[str]` 

UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page.

Deprecated: prefer Cursor, the opaque cursor returned via the Zep-Next-Cursor response header.
    
</dd>
</dl>

<dl>
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

