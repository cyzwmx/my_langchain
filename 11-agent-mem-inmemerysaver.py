# 消息列表的内存管理
# 通过config 实现多会话管理

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv()
checkpointer = InMemorySaver()

agent = create_agent(
    model="deepseek:deepseek-chat",  # ollama:deepseek-r1:1.5b
    checkpointer=checkpointer
)

config = {"configurable": {"thread_id": "1"}}

# 第一轮问答
# 问
result0 = agent.invoke(
    {"messages": [{"role": "user", "content": "来一首古诗"}]},
    config=config
)

# 答
messages = result0["messages"]
print(f"历史消息: {len(messages)}条")
for message in messages:
    message.pretty_print()

# 第二轮问答
# 问
ask = {"role": "user", "content": "再来"}
result1 = agent.invoke({"messages": [{"role": "user", "content": "再来"}]},
                       config=config)
# 答
messages = result1["messages"]
print(f"历史消息: {len(messages)}条")
for message in messages:
    message.pretty_print()
