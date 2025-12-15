---
id: 1
title: create-ros2-module1-spec
stage: spec
date: 2025-12-09
surface: agent
model: claude-opus-4-5-20251101
feature: 001-ros2-module1
branch: 001-ros2-module1
user: ruser
command: /sp.specify
labels: ["spec", "ros2", "education", "module1"]
links:
  spec: specs/001-ros2-module1/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-ros2-module1/spec.md
  - specs/001-ros2-module1/checklists/requirements.md
tests: []
---

## Prompt

```text
Module 1: The Robotic Nervous System (ROS 2)

Target audience: Undergraduate robotics/CS students and developers entering the field of Physical AI. The content must be accessible to learners with basic Python and Linux skills.

Focus: To establish a foundational, practical understanding of ROS 2 as the core middleware for robot control, enabling communication between software agents and physical (or simulated) hardware components.

Success criteria:

Concept Clarity: A learner can diagram and explain the data flow between ROS 2 Nodes, Topics, and Services.

Practical Skill: A learner can write a functional Python script (rclpy) that publishes sensor data (simulated) and subscribes to control commands.

Model Understanding: A learner can interpret a basic URDF file for a humanoid robot, identifying key links, joints, and sensors.

Integration Ready: The provided code snippets and explanations serve as the direct foundation for integration with the FastAPI backend agent in later modules.

Constitution Compliant:

Chapter starts with explicit "Learning Outcomes" and ends with practical "Assessments".

All code follows strict type hints, Google-style docstrings, and is validated via pytest.

The module's structure and depth strictly align with the defined syllabus for Module 1.

Constraints:

Word Count: 4000-6000 words of explanatory text.

Format: MDX (for Docusaurus), with integrated, executable code blocks.

Code: Python 3.12+, using rclpy. All code must be atomic, testable, and runnable in a provided Docker/Dev container environment.

Media: Must include at least 3 diagrams (using Mermaid.js) illustrating ROS 2 graphs and URDF structure.

Timeline: Complete draft for peer review within 48 hours (aligned with hackathon checkpoints).

Not building:

A complete history of ROS 1 vs. ROS 2.

In-depth DDS configuration or advanced QoS profiles.

Creating a complex humanoid URDF from scratch.

Deployment to real hardware (this is covered in the Capstone).

Mandatory Deliverables (Atomic Tasks):

ADR-001: Decision record for the structure of the "Bridging Python Agents to ROS controllers" section, detailing the software pattern chosen (e.g., Action Client/Server, custom service definitions).

module1_intro.mdx: Chapter introduction with Learning Outcomes and an overview of the robotic "nervous system" metaphor.

module1_nodes_topics_services.mdx: Core concepts chapter with Mermaid diagrams and simple publisher/subscriber code examples.

module1_rclpy_bridge.mdx: Chapter focusing on the rclpy Python API, building a small agent that sends/receives ROS 2 messages. Includes pytest for the agent logic.

module1_urdf_primer.mdx: Chapter explaining URDF structure using a simple humanoid model (e.g., a basic biped). Visualizes the model tree and key tags.

module1_assessment.mdx: End-of-module assessment featuring multiple-choice quizzes, a diagram labeling exercise, and a hands-on coding task to fix/complete a provided ROS 2 node.

tests/test_module1_agent.py: Pytest suite validating the core Python agent logic from deliverable #4.

Validation Gates:

Code: All Python code must pass mypy and pytest before commit.

Content: The Lead Architect must perform a "Curriculum Alignment" check against the core syllabus before the module is merged.

Integration Readiness: The rclpy agent code must be structured to allow future import and extension by the FastAPI backend's RAG or orchestration layer (as per Project Vision).
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

The text the user typed after `/sp.specify` in the triggering message **is** the feature description. Assume you always have it available in this conversation even if `Module 1: The Robotic Nervous System (ROS 2)

Target audience: Undergraduate robotics/CS students and developers entering the field of Physical AI. The content must be accessible to learners with basic Python and Linux skills.

Focus: To establish a foundational, practical understanding of ROS 2 as the core middleware for robot control, enabling communication between software agents and physical (or simulated) hardware components.

