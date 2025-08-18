import base64
import os
import string
import random
from dataclasses import dataclass
from datetime import datetime, timedelta

import urllib.parse
import httpx
from fastapi import FastAPI, Request, HTTPException, responses
from dotenv import load_dotenv, set_key

from app.projectdir import project_dir

envpath = project_dir / ".env"

@dataclass
class Config:
    # client_id = os.getenv("CLIENT_ID", "")
    # client_secret = os.getenv("CLIENT_SECRET", "")
    # access_token = os.getenv("ACCESS_TOKEN", "")
    # access_token_expiry = os.getenv("ACCESS_TOKEN_EXPIRY", "")
    def __init__(self):
        load_dotenv(envpath)
        self.client_id = os.getenv("CLIENT_ID", "")
        self.client_secret = os.getenv("CLIENT_SECRET", "")
        self.access_token = os.getenv("ACCESS_TOKEN", "")
        self.access_token_expiry = os.getenv("ACCESS_TOKEN_EXPIRY", "")
    def __post_init__(self):
        if self.client_id == "":
            raise RuntimeError("client_id must be set")
        if self.client_secret == "":
            raise RuntimeError("client_secret must be set")

@dataclass
class SpotifyOAuth:
    """
    A class to handle Spotify OAuth authentication.
    
    This class manages the OAuth flow, including token retrieval and refresh.
    It uses environment variables to store sensitive information securely.
    """

    redirect = "http://127.0.0.1:8000/callback"
    auth_url = "https://accounts.spotify.com/authorize"
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self):
        config = Config()
        self.client_id = config.client_id
        self.client_secret = config.client_secret
        self.access_token = config.access_token
        self.access_token_expiry = config.access_token_expiry
        self.state = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

    def __post_init__(self):
        if not self.client_id or not self.client_secret:
            raise ValueError("Client ID and Client Secret must be set in the environment variables.")

    def get_auth_url(self):
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect,
            "scope": "user-top-read, user-library-read, user-follow-read",
            "state": self.state
        }
        return f"{self.auth_url}?{urllib.parse.urlencode(params)}"

    async def get_tokens(self, code: str) -> dict:
        auth_str = f"{self.client_id}:{self.client_secret}"
        headers = {
            "Authorization": f"Basic {base64.b64encode(auth_str.encode()).decode()}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect
        }

        async with httpx.AsyncClient() as client:
            resp = await client.post(self.token_url, data=data, headers=headers)
            resp.raise_for_status()
            return resp.json()

api_app = FastAPI()

oauth = SpotifyOAuth()
@api_app.get("/")
def login():
    auth_url = oauth.get_auth_url()
    return responses.RedirectResponse(url=auth_url)

@api_app.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")
    if not code:
        raise HTTPException(status_code=400, detail="Invalid authorization code")
    if state != oauth.state:
        raise HTTPException(status_code=400, detail="Invalid authorization state")
    try:
        tokens = await SpotifyOAuth.get_tokens(oauth, code)
        setenv(tokens)
        return tokens
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)

def setenv(tokens):
    set_key(envpath, "ACCESS_TOKEN", tokens["access_token"])
    set_key(envpath, "ACCESS_TOKEN_EXPIRY", str(datetime.now() + timedelta(seconds = tokens["expires_in"])))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api_app, host="127.0.0.1", port=8000)