# Arabic Health Literacy Checker

An AI-powered tool that fact-checks Arabic health claims — including voice notes — against trusted medical sources (WHO EMRO, UAE MOHAP), designed to counter health misinformation that spreads through forwarded messages in the Arabic-speaking world.

## Problem
Health misinformation spreads widely through Arabic-language social media and forwarded voice notes, while most existing fact-checking tools are built primarily for English content. This project targets that gap directly.

## How it works (planned architecture)
1. **Input** — Arabic text or a voice note
2. **Transcription** — Whisper converts voice notes to text
3. **Claim extraction** — an LLM identifies the specific health claim(s) in the text
4. **Fact-checking (RAG)** — each claim is checked against a library of trusted Arabic health sources
5. **Verdict** — a risk-graded, plain-language result with citations

## Tech stack
- Python
- Anthropic/OpenAI API (LLM)
- ChromaDB (vector search)
- Whisper (speech-to-text)
- Streamlit (web interface)
- Deployed on Hugging Face Spaces

## Setup
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # then add your real API key
```

## Project structure
```
src/            → main source code
data/sources/   → trusted reference documents (WHO, MOHAP, etc.)
notebooks/      → quick experiments before code moves into src/
```
