import asyncio
from browser_use import Agent
from langchain_openai import ChatOpenAI

# load OPENAI_API_KEY from .env file
import os
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Get me the top 5 posts on hacker news",
        llm=ChatOpenAI(model="gpt-4o", api_key=os.getenv('OPENAI_API_KEY')),
    )
    await agent.run()

asyncio.run(main())