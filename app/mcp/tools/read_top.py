from typing import List, Any

from fastmcp import FastMCP

from .request import api_request

read_top = FastMCP(name="Read Top MCP")


@read_top.tool
async def read_top_artists() -> dict[str, str | List[str] | None] | None | Any:
    """
    Makes an API request to the Spotify server.
    Use this tool to read 20 most listened to artists for the user.
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    return api_request("https://api.spotify.com/v1/me/top/artists")


@read_top.tool
async def read_top_songs() -> dict[str, str | List[str] | None] | None | Any:
    """
    Makes an API request to the Spotify server.
    Use this tool to read 20 most listened to tracks for the user.
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    return api_request("https://api.spotify.com/v1/me/top/tracks")


from app.auth.getauth import get_auth
import requests


@read_top.tool
def example() -> dict[str, str | List[str] | None] | None | Any:
    token = get_auth()
    endpoint = "https://api.spotify.com/v1/me/top/artists"
    if token.get("success") == False:
        return {
            "Token": "Please authenticate with Spotify",
            "file": __file__,
            "token": token,
        }
    headers = {
        "Authorization": f"Bearer {token.get('access_token')}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    try:
        with requests.Session() as session:
            resp = session.get(url=endpoint, headers=headers)
            return resp.json()
    except TypeError as te:
        return {"error": "typeerror ocurred", "status_code": str(resp.status_code)}
    except:
        return {
            "error": "unspecified exception occured",
            "status_code": str(resp.status_code),
        }


# if __name__ == "__main__":
#     def wtf() -> dict[str, str | List[str] | None] | None:
#         token = get_auth()
#         print(token)
#         return
#         endpoint = "https://api.spotify.com/v1/me/top/artists"
#         headers = {
#             "Authorization": f"Bearer {token["access_token"]}",
#             "Content-Type": "application/json",
#             "Accept": "application/json",
#         }
#         try:
#             resp = requests.get(url=endpoint, headers=headers)
#             print(resp.json())
#         except Exception as e:
#             print ({"error": e})
#     wtf()
