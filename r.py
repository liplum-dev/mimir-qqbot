import os
from dotenv import load_dotenv

load_dotenv()

appid = os.getenv("QQBOT_APP_ID")
if appid is None:
    raise Exception('Missing "QQBOT_APP_ID" environment variable for your bot AppID')

secret = os.getenv("QQBOT_APP_SECRET")
if secret is None:
    raise Exception('Missing "QQBOT_APP_SECRET" environment variable for your AppSecret')

backend = os.getenv("MIMIR_BACKEND_URL", default="http://api.mysit.life")

MCServerApi = os.getenv("MC_SERVER_API")
if MCServerApi is None:
    raise Exception('Missing "MC_SERVER_API" environment variable for your AppSecret')

MCServerHost = os.getenv("MC_SERVER_HOST", default="play.sitmc.club")

WeatherApiToken = os.getenv("WEATHER_API_TOKEN")
if MCServerHost is None:
    raise Exception('Missing "WEATHER_API_TOKEN" environment variable for your AppSecret')

WeatherApi = os.getenv("WEATHER_API", default="https://restapi.amap.com/v3/weather/weatherInfo?")