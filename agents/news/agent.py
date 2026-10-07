import os, requests
from google.adk.agents import Agent

def search_news(query: str="", country: str="", page_size: int=10) -> dict:
    """Search current articles with NewsAPI."""
    key=os.getenv("NEWSAPI_API_KEY")
    if not key: return {"status":"error","error":"NEWSAPI_API_KEY is not configured"}
    n=max(1,min(page_size,50))
    if country and not query:
        endpoint="https://newsapi.org/v2/top-headlines"; params={"apiKey":key,"country":country.lower(),"pageSize":n}
    else:
        endpoint="https://newsapi.org/v2/everything"; params={"apiKey":key,"q":query,"pageSize":n,"sortBy":"publishedAt"}
    r=requests.get(endpoint,params=params,timeout=15); r.raise_for_status()
    return {"status":"success","data":r.json()}

root_agent=Agent(name="news_agent",model="gemini-2.5-flash",description="Live news retrieval agent.",instruction="Use search_news for current news. Summarize, preserve sources and publication times, and never invent stories.",tools=[search_news])
