# Contributing Guide

Thanks for contributing! This repo follows a PRISMA 2020-compliant workflow.

## Ground rules
- Use feature branches: `feat/<short-topic>`, `fix/<short-topic>`
- Keep data privacy: do not upload copyrighted PDFs
- Prefer plain-text templates in `/templates/`; working copies live under `/protocol/` or `/data/`

## Typical contributions
- Updating protocol (`/protocol/prisma_protocol.md`), search strategies, or checklists
- Improving scripts under `/scripts/analysis/` to update PRISMA counts/figures
- Enhancing data extraction or risk-of-bias tooling

## Pull Request checklist
- [ ] PR describes the change and motivation
- [ ] If touching counts, update `results/prisma_counts.json` (schema arrives in next commit)
- [ ] Add/Update tests or sample outputs if applicable
- [ ] No sensitive or proprietary data included

## Code of Conduct
Be respectful, constructive, and transparent. Document assumptions and decisions.
