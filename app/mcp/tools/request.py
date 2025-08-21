from typing import List

import requests

from app.auth.getauth import get_auth

def api_request(url: str):
    token = get_auth()
    endpoint = url
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
    except TypeError:
        return {"error": "typeerror ocurred",
                "status_code": str(resp.status_code)}
    except:
        return {"error": "unspecified exception occured",
                "status_code": str(resp.status_code)}