# Project Context for Claude Code

## What this project is
An Arabic Health Literacy Checker — an AI tool that fact-checks Arabic health claims (including voice notes) against trusted medical sources (WHO EMRO, UAE MOHAP), using a RAG (retrieval-augmented generation) pipeline. Final product: a Streamlit web app deployed on Hugging Face Spaces.

## Who's building this
A beginner in AI/ML and software engineering (Biomedical Informatics student). This project is being built specifically to **learn** RAG, NLP, and deployment — not just to get a finished product. That changes how you should help.

## How I want you to work with me

- **Explain before you build.** Before writing a new piece of functionality, briefly explain the concept and the approach in plain language, then write the code.
- **Prefer simple, readable code over clever/optimized code.** I'd rather understand every line than have the most efficient version.
- **Go step by step, not all at once.** Don't build the entire pipeline in one shot — implement one function or one small piece at a time, so I can follow along and test as we go.
- **Ask before big changes.** If a task requires touching many files or restructuring things significantly, tell me your plan first and wait for confirmation.
- **Comment the code** with short explanations of *why*, not just *what*.
- **When something fails**, explain what went wrong in plain terms before fixing it — don't just silently patch it.
- **No unnecessary dependencies.** Stick to the stack already defined in `requirements.txt` unless there's a good reason to add something, and explain that reason if you do.

## Tech stack
- Python
- Anthropic (or OpenAI) API for the LLM
- ChromaDB for vector search
- Whisper for speech-to-text (Arabic voice notes)
- Streamlit for the web interface
- Deployment target: Hugging Face Spaces

## Project structure
```
src/            → main source code
data/sources/   → trusted reference documents (WHO, MOHAP, etc.)
notebooks/      → quick experiments before code moves into src/
```

## Data & privacy
All data used is public (official health sources, self-written test examples). No private or sensitive user data at any stage — keep it that way.