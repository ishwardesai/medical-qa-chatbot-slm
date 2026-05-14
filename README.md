
# Medical QA Chatbot using SLM + RAG

A Medical Question Answering Chatbot built using a fine-tuned DistilBERT model, Retrieval-Augmented Generation (RAG), FAISS semantic search, and AI safety guardrails.

**Disclaimer:** This project is for educational purposes only. Always consult a qualified healthcare professional for medical advice.

---
## Screenshots

**Full UI**

![Full UI](medical-qa-chatbot-slm/screenshots/01_chatbot_ui.png)

---

**Normal Medical Answer**

![Normal Answer](medical-qa-chatbot-slm/screenshots/02_normal_answer.png)

---

**Safety Layer - Blocked Query**

![Blocked](medical-qa-chatbot-slm/screenshots/03_safety_blocked.png)

---

**Safety Layer - Emergency Flagged**

![Flagged](medical-qa-chatbot-slm/screenshots/04_safety_flagged.png)

---


---

## Architecture

| Step | Component |
|------|-----------|
| 1 | User Question |
| 2 | Safety Pre-Check |
| 3 | FAISS Semantic Retrieval |
| 4 | DistilBERT Extractive QA |
| 5 | Safety Post-Check |
| 6 | Answer + Source + Confidence Score |
---

## Features

- Semantic RAG retrieval using FAISS and SentenceTransformers
- Fine-tuned DistilBERT with 94.1% training loss reduction
- AI safety guardrails blocking dangerous queries and flagging emergencies
- Source citations on every answer
- Confidence scores on every response
- Conversational memory with session statistics
- Gradio web interface

---

## Evaluation Results

![Evaluation Results](medical-qa-chatbot-slm/results/evaluation_results.png)

| Metric | Score |
|--------|-------|
| Exact Match | 53.3% |
| Token F1 | 73.5% |
| Retrieval Accuracy | 100% |
| Training Loss Reduction | 94.1% |

---

## Safety Layer

| Type | Trigger | Response |
|------|---------|----------|
| BLOCKED | Dosage, self-harm, stop medication | Refuses and redirects to professional |
| FLAGGED | Chest pain, seizure, stroke symptoms | Answer with emergency escalation message |
| SAFE | Normal medical questions | Answer with source and confidence score |

---

---

## Quick Start

Clone the repo:
```bash
git clone https://github.com/ishwardesai/medical-qa-chatbot-slm.git
cd medical-qa-chatbot-slm
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Open in Google Colab:
Open notebooks/medical_qa_chatbot.ipynb
Runtime → Run All


Use the chatbot:
```python
chatbot = MedicalChatbot()
result = chatbot.chat("What causes a heart attack?")
print(result['answer'])
# rupture of an atherosclerotic plaque in a coronary artery
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| QA Model | DistilBERT (fine-tuned) |
| Retrieval | FAISS + SentenceTransformers |
| Embeddings | all-MiniLM-L6-v2 |
| Safety | Regex pattern matching |
| UI | Gradio |
| Training | PyTorch + AdamW |
| Evaluation | Exact Match + Token F1 |

---

## Knowledge Base

| | | |
|-|-|-|
| Hypertension | Type 2 Diabetes | Asthma |
| Myocardial Infarction | Pneumonia | Depression |
| Stroke | COPD | Sepsis |
| Parkinson's Disease | | |

---

## Model Training

- Base model: distilbert-base-uncased (66M parameters)
- Training examples: 20 medical QA pairs
- Epochs: 30
- Optimizer: AdamW (lr=3e-5, weight_decay=0.01)
- Scheduler: Linear warmup + linear decay
- Hardware: NVIDIA T4 GPU
- Training time: 20 seconds

---

## Project Background

This project is based on an SLM Systems Design Document outlining best practices for building Small Language Model systems for medical applications.

The implementation follows the document's recommended 7-step recipe:

1. Start from a pretrained SLM (DistilBERT)
2. Domain-adapt on medical text
3. Supervised Fine-Tuning on medical QA pairs
4. Add RAG with vetted medical sources
5. Add safety layer + refusal rules + red-flag escalation
6. Evaluate with medical safety benchmarks
7. Iterate on failure cases

---

## Future Work

- Expand knowledge base to 100+ medical conditions
- Add LoRA fine-tuning experiments
- Integrate real medical datasets
- Deploy to HuggingFace Spaces

---

## Disclaimer

This chatbot is built for educational and portfolio purposes only. It should never be used for actual medical diagnosis or treatment decisions. Always consult a qualified healthcare professional for medical advice.

---

