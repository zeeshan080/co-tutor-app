from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, SQLiteSession ,set_tracing_disabled
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams
from SYSTEMPROMPT import SYSTEMPROMPT
from dotenv import load_dotenv
import os
import asyncio

info = {
    "user_id": "1",
    "course_id": "AI-001",
    "teacher_name": "Qasim",
    "assistant_name": "Alice"
}

load_dotenv()
set_tracing_disabled(True)
gemini_api_key = os.getenv("GEMINI_API_KEY")
mcp_server_url = os.getenv("MCP_SERVER_URL")

external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

async def main():
    mcp_params = MCPServerStreamableHttpParams(url=mcp_server_url)
    async with MCPServerStreamableHttp(params=mcp_params, name="cotutor-server", cache_tools_list=False) as mcp_server:
        try:
            session = SQLiteSession(session_id=info["user_id"], db_path=":memory:")
            cotutor_agent = Agent(
                name="CoTutor",
                mcp_servers=[mcp_server],
                model=llm_model,
                instructions=SYSTEMPROMPT.format(user_id=info["user_id"], course_id=info["course_id"], teacher_name=info["teacher_name"], assistant_name=info["assistant_name"]),
            )
            
            result = await Runner.run(cotutor_agent, "Hello")
            print(f"\n\n[AGENT]: {result.final_output}")

            while True:
                user_input = input("[USER MESSAGE]: ")
                if user_input == "exit":
                    break
                result = await Runner.run(cotutor_agent, user_input,session= session)
                print(f"\n\n[AGENT]: {result.final_output}")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())