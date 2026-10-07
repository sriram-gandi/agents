import os, requests
from google.adk.agents import Agent

def calculate_route(origin: str, destination: str, travel_mode: str="DRIVE") -> dict:
    """Calculate route distance and duration using Google Maps Routes API."""
    key=os.getenv("GOOGLE_MAPS_API_KEY")
    if not key: return {"status":"error","error":"GOOGLE_MAPS_API_KEY is not configured"}
    mode=travel_mode.upper()
    if mode not in {"DRIVE","WALK","BICYCLE","TWO_WHEELER","TRANSIT"}: return {"status":"error","error":"Unsupported travel mode"}
    body={"origin":{"address":origin},"destination":{"address":destination},"travelMode":mode}
    h={"Content-Type":"application/json","X-Goog-Api-Key":key,"X-Goog-FieldMask":"routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline"}
    r=requests.post("https://routes.googleapis.com/directions/v2:computeRoutes",json=body,headers=h,timeout=15); r.raise_for_status()
    return {"status":"success","data":r.json()}

root_agent=Agent(name="travel_agent",model="gemini-2.5-flash",description="Travel routing agent.",instruction="Use calculate_route for route facts. Ask for origin, destination and travel mode. Never invent distance or duration.",tools=[calculate_route])
