from pydantic import BaseModel


class Forecast(BaseModel):
    precipitation: float
    precipitation_category: str
    temp: float
    weather: str