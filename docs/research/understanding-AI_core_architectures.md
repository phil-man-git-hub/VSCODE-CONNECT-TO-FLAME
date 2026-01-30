# Understanding AI Core Architectures

In the world of AI, "Architecture" refers to how different systems are connected to solve complex problems. For a programmer, this is the high-level design pattern of an AI application.

---

## 1. MCP (Model Context Protocol)
**The Universal Connector**

*   **The Problem:** Every time a developer wanted an AI (like Claude or Gemini) to use a tool (like Google Search or a Local Database), they had to write unique, fragile code for that specific combination.
*   **The Solution:** MCP is a standardized "handshake." If you build an MCP server for your data, *any* MCP-compliant AI can immediately understand how to read and use it.
*   **Analogy:** **The USB Port.** Before USB, printers, keyboards, and mice all had different, weird plugs. USB standardized the connection so everything "just works."
*   **Simple Code (Conceptual):**
    ```python
    # Defining an MCP tool that the AI can call
    @mcp.tool()
    def search_local_logs(query: str):
        """Searches through project logs for a specific error."""
        # The AI will decide when to call this based on the user's request
        return run_grep_command(query)
    ```

## 2. RAG (Retrieval-Augmented Generation)
**The Open-Book Exam**

*   **What it is:** Instead of relying on the AI's training (which might be old), we "hand" the AI specific documents relevant to the user's question right before it answers.
*   **Analogy:** **A Librarian.** If you ask a librarian a question, they don't just guess from memory; they go to the shelf, find the right book, read the relevant page, and then summarize the answer for you.
*   **Why use it?** It prevents "hallucinations" (making things up) and allows the AI to talk about private data it was never trained on.
*   **Simple Code (Conceptual):**
    ```python
    # 1. Get the user's question
    question = "How do I setup the Flame Listener?"

    # 2. 'Retrieve' relevant snippets from our docs
    context = search_my_docs_folder(question)

    # 3. 'Augment' the prompt
    final_prompt = f"Using these notes: {context}, answer this: {question}"

    # 4. 'Generate' the answer
    ai_response = model.generate(final_prompt)
    ```

## 3. Agents
**The Autonomous Employee**

*   **What it is:** An AI system that can break a big goal into small steps, execute those steps using tools, and fix its own mistakes.
*   **Analogy:** **A Junior Developer.** If you tell a chatbot "Fix this bug," it might explain how. If you tell an *Agent* "Fix this bug," it will:
    1. Read the code.
    2. Identify the error.
    3. Write a fix.
    4. Run the test.
    5. If the test fails, try a different fix.
*   **The ReAct Loop:** Agents follow a pattern called **Reason + Act**.
    *   **Reason:** "I see the test failed because of a SyntaxError."
    *   **Act:** "I will edit line 42 to add the missing colon."
    *   **Observe:** "The test now passes."
