# System Design

## Architecture Overview
The system operates as an Antigravity skill, using structured markdown prompt files (skills) and client-specific context files to generate professional business documents via AI. The AI agent reads a context file containing engagement details, applies the persona and formatting rules defined in the skill, and produces a polished markdown document. Python-based export scripts then convert the markdown into Word and PDF outputs.

## Tech Stack
- **Language**: Python
- **Environment**: uv
- **Frameworks/Libraries**: 
  - `python-docx` for Word document generation.
  - `xhtml2pdf` and `markdown` for PDF document generation.

## Data Models
- **Context File**: A markdown document containing engagement-specific data (client name, scope of work, fee structures, timeline options, and required materials).
- **Skill File**: A markdown prompt defining the AI persona, tone, formatting rules, and standard document sections.
- **Generated Document**: The finalized markdown content ready for export to `.docx` and `.pdf`.

## Module Boundaries
- **Skill Prompts** (`skills/`): Define the AI agent's persona, writing style, and document structure for each document type.
- **Export Scripts** (`skills/scripts/`): Python scripts that convert generated markdown into professionally styled Word and PDF files.
- **Context Files** (user-created): Provide the engagement-specific data that the AI agent uses to populate the document.

## Directory Structure
- `.agents/`: Antigravity workspace rules and operational behaviors.
- `assets/`: Screenshots and media used in the README.
- `docs/`: Core project documentation (specs, design, roadmap).
- `examples/`: Sample context files, generated proposals, and exported documents for reference.
- `skills/`: Contains the logic and prompt guidelines for different document generation skills.
  - `skills/scripts/`: Python scripts for exporting generated markdown into Word and PDF formats.
- `tiger_work_products/`: User-specific directory for generating and storing active work products. This directory is typically added to `.gitignore`.
