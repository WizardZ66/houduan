from sqlalchemy.orm import Session
from manage.config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()