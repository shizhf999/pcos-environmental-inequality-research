# Changelog

## 2025-09-05 Initial Open Science Release
- Added core methodological scripts (method110, selection, Shapley, inequality metrics).
- Added minimal environment requirements.
- Added open science documentation (README, LICENSE, CONTRIBUTING, data sample placeholder).
- Pending: add pipeline orchestration script & fuller test harness.
# Changelog append – 2025-10-29

## Upgrade: Expanded coverage window and source harmonization
- Scope: Move from “GBD 1990–2021 (247 countries)” wording to “204 countries/territories; overall 1990–2023; outcomes 1990–2023.”
- Data sources: Clarify per-source coverage windows (GBD to 2023; WHO GHO/WDI/ERA5 to 2023; UN demographics to 2023; PM2.5/CO₂ alignment).
- Config: Introduce per-source coverage metadata to avoid hard-coded year ranges.
- Documentation: Update README Data Sources and Objective lines; add note on sample data staying 1990–2010 for quick tests.

### Suggested version bump
- Tag: v0.2.0 (docs + config upgrade; non-breaking API, but updated scope)

### Actions for users
- Pull latest docs.
- Place updated datasets matching data schema for 1990–2023 (outcomes to 2021).
- Review config to set analysis window; defaults to 1990–2023 with source-aware masking.
