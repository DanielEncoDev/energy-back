from pydantic import BaseModel


class StationBase(BaseModel):
    name: str
    location: str
    capacity: int
    status: bool


class StationCreate(StationBase):
    pass


class StationStatusUpdate(BaseModel):
    status: bool


class StationResponse(StationBase):
    id: int

    class Config:
        from_attributes = True
