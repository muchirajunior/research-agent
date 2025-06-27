from langchain_community.tools import WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from  langchain.tools import Tool
from datetime import datetime

#search tool
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name='Search',
    func=search.run,
    description='Searching web information'
)

#wikipedia too
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=4000)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

def save_info(data: str, filename: str='research.md'):
    """
    Save the provided data to a file, appending the current date and time.

    Args:
        data (str): The data to save.
        filename (str): The name of the file to save the data in.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_with_timestamp = f"{data}\nSaved on: {timestamp}\n"
    
    with open(filename, "a") as file:
        file.write(data_with_timestamp)

save_data_tool = Tool(
    name='Save',
    func=save_info,
    description='Save reserch info to a markdown file, pass string of data and filename as second prameter'
)