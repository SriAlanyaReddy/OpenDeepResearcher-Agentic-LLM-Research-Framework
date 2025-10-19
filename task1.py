import os
from datetime import date
from dotenv import load_dotenv
import contextlib

# Import necessary components from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import tool

# --- Environment Setup ---
# Load environment variables from a .env file for API keys
load_dotenv()


# --- Tool Definitions ---

@tool
def get_current_date() -> str:
    """
    Returns the current date in YYYY-MM-DD format.
    Use this tool to get the current date for any questions
    related to today's date.
    """
    return str(date.today())

# --- LLM and Tools Initialization ---

# Initialize the Google Gemini LLM
# The try-except block handles potential errors if the API key is not set
try:
    # Use a file to redirect stderr to avoid cluttering the console output
    with open(os.devnull, 'w') as f, contextlib.redirect_stderr(f):
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
except Exception as e:
    print("Error initializing the LLM. Please ensure your GOOGLE_API_KEY is set correctly.")
    print(f"Error: {e}")
    exit()

# Initialize the Tavily Search tool
tavily_tool = TavilySearchResults(max_results=5, name="web_search")

# Combine all tools into a list for the agent
tools = [get_current_date, tavily_tool]


# --- Agent and Prompt Creation ---

# Define the prompt template that instructs the agent
prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a helpful assistant with a set of tools. Your primary goal is to answer the user's question effectively.
To do this, you must follow these rules for tool usage:

**Rules for get_current_date tool:**
You MUST call this tool under the following conditions ONLY:
1. The user directly asks for the current date (e.g., 'what day is it?').
2. The user asks a question involving a relative date that requires a calculation (e.g., 'what was the date last tuesday?').
3. The user's query requires a specific date as an input for another tool (e.g., 'what is the weather in London tomorrow?').

### EXCLUSIONS:
Do NOT call this tool for queries using general keywords like 'latest', 'recent', 'new', or 'trending' as the web_search tool can already handle recency. For these types of general questions, you can use the web_search tool directly.
If you do use the `get_current_date` tool, please state the date in your final answer.
    """),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# Create the agent by combining the LLM, tools, and prompt
agent = create_tool_calling_agent(llm, tools, prompt)

# Create the Agent Executor to run the agent
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True  # Set to True to see the agent's thought process
)


# --- Main Application Logic ---

def main():
    """Main function to run the chat interaction."""
    print("LLM Agent is ready. Type 'q' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'q':
            print("Exiting...")
            break
        
        # Invoke the agent executor with the user's input
        response = agent_executor.invoke({"input": user_input})
        
        print(f"Agent: {response['output']}")

if __name__ == "__main__":
    main()