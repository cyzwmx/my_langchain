import chromadb


def list_collection(db_path):
    client = chromadb.PersistentClient(db_path)
    collections = client.list_collections()
    print(f"chromadb:{db_path} 有{len(collections)}个")
    for idx, collection in enumerate(collections):
        print(f"collection {idx}: {collection.name}, 共有{collection.count()} 条记录")


def delete_collection(db_path, collection_name):
    try:
        client = chromadb.PersistentClient(db_path)
        client.delete_collection((collection_name))
    except Exception as e:
        print(f"delete {collection_name} err")


db_path = "chroma_langchain_db"
list_collection((db_path))
