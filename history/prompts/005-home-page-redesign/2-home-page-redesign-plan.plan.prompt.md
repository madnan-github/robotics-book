---
id: 2
title: home-page-redesign-plan
stage: plan
date: '2025-12-11'
surface: agent
model: claude-opus-4-5-20251101
feature: 005-home-page-redesign
branch: 005-home-page-redesign
user: ruser
command: /sp.plan
labels:
  - plan
  - home-page
  - docusaurus
  - ui
links:
  SPEC: /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/spec.md
  TICKET: 'null'
  ADR: 'null'
  PR: 'null'
files:
  - /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/plan.md
  - /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/research.md
  - /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/data-model.md
  - /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/quickstart.md
  - /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/contracts/components.md
tests: []
---

# Implementation Plan: Home Page Redesign

**Branch**: `005-home-page-redesign` | **Date**: 2025-12-11 | **Spec**: /home/ruser/q4/robotic-learning-book/specs/005-home-page-redesign/spec.md
**Input**: Feature specification from `/specs/005-home-page-redesign/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan addresses the redesign of the home page for the robotics learning book website. The primary requirements include fixing the "Page Not Found" error, implementing a new layout with a main heading "Physical AI & Humanoid Robotics Learning", adding a 6-7 line descriptive paragraph, creating a "Getting Start" button that routes to the textbook getting started section, and displaying 4 cards containing module names, descriptions, and relevant images. The implementation will follow Docusaurus best practices to ensure proper styling and functionality across environments.

## Technical Context

**Language/Version**: JavaScript/TypeScript, Docusaurus 3.1.0, React 18+
**Primary Dependencies**: @docusaurus/core, @docusaurus/preset-classic, React, Node.js 18+
**Storage**: N/A (static site)
**Testing**: Jest, React Testing Library
**Target Platform**: Web (HTML/CSS/JS bundle deployed to Vercel)
**Project Type**: Web/static documentation site
**Performance Goals**: <3 seconds page load time, 100% of CSS styles applied correctly
**Constraints**: Must work consistently on both local development and Vercel deployment, responsive design for all screen sizes
**Scale/Scope**: Single documentation site serving multiple learning modules

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Spec-First, AI-Augmented**: ✅ Feature specification exists and is detailed
- **Pedagogy-Driven**: ✅ Content structure optimized for learning outcomes with clear module cards
- **Production-Ready**: ✅ Implementation follows Docusaurus best practices for stability
- **Open by Design**: ✅ Architecture supports community contributions through Docusaurus framework
- **Type Safety & Validation**: N/A for Docusaurus MDX content
- **Test Coverage Requirement**: ✅ Will implement Jest tests for React components
- **All Python code requires type hints**: N/A for this JavaScript/Markdown feature
- **API versioning**: N/A for static documentation site
- **Backend test coverage**: N/A for static documentation site

## Project Structure

### Documentation (this feature)

```text
specs/005-home-page-redesign/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
docs/
├── home-page/
│   └── index.md         # Main home page content
├── module1/
├── module2/
├── module3/
└── module4/

src/
├── components/
│   ├── HomepageFeatures/
│   │   └── index.js     # Module cards component
│   └── HomepageHeader/
│       └── index.js     # Header with heading and paragraph
├── pages/
│   └── index.js         # Custom home page implementation
└── css/
    └── custom.css       # Custom styles for home page

static/
├── img/                 # Images for module cards
│   ├── module1.jpg
│   ├── module2.jpg
│   ├── module3.jpg
│   └── module4.jpg
└── ...
```

**Structure Decision**: Web application using Docusaurus framework with custom React components for the home page features. The structure follows Docusaurus conventions while adding custom components for the redesigned home page elements.