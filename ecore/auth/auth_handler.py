import time
import jwt
import itertools
from email_validator import validate_email, EmailNotValidError


SECRET="ECORE_TEST"

ALGO="HS256"
def sign_jwt(username):
    payload = {
        "mail": username,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGO)

    return token_response(token)
    
def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET, algorithms=ALGO)

        return decoded_token #if decoded_token["expires"] >= time.time() else None
    except Exception as e:
        print(str(e))
        return {}

def token_response(token: str):
    return {
        "access_token": token
    }

def validate_ecore_login(token,userdata):
    try:
        
        userdata=list(itertools.chain.from_iterable(userdata))
        print(userdata)
        decoded=decode_jwt(token)
        #print("decoded:")
        #print(decoded)
        #if(not validate_mail(token["mail"])):
            #return False
        #if not isEmailInDB(decoded["mail"],userdata):
            #return False
        return True #if decoded_token["expires"] >= time.time() else None
    except Exception as e:
        print(str(e))
        return False
    
def validate_mail(email):
    try:
        validate_email(email, check_deliverability=False)
        return True
    

    except EmailNotValidError as e:
        print(str(e))
        return False

def isEmailInDB(email, userdata):
    try:
        for entry in userdata:
            if email == entry:
                return True
        return False
    except Exception as e:
        print(str(e))
        return False

