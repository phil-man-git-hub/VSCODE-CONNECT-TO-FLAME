# Understanding AI Deployment Concepts

Once an AI is built and trained, how do we actually "use" it in the real world? These concepts cover the bridge between the AI model and the user.

---

## 1. Inference
**The AI in Action**

*   **What it is:** The process of the AI actually running and generating an answer. When you ask a question and wait for the response, you are waiting for "Inference."
*   **Analogy:** **The Performance.** Training is like the months of rehearsal; Inference is the actual night of the play when the actors are on stage performing.

## 2. HITL (Human-in-the-Loop)
**The Safety Switch**

*   **What it is:** A workflow where the AI does most of the work, but a human must review or approve the result before it's finalized.
*   **Why it matters:** In high-stakes environments (like editing a multi-million dollar commercial in Flame), we don't want the AI making permanent changes without a human saying "Yes, that looks right."

## 3. Evals (Evaluations)
**The AI Report Card**

*   **What it is:** A set of automated tests used to measure how good an AI is at a specific task.
*   **Example:** If we update our Flame helper, we run an "Eval" that asks the AI 100 questions about the Flame API. If it gets 95 right, we know it's ready. If it only gets 60 right, we know we broke something.

## 4. Tokens & Context Window
**Memory Limits**

*   **Tokens:** Think of these as "syllables" for AI. A model doesn't see words; it sees tokens.
*   **Context Window:** The "short-term memory" of the AI. It's the maximum number of tokens the AI can "keep in its head" at one time. If your conversation or file is too long, the AI will start to "forget" the beginning.

## 5. Guardrails
**The Safety Rails**

*   **What it is:** Software that sits around the AI to make sure it doesn't say anything dangerous, leaked secrets, or hallucinate.
*   **Analogy:** **A Bouncer.** The AI might want to answer a question it shouldn't, but the Guardrail blocks the response before the user ever sees it.
