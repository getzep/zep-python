
[![Tests](https://github.com/getzep/zep-python/actions/workflows/test.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/test.yml) [![lint](https://github.com/getzep/zep-python/actions/workflows/lint.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/lint.yml) [![Release to PyPI](https://github.com/getzep/zep-python/actions/workflows/release.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/release.yml) ![GitHub](https://img.shields.io/github/license/getzep/zep-python?color=blue)

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

### How Zep works

Zep does all of this asynchronously, ensuring these operations don't impact your user's chat experience. Data is persisted to database, allowing you to scale out when growth demands.

Zep also provides a simple, easy to use abstraction for document vector search called Document Collections. This is designed to complement Zep's core memory features, but is not designed to be a general purpose vector database.

Zep allows you to be more intentional about constructing your prompt: 
1. automatically adding a few recent messages, with the number customized for your app;
2. a summary of recent conversations prior to the messages above;
3. and/or contextually relevant summaries or messages surfaced from the entire chat session.
4. and/or relevant Business data from Zep Document Collections.

## What is Zep Cloud? ⚡️ 

[Zep Cloud](https://www.getzep.com/) is a managed service with Zep Open Source at its core. In addition to Zep Open Source's memory management features, Zep Cloud offers:
- **Fact Extraction:** Automatically build fact tables from conversations, without having to define a data schema upfront.
- **Dialog Classification:** Instantly and accurately classify chat dialog. Understand user intent and emotion, segment users, and more. Route chains based on semantic context, and trigger events. 
- **Structured Data Extraction:** Quickly extract business data from chat conversations using a schema you define. Understand what your Assistant should ask for next in order to complete its task.


## Zep Python Client

This is the Python client package for the Zep service. For more information about Zep, see https://github.com/getzep/zep.

Zep QuickStart Guide: https://docs.getzep.com/deployment/quickstart

Zep Documentation: [https://docs.getzep.com](https://docs.getzep.com/)

## Installation

```bash
pip install zep-python
```

-- OR --

```bash
poetry add zep-python
```

## Zep Cloud Installation
In order to install Zep Python SDK with Zep Cloud support, you will need to install
a release candidate version.

```bash
pip install --pre zep-python
```

-- OR --

```bash
poetry add zep-python@^2.0.0rc
```

You will also need to provide a Zep Project API key to your zep client for cloud support.
You can find out about Zep Projects in our [cloud docs](https://help.getzep.com/projects.html)

### Using LangChain Zep Classes with `zep-python`

(Currently only available on release candidate versions)

In the pre-release version `zep-python` sdk comes with `ZepChatMessageHistory` and `ZepVectorStore`
classes that are compatible with [LangChain's Python expression language](https://python.langchain.com/docs/expression_language/)

In order to use these classes in your application, you need to make sure that you have
`langchain_core` package installed, please refer to [Langchain's docs installation section](https://python.langchain.com/docs/get_started/installation#langchain-core).

We support `langchain_core@>=0.1.3<0.2.0`

You can import these classes in the following way:

```python
from zep_python.langchain import ZepChatMessageHistory, ZepVectorStore
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



