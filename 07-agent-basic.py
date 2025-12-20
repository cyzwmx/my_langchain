from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()
agent = create_agent(
    model="deepseek:deepseek-chat",  # ollama:deepseek-r1:1.5b
    # model="ollama:deepseek-r1:1.5b",  # ollama:deepseek-r1:1.5b
)
# langgraph.graph.state.CompiledStateGraph object
# Graph: nodes - edges 网状
# print(agent)
# print(agent.nodes)  # 两个节点
"""
{'__start__': <langgraph.pregel._read.PregelNode object at 0x000001CA97D0BB10>, 
'model': <langgraph.pregel._read.PregelNode object at 0x000001CA97D0BE90>}

pregel: google 2010分布的技术
"""

result = agent.invoke({"messages": [{"role": "user", "content": "20251230 天气如何"}]})
print(result)
"""
{'messages': [HumanMessage(content='今天是几号', additional_kwargs={}, response_metadata={},
                           id='aadc3cf5-af18-469a-a4bc-1c2c9f9351d5'),
              AIMessage(content='今天是 **2025 年 7 月 18 日**，星期五。 😊', additional_kwargs={'refusal': None},
                        response_metadata={
                            'token_usage': {'completion_tokens': 20, 'prompt_tokens': 7, 'total_tokens': 27,
                                            'completion_tokens_details': None,
                                            'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0},
                                            'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 7},
                            'model_provider': 'deepseek', 'model_name': 'deepseek-chat',
                            'system_fingerprint': 'fp_eaab8d114b_prod0820_fp8_kvcache',
                            'id': '48848a6e-a073-46c0-bc08-4d961849fb7c', 'finish_reason': 'stop', 'logprobs': None},
                        id='lc_run--ab49ae22-87e6-4a49-8416-a314ca070d03-0',
                        usage_metadata={'input_tokens': 7, 'output_tokens': 20, 'total_tokens': 27,
                                        'input_token_details': {'cache_read': 0}, 'output_token_details': {}})]}
"""
messages = result["messages"]
print(f"历史消息: {len(messages)}条")
for message in messages:
    message.pretty_print()