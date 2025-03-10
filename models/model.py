from sqlalchemy import Column, Integer, String, Boolean
from ..core.database import Base


class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    capacity = Column(Integer)
    status = Column(Boolean, default=True)
