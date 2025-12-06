# from langchain_ollama import ChatOllama
#
# model = ChatOllama(
#     model='deepseek-r1:1.5b',
#     base_url ="http://localhost:11434",
#     temperature=0.1
# )

"""
langchain1.0
"""
from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="ollama:deepseek-r1:1.5b",
    base_url="http://localhost:11434",
    temperature=0.1,
    timeout=30,
    max_token=2000
)
for chunk in model.stream("写一段厦门元旦旅游的计划"):
    print(chunk.content, end="", flush=True)
