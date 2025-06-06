import os
from fastapi import Header, HTTPException, status
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError, DecodeError
from typing import Dict, Any

from ecore.settings import S

# --- Configuration ---
SECRET_KEY = S.SECRET_KEY
ALGORITHM = S.SECRET_ALGORITHM


# --- Dependency Function for Token Validation ---
async def verify_token(authorization: str = Header(...)) -> Dict[str, Any]:
    """
    FastAPI dependency function to extract, decode, and validate a JWT using PyJWT.
    It expects the token in the Authorization header as 'Bearer <token>'.

    Args:
        authorization (str): The Authorization header value (e.g., "Bearer eyJ...").

    Returns:
        Dict[str, Any]: The decoded payload of the JWT if valid.

    Raises:
        HTTPException: If the token is missing, invalid, malformed, or expired.
    """
    print("Verifying token...")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing or malformed (expected 'Bearer <token>')",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = authorization.split(" ")[1]  # Extract the token part after "Bearer "

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return payload  # Return the entire decoded payload

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials: Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except (InvalidTokenError, DecodeError) as e:
        # InvalidTokenError covers signature mismatch, invalid claims, etc.
        # DecodeError covers malformed tokens that can't even be decoded.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Could not validate credentials: {e}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except IndexError:  # In case the split fails (e.g., "Bearer" without token)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header format",
            headers={"WWW-Authenticate": "Bearer"},
        )
