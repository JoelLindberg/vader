import fastapi

# Import from models (created by myself)
from models.location import Location
from models.forecast import Forecast
from services import forecast_service

router = fastapi.APIRouter()

'''
from typing import Optional
@router.get('/api/forecast')
def get_forecast(city: str, country: str = 'se', state: Optional[str] = None):
    return { city }
'''

@router.get('/api/forecast', response_model=Forecast)
async def assemble_forecast(location: Location = fastapi.Depends()):
    data = await forecast_service.get_forecast(location)
    
    category = ''
    precipitation_category = ''
    weather = ''
    temp = 0.0
    
    print(data)
    return Forecast(
        precipitation=category, 
        precipitation_category=precipitation_category, 
        temp=temp, 
        weather=weather)