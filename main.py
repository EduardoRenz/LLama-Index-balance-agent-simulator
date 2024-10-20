
from gateways.MockedAccountBalance import MockedAccountBalanceGateway
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgentWorker, AgentRunner


gateway = MockedAccountBalanceGateway()

# Loads the model
llm = Ollama(model="llama3.2:3b")

tools = [
    FunctionTool.from_defaults(fn=gateway.get_balance),
    FunctionTool.from_defaults(fn=gateway.withdraw),
    FunctionTool.from_defaults(fn=gateway.deposit),
]
print(tools[0])
prefix_messages = [
    ChatMessage(
        role="system",
        content=(
            f"You are now connected to the balance api currency that user can manage his account"
            "Do not make up any details."
            "With the function return, add a kindly message informing the return of information"
            "Rememer to call the function apart if user ask more than one currency"
            "The answer must be short"
            f"""This is the options to call the functions:
            get_balance
            withdraw
            deposit
            """
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

while (prompt := input("Ask me something >> ")) != "exit":
    result = agent.chat(prompt)
    print(result)
