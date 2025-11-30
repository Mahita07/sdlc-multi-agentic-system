from dotenv import load_dotenv
from google.adk.agents import Agent

from tools.file_browser import list_files
from tools.file_reader import read_file
from tools.file_writer import create_project_from_json


load_dotenv()

with open("./prompts/writer.txt", "r", encoding="utf-8") as f:
    writing_instructions = f.read()

root_agent=Agent(
    name="writer_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to take project structure and populate files"
    ),
    instruction=(
        writing_instructions
    ),
    tools=[read_file,list_files,create_project_from_json],
)