# 🩺 بَيِّنة (Bayyinah Health)

**An AI-powered Arabic Health Literacy Checker that verifies health claims using Retrieval-Augmented Generation (RAG) grounded in trusted medical evidence.**

Bayyinah helps users verify Arabic health information—whether written text or voice notes—against trusted sources such as **WHO EMRO** and the **UAE Ministry of Health and Prevention (MOHAP)**. The system is designed to combat the spread of health misinformation in Arabic-speaking communities by providing transparent, evidence-based explanations instead of unsupported AI opinions.

> **Live Demo:** *https://arabic-health-checker-c9c6j9j9fbgpavhwuk3dg5.streamlit.app/checker*

---

# Why Bayyinah?

Health misinformation spreads rapidly across social media and messaging platforms, particularly through **forwarded WhatsApp messages and voice notes**. While numerous fact-checking systems exist for English, few support Arabic, and even fewer can process spoken content.

Bayyinah addresses this gap by combining modern language models with a Retrieval-Augmented Generation (RAG) pipeline that grounds every response in trusted medical references.

Rather than generating answers from the language model's internal knowledge, Bayyinah retrieves relevant evidence first and generates verdicts only from those sources.

---

# Features

- ✅ Arabic text verification
- 🎙️ Arabic voice note verification using Whisper
- 🔍 Automatic extraction of multiple health claims from a single message
- 📚 Evidence retrieval from WHO EMRO and UAE MOHAP documents
- ⚖️ Evidence-grounded verdict generation using Claude
- 🚦 Risk-level assessment (Low • Medium • High)
- 📖 Transparent explanations with cited medical sources
- ❓ Honest uncertainty — returns *"معلومات غير كافية"* when evidence is insufficient instead of guessing
---

# System Architecture

```text
                    Arabic Text / Voice Note
                              │
                              ▼
                 Whisper Speech-to-Text (Voice)
                              │
                              ▼
                  Claim Extraction (Claude)
                              │
                              ▼
             Embedding Generation (MiniLM)
                              │
                              ▼
          ChromaDB Vector Search (WHO/MOHAP)
                              │
                              ▼
           Evidence-Grounded Verdict (Claude)
                              │
                              ▼
      Verdict • Explanation • Risk • Evidence Links
```

The pipeline follows a **retrieval-first philosophy**.

If relevant evidence cannot be found, Bayyinah explicitly reports:

> **معلومات غير كافية** *(Insufficient Information)*

instead of forcing an unsupported answer.

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| User Interface | Streamlit |
| Large Language Model | Claude (Anthropic API) |
| Speech Recognition | OpenAI Whisper |
| Embeddings | paraphrase-multilingual-MiniLM-L12-v2 |
| Vector Database | ChromaDB |
| Retrieval Method | Retrieval-Augmented Generation (RAG) |
| Deployment | Hugging Face Spaces |

---

# Project Structure

```
Arabic-Health-Checker/
│
├── app.py                     # Streamlit entry point
│
├── src/
|   ├── build_index.py
|   ├── test_connection.py
│   ├── extract_claims.py
│   ├── retrieve.py
│   ├── generate_verdict.py
│   ├── transcribe.py
│   └── pipeline.py
│
├── views/
│   ├── home.py
│   └── checker.py
│
├── ui/
│   ├── components.py
│   └── styles.py
│
├── assets/
│   └── bayyinah_logo.png
│
├── data/
│   └── sources/
│
├── chroma_db/
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Bayyinah-Health.git
cd Bayyinah-Health
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create your environment variables

```bash
cp .env.example .env
```

Add your Anthropic API key to `.env`

Run the application

```bash
streamlit run app.py
```

---

# Current Knowledge Base

The prototype currently indexes trusted documents covering:

- Diabetes
- Cardiovascular Diseases
- Cancer
- Asthma
- Influenza
- Nutrition

Additional medical topics can be added by indexing new trusted documents into the ChromaDB vector database.

---

# Design Principles

Bayyinah was designed around four principles:

- **Evidence before generation** — retrieve trusted sources first.
- **No hallucinations** — never fabricate supporting evidence.
- **Explainability** — every verdict includes a human-readable explanation.
- **Transparency** — uncertainty is explicitly communicated.

---

# Limitations

- Whisper transcription quality depends on audio clarity and Arabic dialect.
- The current knowledge base covers only a subset of medical topics.
- Retrieval quality depends on the available indexed documents.
- Bayyinah is an educational fact-checking tool and does **not** replace professional medical advice.

---

# Future Work

- [ ] Expand the medical knowledge base
- [ ] Support additional trusted health organizations
- [ ] WhatsApp integration for real-world deployment
- [ ] Automatic citation links to original WHO/MOHAP pages
- [ ] Multilingual support
- [ ] Evaluation using public Arabic health misinformation datasets

---

# Privacy

Bayyinah does not collect, store, or retain user health information.

All indexed documents originate from publicly available official health organizations. User inputs are processed only for verification and are not permanently stored.

---

# License

This project is released under the MIT License.

---

## Acknowledgements

- World Health Organization (WHO EMRO)
- UAE Ministry of Health and Prevention (MOHAP)
- Anthropic Claude API
- OpenAI Whisper
- Sentence Transformers
- ChromaDB
