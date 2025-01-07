# MCP HTTP Client Example

Simple example client demonstrating how to connect to [Model Context Protocol (MCP)](https://spec.modelcontextprotocol.io) servers over HTTP using Server-Sent Events (SSE) transport.

Uses the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) to handle protocol communication and server interactions.

## Features

- Connects to MCP servers over SSE transport
- Lists available tools, resources and prompts
- Properly handles connection lifecycle with async context managers

## Requirements

- [uv](https://github.com/astral-sh/uv)

## Usage

Clone this repository, then run the example client:

```bash
uv run -- main.py <server_url>
```

For example:

```bash
uv run -- main.py http://localhost:8000/sse
```

The client will:

1. Connect to the specified MCP server
2. List its available capabilities
3. Print them as JSON

## Documentation

- [MCP Specification](https://spec.modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
