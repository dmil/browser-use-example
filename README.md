# Browser-Use Example

This repository demonstrates how to use the `browser-use` library to create AI agents that can autonomously browse the web and extract structured information.

## Overview

The examples in this repository show how to:
- Create simple browsing agents
- Extract structured data from websites
- Save results in structured JSON format
- Customize the browsing behavior

## Installation

1. Clone this repository
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your API keys:

   ```bash
   cp .env.example .env
   ```

Then edit the `.env` file to add your API keys (at minimum, the OPENAI_API_KEY is required for most examples).

## Examples

### Basic Usage

`test_basic.py` demonstrates a simple agent that retrieves the top 5 posts from Hacker News:

```bash
python test_basic.py
```

This example shows the basic pattern of creating an Agent with a task and an LLM, then running it.

### Structured Output

`test_structured_output.py` shows how to extract structured data using Pydantic models:

```bash
python test_structured_output.py
```

This script:
1. Defines a Pydantic model for the expected output structure
2. Creates a Controller with the output model
3. Runs an agent that extracts data into the structured format
4. Saves the results to a JSON file

## Main Components

- **Agent**: The main class that performs browsing tasks
- **Controller**: Manages the structured output format
- **Browser**: Handles the underlying web browsing mechanics

## READ THIS !!!!
Check out [📚 https://docs.browser-use.com/introduction](https://docs.browser-use.com/introduction) for more examples and documentation

## Dependencies

- `browser-use`: Main library for browser automation with AI
- `langchain_openai`: For integration with OpenAI models
- `playwright`: For web automation
- `pydantic`: For data validation and structure
- `python-dotenv`: For environment variable management


🤖 Disclaimer: README was made by ChatGPT with light edits from Dhrumil