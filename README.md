# Zep Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fgetzep%2Fzep-python)
[![pypi](https://img.shields.io/pypi/v/zep-cloud)](https://pypi.python.org/pypi/zep-cloud)

The Zep Python library provides convenient access to the Zep APIs from Python.

## Table of Contents

- [What Is Zep 💬](#what-is-zep-)
- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Pagination](#pagination)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## What is Zep? 💬
Zep is a context engineering platform for AI Assistant apps. With Zep, you can provide AI assistants with the ability to recall past conversations, no matter how distant, while also reducing hallucinations, latency, and cost.

### Cloud Installation
You can install the Zep Cloud SDK by running:
```bash
pip install zep-cloud
```
> [!NOTE]
> Zep Cloud [overview](https://help.getzep.com/concepts) and [cloud sdk guide](https://help.getzep.com/sdks).

### How Zep works

Zep persists and recalls chat histories, and automatically generates summaries and other artifacts from these chat histories. It also embeds messages and summaries, enabling you to search Zep for relevant context from past conversations. Zep does all of this asynchronously, ensuring these operations don't impact your user's chat experience. Data is persisted to database, allowing you to scale out when growth demands.

Zep allows you to be more intentional about constructing your prompt:
1. automatically adding a few recent messages, with the number customized for your app;
2. a summary of recent conversations prior to the messages above;
3. and/or contextually relevant summaries or messages surfaced from the entire chat session.

You will also need to provide a Zep Project API key to your zep client.
You can find out about zep projects in our [cloud docs](https://help.getzep.com/projects.html)

## Installation

```sh
pip install zep-cloud
```

## Reference

A full reference for this library is available [here](https://github.com/getzep/zep-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from zep_cloud import Zep

client = Zep(
    api_key="<value>",
)

client.batch.create()
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from zep_cloud import AsyncZep

client = AsyncZep(
    api_key="<value>",
)


async def main() -> None:
    await client.batch.create()


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from zep_cloud.core.api_error import ApiError

try:
    client.batch.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from zep_cloud import Zep

client = Zep(
    api_key="<value>",
)

client.batch.list(
    limit=1,
    cursor="cursor",
    status="status",
)
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.batch.list(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from zep_cloud import Zep

client = Zep(...)
response = client.batch.with_raw_response.create(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.batch.create(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from zep_cloud import Zep

client = Zep(..., timeout=20.0)

# Override timeout for a specific method
client.batch.create(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from zep_cloud import Zep

client = Zep(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
