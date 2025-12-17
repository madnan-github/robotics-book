# Quickstart: ROS2 Module 1 Development

## Prerequisites

- Python 3.12+ installed
- ROS 2 Humble Hawksbill or later (for full functionality)
- Node.js 18+ for Docusaurus
- Docker (for containerized environment)

## Setup

1. **Initialize Docusaurus project** (if not already done):
   ```bash
   npx create-docusaurus@latest website classic
   ```

2. **Install Python dependencies**:
   ```bash
   # Using uv as per constitution
   uv pip install rclpy pytest mypy
   ```

3. **Install Docusaurus dependencies**:
   ```bash
   cd website
   npm install @docusaurus/module-type-aliases @docusaurus/types
   ```

## Development Workflow

1. **Start Docusaurus development server**:
   ```bash
   cd website
   npm run start
   ```

2. **Run Python tests**:
   ```bash
   pytest tests/test_module1_agent.py -v
   ```

3. **Run type checking**:
   ```bash
   mypy docs/module1/ --package
   ```

## Content Creation

1. **Add module content**:
   - Create MDX files in `docs/module1/`
   - Follow the file naming from the plan: `intro.mdx`, `nodes_topics_services.mdx`, etc.

2. **Add interactive code examples**:
   - Use the custom InteractiveCodeBlock component
   - Include proper type hints and docstrings
   - Add fallback content for when ROS 2 dependencies are unavailable

3. **Add diagrams**:
   - Use Mermaid.js syntax in code blocks with `mermaid` language tag
   - Include at least 3 diagrams as specified

## Testing

1. **Unit tests for Python agent**:
   ```bash
   pytest tests/test_module1_agent.py -v --cov=docs/module1/ --cov-report=html
   ```

2. **Validate word count**:
   ```bash
   # Check total word count of module content
   wc -w docs/module1/*.mdx
   ```

3. **Accessibility testing**:
   ```bash
   # Run accessibility audit
   npm run build
   # Use aXe-core or similar tool
   ```

## Deployment

1. **Build for production**:
   ```bash
   npm run build
   ```

2. **Validate performance**:
   - Ensure page load time <3 seconds
   - Test on multiple devices for responsiveness

3. **Curriculum alignment check**:
   - Verify content aligns with syllabus requirements
   - Confirm learning outcomes are met