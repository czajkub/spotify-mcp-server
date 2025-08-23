from datetime import datetime

from app.auth.oauth import Config, SpotifyOAuth


def get_auth() -> dict[str, str | bool | datetime]:
    """
    Returns a dict with the following keys:
    success: bool
    access_token: str
    expiry: str
    when its okay
    """
    config = Config()
    token = config.access_token
    expiry = config.access_token_expiry
    expiry_date = datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S.%f")
    if token is None or expiry is None or expiry_date < datetime.now():
        print("Please authenticate with Spotify.")
        print("jakastam instrukcja")
        oauth = SpotifyOAuth()
        # uvicorn.run(app, host="127.0.0.1", port=8000)
        return {
            "success": False,
            "instructions": "Run `uv run <project dir>/app/auth/oauth.py` and follow the instructions.",
            "URL": oauth.get_auth_url(),
        }
    return {"success": True, "access_token": token, "access_token_expiry": expiry_date}
