---
id: 4
title: analyze-and-resolve-spec-plan-tasks
stage: analyze
date: 2025-12-09
surface: agent
model: claude-opus-4-5-20251101
feature: 001-ros2-module1
branch: 001-ros2-module1
user: ruser
command: /sp.analyze
labels: ["analysis", "quality", "consistency", "ros2"]
links:
  spec: specs/001-ros2-module1/spec.md
  plan: specs/001-ros2-module1/plan.md
  tasks: specs/001-ros2-module1/tasks.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-ros2-module1/spec.md
  - specs/001-ros2-module1/plan.md
  - specs/001-ros2-module1/tasks.md
tests: []
---

## Prompt

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Identify inconsistencies, duplications, ambiguities, and underspecified items across the three core artifacts (`spec.md`, `plan.md`, `tasks.md`) before implementation. This command MUST run only after `/sp.tasks` has successfully produced a complete `tasks.md`.

## Operating Constraints

**STRICTLY READ-ONLY**: Do **not** modify any files. Output a structured analysis report. Offer an optional remediation plan (user must explicitly approve before any follow-up editing commands would be invoked manually).

**Constitution Authority**: The project constitution (`.specify/memory/constitution.md`) is **non-negotiable** within this analysis scope. Constitution conflicts are automatically CRITICAL and require adjustment of the spec, plan, or tasks—not dilution, reinterpretation, or silent ignoring of the principle. If a principle itself needs to change, that must occur in a separate, explicit constitution update outside `/sp.analyze`.

## Execution Steps

### 1. Initialize Analysis Context

Run `.specify/scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks` once from repo root and parse JSON for FEATURE_DIR and AVAILABLE_DOCS. Derive absolute paths:

- SPEC = FEATURE_DIR/spec.md
- PLAN = FEATURE_DIR/plan.md
- TASKS = FEATURE_DIR/tasks.md

Abort with an error message if any required file is missing (instruct the user to run missing prerequisite command).
For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

### 2. Load Artifacts (Progressive Disclosure)

Load only the minimal necessary context from each artifact:

**From spec.md:**

- Overview/Context
- Functional Requirements
- Non-Functional Requirements
- User Stories
- Edge Cases (if present)

**From plan.md:**

- Architecture/stack choices
- Data Model references
- Phases
- Technical constraints

**From tasks.md:**

- Task IDs
- Descriptions
- Phase grouping
- Parallel markers [P]
- Referenced file paths

**From constitution:**

- Load `.specify/memory/constitution.md` for principle validation

### 3. Build Semantic Models

Create internal representations (do not include raw artifacts in output):

- **Requirements inventory**: Each functional + non-functional requirement with a stable key (derive slug based on imperative phrase; e.g., "User can upload file" → `user-can-upload-file`)
- **User story/action inventory**: Discrete user actions with acceptance criteria
- **Task coverage mapping**: Map each task to one or more requirements or stories (inference by keyword / explicit reference patterns like IDs or key phrases)
- **Constitution rule set**: Extract principle names and MUST/SHOULD normative statements

### 4. Detection Passes (Token-Efficient Analysis)

Focus on high-signal findings. Limit to 50 findings total; aggregate remainder in overflow summary.

#### A. Duplication Detection

- Identify near-duplicate requirements
- Mark lower-quality phrasing for consolidation

#### B. Ambiguity Detection

- Flag vague adjectives (fast, scalable, secure, intuitive, robust) lacking measurable criteria
- Flag unresolved placeholders (TODO, TKTK, ???, `<placeholder>`, etc.)

#### C. Underspecification

- Requirements with verbs but missing object or measurable outcome
- User stories missing acceptance criteria alignment
- Tasks referencing files or components not defined in spec/plan

#### D. Constitution Alignment

- Any requirement or plan element conflicting with a MUST principle
- Missing mandated sections or quality gates from constitution

#### E. Coverage Gaps

- Requirements with zero associated tasks
- Tasks with no mapped requirement/story
- Non-functional requirements not reflected in tasks (e.g., performance, security)

