---
id: 1
title: update-project-constitution
stage: constitution
date: 2025-12-09
surface: agent
model: claude-opus-4-5-20251101
feature: none
branch: master
user: ruser
command: /sp.constitution
labels: ["constitution", "project-setup", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests: []
---

## Prompt

```text
Project Constitution: Physical AI & Humanoid Robotics Learning
1.0 Project Identity & Vision
Project Name: Physical AI & Humanoid Robotics Learning Platform
Version: 1.0.0
Status: IMMUTABLE (Hackathon Edition)

1.1 Core Mission
Build an AI-native, interactive learning platform that democratizes access to Physical AI education through a hybrid textbook-chatbot system.

1.2 Philosophical Tenets
Spec-First, AI-Augmented: No code or content without validated specifications

Pedagogy-Driven: Content structure must optimize learning outcomes

Production-Ready: Hackathon speed cannot compromise system stability

Open by Design: Architecture must support community contributions

2.0 Technical Architecture (Non-Negotiable)
2.1 Stack Requirements
text
Frontend: Docusaurus 3.x (React 18+, TypeScript 5+)
Backend: FastAPI (Python 3.12+)
Package Manager: uv (strictly enforced)
Database: Neon PostgreSQL (operational), Qdrant (vector)
Authentication: Better-Auth
Orchestration: Claude Code CLI + Spec-Kit Plus
2.2 Infrastructure Rules
All Python dependencies pinned via uv.lock

Environment variables managed through .env.production only

Vector embeddings: all-MiniLM-L6-v2 (default), configurable

API versioning: /v1/* prefix mandatory

3.0 Content & Curriculum Standards
3.1 Syllabus Structure (IMMUTABLE)
Module 1: The Robotic Nervous System (ROS 2)


Chapter 1.1: ROS 2 Architecture Fundamentals
Chapter 1.2: Nodes, Topics, and Services in Practice
Chapter 1.3: rclpy - Bridging Python Agents to ROS
Chapter 1.4: URDF for Humanoid Robotics
Assessment: Build a URDF for a 6-DOF robotic arm
Module 2: The Digital Twin (Gazebo & Unity)


Chapter 2.1: Physics Simulation Fundamentals (Gazebo)
Chapter 2.2: High-Fidelity Rendering & HRI (Unity)
Chapter 2.3: Sensor Simulation Suite (LiDAR, Depth, IMU)
Chapter 2.4: Environment Design for Humanoid Training
Assessment: Simulate sensor feedback for obstacle avoidance
Module 3: The AI-Robot Brain (NVIDIA Isaac™)


Chapter 3.1: Isaac Sim - Photorealistic Simulation
Chapter 3.2: Synthetic Data Generation for Training
Chapter 3.3: Isaac ROS - Hardware-Accelerated VSLAM
Chapter 3.4: Nav2 for Bipedal Path Planning
Assessment: Implement visual SLAM in simulated environment
Module 4: Vision-Language-Action (VLA)


Chapter 4.1: Voice-to-Action Pipelines (OpenAI Whisper)
Chapter 4.2: LLM-Based Cognitive Planning
Chapter 4.3: Natural Language to ROS Action Sequences
Chapter 4.4: Multimodal Integration Strategies
Assessment: Create "Clean the room" command pipeline
Capstone Project: The Autonomous Humanoid


Phase 1: Voice Command Processing
Phase 2: Cognitive Task Planning
Phase 3: Navigation & Obstacle Avoidance
Phase 4: Object Recognition & Manipulation
Deliverable: Complete simulation video with telemetry
3.2 Content Creation Rules
Every chapter must begin with: "## Learning Outcomes" (3-5 bullet points)

Every chapter must end with: "## Assessments" (hands-on exercises)

Code blocks: Language-tagged, executable where possible

Diagrams: Mermaid.js syntax preferred, SVG required for production

References: Academic citations in APA 7th edition format

4.0 Development Standards
4.1 Python Code (Backend)
python
# TYPE HINTS: Non-negotiable
def process_sensor_data(data: SensorReading) -> ProcessedReading:
    """Google-style docstrings required for all functions.

    Args:
        data: Raw sensor reading with timestamp and values

    Returns:
        Processed reading with noise reduction applied

    Raises:
        SensorError: If data format is invalid
    """
    # mypy compliance mandatory
    pass

# TESTING: pytest with 90%+ coverage
# STRUCTURE: src/ layout with clear separation
4.2 TypeScript/React (Frontend)
typescript
// STRICT MODE: Enabled globally
// COMPONENTS: Reusable with props interfaces
interface LearningComponentProps {
  chapterId: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  onComplete?: () => void;
}

// STATE MANAGEMENT: React Context for user progress
// STYLING: Tailwind CSS with design tokens
4.3 Database Schemas
sql
-- Users table (Better-Auth extended)
CREATE TABLE user_profiles (
    id UUID PRIMARY KEY,
    learning_style VARCHAR(50), -- 'visual', 'hands-on', 'theoretical'
    language_preference VARCHAR(10) DEFAULT 'en',
    proficiency_level INTEGER CHECK (proficiency_level BETWEEN 1 AND 5),
    personalized_pathways JSONB
);

-- Learning analytics
CREATE TABLE learning_sessions (
    session_id UUID PRIMARY KEY,
    user_id UUID REFERENCES user_profiles(id),
    chapter_completed VARCHAR(100),
    time_spent INTERVAL,
    assessment_score DECIMAL(5,2)
);
5.0 Mandatory Architectural Decisions (ADRs)
ADR-001: RAG Retrieval Logic
Decision: Hybrid retrieval with semantic + keyword search
Reason: Balances precision with recall for educational content
Implementation: Qdrant with BM25 fallback, chunk size 512 tokens

ADR-002: Urdu Translation Pipeline
Decision: Two-stage translation with human review
Stage 1: Machine translation (Google Translate API)
Stage 2: Domain-specific fine-tuning (technical terms glossary)
Quality Gate: BLEU score > 0.65 required for deployment

ADR-003: Personalization Schema
Decision: Multi-dimensional profiling
Dimensions: Learning style, pace, prior knowledge, language
Storage: JSONB column with incremental updates
Privacy: All personalization data opt-in only

6.0 Hackathon Execution Protocol
6.1 Workflow Rules
Atomic Tasks: All work decomposed to <2 hour units

Validation Gates:

Code: Unit tests + integration tests passing

Content: Curriculum alignment check + peer review

Commit Standards:

Conventional commits: feat:, fix:, docs:, content:

No direct pushes to main - PRs only

Checkpoints: Every 4 hours - demonstrable progress required

6.2 Bonus Feature Implementation Order
text
PRIORITY 1: Authentication (Day 1)
PRIORITY 2: RAG Chatbot Core (Day 1-2)
PRIORITY 3: Personalization Framework (Day 2)
PRIORITY 4: Urdu Translation Pipeline (Day 3)
6.3 Quality Metrics (Minimum Viable)
Backend test coverage: ≥85%

Page load time: <3 seconds

RAG response accuracy: >90% on test queries

Translation quality: >70% human evaluator score

Mobile responsiveness: 100% chapters

7.0 Governance & Compliance
7.1 Decision Authority
Technical Decisions: Lead Architect (specified in ADRs)

Content Decisions: Curriculum Committee (3 members minimum)

Merge Authority: Two approved reviews required

7.2 Change Management
Constitution amendments: Unanimous team vote required

Syllabus changes: Curriculum Committee + one industry expert

Breaking API changes: 48-hour deprecation notice

7.3 Success Criteria (Hackathon)
text
PRIMARY: Functional platform with all 4 bonus features
SECONDARY: Complete Modules 1 & 2 content
TERTIARY: Deployed and accessible via public URL
8.0 Risk Mitigation
8.1 Technical Risks
Vector DB failure: SQLite fallback with TF-IDF

Auth service outage: Read-only mode with cached content

Translation API limits: Queue system with exponential backoff

8.2 Content Risks
Chapter delays: Skeleton content with TODO markers

Complexity overflow: "Core path" vs "deep dive" separation

Accuracy concerns: Peer review + LLM fact-checking pipeline

Constitutional Ratification Date: $(date)
Hackathon Deadline: $(date + 3 days)
Review Cycle: Post-hackathon, then quarterly
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

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

I have successfully updated the project constitution at `.specify/memory/constitution.md` with the values from your user input. Here's what was accomplished:

**New Version and Bump Rationale:**
- Version: 1.0.0 (initial version based on your specification)
- This is the initial constitution for the "Physical AI & Humanoid Robotics Learning Platform" project, so it starts at version 1.0.0 as specified in your input.

**Files Updated:**
- `.specify/memory/constitution.md` - Updated with all the project principles, technical requirements, and governance information from your input.

**Key Changes Made:**
1. Replaced all placeholder tokens with concrete values from your user input
2. Added 6 core principles based on the Philosophical Tenets section
3. Included Technical Architecture Requirements with specific stack requirements
4. Added Development Standards & Quality Metrics sections
5. Included Governance section with workflow rules, decision authority, and risk mitigation
6. Added a Sync Impact Report as an HTML comment at the top of the file

**Files Flagged for Manual Follow-up:**
- `.specify/templates/plan-template.md` - Constitution Check section should reference new principles
- `.specify/templates/spec-template.md` - May need updates to align functional requirements with new principles
- `.specify/templates/tasks-template.md` - May need updates for test coverage requirements
- README.md - Should reference new constitution principles if it exists

**Suggested Commit Message:**
`docs: create constitution for Physical AI & Humanoid Robotics Learning Platform v1.0.0`

The constitution now accurately reflects all the requirements, principles, and governance structures specified in your user input, and is ready for use in the project.

## Outcome

- ✅ Impact: Created complete project constitution with 6 core principles, technical requirements, and governance structure
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md with new constitution content
- 🔁 Next prompts: Ready for feature specification and planning tasks
- 🧠 Reflection: Constitution properly captures all requirements from user input and establishes project governance

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification based on constitution