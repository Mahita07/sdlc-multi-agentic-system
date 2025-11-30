from google.adk.agents import SequentialAgent
from agents.story_grooming import agent as story_groomer
from agents.testing import agent as test_writer
from agents.code import agent as code_writer

code_pipeline_agent = SequentialAgent(
    name="CodePipelineAgent",
    sub_agents=[story_groomer.root_agent,code_writer.root_agent, test_writer.root_agent],
    description="Executes a sequence of story grooming, code writing and unit test writing",
)

root_agent = code_pipeline_agent