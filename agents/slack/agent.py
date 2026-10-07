import os, requests
from google.adk.agents import Agent

def search_slack(query: str) -> dict:
    """Search Slack messages using a bot token."""
    token=os.getenv("SLACK_BOT_TOKEN")
    if not token: return {"status":"error","error":"SLACK_BOT_TOKEN is not configured"}
    r=requests.get("https://slack.com/api/search.messages",headers={"Authorization":f"Bearer {token}"},params={"query":query},timeout=15); r.raise_for_status()
    data=r.json()
    if not data.get("ok"): return {"status":"error","error":data.get("error","Slack API error")}
    return {"status":"success","messages":data.get("messages",{})}

root_agent=Agent(name="slack_agent",model="gemini-2.5-flash",description="Slack search and summarization agent.",instruction="Use search_slack to find relevant conversations. Summarize findings and cite channel/user metadata returned by Slack. Never claim to send messages.",tools=[search_slack])
