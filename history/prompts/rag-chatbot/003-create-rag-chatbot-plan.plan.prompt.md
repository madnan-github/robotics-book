---
id: 3
title: Create RAG Chatbot Plan
stage: plan
date: 2025-12-16
surface: agent
model: claude-opus-4-5-20251101
feature: rag-chatbot
branch: 001-rag-chatbot
user: ruser
command: /sp.plan
labels: [plan, rag, chatbot, ai, architecture]
links:
  spec: specs/001-rag-chatbot/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-rag-chatbot/plan.md
 - specs/001-rag-chatbot/research.md
 - specs/001-rag-chatbot/data-model.md
 - specs/001-rag-chatbot/quickstart.md
 - specs/001-rag-chatbot/contracts/api-contracts.md
tests:
 - none
---

## Prompt

```text
Goal:
Plan the end-to-end implementation of the Integrated RAG Chatbot backend for the
"Physical AI & Humanoid Robotics Learning" project, from local setup to production deployment.

Plan Must Define:
- Logical backend architecture
- `backend/` folder and file structure
- RAG pipeline flow (ingest → embed → retrieve → generate)
- Agent design using OpenAI Agents / ChatKit SDK
- FastAPI endpoint contracts
- Local testing and Hugging Face deployment steps
- End-to-end validation checklist

Implementation Phases:
1. Foundation
   - Create separate Git branch
   - Initialize FastAPI app
   - Load config from `.env`
   - Set up `backend/` structure

2. Ingestion & Indexing
   - Extract book content
   - Chunk and embed using Cohere
   - Store vectors in Qdrant Cloud

3. RAG & Agent
   - Configure Gemini model
   - Implement full-book and selected-text-only retrieval
   - Enforce refusal when context is missing

4. Persistence
   - Design Neon Postgres schema
   - Store chat sessions and retrieval metadata

5. API Layer
   - Implement async endpoints:
     - /chat
     - /chat/selected-text
     - /health
   - Enable CORS for Vercel frontend

6. Testing & Deployment
   - Test locally
   - Deploy backend on Hugging Face
   - Verify frontend (Vercel) integration

Decisions to Document:
- Chunk size and overlap
- Top-k retrieval
- Selected-text enforcement logic
- Gemini configuration
- Qdrant and Neon schema design

Validation Strategy:
- Health checks
- Correct answer from known passages
- Out-of-scope refusal
- Selected-text-only enforcement
- Local vs deployed parity

Non-Goals:
- Fine-tuning
- Web search
- Frontend changes
```

## Response snapshot

Created comprehensive implementation plan for the RAG Chatbot with technical context, constitution check, and project structure. Generated research.md with decisions on chunk size (512-token with 64-token overlap), top-k retrieval (5 for full-book, 3 for selected-text), selected-text enforcement logic, Gemini configuration, and schema designs. Created data-model.md with 5 entities (Book Content, User Query, Retrieved Context, Generated Response, Chat Session, Book Metadata). Generated API contracts for /chat, /chat/selected-text, and /health endpoints. Created quickstart.md with setup instructions and example usage.

## Outcome

- ✅ Impact: Complete implementation plan with architecture, data models, and API contracts
- 🧪 Tests: none
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, contracts/api-contracts.md
- 🔁 Next prompts: Ready for task generation with `/sp.tasks`
- 🧠 Reflection: Plan aligns with constitution requirements and defines clear implementation path

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): not applicable
- Prompt variant (if applicable): not applicable
- Next experiment (smallest change to try): proceed with task generation