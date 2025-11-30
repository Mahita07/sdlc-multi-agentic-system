from dotenv import load_dotenv
from google.adk.agents import Agent
import asyncio

# 🟢 FIX 1: Import the base Session class and the Runner from the correct module
#from google.adk.runners import Runner
#from google.adk.sessions import Session, DatabaseSessionService 


from .story import GroomedStory

load_dotenv()

# --- Agent Definition (Required for Runner setup) ---
# NOTE: Ensure ./prompts/story-grooming.txt exists and has content
try:
    with open("./prompts/story-grooming.txt", "r", encoding="utf-8") as f:
        story_grooming_instructions = f.read()
except FileNotFoundError:
    story_grooming_instructions = "You are a story groomer agent. Return markdown."


root_agent = Agent(
    name="story_groomer_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to write user stories"
    ),
    instruction=(
        story_grooming_instructions
    ),
    output_key="groomed_story",
    output_schema=GroomedStory
)