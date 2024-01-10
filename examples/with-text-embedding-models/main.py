import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    import uuid
    from typing import List
    from langchain_community.embeddings import OpenAIEmbeddings
    from tidb_vector import VectorStore, VectorDocument


    class TextStore:
        def __init__(self, name: str):
            self.embeddings = OpenAIEmbeddings()
            self.store = VectorStore()
            self.collection = self.store.open_collection(name=name)

        def insert(self, documents: List[str]):
            vectors = self.embeddings.embed_documents(documents)

            vector_documents: List[VectorDocument] = []
            for i in range(0, len(documents)):
                vector_documents.append(VectorDocument(
                    document_id=uuid.uuid4().hex,
                    vector=vectors[i],
                    content=documents[i],
                    metadata={'embedding_model': 'openai'}
                ))

            self.collection.insert(vector_documents)

        def similarity_search(self, query: str):
            vector = self.embeddings.embed_query(query)
            return self.collection.cosine_similarity(vector, 1)[0].content


    text_store = TextStore(name='test')

    text_store.insert([
        'The quick brown fox jumps over the lazy dog.',
        'A journey of a thousand miles begins with a single step.',
        'To be or not to be, that is the question.'
    ])

    # should print 'A journey of a thousand miles begins with a single step.'
    print(text_store.similarity_search('Exploring the essence of long journeys in literature.'))
