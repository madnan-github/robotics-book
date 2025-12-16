# Implementation Plan: RAG Chatbot for Physical AI & Humanoid Robotics Learning

**Branch**: `001-rag-chatbot` | **Date**: 2025-12-16 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a Retrieval-Augmented Generation (RAG) chatbot that answers questions strictly from the "Physical AI & Humanoid Robotics Learning" book content. The system will provide two query modes: full-book semantic retrieval and user-selected-text-only retrieval. The backend will be built with FastAPI, using OpenAI Agents SDK, Cohere embeddings, Qdrant vector storage, and Neon Postgres for persistence. The system will be deployed on Hugging Face with integration to the existing Vercel frontend.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, OpenAI Agents SDK / ChatKit SDK, Google Generative AI (Gemini), Cohere, Qdrant, Neon Postgres, Pydantic
**Storage**: Qdrant Cloud (vector database) for embeddings, Neon Serverless Postgres (relational database)
**Testing**: pytest for unit and integration testing
**Target Platform**: Linux server (Hugging Face Spaces)
**Project Type**: Web application (backend API)
**Performance Goals**: <5 second response time for 90% of requests, handle concurrent users
**Constraints**: Must refuse answers when no relevant context exists, all secrets in .env files, backend in `backend/` directory
**Scale/Scope**: Single book content, multiple concurrent users, production-ready

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Based on constitution file:
- ✅ Production-Ready Backend Architecture: All code in `backend/` directory, using FastAPI
- ✅ Strict Technology Stack Compliance: Using OpenAI Agents SDK, Gemini, Cohere, Qdrant Cloud, Neon Postgres
- ✅ Security-First Approach: Secrets stored in `.env` files, no hardcoded secrets
- ✅ RAG Pipeline Excellence: Full-book and selected-text retrieval with refusal when context missing
- ✅ API Standardization: Required endpoints `/chat`, `/chat/selected-text`, `/health`
- ✅ Zero Trust Architecture: Only book content, no external data sources

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── main.py                 # FastAPI application entry point
├── .env                    # Environment variables (gitignored)
├── requirements.txt        # Python dependencies
├── config/
│   ├── __init__.py
│   ├── settings.py         # Configuration management
│   └── database.py         # Database connection setup
├── models/
│   ├── __init__.py
│   ├── chat.py             # Chat-related Pydantic models
│   ├── embedding.py        # Embedding data models
│   └── user_query.py       # User query models
├── services/
│   ├── __init__.py
│   ├── embedding_service.py # Cohere embedding operations
│   ├── retrieval_service.py # Qdrant retrieval operations
│   ├── generation_service.py # Gemini generation operations
│   ├── rag_service.py      # RAG pipeline orchestration
│   └── agent_service.py    # OpenAI Agents orchestration
├── api/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── chat.py         # Chat endpoints
│   │   ├── health.py       # Health check endpoints
│   │   └── selected_text.py # Selected text endpoints
│   └── dependencies.py     # FastAPI dependencies
├── core/
│   ├── __init__.py
│   ├── database.py         # Database initialization
│   ├── security.py         # Security utilities
│   └── constants.py        # Application constants
└── tests/
    ├── __init__.py
    ├── test_chat.py        # Chat endpoint tests
    ├── test_health.py      # Health endpoint tests
    ├── test_selected_text.py # Selected text endpoint tests
    ├── conftest.py         # Test configuration
    └── integration/
        ├── __init__.py
        └── test_rag_pipeline.py # RAG pipeline integration tests
```

**Structure Decision**: Web application with dedicated backend structure. The backend contains all required components for the RAG system including configuration, models, services for each major function (embedding, retrieval, generation), API routes, and tests.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
