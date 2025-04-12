import asyncio
import os
from typing import List, Optional
from browser_use import Browser, Controller, Agent, ActionResult
from pydantic import BaseModel, Field  # For data validation and schema definition
from langchain_openai import ChatOpenAI 

# Load OPENAI_API_KEY from .env file
from dotenv import load_dotenv
load_dotenv()

# Define the output format as Pydantic models
# Pydantic helps with data validation and provides automatic JSON serialization

class Post(BaseModel):
    """
    Model representing a single Hacker News post with relevant information.
    Each field will be validated according to its type.
    """
    post_title: str  # The title of the post
    post_url: str  # The URL of the post
    num_comments: int  # Number of comments on the post
    hours_since_post: int  # How many hours ago the post was made


class Posts(BaseModel):
    """
    Container model that holds a list of Post objects.
    This defines the overall structure of our output data.
    """
    posts: List[Post]  # A list of Post objects


# Set up the controller with our expected output format
# The controller will help manage the browser interaction
controller = Controller(output_model=Posts)

# The webpage we want to scrape data from
source = "https://news.ycombinator.com/show"

async def main():

    # Define the task for the agent in plain English
    task = f"Go to {source} and give me the first 5 posts"
    
    # Initialize the AI model (GPT-4o) with OpenAI API key from environment variables
    model = ChatOpenAI(model='gpt-4o', api_key=os.getenv('OPENAI_API_KEY'))
    
    # Create an agent with our task, language model, and controller
    agent = Agent(task=task, llm=model, controller=controller)

    # Execute the agent's task and get the interaction history
    # This is where the agent will browse the website and collect data
    history = await agent.run()

    # Extract the final result from the agent's interaction history
    result = history.final_result()
    if result:
        # Parse the JSON result into our Pydantic model
        # This validates the data structure and types
        parsed: Posts = Posts.model_validate_json(result)
        
        # Convert the parsed data back to JSON with nice formatting (indentation)
        json_output = parsed.model_dump_json(indent=2)
        
        # Output the formatted JSON to the console
        print(json_output)
        
        # Save the JSON output to a file for later use
        output_file = "posts.json"
        with open(output_file, "w") as f:
            f.write(json_output)

    else:
        # Handle the case where no result was returned
        print('No result')


# Standard Python idiom to ensure the main() function runs only when
# this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    # Run the asynchronous main function using asyncio
    asyncio.run(main())