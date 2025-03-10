from sqlalchemy.orm import Session

from ..schemas import station_schema
from ..models import model


def create_station(db: Session, station: station_schema.StationCreate):
    new_station = model.Station(**station.model_dump())
    db.add(new_station)
    db.commit()
    db.refresh(new_station)
    return new_station


def get_stations(db: Session):
    return db.query(model.Station).all()


def get_station(db: Session, station_id: int):
    return db.query(model.Station).filter(model.Station.id == station_id).first()


def toggle_station_status(db: Session, station_id: int):
    new_station = db.query(model.Station).filter(model.Station.id == station_id).first()

    if not new_station:
        return None

    new_station.status = not new_station.status
    db.commit()
    db.refresh(new_station)

    return new_station


def get_stations_by_capacity(db: Session, capacity: int):
    return db.query(model.Station).filter(model.Station.capacity >= capacity).all()
