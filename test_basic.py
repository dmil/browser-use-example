import os 
import asyncio 
from browser_use import Agent
from langchain_openai import ChatOpenAI

# Load OPENAI_API_KEY from .env file
from dotenv import load_dotenv 
load_dotenv() 

async def main():
    # Create an AI agent that will perform our web browsing task
    agent = Agent(
        # Plain English description of what we want the agent to do
        task="Get me the top 5 posts on hacker news",
        llm=ChatOpenAI(model="gpt-4o", api_key=os.getenv('OPENAI_API_KEY')),
    )
    await agent.run()

# Start the program by running the main() function
# asyncio.run() is the entry point for running an async function
asyncio.run(main())