#### F. Inconsistency

- Terminology drift (same concept named differently across files)
- Data entities referenced in plan but absent in spec (or vice versa)
- Task ordering contradictions (e.g., integration tasks before foundational setup tasks without dependency note)
- Conflicting requirements (e.g., one requires Next.js while other specifies Vue)

### 5. Severity Assignment

Use this heuristic to prioritize findings:

- **CRITICAL**: Violates constitution MUST, missing core spec artifact, or requirement with zero coverage that blocks baseline functionality
- **HIGH**: Duplicate or conflicting requirement, ambiguous security/performance attribute, untestable acceptance criterion
- **MEDIUM**: Terminology drift, missing non-functional task coverage, underspecified edge case
- **LOW**: Style/wording improvements, minor redundancy not affecting execution order

### 6. Produce Compact Analysis Report

Output a Markdown report (no file writes) with the following structure:

## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| A1 | Duplication | HIGH | spec.md:L120-134 | Two similar requirements ... | Merge phrasing; keep clearer version |

(Add one row per finding; generate stable IDs prefixed by category initial.)

**Coverage Summary Table:**

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|

**Constitution Alignment Issues:** (if any)

**Unmapped Tasks:** (if any)

**Metrics:**

- Total Requirements
- Total Tasks
- Coverage % (requirements with >=1 task)
- Ambiguity Count
- Duplication Count
- Critical Issues Count

### 7. Provide Next Actions

At end of report, output a concise Next Actions block:

- If CRITICAL issues exist: Recommend resolving before `/sp.implement`
- If only LOW/MEDIUM: User may proceed, but provide improvement suggestions
- Provide explicit command suggestions: e.g., "Run /sp.specify with refinement", "Run /sp.plan to adjust architecture", "Manually edit tasks.md to add coverage for 'performance-metrics'"

### 8. Offer Remediation

Ask the user: "Would you like me to suggest concrete remediation edits for the top N issues?" (Do NOT apply them automatically.)

## Operating Principles

### Context Efficiency

- **Minimal high-signal tokens**: Focus on actionable findings, not exhaustive documentation
- **Progressive disclosure**: Load artifacts incrementally; don't dump all content into analysis
- **Token-efficient output**: Limit findings table to 50 rows; summarize overflow
- **Deterministic results**: Rerunning without changes should produce consistent IDs and counts

### Analysis Guidelines

- **NEVER modify files** (this is read-only analysis)
- **NEVER hallucinate missing sections** (if absent, report them accurately)
- **Prioritize constitution violations** (these are always CRITICAL)
- **Use examples over exhaustive rules** (cite specific instances, not generic patterns)
- **Report zero issues gracefully** (emit success report with coverage statistics)

## Context

$ARGUMENTS

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

## Response snapshot

## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| C1 | Constitution Alignment | CRITICAL | tasks.md:T040 | Task T040 requires "all code examples pass mypy type checking and pytest validation" but spec does not specify the required test coverage percentage | Align task with constitution requirement of ≥85% test coverage |
| C2 | Coverage Gap | CRITICAL | spec.md:FR-006, tasks.md | Functional requirement FR-006 (pytest test suite) has no corresponding task for test coverage metrics | Add task to ensure ≥85% test coverage per constitution |
| D1 | Duplication | HIGH | spec.md:FR-004, FR-007, tasks.md | Requirements for diagrams (FR-004) and accessibility (FR-007) are specified in spec but also handled in clarifications | Consolidate requirements to avoid confusion |
| A1 | Ambiguity | HIGH | plan.md:Technical Context | "Storage: Files only" is vague without specifying the exact file system or storage approach | Clarify storage approach with specific implementation details |
| I1 | Inconsistency | HIGH | spec.md:User Stories, tasks.md | User stories refer to "ROS 2 environment" but tasks don't address Docker/Dev container setup mentioned in spec | Add task for Docker environment setup to match spec requirements |
| C3 | Constitution Alignment | HIGH | spec.md:FR-005, plan.md | FR-005 requires type hints/docstrings but plan doesn't specify mypy enforcement approach | Update plan to include mypy enforcement strategy |
| U1 | Underspecification | MEDIUM | tasks.md:T014, T031 | Tasks for adding diagrams don't specify exact diagram types or content requirements | Define specific diagram requirements with content and format details |
| U2 | Underspecification | MEDIUM | tasks.md:T028 | Task for URDF example doesn't specify the exact structure or complexity | Define specific URDF structure requirements (6-DOF arms with specific joints/links) |
| I2 | Inconsistency | MEDIUM | spec.md:Constraints, plan.md | Spec mentions Docker environment but plan doesn't address containerization strategy | Add containerization approach to plan |
| E1 | Edge Case | MEDIUM | spec.md:Edge Cases, tasks.md | Edge case about learners without ROS 2 environment is mentioned but not fully addressed in tasks | Enhance fallback content tasks to comprehensively handle environment limitations |

