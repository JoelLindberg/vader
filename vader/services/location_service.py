import httpx
from os import environ
from starlette import requests

from models.location import Location



async def get_location() -> Location:
    print(requests.Request.client)
    token = environ["IPINFO_TOKEN"]
    url = f"https://ipinfo.io/[IP address]?token={token}"