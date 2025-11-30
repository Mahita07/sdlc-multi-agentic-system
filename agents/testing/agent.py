from pathlib import Path
from dotenv import load_dotenv
from google.adk.agents import Agent

from agents.testing.tests import UnitTestGeneration

load_dotenv()

with open("./prompts/testing.txt", "r", encoding="utf-8") as f:
    testing_instructions = f.read()

root_agent = Agent(
    name="test_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to write unit tests"
    ),
    instruction=(
        testing_instructions
    ),
    output_key="generated_tests",
    output_schema=UnitTestGeneration
)