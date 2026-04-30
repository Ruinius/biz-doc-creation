# System Design

## Architecture Overview
The system will operate as an Antigravity skill, taking natural language inputs and document requirements to generate structured business documents. It will use a templating engine to format the content and document generation libraries to produce Word and PDF outputs.

## Tech Stack
- **Language**: Python
- **Environment**: uv
- **Frameworks/Libraries**: 
  - `python-docx` for Word document generation.
  - `xhtml2pdf` and `markdown` for PDF document generation.

## Data Models
- **Document Request**: Contains user prompt, document type (Proposal, LOI, SOW), and required fields.
- **Template**: Defines the structure and style of the output document.
- **Generated Document**: The finalized content ready for export.

## Module Boundaries
- **Input Parser**: Interprets the user's intent and extracts required information.
- **Content Generator**: Interfaces with the LLM to draft the document body based on the parsed input and template.
- **Export Engine**: Takes the generated content and compiles it into `.docx` and `.pdf` files.

## Directory Structure
- `.agents/`: Antigravity workspace rules and operational behaviors.
- `docs/`: Project documentation and architecture notes.
- `examples/`: Sample documents and reference materials for the skill to read and use as context.
- `skills/`: Contains the logic and prompt guidelines for different document generation skills (e.g., `skills/proposal/`).
  - `skills/scripts/`: Python scripts for exporting generated markdown into Word and PDF formats.
- `<User-created folder>` (e.g., `work_products/`): A directory for generating and storing confidential, personal documents. Users should create their own directory for this purpose and ensure it is added to `.gitignore`.
