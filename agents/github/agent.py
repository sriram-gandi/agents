import os, requests
from google.adk.agents import Agent

def list_issues(owner: str, repo: str, state: str="open") -> dict:
    """List GitHub repository issues."""
    token=os.getenv("GITHUB_TOKEN")
    if not token: return {"status":"error","error":"GITHUB_TOKEN is not configured"}
    h={"Accept":"application/vnd.github+json","Authorization":f"Bearer {token}","X-GitHub-Api-Version":"2026-03-10"}
    r=requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues",headers=h,params={"state":state,"per_page":50},timeout=15); r.raise_for_status()
    return {"status":"success","issues":r.json()}

root_agent=Agent(name="github_agent",model="gemini-2.5-flash",description="GitHub repository issue analysis agent.",instruction="Use list_issues to inspect repository work. Summarize bugs, priorities, and patterns. Do not claim to modify GitHub unless a write tool is explicitly added.",tools=[list_issues])
