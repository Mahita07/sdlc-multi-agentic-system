import asyncio
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from google.adk.agents import SequentialAgent
from dotenv import load_dotenv
from google.genai import types
from uuid import uuid4

load_dotenv()

from agents.story_grooming.agent import root_agent as groomer_agent
from agents.code.agent import root_agent as code_agent
from agents.testing.agent import root_agent as test_agent
from agents.writer.agent import root_agent as writer_agent

DB_URL = "sqlite+aiosqlite:///./session_management.db"
print(f"💾 Central Session Service initialized using {DB_URL}")

session_service = DatabaseSessionService(db_url=DB_URL)



sdlc_pipeline = SequentialAgent(
    name="sdlc_master_pipeline",
    sub_agents=[
        groomer_agent,
        code_agent,
        test_agent,
        writer_agent
    ],
)

runner = Runner(
    agent=sdlc_pipeline, 
    session_service=session_service, 
    app_name="agents" 
)


APP_NAME = "agents"   
USER_ID = "user_001"
SESSION_ID = f"sdlc_{uuid4().hex[:12]}"



async def interactive_run():
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    print("\n✅ SDLC Pipeline ready.")
    print("Type your input below (file path, instruction, etc.)")
    print("Type 'exit' to stop.\n")

    while True:
        user_input = input("YOU> ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("👋 Session ended.")
            break

        content = types.Content(
            role="user",
            parts=[types.Part(text=user_input)]
        )

        print("\n🤖 PIPELINE RUNNING...\n")

        for event in runner.run(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=content
        ):
            if event.is_final_response():
                print("✅ FINAL OUTPUT:\n", event.content)


if __name__ == "__main__":
    asyncio.run(interactive_run())