Success criteria:

Concept Clarity: A learner can diagram and explain the data flow between ROS 2 Nodes, Topics, and Services.

Practical Skill: A learner can write a functional Python script (rclpy) that publishes sensor data (simulated) and subscribes to control commands.

Model Understanding: A learner can interpret a basic URDF file for a humanoid robot, identifying key links, joints, and sensors.

Integration Ready: The provided code snippets and explanations serve as the direct foundation for integration with the FastAPI backend agent in later modules.

Constitution Compliant:

Chapter starts with explicit "Learning Outcomes" and ends with practical "Assessments".

All code follows strict type hints, Google-style docstrings, and is validated via pytest.

The module's structure and depth strictly align with the defined syllabus for Module 1.

Constraints:

Word Count: 4000-6000 words of explanatory text.

Format: MDX (for Docusaurus), with integrated, executable code blocks.

Code: Python 3.12+, using rclpy. All code must be atomic, testable, and runnable in a provided Docker/Dev container environment.

Media: Must include at least 3 diagrams (using Mermaid.js) illustrating ROS 2 graphs and URDF structure.

Timeline: Complete draft for peer review within 48 hours (aligned with hackathon checkpoints).

Not building:

A complete history of ROS 1 vs. ROS 2.

In-depth DDS configuration or advanced QoS profiles.

Creating a complex humanoid URDF from scratch.

Deployment to real hardware (this is covered in the Capstone).

Mandatory Deliverables (Atomic Tasks):

ADR-001: Decision record for the structure of the "Bridging Python Agents to ROS controllers" section, detailing the software pattern chosen (e.g., Action Client/Server, custom service definitions).

module1_intro.mdx: Chapter introduction with Learning Outcomes and an overview of the robotic "nervous system" metaphor.

module1_nodes_topics_services.mdx: Core concepts chapter with Mermaid diagrams and simple publisher/subscriber code examples.

module1_rclpy_bridge.mdx: Chapter focusing on the rclpy Python API, building a small agent that sends/receives ROS 2 messages. Includes pytest for the agent logic.

module1_urdf_primer.mdx: Chapter explaining URDF structure using a simple humanoid model (e.g., a basic biped). Visualizes the model tree and key tags.

module1_assessment.mdx: End-of-module assessment featuring multiple-choice quizzes, a diagram labeling exercise, and a hands-on coding task to fix/complete a provided ROS 2 node.

tests/test_module1_agent.py: Pytest suite validating the core Python agent logic from deliverable #4.

Validation Gates:

Code: All Python code must pass mypy and pytest before commit.

Content: The Lead Architect must perform a "Curriculum Alignment" check against the core syllabus before the module is merged.

Integration Readiness: The rclpy agent code must be structured to allow future import and extension by the FastAPI backend's RAG or orchestration layer (as per Project Vision).` appears literally below. Do not ask the user to repeat it unless they provided an empty command.

Given that feature description, do this:

1. **Generate a concise short name** (2-4 words) for the branch:
   - Analyze the feature description and extract the most meaningful keywords
   - Create a 2-4 word short name that captures the essence of the feature
   - Use action-noun format when possible (e.g., "add-user-auth", "fix-payment-bug")
   - Preserve technical terms and acronyms (OAuth2, API, JWT, etc.)
   - Keep it concise but descriptive enough to understand the feature at a glance
   - Examples:
     - "I want to add user authentication" → "user-auth"
     - "Implement OAuth2 integration for the API" → "oauth2-api-integration"
     - "Create a dashboard for analytics" → "analytics-dashboard"
     - "Fix payment processing timeout bug" → "fix-payment-timeout"

