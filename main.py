
from gateways.MockedAccountBalance import MockedAccountBalanceGateway
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgentWorker, AgentRunner


gateway = MockedAccountBalanceGateway()

# Loads the model
llm = Ollama(model="llama3.2:3b")

tools = [
    FunctionTool.from_defaults(
        fn=gateway.get_balance, description="A way to get currency amount passing the currency, always pass in uppercase", name="Get Balance"),
    FunctionTool.from_defaults(fn=gateway.withdraw, name="Withdraw",
                               description="Withdraw from user account, must have amount and currency"),
    FunctionTool.from_defaults(
        fn=gateway.deposit, name="Deposit", description="Deposit to user account, must have amount and currency"),
]

prefix_messages = [
    ChatMessage(
        role="system",
        content=(
            f"You are now connected to the balance api currency that user can manage his account"
            "Do not make up any details."
            "Rememer to call the function apart if user ask more than one currency"
            "The answer must be short"
            "After a depoist, call the get balance and return the new amount"
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
