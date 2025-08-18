from typing import List

from fastmcp import FastMCP
from aiohttp import ClientSession

from app.auth.getauth import get_auth

read_follow = FastMCP(name="Read Follow MCP")

@read_follow.tool
async def read_follow() -> dict[str, str | List[str] | None] | None:
    """
    Makes an API request to the Spotify server.
    Use this tool to get the user's followed artists.
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    token = get_auth()
    endpoint = "https://api.spotify.com/v1/me/following?type=artist&limit=50"
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