2. **Check for existing branches before creating new one**:

   a. First, fetch all remote branches to ensure we have the latest information:
      ```bash
      git fetch --all --prune
      ```

   b. Find the highest feature number across all sources for the short-name:
      - Remote branches: `git ls-remote --heads origin | grep -E 'refs/heads/[0-9]+-<short-name>$'`
      - Local branches: `git branch | grep -E '^[* ]*[0-9]+-<short-name>$'`
      - Specs directories: Check for directories matching `specs/[0-9]+-<short-name>`

   c. Determine the next available number:
      - Extract all numbers from all three sources
      - Find the highest number N
      - Use N+1 for the new branch number

   d. Run the script `.specify/scripts/bash/create-new-feature.sh --json "Module 1: The Robotic Nervous System (ROS 2)

Target audience: Undergraduate robotics/CS students and developers entering the field of Physical AI. The content must be accessible to learners with basic Python and Linux skills.

Focus: To establish a foundational, practical understanding of ROS 2 as the core middleware for robot control, enabling communication between software agents and physical (or simulated) hardware components.

Success criteria:

Concept Clarity: A learner can diagram and explain the data flow between ROS 2 Nodes, Topics, and Services.

Practical Skill: A learner can write a functional Python script (rclpy) that publishes sensor data (simulated) and subscribes to control commands.

Model Understanding: A learner can interpret a basic URDF file for a humanoid robot, identifying key links, joints, and sensors.

Integration Ready: The provided code snippets and explanations serve as the direct foundation for integration with the FastAPI backend agent in later modules.

Constitution Compliant:

Chapter starts with explicit "Learning Outcomes" and ends with practical "Assessments".

All code follows strict type hints, Google-style docstrings, and is validated via pytest.

The module's structure and depth strictly align with the defined syllabus for Module 1.

Constraints:

Word Count: 4000-6000 words of explanatory text.

Format: MDX (for Docusaurus), with integrated, executable code blocks.

Code: Python 3.12+, using rclpy. All code must be atomic, testable, and runnable in a provided Docker/Dev container environment.

Media: Must include at least 3 diagrams (using Mermaid.js) illustrating ROS 2 graphs and URDF structure.

Timeline: Complete draft for peer review within 48 hours (aligned with hackathon checkpoints).

Not building:

A complete history of ROS 1 vs. ROS 2.

In-depth DDS configuration or advanced QoS profiles.

Creating a complex humanoid URDF from scratch.

Deployment to real hardware (this is covered in the Capstone).

Mandatory Deliverables (Atomic Tasks):

ADR-001: Decision record for the structure of the "Bridging Python Agents to ROS controllers" section, detailing the software pattern chosen (e.g., Action Client/Server, custom service definitions).

module1_intro.mdx: Chapter introduction with Learning Outcomes and an overview of the robotic "nervous system" metaphor.

module1_nodes_topics_services.mdx: Core concepts chapter with Mermaid diagrams and simple publisher/subscriber code examples.

module1_rclpy_bridge.mdx: Chapter focusing on the rclpy Python API, building a small agent that sends/receives ROS 2 messages. Includes pytest for the agent logic.

module1_urdf_primer.mdx: Chapter explaining URDF structure using a simple humanoid model (e.g., a basic biped). Visualizes the model tree and key tags.

module1_assessment.mdx: End-of-module assessment featuring multiple-choice quizzes, a diagram labeling exercise, and a hands-on coding task to fix/complete a provided ROS 2 node.

tests/test_module1_agent.py: Pytest suite validating the core Python agent logic from deliverable #4.

Validation Gates:

Code: All Python code must pass mypy and pytest before commit.

Content: The Lead Architect must perform a "Curriculum Alignment" check against the core syllabus before the module is merged.

Integration Readiness: The rclpy agent code must be structured to allow future import and extension by the FastAPI backend's RAG or orchestration layer (as per Project Vision)."` with the calculated number and short-name:
      - Pass `--number N+1` and `--short-name "your-short-name"` along with the feature description
      - Bash example: `.specify/scripts/bash/create-new-feature.sh --json "Module 1: The Robotic Nervous System (ROS 2)

Target audience: Undergraduate robotics/CS students and developers entering the field of Physical AI. The content must be accessible to learners with basic Python and Linux skills.

Focus: To establish a foundational, practical understanding of ROS 2 as the core middleware for robot control, enabling communication between software agents and physical (or simulated) hardware components.

Success criteria:

Concept Clarity: A learner can diagram and explain the data flow between ROS 2 Nodes, Topics, and Services.

Practical Skill: A learner can write a functional Python script (rclpy) that publishes sensor data (simulated) and subscribes to control commands.

Model Understanding: A learner can interpret a basic URDF file for a humanoid robot, identifying key links, joints, and sensors.

Integration Ready: The provided code snippets and explanations serve as the direct foundation for integration with the FastAPI backend agent in later modules.

Constitution Compliant:

Chapter starts with explicit "Learning Outcomes" and ends with practical "Assessments".

All code follows strict type hints, Google-style docstrings, and is validated via pytest.

The module's structure and depth strictly align with the defined syllabus for Module 1.

Constraints:

Word Count: 4000-6000 words of explanatory text.

Format: MDX (for Docusaurus), with integrated, executable code blocks.

Code: Python 3.12+, using rclpy. All code must be atomic, testable, and runnable in a provided Docker/Dev container environment.

Media: Must include at least 3 diagrams (using Mermaid.js) illustrating ROS 2 graphs and URDF structure.

Timeline: Complete draft for peer review within 48 hours (aligned with hackathon checkpoints).

Not building:

A complete history of ROS 1 vs. ROS 2.

In-depth DDS configuration or advanced QoS profiles.

Creating a complex humanoid URDF from scratch.

Deployment to real hardware (this is covered in the Capstone).

Mandatory Deliverables (Atomic Tasks):

ADR-001: Decision record for the structure of the "Bridging Python Agents to ROS controllers" section, detailing the software pattern chosen (e.g., Action Client/Server, custom service definitions).

module1_intro.mdx: Chapter introduction with Learning Outcomes and an overview of the robotic "nervous system" metaphor.

module1_nodes_topics_services.mdx: Core concepts chapter with Mermaid diagrams and simple publisher/subscriber code examples.

module1_rclpy_bridge.mdx: Chapter focusing on the rclpy Python API, building a small agent that sends/receives ROS 2 messages. Includes pytest for the agent logic.

module1_urdf_primer.mdx: Chapter explaining URDF structure using a simple humanoid model (e.g., a basic biped). Visualizes the model tree and key tags.

module1_assessment.mdx: End-of-module assessment featuring multiple-choice quizzes, a diagram labeling exercise, and a hands-on coding task to fix/complete a provided ROS 2 node.

tests/test_module1_agent.py: Pytest suite validating the core Python agent logic from deliverable #4.

Validation Gates:

Code: All Python code must pass mypy and pytest before commit.

Content: The Lead Architect must perform a "Curriculum Alignment" check against the core syllabus before the module is merged.

Integration Readiness: The rclpy agent code must be structured to allow future import and extension by the FastAPI backend's RAG or orchestration layer (as per Project Vision)." --json --number 5 --short-name "user-auth" "Add user authentication"`
      - PowerShell example: `.specify/scripts/bash/create-new-feature.sh --json "Module 1: The Robotic Nervous System (ROS 2)

Target audience: Undergraduate robotics/CS students and developers entering the field of Physical AI. The content must be accessible to learners with basic Python and Linux skills.

Focus: To establish a foundational, practical understanding of ROS 2 as the core middleware for robot control, enabling communication between software agents and physical (or simulated) hardware components.

Success criteria:

Concept Clarity: A learner can diagram and explain the data flow between ROS 2 Nodes, Topics, and Services.

Practical Skill: A learner can write a functional Python script (rclpy) that publishes sensor data (simulated) and subscribes to control commands.

Model Understanding: A learner can interpret a basic URDF file for a humanoid robot, identifying key links, joints, and sensors.

Integration Ready: The provided code snippets and explanations serve as the direct foundation for integration with the FastAPI backend agent in later modules.

Constitution Compliant:

Chapter starts with explicit "Learning Outcomes" and ends with practical "Assessments".

All code follows strict type hints, Google-style docstrings, and is validated via pytest.

The module's structure and depth strictly align with the defined syllabus for Module 1.

Constraints:

Word Count: 4000-6000 words of explanatory text.

Format: MDX (for Docusaurus), with integrated, executable code blocks.

Code: Python 3.12+, using rclpy. All code must be atomic, testable, and runnable in a provided Docker/Dev container environment.

Media: Must include at least 3 diagrams (using Mermaid.js) illustrating ROS 2 graphs and URDF structure.

Timeline: Complete draft for peer review within 48 hours (aligned with hackathon checkpoints).

Not building:

A complete history of ROS 1 vs. ROS 2.

In-depth DDS configuration or advanced QoS profiles.

Creating a complex humanoid URDF from scratch.

Deployment to real hardware (this is covered in the Capstone).

Mandatory Deliverables (Atomic Tasks):

ADR-001: Decision record for the structure of the "Bridging Python Agents to ROS controllers" section, detailing the software pattern chosen (e.g., Action Client/Server, custom service definitions).

module1_intro.mdx: Chapter introduction with Learning Outcomes and an overview of the robotic "nervous system" metaphor.

module1_nodes_topics_services.mdx: Core concepts chapter with Mermaid diagrams and simple publisher/subscriber code examples.

module1_rclpy_bridge.mdx: Chapter focusing on the rclpy Python API, building a small agent that sends/receives ROS 2 messages. Includes pytest for the agent logic.

module1_urdf_primer.mdx: Chapter explaining URDF structure using a simple humanoid model (e.g., a basic biped). Visualizes the model tree and key tags.

module1_assessment.mdx: End-of-module assessment featuring multiple-choice quizzes, a diagram labeling exercise, and a hands-on coding task to fix/complete a provided ROS 2 node.

tests/test_module1_agent.py: Pytest suite validating the core Python agent logic from deliverable #4.

Validation Gates:

Code: All Python code must pass mypy and pytest before commit.

Content: The Lead Architect must perform a "Curriculum Alignment" check against the core syllabus before the module is merged.

Integration Readiness: The rclpy agent code must be structured to allow future import and extension by the FastAPI backend's RAG or orchestration layer (as per Project Vision)." -Json -Number 5 -ShortName "user-auth" "Add user authentication"`

   **IMPORTANT**:
   - Check all three sources (remote branches, local branches, specs directories) to find the highest number
   - Only match branches/directories with the exact short-name pattern
   - If no existing branches/directories found with this short-name, start with number 1
   - You must only ever run this script once per feature
   - The JSON is provided in the terminal as output - always refer to it to get the actual content you're looking for
   - The JSON output will contain BRANCH_NAME and SPEC_FILE paths
   - For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot")

