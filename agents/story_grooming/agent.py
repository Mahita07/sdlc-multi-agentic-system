from dotenv import load_dotenv
from google.adk.agents import Agent

from .story import GroomedStory

load_dotenv()

with open("./prompts/story-grooming.txt", "r", encoding="utf-8") as f:
    story_grooming_instructions = f.read()

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