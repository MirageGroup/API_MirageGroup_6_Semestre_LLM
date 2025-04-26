import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

persist_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'client'))
collection_name = 'test_collection_chunknized'

embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


try:
    chroma_collection_chunknized = Chroma(
        persist_directory=persist_directory,
        collection_name=collection_name,
        embedding_function=embedding_function
    )


    doc_count = chroma_collection_chunknized._collection.count()
    print(f"Coleção '{collection_name}' carregada com sucesso.")
    print(f"Documentos na coleção: {doc_count}")

except Exception as e:
    print(f"Erro ao carregar a coleção Chroma: {e}")
    print("Verifique se o diretório de persistência e o nome da coleção estão corretos e se a coleção existe.")

    import traceback
    traceback.print_exc()