3. Load `.specify/templates/spec-template.md` to understand required sections.

4. Follow this execution flow:

    1. Parse user description from Input
       If empty: ERROR "No feature description provided"
    2. Extract key concepts from description
       Identify: actors, actions, data, constraints
    3. For unclear aspects:
       - Make informed guesses based on context and industry standards
       - Only mark with [NEEDS CLARIFICATION: specific question] if:
         - The choice significantly impacts feature scope or user experience
         - Multiple reasonable interpretations exist with different implications
         - No reasonable default exists
       - **LIMIT: Maximum 3 [NEEDS CLARIFICATION] markers total**
       - Prioritize clarifications by impact: scope > security/privacy > user experience > technical details
    4. Fill User Scenarios & Testing section
       If no clear user flow: ERROR "Cannot determine user scenarios"
    5. Generate Functional Requirements
       Each requirement must be testable
       Use reasonable defaults for unspecified details (document assumptions in Assumptions section)
    6. Define Success Criteria
       Create measurable, technology-agnostic outcomes
       Include both quantitative metrics (time, performance, volume) and qualitative measures (user satisfaction, task completion)
       Each criterion must be verifiable without implementation details
    7. Identify Key Entities (if data involved)
    8. Return: SUCCESS (spec ready for planning)

5. Write the specification to SPEC_FILE using the template structure, replacing placeholders with concrete details derived from the feature description (arguments) while preserving section order and headings.

