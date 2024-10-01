
[![Release to PyPI](https://github.com/getzep/zep-python/actions/workflows/release.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/release.yml) ![GitHub](https://img.shields.io/github/license/getzep/zep-python?color=blue) [![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)


<p align="center">
  <a href="https://www.getzep.com/">
    <img src="https://raw.githubusercontent.com/getzep/zep/main/assets/zep-logo-icon-gradient-rgb.svg" width="150" alt="Zep Logo">
  </a>
</p>

<h1 align="center">
Zep: Long-Term Memory for ‍AI Assistants.
</h1>
<h2 align="center">Recall, understand, and extract data from chat histories. Power personalized AI experiences.</h2>
<br />

<p align="center">
<a href="https://docs.getzep.com/deployment/quickstart/">Quick Start</a> | 
<a href="https://docs.getzep.com/">Documentation</a> | 
<a href="https://docs.getzep.com/sdk/langchain/">LangChain</a> and 
<a href="https://docs.getzep.com/sdk/langchain/">LlamaIndex</a> Support | 
<a href="https://discord.gg/W8Kw6bsgXQ">Discord</a><br />
<a href="https://www.getzep.com">www.getzep.com</a>
</p>

## What is Zep? 💬
Zep is a long-term memory service for AI Assistant apps. With Zep, you can provide AI assistants with the ability to recall past conversations, no matter how distant, while also reducing hallucinations, latency, and cost.

### Cloud Installation
You can install the Zep Cloud SDK by running:
```bash
pip install zep-cloud
```
> [!NOTE]
> Zep Cloud [overview](https://help.getzep.com/concepts) and [cloud sdk guide](https://help.getzep.com/sdks).

### Community Installation
```bash
pip install zep-python
```
> [!NOTE]
> Zep Community Edition [quick start](https://help.getzep.com/ce/quickstart) and [sdk guide](https://help.getzep.com/ce/sdks).

### Zep v0.x Compatible SDK
You can install Zep v0.x compatible sdk by running:
```bash
pip install "zep-python>=1.5.0,<2.0.0"
```
> [!NOTE]
> Zep v0.x [quick start](https://help.getzep.com/ce/legacy/deployment/quickstart) and [sdk guide](https://help.getzep.com/ce/legacy/sdk).

### How Zep works

Zep persists and recalls chat histories, and automatically generates summaries and other artifacts from these chat histories. It also embeds messages and summaries, enabling you to search Zep for relevant context from past conversations. Zep does all of this asynchronously, ensuring these operations don't impact your user's chat experience. Data is persisted to database, allowing you to scale out when growth demands.

Zep also provides a simple, easy to use abstraction for document vector search called Document Collections. This is designed to complement Zep's core memory features, but is not designed to be a general purpose vector database.

Zep allows you to be more intentional about constructing your prompt:
1. automatically adding a few recent messages, with the number customized for your app;
2. a summary of recent conversations prior to the messages above;
3. and/or contextually relevant summaries or messages surfaced from the entire chat session.
4. and/or relevant Business data from Zep Document Collections.

Zep Cloud offers:
- **Fact Extraction:** Automatically build fact tables from conversations, without having to define a data schema upfront.
- **Dialog Classification:** Instantly and accurately classify chat dialog. Understand user intent and emotion, segment users, and more. Route chains based on semantic context, and trigger events.
- **Structured Data Extraction:** Quickly extract business data from chat conversations using a schema you define. Understand what your Assistant should ask for next in order to complete its task.

You will also need to provide a Zep Project API key to your zep client.
You can find out about zep projects in our [cloud docs](https://help.getzep.com/projects.html)

### Using LangChain Zep Classes with `zep-python`

(Currently only available on release candidate versions)

In the pre-release version `zep-python` sdk comes with `ZepChatMessageHistory` and `ZepVectorStore`
classes that are compatible with [LangChain's Python expression language](https://python.langchain.com/docs/expression_language/)

In order to use these classes in your application, you need to make sure that you have
`langchain_core` package installed, please refer to [Langchain's docs installation section](https://python.langchain.com/docs/get_started/installation#langchain-core).

We support `langchain_core@>=0.1.3<0.2.0`

You can import these classes in the following way:

```python
from zep_cloud.langchain import ZepChatMessageHistory, ZepVectorStore
```

### Running Examples
You will need to set the following environment variables to run examples in the `examples` directory:

```dotenv
# Please use examples/.env.example as a template for .env file

# Required
ZEP_API_KEY=<zep-project-api-key># Your Zep Project API Key
ZEP_COLLECTION=<zep-collection-name># used in ingestion script and in vector store examples
OPENAI_API_KEY=<openai-api-key># Your OpenAI API Key

# Optional (If you want to use langsmith with LangServe Sample App)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=<your-langchain-api-key>
LANGCHAIN_PROJECT=<your-langchain-project-name># If not specified, defaults to "default"
```


