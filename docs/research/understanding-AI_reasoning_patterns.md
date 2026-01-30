# Understanding AI Reasoning Patterns

How an AI "thinks" depends on the instructions we give it. Just like a human, an AI is more accurate when it takes its time and follows a logical process.

---

## 1. CoT (Chain of Thought)
**"Show Your Work"**

*   **What it is:** Forcing the AI to write out its step-by-step logic *before* giving the final answer.
*   **Why it matters:** LLMs are "prediction engines." If they jump straight to the answer, they often guess wrong. If they walk through the logic, they catch their own errors.
*   **Analogy:** **A Math Student.** A student who writes down every step of an equation is much less likely to make a mistake than one who tries to do it all in their head.

## 2. ReAct (Reason + Act)
**The Agent's Heartbeat**

*   **What it is:** A loop where the AI **Reasons** about its situation, takes an **Action** (using a tool), and then **Observes** the result before deciding what to do next.
*   **Simple Logic:**
    1.  **Thought:** I need to know the current Flame project name.
    2.  **Action:** Run `print_project_name.py`.
    3.  **Observation:** The script output "Commercial_Project_v2".
    4.  **Final Thought:** The project is "Commercial_Project_v2".

## 3. Zero-Shot vs. Few-Shot
**Learning on the Fly**

*   **Zero-Shot:** Asking the AI to do something without giving it any examples. 
    *   *Example:* "Translate 'Hello' to French."
*   **Few-Shot:** Giving the AI 2 or 3 examples of how you want the task done before asking it to perform.
    *   **Analogy:** **Training a New Intern.** You don't just say "Do the filing." You show them two folders you've already filed so they understand your specific system.
    *   **Simple Prompt:**
        ```text
        Input: "The movie was great!" -> Sentiment: Positive
        Input: "I hated the food." -> Sentiment: Negative
        Input: "The service was okay." -> Sentiment: 
        ```

## 4. Multi-Hop Reasoning
**Connecting the Dots**

*   **What it is:** Solving a problem that requires finding Answer A, then using Answer A to find Answer B.
*   **Example:** "Who is the CEO of the company that made the first movie John Doe starred in?"
    1.  Hop 1: Find John Doe's first movie.
    2.  Hop 2: Find the company that made it.
    3.  Hop 3: Find that company's CEO.
