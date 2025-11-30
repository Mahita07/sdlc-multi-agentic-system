from pathlib import Path
from dotenv import load_dotenv
from google.adk.agents import Agent
from agents.code.code import CodeGenerationOutput

load_dotenv()

with open("./prompts/code-agent.txt", "r", encoding="utf-8") as f:
    code_instructions = f.read()
   
root_agent = Agent(
    name="code_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to write efficient code"
    ),
    instruction=(
        code_instructions
    ),
    output_key="generated_code",
    output_schema=CodeGenerationOutput
)