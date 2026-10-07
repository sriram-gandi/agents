import os, json
from google.adk.agents import Agent
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES=["https://www.googleapis.com/auth/calendar.readonly"]

def upcoming_events(max_results: int=10) -> dict:
    """List upcoming Google Calendar events using OAuth."""
    token=os.getenv("GOOGLE_CALENDAR_TOKEN_JSON")
    if not token: return {"status":"error","error":"GOOGLE_CALENDAR_TOKEN_JSON is not configured"}
    creds=Credentials.from_authorized_user_info(json.loads(token),SCOPES)
    service=build("calendar","v3",credentials=creds)
    result=service.events().list(calendarId="primary",maxResults=max(1,min(max_results,50)),singleEvents=True,orderBy="startTime").execute()
    return {"status":"success","events":result.get("items",[])}

root_agent=Agent(name="calendar_agent",model="gemini-2.5-flash",description="Google Calendar planning agent.",instruction="Use upcoming_events for calendar facts. Help identify conflicts and planning opportunities. Do not claim events were created or modified.",tools=[upcoming_events])
