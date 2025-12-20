from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()
agent = create_agent(
    model="deepseek:deepseek-chat",  # ollama:deepseek-r1:1.5b
)
his_messages = []

# 第一轮问答
# 问
result0 = agent.invoke({"messages": [{"role": "user", "content": "来一首古诗"}]})

# 答
messages = result0["messages"]
print(f"历史消息: {len(messages)}条")
for message in messages:
    message.pretty_print()

his_messages = messages

# 第二轮问答
# 问
ask = {"role": "user", "content": "再来"}
his_messages.append(ask)
result1 = agent.invoke({"messages": his_messages})
# 答
messages = result1["messages"]
print(f"历史消息: {len(messages)}条")
for message in messages:
    message.pretty_print()
