from typing import Generator
from ecore.db.database import client_db

def get_db() -> Generator:
    db = client_db()
    try:
        yield db
    finally:
        db.close()
