from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Get me the top 5 posts on hacker news",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())