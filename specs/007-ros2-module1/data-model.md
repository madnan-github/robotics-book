# Data Model: ROS2 Module 1

## Entities

### LearningModule
- **id**: string (unique identifier for the module)
- **title**: string (e.g., "ROS2 Module 1: The Robotic Nervous System")
- **description**: string (module overview)
- **learningOutcomes**: array of strings (3-5 learning outcomes)
- **content**: array of ContentSections
- **assessments**: array of AssessmentItems
- **metadata**: object (word count, creation date, last updated)

### ContentSection
- **id**: string (unique identifier for the section)
- **title**: string (section title)
- **type**: enum ("introduction", "concept", "practical", "assessment")
- **content**: string (MDX formatted content)
- **learningObjectives**: array of strings (specific objectives for this section)
- **diagrams**: array of Diagram objects
- **codeExamples**: array of CodeExample objects
- **nextSectionId**: string (ID of the following section)

### CodeExample
- **id**: string (unique identifier)
- **title**: string (brief description)
- **language**: string (e.g., "python")
- **code**: string (the actual code snippet)
- **description**: string (explanation of what the code does)
- **expectedOutput**: string (what the code should produce)
- **isInteractive**: boolean (whether it can be executed in browser)

### Diagram
- **id**: string (unique identifier)
- **title**: string (brief description)
- **type**: enum ("mermaid-flowchart", "mermaid-sequence", "mermaid-graph")
- **definition**: string (Mermaid.js code)
- **caption**: string (explanation of the diagram)

### AssessmentItem
- **id**: string (unique identifier)
- **type**: enum ("multiple-choice", "diagram-labeling", "coding-task")
- **question**: string (the question or task)
- **options**: array of strings (for multiple choice)
- **expectedAnswer**: string (the correct answer)
- **explanation**: string (why this is the correct answer)
- **difficulty**: enum ("beginner", "intermediate", "advanced")

### UserProgress
- **userId**: string (identifier for the learner)
- **moduleId**: string (which module this progress is for)
- **completedSections**: array of strings (IDs of completed sections)
- **assessmentScores**: object (scores for each assessment item)
- **timeSpent**: number (time spent in seconds)
- **lastAccessed**: date (when the user last accessed this module)

## Relationships

- LearningModule contains many ContentSections
- ContentSection contains many CodeExamples and Diagrams
- LearningModule contains many AssessmentItems
- UserProgress tracks progress for a User through a LearningModule

## Validation Rules

- Each LearningModule must have 1-5 learning outcomes
- Each ContentSection must have at least one learning objective
- CodeExamples must follow type hints and docstring standards as per constitution
- Content must be between 4000-6000 words total (as per spec constraints)
- AssessmentItems must have appropriate difficulty levels for target audience
- All diagrams must be in Mermaid.js format (as per spec)

## State Transitions

- ContentSection: draft → review → approved → published
- UserProgress: not-started → in-progress → completed
- LearningModule: planned → in-development → in-review → published