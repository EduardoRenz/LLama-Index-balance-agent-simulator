from api.balance import get_balance
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.tools import QueryEngineTool, ToolMetadata, FunctionTool
from llama_index.core.agent import FunctionCallingAgentWorker, AgentRunner


# Loads the model
llm = Ollama(model="llama3.2:1b")


# response = query_engine.query("Qual o nome do FII?")
# print(response)

tools = [
    FunctionTool.from_defaults(fn=get_balance)
]

prefix_messages = [
    ChatMessage(
        role="system",
        content=(
            f"You are now connected to the balance api, if user asks for get_balance, call get_balance passing the currency that user wants"
            "Do not make up any details."
            "With the function return, add a kindly message informing the return of information"
            "Rememer to call the function apart if user ask more than one currency"
        ),
    )
]


worker = FunctionCallingAgentWorker(
    tools=tools,
    llm=llm,
    prefix_messages=prefix_messages,
    max_function_calls=10,
    allow_parallel_tool_calls=False,
    verbose=True,
)

agent = AgentRunner(worker)


result = agent.chat("What is my balance for USD?")


print(result)
