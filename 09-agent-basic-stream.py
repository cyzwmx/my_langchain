from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


def get_weather(city: str):
    """Get weather for a given city"""
    return f"It's always sunny in {city}"


def get_lol_champion():
    """返回2025年英雄联盟S15的冠军战队"""
    # 假设我们知道冠军战队是"T1"
    team = "T1"
    return f"又是{team}"


agent = create_agent(
    model="deepseek:deepseek-chat",
    tools=[get_weather, get_lol_champion]

)

"""
{'__start__': <langgraph.pregel._read.PregelNode object at 0x00000240D64B6F10>, 
'model': <langgraph.pregel._read.PregelNode object at 0x00000240D6A653D0>,
'tools': <langgraph.pregel._read.PregelNode object at 0x00000240D6A8EB90>}
"""

# for event in agent.stream(
#     {"messages": [{"role": "user", "content": "2025年英雄联盟S15的冠军是什么战队"}]},
#     stream_mode="values"  # message by message
# ):
#     messages = event["messages"]
#     print(f"历史消息: {len(messages)}条")
#     # for message in messages:
#     #     message.pretty_print()
#     messages[-1].pretty_print()


for chunk in agent.stream(
        {"messages": [{"role": "user", "content": "2025年英雄联盟S15的冠军是什么战队"}]},
        stream_mode="messages"  # token by token
):
    print(chunk[0].content, end='')
