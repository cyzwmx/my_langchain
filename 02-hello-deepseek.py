from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
# model = ChatDeepSeek(
#     model="deepseek-chat",  # deepseek-reasoner
#     temperature=0.1,
#     max_tokens=2000,
#     timeout=None,
#     max_retries=2
# )


model = init_chat_model(
    model='deepseek-chat',
    model_provider='deepseek',
    temperature=0.1
)

for chunk in model.stream("输出一首古诗词"):
    print(chunk.content, end="", flush=True)
