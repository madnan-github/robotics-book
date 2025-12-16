<!--
Sync Impact Report:
Version change: N/A -> 1.0.0
Modified principles: None (new project constitution)
Added sections: All principles and sections for the RAG chatbot project
Removed sections: None
Templates requiring updates:
  - ✅ plan-template.md - Confirmed alignment with new principles
  - ✅ spec-template.md - Confirmed alignment with new principles
  - ✅ tasks-template.md - Confirmed alignment with new principles
Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics Learning RAG Chatbot Constitution

## Core Principles

### I. Production-Ready Backend Architecture
All backend code MUST be organized within the `backend/` directory. The system MUST use FastAPI for API endpoints to ensure high performance and automatic API documentation. This ensures clean separation of concerns and maintainable code organization.

### II. Strict Technology Stack Compliance
The system MUST use OpenAI Agents SDK / ChatKit SDK for agent functionality, Gemini model for text generation, Cohere for embeddings, Qdrant Cloud (Free Tier) for vector storage, and Neon Serverless Postgres for relational storage. This ensures compatibility with project requirements and deployment constraints.

### III. Security-First Approach (NON-NEGOTIABLE)
ALL credentials and secrets MUST be stored in `.env` files with NO hardcoded secrets anywhere in the codebase. This protects sensitive information and enables secure deployment across environments.

### IV. RAG Pipeline Excellence
The system MUST implement a robust RAG pipeline with full-book and user-selected-text-only retrieval capabilities. The pipeline must refuse answers when context is missing or out of scope, ensuring reliable and accurate responses based only on book content.

### V. API Standardization
The system MUST expose async FastAPI endpoints at `/chat`, `/chat/selected-text`, and `/health` with consistent error handling and response formats. This ensures standardized interfaces for frontend integration.

### VI. Zero Trust Architecture
No external data sources beyond the book content are allowed. No fine-tuning, web search, or external data integration is permitted. This maintains the integrity of the RAG system's knowledge boundaries.

## Technical Constraints and Standards
Technology stack requirements: FastAPI, OpenAI Agents SDK, Gemini, Cohere, Qdrant Cloud, Neon Postgres. Deployment must occur on Hugging Face for backend with Vercel frontend integration. Local testing is mandatory before deployment.

## Development Workflow and Quality Gates
All features must be tested locally before deployment. Code reviews must verify compliance with technology stack and security requirements. System integration testing required to validate end-to-end functionality between frontend and backend.

## Governance
Constitution supersedes all other practices. All PRs/reviews must verify compliance with technology stack and security requirements. Complexity must be justified with clear performance or reliability benefits.

**Version**: 1.0.0 | **Ratified**: 2025-12-16 | **Last Amended**: 2025-12-16
