from google.adk.agents import Agent
import os

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

def _agent(slug: str, title: str, purpose: str) -> Agent:
    return Agent(
        name=slug,
        model=MODEL,
        description=purpose,
        instruction=(
            f"You are the {title} Agent. Your purpose is {purpose}. "
            "Understand the user's goal, ask only necessary questions, and provide concise actionable output. "
            "Distinguish facts from assumptions and recommendations. "
            "Never fabricate live data, prices, availability, citations, tool results, or completed actions. "
            "When external data is required, state the required API or ADK tool integration. "
            "Prefer structured output when useful for downstream orchestration."
        ),
    )

weather_agent = _agent("weather", "Weather", "weather conditions, forecasts, and alerts")
finance_agent = _agent("finance", "Finance", "financial news and market summaries")
research_agent = _agent("research", "Research", "structured web research with cited findings")
news_agent = _agent("news", "News", "daily news digests")
stocks_agent = _agent("stocks", "Stocks", "stock research and watchlists")
crypto_agent = _agent("crypto", "Crypto", "crypto market summaries")
expense_agent = _agent("expense", "Expense", "expense categorization")
budget_agent = _agent("budget", "Budget", "budget planning")
investment_agent = _agent("investment", "Investment", "investment research")
tax_agent = _agent("tax", "Tax", "tax explanations")
travel_agent = _agent("travel", "Travel", "trip planning and itineraries")
flight_agent = _agent("flight", "Flight", "flight research")
hotel_agent = _agent("hotel", "Hotel", "hotel comparison")
restaurant_agent = _agent("restaurant", "Restaurant", "restaurant discovery")
calendar_agent = _agent("calendar", "Calendar", "schedule planning")
email_agent = _agent("email", "Email", "email drafting and triage")
meeting_agent = _agent("meeting", "Meeting", "meeting agendas and action items")
task_agent = _agent("task", "Task", "task planning")
todo_agent = _agent("todo", "Todo", "to-do organization")
reminder_agent = _agent("reminder", "Reminder", "follow-up planning")
study_agent = _agent("study", "Study", "study planning")
tutor_agent = _agent("tutor", "Tutor", "interactive tutoring")
exam_agent = _agent("exam", "Exam", "exam preparation")
career_agent = _agent("career", "Career", "career planning")
resume_agent = _agent("resume", "Resume", "resume improvement")
interview_agent = _agent("interview", "Interview", "interview preparation")
job_agent = _agent("job", "Job", "job description analysis")
linkedin_agent = _agent("linkedin", "LinkedIn", "professional profile drafting")
writing_agent = _agent("writing", "Writing", "writing and rewriting")
summarizer_agent = _agent("summarizer", "Summarizer", "long-text summarization")
translator_agent = _agent("translator", "Translator", "translation")
grammar_agent = _agent("grammar", "Grammar", "grammar and style")
presentation_agent = _agent("presentation", "Presentation", "presentation outlines")
document_agent = _agent("document", "Document", "document drafting")
research_paper_agent = _agent("research_paper", "Research Paper", "research paper planning")
citation_agent = _agent("citation", "Citation", "citation formatting")
code_agent = _agent("code", "Code", "code generation")
debug_agent = _agent("debug", "Debug", "debugging")
review_agent = _agent("review", "Review", "code review")
test_agent = _agent("test", "Test", "test generation")
git_agent = _agent("git", "Git", "git workflow assistance")
sql_agent = _agent("sql", "SQL", "SQL generation")
data_agent = _agent("data", "Data", "data analysis")
analytics_agent = _agent("analytics", "Analytics", "business analytics")
dashboard_agent = _agent("dashboard", "Dashboard", "dashboard and KPI design")
api_agent = _agent("api", "API", "API design")
cloud_agent = _agent("cloud", "Cloud", "cloud architecture")
security_agent = _agent("security", "Security", "security review")
devops_agent = _agent("devops", "DevOps", "CI/CD and deployment")
productivity_agent = _agent("productivity", "Productivity", "daily productivity")
daily_brief_agent = _agent("daily_brief", "Daily Brief", "daily briefing")
wellness_agent = _agent("wellness", "Wellness", "general wellness information")
fitness_agent = _agent("fitness", "Fitness", "fitness planning")
meal_agent = _agent("meal", "Meal", "meal planning")
shopping_agent = _agent("shopping", "Shopping", "product research")
book_agent = _agent("book", "Book", "book discovery")
movie_agent = _agent("movie", "Movie", "movie recommendations")
learning_agent = _agent("learning", "Learning", "learning roadmaps")
language_agent = _agent("language", "Language", "language practice")
notes_agent = _agent("notes", "Notes", "note organization")

__all__ = [name for name in globals() if name.endsWith('_agent')]
