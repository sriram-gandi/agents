import os, json
from google.adk.agents import Agent
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES=["https://www.googleapis.com/auth/drive.metadata.readonly"]

def search_files(name_contains: str="", max_results: int=20) -> dict:
    """Search Google Drive file metadata."""
    token=os.getenv("GOOGLE_DRIVE_TOKEN_JSON")
    if not token: return {"status":"error","error":"GOOGLE_DRIVE_TOKEN_JSON is not configured"}
    creds=Credentials.from_authorized_user_info(json.loads(token),SCOPES)
    service=build("drive","v3",credentials=creds)
    q="trashed = false"
    if name_contains: q += f" and name contains '{name_contains.replace(chr(39), chr(92)+chr(39))}'"
    result=service.files().list(q=q,pageSize=max(1,min(max_results,100)),fields="files(id,name,mimeType,modifiedTime,webViewLink)").execute()
    return {"status":"success","files":result.get("files",[])}

root_agent=Agent(name="drive_agent",model="gemini-2.5-flash",description="Google Drive file discovery agent.",instruction="Use search_files to locate files. Report exact names, types, and modification times. Never claim a file was changed.",tools=[search_files])
