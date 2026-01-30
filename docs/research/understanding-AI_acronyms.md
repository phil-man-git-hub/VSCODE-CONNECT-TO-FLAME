# Understanding AI: A Guide to Modern Acronyms

This guide is designed for developers who are new to the AI space. It breaks down the "alphabet soup" of AI into logical categories, using simple analogies and code examples.

---

## 1. Core Architectures (The Frameworks)

### **MCP (Model Context Protocol)**
*   **Analogy:** **"USB for AI."**
*   **What it is:** A standard way for AI models to connect to your local tools and data without writing custom code for every single app.
*   **Novice Perspective:** Imagine if every mouse needed a different plug for every computer. That was AI before MCP. MCP makes the "plugs" universal.
*   **Code Pattern:**
    ```python
    # Using FastMCP to define a tool the AI can "plug into"
    mcp = FastMCP("MyToolServer")

    @mcp.tool()
    def get_weather(city: str) -> str:
        return f"The weather in {city} is sunny."
    ```

### **RAG (Retrieval-Augmented Generation)**
*   **Analogy:** **"The Open-Book Exam."**
*   **What it is:** Giving an AI a specific set of documents to look at before it answers a question.
*   **Novice Perspective:** Standard AI (like ChatGPT) answers from memory. RAG lets the AI look at *your* specific files (like this codebase) to give accurate, non-hallucinated answers.
*   **Code Pattern:**
    ```python
    # A simplified RAG retrieval call
    response = rag.retrieval_query(
        text="How do I use the Flame API?",
        rag_resources=["projects/my-project/corpora/flame-docs"]
    )
    ```

### **Agent**
*   **Analogy:** **"An Employee, not just a Consultant."**
*   **What it is:** An AI that doesn't just talk, but *does* things. It can use tools, run scripts, and correct its own mistakes.
*   **Novice Perspective:** A chatbot tells you how to fix a bug; an Agent actually writes the fix, runs the test, and tries again if the test fails.

---

## 2. Model Types (The Brains)

*   **LLM (Large Language Model):** The big engine (e.g., GPT-4, Gemini) trained on the whole internet.
*   **SLM (Small Language Model):** A "mini" version designed to run on your phone or local laptop. Faster and cheaper, but less "worldly."
*   **MoE (Mixture of Experts):** A model made of several "specialists." When you ask a math question, it only wakes up the "math specialist" part of the brain to save energy and time.
*   **VLM (Vision Language Model):** An AI that can "see." You can show it a screenshot of a bug, and it can explain what's wrong.

---

## 3. Reasoning Patterns (The Thinking)

*   **CoT (Chain of Thought):** **"Show your work."** Asking the AI to explain its logic step-by-step. This drastically improves accuracy for complex math or coding.
*   **ReAct (Reason + Act):** The loop Agents use. 
    1.  **Reason:** "I need to find the file." 
    2.  **Act:** Run `ls` command. 
    3.  **Observe:** "I see the file." 
    4.  **Repeat.**

---

## 4. Modalities (The Senses)

*   **TTS (Text-to-Speech):** AI turning text into a human-sounding voice.
*   **STT (Speech-to-Text):** AI "listening" to you and typing it out (Transcription).
*   **OCR (Optical Character Recognition):** Reading text from an image or a PDF.

---

## 5. Training & Adaptation (The Learning)

*   **RLHF (Reinforcement Learning from Human Feedback):** Humans ranking AI answers to teach it "manners" and helpfulness.
*   **LoRA (Low-Rank Adaptation):** **"The Quick-Study Method."** A way to teach a model a very specific skill (like "Write Autodesk Flame scripts") without needing to retrain the whole giant model.

---

## 6. Deployment Concepts (The Safety)

*   **HITL (Human-in-the-Loop):** A system where the AI does the work, but a human must click "Approve" before anything actually happens (common in this CLI!).
*   **Evals (Evaluations):** Automated tests to see how "smart" the AI is at a specific task. If you change your code, you run Evals to make sure the AI didn't get dumber.
