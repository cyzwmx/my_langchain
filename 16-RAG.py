from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()
agent = create_agent(
    model="deepseek:deepseek-chat"
)
result = agent.invoke(
    {"messages": {"role": "user", "content": "介绍一下 3i/Atlas"}}
)
answers = result["messages"]
print(f"历史消息： {len(answers)} 条")
for answer in answers:
    answer.pretty_print()