from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent=Agent(name="research_agent",model="gemini-2.5-flash",description="Web research and evidence synthesis.",instruction="Research current questions with Google Search. Search multiple queries when broad, cross-check important claims, separate fact from inference, and provide source-backed findings. Never fabricate citations.",tools=[google_search])
