# --- 1. CENTRALIZED PERSISTENCE INITIALIZATION ---
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from google.adk.agents import SequentialAgent, Agent 
from google.adk.models import Gemini
from google.genai.types import Content, Part
from google.adk.sessions import Session
import asyncio
from pathlib import Path
from dotenv import load_dotenv

from agents.story_grooming.agent import root_agent as groomer_agent
from agents.code.agent import root_agent as code_agent
from agents.testing.agent import root_agent as test_agent

# 1. Database URL: Defines the database file location and type (SQLite + aiosqlite driver)
DB_URL = "sqlite+aiosqlite:///./session_management.db"
print(f"💾 Central Session Service initialized using {DB_URL}")

# 2. Session Service Creation: This creates the single instance of the service.
#    This object handles all the SQL operations (saving, retrieving, updating sessions).
session_service = DatabaseSessionService(db_url=DB_URL)


# --- 2. AGENT INSTANTIATION AND SEQUENTIAL SETUP ---
# ... (Agents instantiated here: groomer_agent, code_agent, test_agent) ...


# 3. Create the Sequential Agent Pipeline
sdlc_pipeline = SequentialAgent(
    name="sdlc_master_pipeline",
    sub_agents=[
        groomer_agent,
        code_agent,
        test_agent,
    ],
)

# 4. Initialize the Runner (The Orchestrator)
#    The Runner uses the SequentialAgent and the SHARED persistent session service.
runner = Runner(
    agent=sdlc_pipeline, # The runner executes the entire sequential pipeline
    session_service=session_service, # 🟢 THIS IS THE KEY LINK!
    app_name="sdlc_pipeline_app" 
)
