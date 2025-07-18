from fastapi import Header, HTTPException
import time

AUTH_TOKEN = 'DEyZwVbMaSz0DMb7rSCRc1dKEGLwmKANWC7G'
SESSIONS = {}

def validate_token(token: str = Header(...)):
    if token != AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

