## 索引
# 1、读取PDF  按照页管理 Document List[Document]
# 2、分割文本 文本段（chunk）Document  List[Document]
# 3、向量化 文本段 <=> 向量  需要嵌入模型
# 4、向量库 把文本段和向量存到向量库

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path = 'test_document.pdf'
loader = PyPDFLoader(file_path)
docs = loader.load()
# print(len(docs))
# print(type(docs[0]))
# print(docs[1])
# page_content=''  第一页内容
# metadata = {'producer': 'Adobe PDF Library 10.0.1', 'creator': 'Adobe InDesign CS6 (Windows)',
#             'creationdate': '2019-12-18T14:42:02+08:00', 'moddate': '2023-04-13T16:13:02+08:00', 'trapped': '/False',
#             'source': 'test_document.pdf', 'total_pages': 49, 'page': 0, 'page_label': 'ml1'}

# 2. 分割文本

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # char/token/chunk
    chunk_overlap=200,  # 重叠部分大小
    add_start_index=True  # 要不要index
)

all_splits = text_splitter.split_documents(docs)
print(len(all_splits))
print(all_splits[0])

# 3. 向量化
from langchain_ollama import OllamaEmbeddings

embedding = OllamaEmbeddings(model='nomic-embed-text:latest')
# vector_0 = embedding.embed_query(all_splits[0].page_content)
# print(len(vector_0))
# print(vector_0)
# print(type(vector_0))

# 4. 向量存储 向量/文本块
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name='example_collection',
    embedding_function=embedding,
    persist_directory='./chroma_langchain_db'
)
ids = vector_store.add_documents(documents=all_splits)

print(len(ids))
print(ids)
