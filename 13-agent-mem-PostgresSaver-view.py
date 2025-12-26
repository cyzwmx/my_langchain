# 消息列表的内存管理
# 通过config 实现多会话管理

from langchain.agents import create_agent
from langgraph.checkpoint.postgres import PostgresSaver
from dotenv import load_dotenv

load_dotenv()

DB_URL = "postgresql://postgres:123525@localhost:5432/postgres?sslmode=disable"
with PostgresSaver.from_conn_string(DB_URL) as checkpointer:
    checkpoints = checkpointer.list(
        {"configurable": {"thread_id": "1"}}
    )
    for checkpoint in checkpoints:
        messages = checkpoint[1]["channel_values"]["messages"]
        for message in messages:
            message.pretty_print()
        break
