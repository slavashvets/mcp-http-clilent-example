"""MCP HTTP client example using MCP SDK."""

import asyncio
import sys
from typing import Any
from urllib.parse import urlparse

from mcp.client.session import ClientSession
from mcp.client.sse import sse_client


def print_items(name: str, result: Any) -> None:
    """Print items with formatting.

    Args:
        name: Category name (tools/resources/prompts)
        result: Result object containing items list
    """
    print("", f"Available {name}:", sep="\n")
    items = getattr(result, name)
    if items:
        for item in items:
            print(" *", item)
    else:
        print("No items available")


async def main(server_url: str):
    """Connect to MCP server and list its capabilities.

    Args:
        server_url: Full URL to SSE endpoint (e.g. http://localhost:8000/sse)
    """
    if urlparse(server_url).scheme not in ("http", "https"):
        print("Error: Server URL must start with http:// or https://")
        sys.exit(1)

    try:
        async with sse_client(server_url) as streams:
            async with ClientSession(streams[0], streams[1]) as session:
                await session.initialize()
                print("Connected to MCP server at", server_url)
                print_items("tools", (await session.list_tools()))
                print_items("resources", (await session.list_resources()))
                print_items("prompts", (await session.list_prompts()))

    except Exception as e:
        print(f"Error connecting to server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: uv run -- main.py <server_url>")
        print("Example: uv run -- main.py http://localhost:8000/sse")
        sys.exit(1)

    asyncio.run(main(sys.argv[1]))
