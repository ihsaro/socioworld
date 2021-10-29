from typing import final
from configurations.database import SessionLocal


def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
