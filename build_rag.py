import os
import glob
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.embeddings.ollama import OllamaEmbedding
import chromadb

def build_rag():
    # Paths to documentation
    docs_paths = [
        "docs/api",
        "docs/insight"
    ]

    # Collect all Markdown files
    md_files = []
    for path in docs_paths:
        md_files.extend(glob.glob(os.path.join(path, "**/*.md"), recursive=True))

    print(f"Found {len(md_files)} Markdown files")

    # Load documents
    documents = SimpleDirectoryReader(input_files=md_files).load_data()

    # Parse into nodes (chunks)
    parser = MarkdownNodeParser()
    nodes = parser.get_nodes_from_documents(documents)

    print(f"Created {len(nodes)} chunks")

    # Create Chroma client and collection
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = chroma_client.get_or_create_collection("flame_docs")

    # Create vector store
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Build index with Ollama embeddings
    index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=OllamaEmbedding(model_name="nomic-embed-text"))

    print("RAG system built and saved to ./chroma_db")

    return index

if __name__ == "__main__":
    build_rag()