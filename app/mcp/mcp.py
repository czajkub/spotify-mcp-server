from fastmcp import FastMCP

from tools import read_top


mcp_router = FastMCP(name="main mcp")

mcp_router.mount(read_top.read_top_artists)

