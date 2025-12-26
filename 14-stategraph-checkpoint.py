# checkpointer  检查点管理器  存储
# checkpoint  检查点 状态图的总体快照
# thread_id  管理
# 作用  记忆管理、时间旅行 pause暂停 容错
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from typing import Annotated
from typing_extensions import TypedDict
from operator import add


class State(TypedDict):
    foo: str
    bar: Annotated[list[str], add]


def node_a(state: State):
    return {"foo": "a", "bar": ["a"]}


def node_b(state: State):
    return {"foo": "b", "bar": ["b"]}


# 构建状态图
workflow = StateGraph(State)
workflow.add_node(node_a)
workflow.add_node(node_b)
workflow.add_edge(START, 'node_a')
workflow.add_edge('node_a', 'node_b')
workflow.add_edge('node_b', END)

# 检查管理器
checkpointer = InMemorySaver()
config: RunnableConfig = {
    'configurable': {"thread_id": "1"}
}

# 编译
graph = workflow.compile(checkpointer=checkpointer)
# 调用
result = graph.invoke({"foo": ""}, config)
print(result)

# 状态查看
# print(graph.get_state(config=config))

for checkpoint_tuple in checkpointer.list(config=config):
    print("\n")
    # print(checkpoint_tuple)
    print(checkpoint_tuple[2])


"""
CheckpointTuple(config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1f0e2312-c10d-61b9-8002-b0480a870626'}},
 checkpoint={'v': 4, 'ts': '2025-12-26T08:02:06.906002+00:00', 'id': '1f0e2312-c10d-61b9-8002-b0480a870626',
  'channel_versions': {'__start__': '00000000000000000000000000000002.0.15043966117757523', 'foo': '00000000000000000000000000000004.0.5147588893816559', 'branch:to:node_a': '00000000000000000000000000000003.0.06358948884796345', 'bar': '00000000000000000000000000000004.0.5147588893816559', 'branch:to:node_b': '00000000000000000000000000000004.0.5147588893816559'},
   'versions_seen': {'__input__': {}, '__start__': {'__start__': '00000000000000000000000000000001.0.01851568739767695'},
    'node_a': {'branch:to:node_a': '00000000000000000000000000000002.0.15043966117757523'},
     'node_b': {'branch:to:node_b': '00000000000000000000000000000003.0.06358948884796345'}}, 
     'updated_channels': ['bar', 'foo'], 'channel_values': {'foo': 'b', 'bar': ['a', 'b']}}, 
     metadata={'source': 'loop', 'step': 2, 'parents': {}}, 
     parent_config={'configurable': {'thread_id': '1', 'checkpoint_ns': '', 'checkpoint_id': '1f0e2312-c10a-6a65-8001-c211e93e4e74'}}, pending_writes=[])

"""
