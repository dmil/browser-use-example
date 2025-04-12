import asyncio
import os
import json
from typing import List, Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from browser_use import Browser, Controller, Agent, ActionResult
from langchain_openai import ChatOpenAI

# load OPENAI_API_KEY from .env file
load_dotenv()

# Define the output format as a Pydantic model
class Post(BaseModel):
    post_title: str
    post_url: str
    num_comments: int
    hours_since_post: int


class Posts(BaseModel):
    posts: List[Post]


controller = Controller(output_model=Posts)

source = "https://news.ycombinator.com/show"

async def main():
    task = f"Go to {source} and give me the first 5 posts"
    model = ChatOpenAI(model='gpt-4o', api_key=os.getenv('OPENAI_API_KEY'))
    agent = Agent(task=task, llm=model, controller=controller)

    history = await agent.run()

    result = history.final_result()
    if result:
        parsed: Posts = Posts.model_validate_json(result)
        
        # Convert to JSON with formatting
        json_output = parsed.model_dump_json(indent=2)
        
        # Print JSON to console
        print(json_output)
        
        # Save JSON to file
        output_file = "posts.json"
        with open(output_file, "w") as f:
            f.write(json_output)

    else:
        print('No result')


if __name__ == '__main__':
    asyncio.run(main())