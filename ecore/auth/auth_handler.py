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
    

def auth(nome:str,password:str):
    return 