[![Tests](https://github.com/getzep/zep-python/actions/workflows/test.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/test.yml) [![lint](https://github.com/getzep/zep-python/actions/workflows/lint.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/lint.yml) [![Release to PyPI](https://github.com/getzep/zep-python/actions/workflows/release.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/release.yml) ![GitHub](https://img.shields.io/github/license/getzep/zep-python?color=blue)


<p align="center">
  <a href="https://squidfunk.github.io/mkdocs-material/">
    <img src="https://github.com/getzep/zep/blob/main/assets/zep-bot-square-200x200.png?raw=true" width="150" alt="Zep Logo">
  </a>
</p>

<h1 align="center">
Zep: Fast, scalable building blocks for LLM apps
</h1>
<h2 align="center">Chat history memory, embedding, vector search, data enrichment, and more.</h2>

<p align="center">
<a href="https://docs.getzep.com/deployment/quickstart/">Quick Start</a> | 
<a href="https://docs.getzep.com/">Documentation</a> | 
<a href="https://docs.getzep.com/sdk/langchain/">LangChain</a> and 
<a href="https://docs.getzep.com/sdk/langchain/">LlamaIndex</a> Support | 
<a href="https://discord.gg/W8Kw6bsgXQ">Discord</a><br />
<a href="https://www.getzep.com">www.getzep.com</a>
</p>

## What is Zep?
Zep is an open source platform for productionizing LLM apps. Zep summarizes, embeds, and enriches chat histories and documents asynchronously, ensuring these operations don't impact your user's chat experience. Data is persisted to database, allowing you to scale out when growth demands. As drop-in replacements for popular LangChain components, you can get to production in minutes without rewriting code.

[![Zep Demo Video](https://img.youtube.com/vi/d6ryNEvMXno/maxresdefault.jpg)](https://vimeo.com/865785086?share=copy)

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