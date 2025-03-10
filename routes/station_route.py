from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..cruds.auth_crud import verify_token

from ..cruds import station_crud
from ..schemas import station_schema
from ..core.dependencies import get_db

from apscheduler.schedulers.background import BackgroundScheduler

router_station = APIRouter()


@router_station.post("/stations/", response_model=station_schema.StationResponse)
def create_station(
    station: station_schema.StationCreate,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token),
):
    return station_crud.create_station(db, station)


@router_station.get("/stations/", response_model=list[station_schema.StationResponse])
def get_stations(db: Session = Depends(get_db), user: str = Depends(verify_token)):
    return station_crud.get_stations(db)


@router_station.get(
    "/stations/{station_id}", response_model=station_schema.StationResponse
)
def get_station(
    station_id: int, db: Session = Depends(get_db), user: str = Depends(verify_token)
):
    return station_crud.get_station(db, station_id)


@router_station.put("/stations/{station_id}")
def update_station_status(
    station_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token),
):
    return station_crud.toggle_station_status(db, station_id)


@router_station.get("/stations/{station_id}/schedule")
def schedule_station(
    station_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token),
):
    def toggle_station_status():
        station_crud.toggle_station_status(db, station_id)

    scheduler = BackgroundScheduler()
    scheduler.add_job(toggle_station_status, "interval", seconds=5)
    scheduler.start()
    return {"message": "Job scheduled successfully"}


@router_station.get("/stations/capacity/{capacity}")
def get_stations_by_capacity(
    capacity: int, db: Session = Depends(get_db), user: str = Depends(verify_token)
):
    return station_crud.get_stations_by_capacity(db, capacity)
