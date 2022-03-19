# Väder
**What**: Weather in your current location in Sweden.

**Why**: Personal learning project.

**Credits and thanks** to JetBrains and Michael Kennedy (from "*Talk Python*") for their tutorial on FastAPI:\
https://www.youtube.com/watch?v=sBVb4IB3O_U

I followed along and used Michael's example structure as a base for my project as I'm trying to pickup good habits around structuring things. It looks similar to Django's MVT (Model View Template).

## External services
Connects to ipinfo.io to get the location of the visitor\
https://ipinfo.io/
https://ipinfo.io/developers

Connects to SMHI Open Data API to get weather data from the visitors location\
https://opendata.smhi.se/apidocs/metfcst/index.html

## Usage (not working yet)
1. Clone the repo
2. Setup python venv and activate\
python3 -m venv venv\
source venv/bin/activate
3. Install requirements (pip3 install -r requirements.txt)
4. Run\
python main.py

Automatically created documentation (FastAPI feature) for your API:
http://127.0.0.1:8000/docs