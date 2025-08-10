import os
from datetime import datetime
from dataclasses import dataclass

import uvicorn
from dotenv import load_dotenv

from oauth import Config, SpotifyOAuth, app


def get_auth():
    config = Config()
    token = config.access_token
    expiry = config.access_token_expiry
    expiry_date = datetime.strptime(expiry, '%Y-%m-%d %H:%M:%S.%f')
    if token is None or expiry is None or expiry_date < datetime.now():
        print("Please authenticate with Spotify.")
        uvicorn.run(app, host="127.0.0.1", port=8000)
        exit(1)
    return {
        "access_token": token,
        "access_token_expiry": expiry_date
    }