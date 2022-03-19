from pydantic import BaseModel

class Location(BaseModel):
    ip: str
    city: str
    lat: float
    lon: float