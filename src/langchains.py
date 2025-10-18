from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import MessagesPlaceholder
from todoist_api_python.api import TodoistAPI

load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

todoistApi = TodoistAPI(todoist_api_key)

@tool
def add_task(task, desc=None):
    """Add a new task to the user's task list. Use this when user wants to add or create a task"""
    print("Adding a task", task)
    print("Task added")
    todoistApi.add_task(content=task, description=desc)

@tool
def show_tasks():
    """Show all tasks, Use this tool when user wants to see their tasks."""
    print('showTasks')
    result_paginator = todoistApi.get_tasks()
    tasks = []
    for task_list in result_paginator:
        for task in task_list:
            tasks.append(task)
    return tasks

tools = [add_task, show_tasks]
llm =ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_promt = """You are helpful assistant. 
You will help user add tasks.
You will help to show existing tasks. if user asks to show the tasks: for example "Show me the tasks"
print out the tasks to the user. Print them in bullet list format.
"""

# user_input = "add new task to get new tyre"
prompt = ChatPromptTemplate([
    ("system",system_promt),
    MessagesPlaceholder("history"),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])

# chain = prompt| llm |StrOutputParser()

agent = create_openai_tools_agent(
    llm, tools, prompt
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# print(chain)

# response = chain.invoke({"input": user_input})


# print(response)
history = []
while True:
    user_input = input("You: ")
    response = agent_executor.invoke({"input": user_input, "history": history})
    print(response)
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response['output']))

# gradion interface library impl