6. **Specification Quality Validation**: After writing the initial spec, validate it against quality criteria:

   a. **Create Spec Quality Checklist**: Generate a checklist file at `FEATURE_DIR/checklists/requirements.md` using the checklist template structure with these validation items:

      ```markdown
      # Specification Quality Checklist: [FEATURE NAME]

      **Purpose**: Validate specification completeness and quality before proceeding to planning
      **Created**: [DATE]
      **Feature**: [Link to spec.md]

      ## Content Quality

      - [ ] No implementation details (languages, frameworks, APIs)
      - [ ] Focused on user value and business needs
      - [ ] Written for non-technical stakeholders
      - [ ] All mandatory sections completed

      ## Requirement Completeness

      - [ ] No [NEEDS CLARIFICATION] markers remain
      - [ ] Requirements are testable and unambiguous
      - [ ] Success criteria are measurable
      - [ ] Success criteria are technology-agnostic (no implementation details)
      - [ ] All acceptance scenarios are defined
      - [ ] Edge cases are identified
      - [ ] Scope is clearly bounded
      - [ ] Dependencies and assumptions identified

      ## Feature Readiness

      - [ ] All functional requirements have clear acceptance criteria
      - [ ] User scenarios cover primary flows
      - [ ] Feature meets measurable outcomes defined in Success Criteria
      - [ ] No implementation details leak into specification

      ## Notes

      - Items marked incomplete require spec updates before `/sp.clarify` or `/sp.plan`
      ```

   b. **Run Validation Check**: Review the spec against each checklist item:
      - For each item, determine if it passes or fails
      - Document specific issues found (quote relevant spec sections)

   c. **Handle Validation Results**:

      - **If all items pass**: Mark checklist complete and proceed to step 6

      - **If items fail (excluding [NEEDS CLARIFICATION])**:
        1. List the failing items and specific issues
        2. Update the spec to address each issue
        3. Re-run validation until all items pass (max 3 iterations)
        4. If still failing after 3 iterations, document remaining issues in checklist notes and warn user

      - **If [NEEDS CLARIFICATION] markers remain**:
        1. Extract all [NEEDS CLARIFICATION: ...] markers from the spec
        2. **LIMIT CHECK**: If more than 3 markers exist, keep only the 3 most critical (by scope/security/UX impact) and make informed guesses for the rest
        3. For each clarification needed (max 3), present options to user in this format:

           ```markdown
           ## Question [N]: [Topic]

           **Context**: [Quote relevant spec section]

           **What we need to know**: [Specific question from NEEDS CLARIFICATION marker]

           **Suggested Answers**:

           | Option | Answer | Implications |
           |--------|--------|--------------|
           | A      | [First suggested answer] | [What this means for the feature] |
           | B      | [Second suggested answer] | [What this means for the feature] |
           | C      | [Third suggested answer] | [What this means for the feature] |
           | Custom | Provide your own answer | [Explain how to provide custom input] |

           **Your choice**: _[Wait for user response]_
           ```

        4. **CRITICAL - Table Formatting**: Ensure markdown tables are properly formatted:
           - Use consistent spacing with pipes aligned
           - Each cell should have spaces around content: `| Content |` not `|Content|`
           - Header separator must have at least 3 dashes: `|--------|`
           - Test that the table renders correctly in markdown preview
        5. Number questions sequentially (Q1, Q2, Q3 - max 3 total)
        6. Present all questions together before waiting for responses
        7. Wait for user to respond with their choices for all questions (e.g., "Q1: A, Q2: Custom - [details], Q3: B")
        8. Update the spec by replacing each [NEEDS CLARIFICATION] marker with the user's selected or provided answer
        9. Re-run validation after all clarifications are resolved

   d. **Update Checklist**: After each validation iteration, update the checklist file with current pass/fail status

7. Report completion with branch name, spec file path, checklist results, and readiness for the next phase (`/sp.clarify` or `/sp.plan`).

**NOTE:** The script creates and checks out the new branch and initializes the spec file before writing.

## General Guidelines

## Quick Guidelines

- Focus on **WHAT** users need and **WHY**.
- Avoid HOW to implement (no tech stack, APIs, code structure).
- Written for business stakeholders, not developers.
- DO NOT create any checklists that are embedded in the spec. That will be a separate command.

### Section Requirements

- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation

When creating this spec from a user prompt:

1. **Make informed guesses**: Use context, industry standards, and common patterns to fill gaps
2. **Document assumptions**: Record reasonable defaults in the Assumptions section
3. **Limit clarifications**: Maximum 3 [NEEDS CLARIFICATION] markers - use only for critical decisions that:
   - Significantly impact feature scope or user experience
   - Have multiple reasonable interpretations with different implications
   - Lack any reasonable default
4. **Prioritize clarifications**: scope > security/privacy > user experience > technical details
5. **Think like a tester**: Every vague requirement should fail the "testable and unambiguous" checklist item
6. **Common areas needing clarification** (only if no reasonable default exists):
   - Feature scope and boundaries (include/exclude specific use cases)
   - User types and permissions (if multiple conflicting interpretations possible)
   - Security/compliance requirements (when legally/financially significant)
   - Integration patterns: RESTful APIs unless specified otherwise

