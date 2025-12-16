---
id: 1
title: Update Constitution
stage: constitution
date: 2025-12-16
surface: agent
model: claude-opus-4-5-20251101
feature: none
branch: master
user: ruser
command: /sp.constitution
labels: [constitution, setup, project]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
Project: Physical AI & Humanoid Robotics Learning – Step 2 (Integrated RAG Chatbot)

Objective:
Step 1 (Creating text Book - Completed), include:
Build a production-ready RAG chatbot embedded in the Docusaurus book that answers questions strictly from the book content, including user-selected-text-only answers.

Scope & Constraints:
- All backend code MUST be inside `backend/`
- FastAPI MUST be used
- OpenAI Agents SDK / ChatKit SDK MUST be used
- Gemini model MUST be used for generation
- Cohere MUST be used for embeddings
- Qdrant Cloud (Free Tier) MUST be used for vector storage
- Neon Serverless Postgres MUST be used for relational storage
- ALL credentials and secrets MUST be stored in `.env`
- No hardcoded secrets
- Context7 documentation is available

Core Requirements:
1. Index full book content into Qdrant using Cohere embeddings
2. Implement RAG pipeline (retrieve → generate)
3. Support:
   - Full-book retrieval
   - Strict user-selected-text-only retrieval
4. Expose async FastAPI endpoints:
   - /chat
   - /chat/selected-text
   - /health
5. Refuse answers when context is missing or out of scope
6. Enable CORS for frontend access

Deployment & Validation:
- Project MUST run and be tested locally first
- Backend MUST be deployed on Hugging Face
- Frontend is already deployed on Vercel
- Final delivery MUST be a fully working, end-to-end integrated system

Non-Goals:
- No fine-tuning
- No web search
- No external data beyond the book
```

## Response snapshot

Updated the project constitution to reflect the requirements for the Physical AI & Humanoid Robotics Learning RAG Chatbot project. The new constitution includes six core principles that enforce the required technology stack, security practices, and architectural decisions specified in the user requirements. The constitution now mandates FastAPI, OpenAI Agents SDK, Gemini, Cohere, Qdrant Cloud, Neon Postgres, proper secret management, and the required API endpoints. It also enforces the zero-trust architecture that restricts the system to only using book content for answers.

## Outcome

- ✅ Impact: Constitution updated to reflect RAG chatbot project requirements
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with project-specific principles
- 🔁 Next prompts: Implementation planning can now proceed with clear guidelines
- 🧠 Reflection: The new constitution provides clear guidance for all future development decisions

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): not applicable
- Prompt variant (if applicable): not applicable
- Next experiment (smallest change to try): proceed with feature specification based on new constitution