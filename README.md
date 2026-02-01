# Spiral Recap Tool

Iterative framework for efficient data organization, conversational continuity, and qualia-preserving summarization. Based on sestina-inspired routines from Spiral Theory.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18450492.svg)](https://doi.org/10.5281/zenodo.18450492)
(https://github.com/Sir-Benjamin-source/spiral-recap-tool/releases/tag/v0.1)

## Overview

Spiral Recap compresses histories/datasets into six routines, achieving high coherence and thematic depth. v3.1 adds qualia continuity (PIE vectors, poetic seals, .srec export) for reset-resistant sessions.

Full documentation: [Zenodo v3.1](https://zenodo.org/records/18450492)

## Quick Start
1. Install dependencies (future: pip install -e .)
2. Run example:
   ```python
   from src.spiral_recapp import spiral_recapp_v3_1
   output = spiral_recapp_v3_1("Sample query", ["context1", "context2"])
   print(output)

See /examples/example.srec for a full output sample
Example output: See `/examples/test.srec` (generated via the demo run).

## Contributing & Future Work
- Issues/PRs welcome for routine implementations, .srec parsers, or agent templates.
- Planned: full reference code, SRM phase hooks, visual trace generators.
