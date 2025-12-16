---
description: "Task list for RAG Chatbot for Physical AI & Humanoid Robotics Learning"
---

# Tasks: RAG Chatbot for Physical AI & Humanoid Robotics Learning

**Input**: Design documents from `/specs/001-rag-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create backend directory structure per implementation plan
- [X] T002 [P] Initialize Python project with requirements.txt containing FastAPI, Google Generative AI, Cohere, Qdrant, Neon Postgres, Pydantic, pytest dependencies
- [X] T003 Create .env file with placeholder for API keys (gitignored)
- [X] T004 Create .gitignore file with proper exclusions including .env, __pycache__, etc.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T005 Create configuration management in backend/config/settings.py using Pydantic BaseSettings
- [X] T006 Create database connection setup in backend/config/database.py for Neon Postgres
- [X] T007 [P] Set up Qdrant client connection in backend/core/database.py
- [X] T008 Create CORS middleware setup in backend/main.py
- [X] T009 Create main FastAPI application instance in backend/main.py
- [X] T010 Create constants file in backend/core/constants.py for application constants
- [X] T011 Create security utilities in backend/core/security.py
- [X] T012 [P] Create book content extraction utility in backend/core/content_extraction.py
- [X] T013 Create book indexing pipeline in backend/services/indexing_service.py to load content into Qdrant
- [X] T014 Implement agent service using OpenAI Agents SDK in backend/services/agent_service.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Book Content Question Answering (Priority: P1) 🎯 MVP

**Goal**: Learners can ask questions about the book content and receive accurate answers based on the book's information, with the system refusing answers when no relevant context exists.

**Independent Test**: A learner can ask a question about a robotics concept and receive an accurate answer based only on the book content without any hallucination.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T015 [P] [US1] Contract test for /chat endpoint in backend/tests/test_chat.py
- [ ] T016 [P] [US1] Integration test for full-book retrieval journey in backend/tests/integration/test_rag_pipeline.py

### Implementation for User Story 1

- [X] T027 [P] [US1] Create ChatSession model in backend/models/chat.py
- [X] T028 [P] [US1] Create UserQuery model in backend/models/user_query.py
- [X] T029 [P] [US1] Create RetrievedContext model in backend/models/embedding.py
- [X] T030 [P] [US1] Create GeneratedResponse model in backend/models/chat.py
- [X] T031 [US1] Create BookMetadata model in backend/models/embedding.py
- [X] T032 [US1] Create embedding service in backend/services/embedding_service.py using Cohere
- [X] T033 [US1] Create retrieval service in backend/services/retrieval_service.py using Qdrant
- [X] T034 [US1] Create generation service in backend/services/generation_service.py using Gemini
- [X] T035 [US1] Create RAG service in backend/services/rag_service.py orchestrating the pipeline
- [X] T036 [US1] Implement /chat endpoint in backend/api/routes/chat.py with full-book retrieval
- [X] T037 [US1] Add validation and error handling for /chat endpoint
- [X] T038 [US1] Implement refusal logic when no relevant context is found for /chat endpoint
- [X] T039 [US1] Add logging for user story 1 operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - User-Selected Text Mode (Priority: P2)

**Goal**: Learners can select specific text from the book and ask questions only about that selected text, receiving answers that only reference the selected text.

**Independent Test**: A learner can select text from the book, ask a question about it, and receive an answer that only references the selected text.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T040 [P] [US2] Contract test for /chat/selected-text endpoint in backend/tests/test_selected_text.py
- [ ] T041 [P] [US2] Integration test for selected-text-only retrieval journey in backend/tests/integration/test_rag_pipeline.py

### Implementation for User Story 2

- [X] T042 [P] [US2] Create SelectedText model in backend/models/user_query.py extending UserQuery
- [X] T043 [US2] Update RAG service in backend/services/rag_service.py to support selected-text-only mode
- [X] T044 [US2] Create selected-text enforcement logic in backend/services/retrieval_service.py
- [X] T045 [US2] Implement /chat/selected-text endpoint in backend/api/routes/selected_text.py
- [X] T046 [US2] Add validation and error handling for /chat/selected-text endpoint
- [X] T047 [US2] Implement refusal logic when no relevant context is found in selected text
- [X] T048 [US2] Add logging for user story 2 operations

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - System Health and Availability (Priority: P3)

**Goal**: System administrators and users can verify that the RAG chatbot is operational and ready to process requests.

**Independent Test**: An admin or user can check the health endpoint and receive confirmation that the system is running properly.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T049 [P] [US3] Contract test for /health endpoint in backend/tests/test_health.py
- [ ] T050 [P] [US3] Integration test for health check dependencies in backend/tests/integration/test_rag_pipeline.py

### Implementation for User Story 3

- [X] T051 [P] [US3] Create HealthCheck model in backend/models/chat.py
- [X] T052 [US3] Implement /health endpoint in backend/api/routes/health.py
- [X] T053 [US3] Add dependency health checks (Qdrant, Gemini, Cohere, Neon) to health endpoint
- [X] T054 [US3] Add logging for user story 3 operations

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T055 [P] Documentation updates in backend/README.md with API usage examples
- [ ] T056 Code cleanup and refactoring
- [ ] T057 Performance optimization across all stories
- [ ] T058 [P] Additional unit tests (if requested) in backend/tests/
- [ ] T059 Security hardening
- [ ] T060 Run quickstart.md validation
- [ ] T061 Add performance validation framework to measure response times
- [ ] T062 Create load testing script to validate <5s response time for 90% of requests
- [ ] T063 Add accuracy testing framework to validate 95% answer accuracy from book content
- [ ] T064 Implement error handling for Qdrant unavailability with graceful fallbacks
- [ ] T065 Add handling for ambiguous or general queries with appropriate responses

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for /chat endpoint in backend/tests/test_chat.py"
Task: "Integration test for full-book retrieval journey in backend/tests/integration/test_rag_pipeline.py"

# Launch all models for User Story 1 together:
Task: "Create ChatSession model in backend/models/chat.py"
Task: "Create UserQuery model in backend/models/user_query.py"
Task: "Create RetrievedContext model in backend/models/embedding.py"
Task: "Create GeneratedResponse model in backend/models/chat.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence