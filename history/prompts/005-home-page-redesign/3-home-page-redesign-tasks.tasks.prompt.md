---
id: 3
title: home-page-redesign-tasks
stage: tasks
date: '2025-12-11'
surface: agent
model: claude-opus-4-5-20251101
feature: 005-home-page-redesign
branch: 005-home-page-redesign
user: ruser
command: /sp.tasks
labels:
  - tasks
  - home-page
  - docusaurus
  - ui
links:
  SPEC: /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/spec.md
  PLAN: /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/plan.md
  TICKET: 'null'
  ADR: 'null'
  PR: 'null'
files:
  - /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/tasks.md
tests: []
---

---
description: "Task list for home page redesign implementation"
---

# Tasks: Home Page Redesign

**Input**: Design documents from `/specs/005-home-page-redesign/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Docusaurus project**: `src/`, `docs/`, `static/` at repository root
- **Components**: `src/components/`
- **Pages**: `src/pages/`
- **CSS**: `src/css/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan
- [ ] T002 [P] Set up development environment with Node.js and Docusaurus
- [ ] T003 [P] Verify existing Docusaurus installation and dependencies

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Create custom home page directory structure
- [ ] T005 Set up static assets directory for module images
- [ ] T006 Configure Docusaurus for custom home page implementation

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Fix Home Page Access (Priority: P1) 🎯 MVP

**Goal**: Fix the "Page Not Found" error on the home page so users can access the content

**Independent Test**: Can visit the home page URL and see content instead of a 404 error

### Implementation for User Story 1

- [ ] T007 [P] [US1] Create custom home page component at src/pages/index.js
- [ ] T008 [US1] Configure Docusaurus to use custom home page instead of default
- [ ] T009 [US1] Test home page access locally to ensure no "Page Not Found" error
- [ ] T010 [US1] Verify home page loads without errors in development server

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Display Engaging Home Page Content (Priority: P1)

**Goal**: Display the main heading "Physical AI & Humanoid Robotics Learning" and a 6-7 line descriptive paragraph

**Independent Test**: Visit the home page and verify the heading and paragraph are displayed as specified

### Implementation for User Story 2

- [ ] T011 [P] [US2] Create HomepageHeader component at src/components/HomepageHeader/index.js
- [ ] T012 [US2] Implement main heading "Physical AI & Humanoid Robotics Learning" in the header component
- [ ] T013 [US2] Add 6-7 line descriptive paragraph about Physical AI & Humanoid Robotics Learning
- [ ] T014 [US2] Integrate HomepageHeader component into the custom home page
- [ ] T015 [US2] Apply basic styling to the heading and paragraph for visual appeal

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Enable Navigation to Learning Content (Priority: P1)

**Goal**: Create a "Getting Start" button that routes users to the textbook getting started section

**Independent Test**: Click the "Getting Start" button and verify it navigates to the correct section

### Implementation for User Story 3

- [ ] T016 [P] [US3] Create GetStartedButton component at src/components/GetStartedButton/index.js
- [ ] T017 [US3] Implement button with text "Getting Start" using Docusaurus Link component
- [ ] T018 [US3] Set button destination to textbook getting started section
- [ ] T019 [US3] Integrate GetStartedButton component into the custom home page
- [ ] T020 [US3] Test button functionality to ensure proper navigation

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Browse Learning Modules via Cards (Priority: P2)

**Goal**: Display 4 cards containing module names, descriptions, and relevant images

**Independent Test**: View the 4 module cards and verify each contains a module name, description, and relevant image

### Implementation for User Story 4

- [ ] T021 [P] [US4] Create HomepageFeatures component at src/components/HomepageFeatures/index.js
- [ ] T022 [P] [US4] Prepare module images for Module 1, 2, 3, and 4 in static/img/
- [ ] T023 [US4] Implement card layout with 4 module cards in HomepageFeatures component
- [ ] T024 [US4] Add module names to each card
- [ ] T025 [US4] Add module descriptions to each card
- [ ] T026 [US4] Add relevant images to each card
- [ ] T027 [US4] Integrate HomepageFeatures component into the custom home page
- [ ] T028 [US4] Implement responsive design for the module cards
- [ ] T029 [US4] Test that all 4 cards display correctly with images, names, and descriptions

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T030 [P] Apply consistent styling across all home page elements
- [ ] T031 [P] Ensure responsive design works on mobile, tablet, and desktop
- [ ] T032 [P] Optimize image loading and add appropriate alt text for accessibility
- [ ] T033 [P] Test page load time and optimize if needed to stay under 3 seconds
- [ ] T034 [P] Test all functionality on local development server
- [ ] T035 [P] Update documentation to reflect new home page structure
- [ ] T036 Run quickstart.md validation to ensure deployment works correctly

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
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Depends on US1 (needs working home page)
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - Depends on US1 (needs working home page)
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 (needs working home page)

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 4

```bash
# Launch all components for User Story 4 together:
Task: "Create HomepageFeatures component at src/components/HomepageFeatures/index.js"
Task: "Prepare module images for Module 1, 2, 3, and 4 in static/img/"
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
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence