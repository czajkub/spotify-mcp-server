from fastmcp import FastMCP

from tools import read_top, read_follow, read_library


mcp = FastMCP("Spotify MCP server")

router = FastMCP(name="Spotify MCP router")

router.mount(read_top.read_top )
# router.mount(read_follow.read_follow)
router.mount(read_library.read_library)

mcp.mount(router)

if __name__ == "__main__":
    mcp.run()