import httpx

from models.location import Location

async def get_forecast(location: Location):
    url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{location.lon}/lat/{location.lat}/data.json"
    
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    return data