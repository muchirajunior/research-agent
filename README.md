# Research Agent

Research Agent is a Python-based tool designed to assist with information gathering, summarization, and saving research data. It leverages OpenAI's GPT models and integrates tools for web search and Wikipedia queries.

## Features

- **Natural Language Querying**: Ask questions and get structured responses.
- **Web Search Integration**: Uses DuckDuckGo for retrieving web information.
- **Wikipedia Queries**: Fetch concise summaries from Wikipedia.
- **Data Saving**: Save research data to a markdown file with timestamps.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/muchirajunior/research-agent
    cd research-agent
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key in .env:

    ```bash
    OPENAI_API_KEY=your_api_key_here
    ```

### File Structure
- **main.py**: Entry point for the application.
- **tools.py**: Contains tools for web search, Wikipedia queries, and saving data.
- **research.md**: Stores saved research data.
- **requirements.txt**: Lists dependencies for the project.

### License
This project is licensed under the MIT License. See the LICENSE file for details.