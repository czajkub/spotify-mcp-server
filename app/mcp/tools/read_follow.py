from typing import List, Any

from fastmcp import FastMCP

from .request import api_request

read_follow = FastMCP(name="Read Follow MCP")

@read_follow.tool
async def read_follow() -> dict[str, str | List[str] | None] | None | Any:
    """
    Makes an API request to the Spotify server.
    Use this tool to get the user's followed artists.
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    return api_request("https://api.spotify.com/v1/me/following?type=artist&limit=50")