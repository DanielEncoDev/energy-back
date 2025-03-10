from sqlalchemy.orm import Session
from .database import SessionLocal


# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
