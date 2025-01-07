"""MCP HTTP client example using MCP SDK."""

import asyncio
import sys
from urllib.parse import urlparse

from mcp.client.session import ClientSession
from mcp.client.sse import sse_client


async def main(server_url: str):
    """Connect to MCP server and list its capabilities.

    Args:
        server_url: Full URL to SSE endpoint (e.g. http://localhost:8000/sse)
    """

    # Validate URL
    if urlparse(server_url).scheme not in ("http", "https"):
        print("Error: Server URL must start with http:// or https://")
        sys.exit(1)

    try:
        # Connect to server using SSE transport
        async with sse_client(server_url) as streams:
            async with ClientSession(streams[0], streams[1]) as session:

                # Initialize the connection
                await session.initialize()
                print(f"Connected to MCP server at {server_url}", "\n")

                # List available tools
                tools = await session.list_tools()
                print("Available tools:", tools.model_dump(), "\n")

                # List available resources
                resources = await session.list_resources()
                print("Available resources:", resources.model_dump(), "\n")

                # List prompts
                prompts = await session.list_prompts()
                print("Available prompts:", prompts.model_dump(), "\n")

    except Exception as e:
        print(f"Error connecting to server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: uv run -- main.py <server_url>")
        print("Example: uv run -- main.py http://localhost:8000/sse")
        sys.exit(1)

    asyncio.run(main(sys.argv[1]))
