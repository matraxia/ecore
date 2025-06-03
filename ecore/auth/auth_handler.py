import time
import jwt

SECRET="ECORE_TEST"

ALGO="HS256"
def sign_jwt(username):
    payload = {
        "username": username,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGO)

    return token_response(token)
    
def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET, algorithms=[ALGO])
        return decoded_token #if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def token_response(token: str):
    return {
        "access_token": token
    }