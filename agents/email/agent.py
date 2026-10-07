import os
from google.adk.agents import Agent
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES=["https://www.googleapis.com/auth/gmail.readonly"]

def list_emails(query: str="", max_results: int=10) -> dict:
    """List Gmail messages matching a Gmail search query. Requires OAuth token in GMAIL_TOKEN_JSON."""
    token=os.getenv("GMAIL_TOKEN_JSON")
    if not token: return {"status":"error","error":"GMAIL_TOKEN_JSON is not configured"}
    creds=Credentials.from_authorized_user_info(__import__("json").loads(token),SCOPES)
    service=build("gmail","v1",credentials=creds)
    result=service.users().messages().list(userId="me",q=query,maxResults=max(1,min(max_results,50))).execute()
    return {"status":"success","messages":result.get("messages",[]),"nextPageToken":result.get("nextPageToken")}

root_agent=Agent(name="email_agent",model="gemini-2.5-flash",description="Gmail triage agent.",instruction="Use list_emails to retrieve matching messages. Summarize metadata only unless the user asks for message content and appropriate scopes are configured. Never claim an email was sent.",tools=[list_emails])