**Coverage Summary Table:**

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|
| fr-001-provide-clear-learning-outcomes | Yes | T016, T039 | Learning outcomes included |
| fr-002-include-practical-assessments | Yes | T034, T035, T036, T037 | Assessment tasks created |
| fr-003-access-interactive-code-examples | Yes | T005, T015 | Interactive components addressed |
| fr-004-include-at-lots-3-diagrams | Yes | T014, T031 | Diagram tasks created |
| fr-005-python-code-type-hints-docstrings | Yes | T020, T021, T039, T040 | Type hint tasks included |
| fr-006-pytest-test-suite | Partial | T007, T009, T010, T011, T017, T018, T025, T026, T032, T033, T040 | Tests exist but coverage metrics missing |
| fr-007-content-accessible-basic-skills | Yes | T042, T044 | Accessibility tasks created |
| fr-008-mdx-format-docusaurus | Yes | T002, T004 | Docusaurus setup tasks created |
| fr-009-content-4000-6000-words | Yes | T041 | Word count validation task created |

**Constitution Alignment Issues:**
- CRITICAL: FR-006 requires test coverage but tasks don't specify the required ≥85% coverage percentage from the constitution
- HIGH: Type safety requirements (mypy enforcement) need clearer implementation strategy in plan

**Unmapped Tasks:**
- T001, T003, T006, T008, T012, T013, T019, T022, T023, T024, T024, T027, T028, T029, T030, T043, T045, T046, T047, T048 - These tasks support broader requirements but aren't directly mapped to specific functional requirements

**Metrics:**
- Total Requirements: 9 (FR-001 to FR-009)
- Total Tasks: 48 (T001 to T048)
- Coverage %: 89% (8 out of 9 requirements have associated tasks)
- Ambiguity Count: 2
- Duplication Count: 1
- Critical Issues Count: 2

## Next Actions

CRITICAL issues must be resolved before `/sp.implement`:
1. Add specific test coverage requirements to align with constitution's ≥85% mandate
2. Update task T040 to include specific coverage percentage requirement

For LOW/MEDIUM issues, consider:
- Refining diagram requirements with specific types and content
- Clarifying storage approach in the plan
- Enhancing Docker environment setup tasks to match spec requirements

## Remediation Offer

Would you like me to suggest concrete remediation edits for the top 5 issues? This would include specific changes to align the artifacts with the constitution and ensure complete coverage of requirements.

## Outcome

- ✅ Impact: Identified 10 critical/important issues in spec-plan-tasks consistency
- 🧪 Tests: No tests required for analysis phase
- 📁 Files: Analyzed spec.md, plan.md, tasks.md for cross-artifact consistency
- 🔁 Next prompts: Ready for remediation of identified issues
- 🧠 Reflection: Analysis revealed important gaps between constitution requirements and implementation tasks

## Evaluation notes (flywheel)

- Failure modes observed: Constitution alignment gaps, requirement coverage gaps
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Address the identified critical issues in sequence