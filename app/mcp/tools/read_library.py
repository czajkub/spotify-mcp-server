from typing import List, Any

from fastmcp import FastMCP

from .request import api_request

read_library = FastMCP(name="Read Library MCP")


@read_library.tool
async def read_albums() -> dict[str, str | List[str] | None] | None | Any:
    """
    Makes an API request to the Spotify server.
    Use this tool to check the user's saved albums
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    return api_request("https://api.spotify.com/v1/me/albums?limit=50")


@read_library.tool
async def read_tracks() -> dict[str, str | List[str] | None] | None | Any:
    """
    Makes an API request to the Spotify server.
    Use this tool to check the user's saved tracks
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    return api_request("https://api.spotify.com/v1/me/tracks?limit=50")
