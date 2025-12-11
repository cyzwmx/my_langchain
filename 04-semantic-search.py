from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# 嵌入模型
embedding = OllamaEmbeddings(model='nomic-embed-text:latest')
# 向量库（知识库）
vector_store = Chroma(
    collection_name='example_collection',
    embedding_function=embedding,
    persist_directory='./chroma_langchain_db'
)

# 相似度查询
results = vector_store.similarity_search_with_score(
        "程序员面试应该注意什么？"
    )
for doc, score in results:
    print(score)
    print(doc.page_content[:100])
    print("\n\n")


# 用向量进行查询

vector = embedding.embed_query(
    "程序员面试应该注意什么?"
)
results = vector_store.similarity_search_by_vector(
        vector
    )
for index, doc in enumerate(results):
    print(index)
    print(doc.page_content[:100])
    print("\n\n")


# 封装为chain ：langchain : LLM 提示词模板、 tools， output, Runnable

from typing import List
from langchain_core.documents import Document
from langchain_core.runnables import chain

@chain
def retriever(query: str) -> List[Document]:
    return vector_store.similarity_search(query, k=1)

results = retriever.invoke("程序员面试应该注意什么?")
for index, doc in enumerate(results):
    print(index)
    print(doc.page_content[:100])
    print("\n\n")