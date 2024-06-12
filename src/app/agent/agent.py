from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.pydantic_v1 import ValidationError
from langchain_core.tools import ToolException


from .templates import load_chat_template
from .tools import daily_menu_tool
from .llm import create_llm


def run_agent(user_request: str, chat_history: list=[]):
    """Simple method to run the make a call to the agent.

       This function prepares a chat template, formats the input prompt, and executes
       an agent to retrieve responses

           Parameters:
               question (str): The main question to retrieve responses for.

           Returns:
               A dictionary of the form:
               {
                'user_request': <user_request>,
                'chat_history': [{'role': 'user', 'content': 'what is it you want?'}],
                'output': 'response-from-the-agent-as-a-result'
                }
    """
    print("************* user request ")
    print(user_request)

    # Create an instance of the LLM (Azure OpenAI instance), load the chat template & create the Agent.
    llm = create_llm()

    # Load a Langchain ChatPromptTemplate instance using the templates in the 'prompts' subdirectory.
    # The resulting ChatPromptTemplate has two possible input variables: 'input' and 'chat_history'.
    chat_template = load_chat_template()

    # Load the Tools. See the 'tools' subdirectory for each tool definition.
    tools = [daily_menu_tool]

    # Create the Langchain Agent which requires the LLM, Tools and PromptTemplate
    agent = create_openai_tools_agent(llm, tools, chat_template)

    # Create the runtime in charge of executing the agent.  ie. it is in charge of calling the LLM,
    # running the tools when the LLM says to use a particular tool, adding the tool output (returned data)
    # into the message history, and calling the llm again, etc.
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Invoke the agent
    # https://api.python.langchain.com/en/latest/agents/langchain.agents.agent.AgentExecutor.html
    response = agent_executor.invoke({"user_request": user_request, "chat_history": chat_history})
    return response

