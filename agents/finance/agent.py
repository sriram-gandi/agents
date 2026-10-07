import os, requests
from google.adk.agents import Agent

def market_data(symbol: str, mode: str="quote") -> dict:
    """Fetch Alpha Vantage quote, daily history, company overview, or market status."""
    key=os.getenv("ALPHAVANTAGE_API_KEY")
    if not key: return {"status":"error","error":"ALPHAVANTAGE_API_KEY is not configured"}
    fn={"quote":"GLOBAL_QUOTE","daily":"TIME_SERIES_DAILY","overview":"OVERVIEW","market_status":"MARKET_STATUS"}.get(mode.lower())
    if not fn: return {"status":"error","error":"mode must be quote, daily, overview, or market_status"}
    p={"function":fn,"apikey":key}
    if fn!="MARKET_STATUS": p["symbol"]=symbol.upper()
    r=requests.get("https://www.alphavantage.co/query",params=p,timeout=15); r.raise_for_status()
    return {"status":"success","data":r.json()}

root_agent=Agent(name="finance_agent",model="gemini-2.5-flash",description="Market data agent.",instruction="Use market_data for live market facts. Explain metrics but do not present personalized investment advice as certainty.",tools=[market_data])
