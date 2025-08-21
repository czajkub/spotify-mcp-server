from typing import List, Any

from fastmcp import FastMCP
import requests

from app.auth.getauth import get_auth

read_top = FastMCP(name="Read Top MCP")

@read_top.tool
async def read_top_artists() -> dict[str, str | List[str] | None] | None:
    """
    Makes an API request to the Spotify server.
    Use this tool to read 20 most listened to artists for the user.
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    token = get_auth()
    if token["success"] is False:
        return {"Token": "Please authenticate with Spotify by clicking the URL below.",
                "URL": token["URL"],
                "instructions": token["instructions"]}
    endpoint = "https://api.spotify.com/v1/me/top/artists"
    try:
        headers = {
            "Authorization": f"Bearer {token["access_token"]}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        resp = requests.get(endpoint, headers=headers)
        if resp.status_code != 200:
            return {"resp": "Something went wrong with the request",
                    "status_code": resp.status_code
                    }
        return await resp.json()
        # async with ClientSession(headers=headers) as session:
        #     async with session.get(endpoint) as response:
        #         return await response.json()
    except Exception as e:
        print(e)

@read_top.tool
async def read_top_songs() -> dict[str, str | List[str] | None] | None:
    """
    Makes an API request to the Spotify server.
    Use this tool to read 20 most listened to tracks for the user.
    Rules:
        - Do not guess, autofill, or assume any missing data.
    Returns:
        JSON response from the Spotify server
    """

    token = get_auth()
    if token["success"] is False:
        return {"Token": "Please authenticate with Spotify by clicking the URL below.",
                "URL": token["URL"],
                "instructions": token["instructions"]}
    endpoint = "https://api.spotify.com/v1/me/top/tracks"
    try:
        headers = {
            "Authorization": f"Bearer {token["access_token"]}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        resp = requests.get(endpoint, headers=headers)
        if resp.status_code != 200:
            return {"resp": "Something went wrong with the request",
                    "status_code": resp.status_code
                    }
        return await resp.json()
        # async with ClientSession(headers=headers) as session:
        #     async with session.get(endpoint) as response:
        #         return await response.json()
    except Exception as e:
        print(e)

@read_top.tool
def example() -> dict[str, str | List[str] | None | Any] | None:
    token = get_auth()
    endpoint = "https://api.spotify.com/v1/me/top/artists"
    if token.get("success") == False:
        return {"Token": "Please authenticate with Spotify",
                "file": __file__,
                "token": token}
    headers = {
        "Authorization": f"Bearer {token.get("access_token")}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    try:
        with requests.Session() as session:
            resp = session.get(url=endpoint, headers=headers)
            return resp.json()
    except TypeError as te:
        print(te)
        return {"error": "typeerror"}
    except Exception as e:
        return {"error": "some error occured bro"}
    return {"status_code": resp.status_code}

    return {"uhh:" "this somewhat worked?"}

if __name__ == "__main__":
    def wtf() -> dict[str, str | List[str] | None] | None:
        token = get_auth()
        print(token)
        return
        endpoint = "https://api.spotify.com/v1/me/top/artists"
        headers = {
            "Authorization": f"Bearer {token["access_token"]}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        try:
            resp = requests.get(url=endpoint, headers=headers)
            print(resp.json())
        except Exception as e:
            print ({"error": e})
    wtf()