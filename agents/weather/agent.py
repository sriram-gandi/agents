import requests
from google.adk.agents import Agent

def get_weather(location: str, days: int = 3) -> dict:
    """Get current weather and a forecast using Open-Meteo."""
    days=max(1,min(days,7))
    g=requests.get("https://geocoding-api.open-meteo.com/v1/search",params={"name":location,"count":1,"language":"en","format":"json"},timeout=10)
    g.raise_for_status(); places=g.json().get("results",[])
    if not places: return {"status":"error","error":"Location not found"}
    p=places[0]
    r=requests.get("https://api.open-meteo.com/v1/forecast",params={"latitude":p["latitude"],"longitude":p["longitude"],"current":"temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m","daily":"weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,wind_speed_10m_max","forecast_days":days,"timezone":"auto"},timeout=10)
    r.raise_for_status(); return {"status":"success","location":p,"forecast":r.json()}

root_agent=Agent(name="weather_agent",model="gemini-2.5-flash",description="Live weather and forecast agent.",instruction="Use get_weather for live weather. Ask for location when missing. Never invent weather data.",tools=[get_weather])
