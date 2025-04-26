from src.vector_db.store import chroma_collection_chunknized

def augmented_prompt(query: str) -> str:
    results = chroma_collection_chunknized.similarity_search(query, k=5)
    source_knowledge = '\n'.join([x.page_content for x in results])
    rag_prompt = f"""
    Use o contexto abaixo para responder à pergunta.

    Contexto:
    {source_knowledge}

    Pergunta: {query}
    """
    return rag_prompt