**Examples of reasonable defaults** (don't ask about these):

- Data retention: Industry-standard practices for the domain
- Performance targets: Standard web/mobile app expectations unless specified
- Error handling: User-friendly messages with appropriate fallbacks
- Authentication method: Standard session-based or OAuth2 for web apps

### Success Criteria Guidelines

Success criteria must be:

1. **Measurable**: Include specific metrics (time, percentage, count, rate)
2. **Technology-agnostic**: No mention of frameworks, languages, databases, or tools
3. **User-focused**: Describe outcomes from user/business perspective, not system internals
4. **Verifiable**: Can be tested/validated without knowing implementation details

**Good examples**:

- "Users can complete checkout in under 3 minutes"
- "System supports 10,000 concurrent users"
- "95% of searches return results in under 1 second"
- "Task completion rate improves by 40%"

**Bad examples** (implementation-focused):

- "API response time is under 200ms" (too technical, use "Users see results instantly")
- "Database can handle 1000 TPS" (implementation detail, use user-facing metric)
- "React components render efficiently" (framework-specific)
- "Redis cache hit rate above 80%" (technology-specific)

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

I have successfully completed the specification for "Module 1: The Robotic Nervous System (ROS 2)" with the following accomplishments:

**Branch Creation:**
- Created branch `001-ros2-module1` following the proper naming convention
- Created the specification directory `specs/001-ros2-module1/`

**Specification Creation:**
- Created a comprehensive feature specification document at `specs/001-ros2-module1/spec.md`
- Included all required sections: User Scenarios & Testing, Requirements, and Success Criteria
- Defined 3 user stories with proper priorities:
  - ROS 2 Concepts Understanding (P1)
  - Practical Python Agent Development (P2)
  - URDF Model Interpretation (P3)
- Created 9 functional requirements and 5 key entities
- Established 7 measurable success criteria

**Quality Validation:**
- Created a specification quality checklist at `specs/001-ros2-module1/checklists/requirements.md`
- Validated the specification against all criteria
- Resolved all NEEDS CLARIFICATION markers
- Appropriately balanced domain-specific terminology (ROS 2, rclpy, URDF) with educational objectives
- Ensured all requirements are testable and success criteria are measurable

**Key Features of the Specification:**
- Targets undergraduate robotics/CS students and developers entering Physical AI
- Focuses on establishing foundational understanding of ROS 2 as middleware for robot control
- Ensures content accessibility with clear learning outcomes and assessments
- Maintains alignment with the project constitution's requirements for type hints, docstrings, and pytest validation

The specification is now ready for the next phase (`/sp.clarify` or `/sp.plan`) and fully complies with the constitutional requirements specified in the project constitution.

## Outcome

- ✅ Impact: Created comprehensive ROS2 module specification with user stories, requirements, and success criteria
- 🧪 Tests: No tests required for specification creation
- 📁 Files: Created specs/001-ros2-module1/spec.md and specs/001-ros2-module1/checklists/requirements.md
- 🔁 Next prompts: Ready for feature clarification or planning phase
- 🧠 Reflection: Specification balances domain-specific terminology with educational objectives effectively

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature planning based on completed specification