from typing import List

from fastmcp import FastMCP
from aiohttp import ClientSession

from app.auth.getauth import get_auth

read_library = FastMCP(name="Read Library MCP")

@read_library.tool
async def read_albums() -> dict[str, str | List[str] | None] | None:
    """
    Makes an API request to the Spotify server.
    Use this tool to check the user's saved albums
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    token = get_auth()
    endpoint = "https://api.spotify.com/v1/me/albums?limit=50"
    try:
        headers = {
            "Authorization": f"Bearer {token.access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        async with ClientSession(headers=headers) as session:
            async with session.get(endpoint) as response:
                return await response.json()
    except Exception as e:
        print(e)


@read_library.tool
async def read_tracks() -> dict[str, str | List[str] | None] | None:
    """
    Makes an API request to the Spotify server.
    Use this tool to check the user's saved tracks
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    token = get_auth()
    endpoint = "https://api.spotify.com/v1/me/tracks?limit=50"
    try:
        headers = {
            "Authorization": f"Bearer {token.access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        async with ClientSession(headers=headers) as session:
            async with session.get(endpoint) as response:
                return await response.json()
    except Exception as e:
        print(e)
