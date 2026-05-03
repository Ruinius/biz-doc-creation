# Documentation Index

This file serves as the primary index for the project's documentation, located in the `docs/` directory.

## Core Documentation
- [Product Specification](PRODUCT_SPEC.md): Outlines the goals, features, and requirements of the project.
- [System Design](SYSTEM_DESIGN.md): Details the architecture, data models, and technical approach.
- [Roadmap](ROADMAP.md): Tracks project milestones, planned features, and progress.

*Always keep this index and the corresponding documentation up-to-date with code changes.*

## Project Folder Structure

```text
biz-doc-creation/
├── .agents/                # Antigravity workspace rules and behaviors
├── assets/                 # Brand assets and images
├── docs/                   # Core project documentation
│   ├── DOC_INDEX.md        # This file
│   ├── PRODUCT_SPEC.md     # Product goals and features
│   ├── ROADMAP.md          # Project milestones
│   └── SYSTEM_DESIGN.md    # Architecture and data models
├── examples/               # Reference examples for testing and demonstration
│   ├── sample_context.md   # Baseline context file for a fictional client
│   ├── lumina_proposal.md  # Generated proposal (Jane Doe)
│   ├── lumina_proposal.docx# Word export of the sample proposal
│   └── lumina_proposal.pdf # PDF export of the sample proposal
├── skills/                 # Antigravity skill definitions and logic
│   ├── proposal/           # Proposal generation guidelines
│   │   └── proposal_writer.md
│   └── scripts/            # Export utilities
│       ├── export_docx.py  # Markdown to Word converter
│       └── export_pdf.py   # Markdown to PDF converter
├── tiger_work_products/    # User active working directory (GIT IGNORED)
└── pyproject.toml          # Project dependencies
```

## Active Skills
- **Proposal Writer**: Guided writing for high-value strategic proposals. Located in `skills/proposal/proposal_writer.md`.
