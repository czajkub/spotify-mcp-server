from fastmcp import FastMCP
from aiohttp import ClientSession

from app.auth.oauth import Config
from app.auth.token import get_auth

read_top = FastMCP(name="Read Top MCP")

@read_top.tool
async def read_top_artists(config: Config):
    """
    Makes an API request to the Spotify server.
    Use this tool to read 20 most listened to artists for the user.
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    token = get_auth()
    endpoint = "https://api.spotify.com/v1/me/top/artists"
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

@read_top.tool
async def read_top_songs(config: Config):
    """
    Makes an API request to the Spotify server.
    Use this tool to read 20 most listened to tracks for the user.
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    token = get_auth()
    endpoint = "https://api.spotify.com/v1/me/top/tracks"
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