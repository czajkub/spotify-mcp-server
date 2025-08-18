import asyncio

# from fastmcp import FastMCP, Client
import fastmcp

from tools import read_top, read_follow, read_library


mcp = fastmcp.FastMCP("Spotify MCP server")

router = fastmcp.FastMCP(name="Spotify MCP router")

router.mount(read_top.read_top )
# router.mount(read_follow.read_follow)
router.mount(read_library.read_library)

mcp.mount(router)

client = fastmcp.Client(mcp)


async def call_tool(name: str):
    async with client:
        result = await client.call_tool(name)
        print(result)

if __name__ == "__main__":
    mcp.run()
    # asyncio.run(call_tool("read_top"))
