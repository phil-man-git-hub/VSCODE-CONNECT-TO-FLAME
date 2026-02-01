# Goal: FU_Encyclopedia (Knowledge RAG)

## Objective
Create `fu_encyclopedia.py` to act as the "Intelligence Layer" for the FLAME-UTILITIES ecosystem. It will provide semantic search capabilities over the vast amount of synthesized documentation and API stubs, allowing AI agents to find precise workflow details without consuming the entire context window.

## Core Capabilities
- **Semantic Indexing:** Index all Markdown files in `docs/` and Python stubs in `stubs/`.
- **Knowledge Retrieval:** Provide a tool for `fu_whisper` to perform semantic queries (e.g., "Find the method for tagging ARRI LogC4 in a Pybox").
- **Version Awareness:** Index version-specific quirks extracted from the research docs.
- **Vertex AI Integration:** Utilize `vertexai.preview.rag` for corpus management and high-quality embeddings (`text-embedding-005`).

## Technical Implementation (fu_encyclopedia.py)
- **Corpus Management:** Functions to create and update the `RagCorpus`.
- **File Upload:** Automated scripts to sync the local `docs/` directory with the Vertex AI RAG backend.
- **Retrieval Logic:** Implementation of `rag.retrieval_query` to return relevant contexts to the LLM.

## Integration with FU_Whisper
- `fu_whisper.py` will be updated to include a new tool: `search_flame_encyclopedia(query: str)`.
- When a user asks a complex question, the AI will first query the encyclopedia, retrieve the relevant documentation snippets, and then execute the appropriate Flame commands.

## Success Metrics
- Reduction in token usage by only providing relevant documentation snippets.
- Higher accuracy in generating complex multi-node Batch setups.
- Ability to answer "how-to" questions that aren't explicitly in the prompt.
