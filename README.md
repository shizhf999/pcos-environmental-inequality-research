# PCOS Environmental Health Inequality Analysis — Open Science Release

This repository provides open-source code to analyze population-level links between environmental determinants and PCOS (polycystic ovary syndrome) burden and inequality using a suite of statistical and machine-learning methods.

## 🔬 Research Overview

**Objective**: Analyze the relationship between environmental factors and PCOS health inequality across 204 countries and territories (overall coverage 1990–2023; GBD outcomes available 1990–2023).

- Multi-source integration: environmental, climate, socioeconomic, occupational, and demographic indicators
- Inequality metrics: concentration index, Gini, Atkinson, Theil (with decomposition)
- Robust modeling: Shapley-based feature attribution, spatial analysis, and multi-layer ML ensembles
- Transparency: end-to-end scripts, documented methods, and light sample data for quick tests

> Note: The full analysis window is 1990–2023 for most sources; GBD outcomes (PCOS prevalence/DALYs) are available through 2023 per the latest public release utilized in this project. Pipelines respect per-source valid years.

## 📁 Repository Structure

```
├── code/                    # Complete analysis suite (Python scripts)
│   ├── method1-10_*.py     # Core statistical methods
│   ├── progressive_ml_*.py # Machine learning frameworks (5 layers)
│   └── specialized_*.py    # Domain-specific analyses
├── config/                 # Central configuration (coverage, paths)
│   └── data_sources_coverage.yaml
├── data_sample/            # Lightweight sample datasets (quick tests)
│   ├── sample_pcos_data.csv
│   ├── sample_environmental_data.csv
│   └── data_schema.json
├── environment/            # Dependencies and setup
│   └── requirements_minimal.txt
├── docs/                   # Documentation and methodology
├── results_samples/        # Example outputs (for illustration)
└── tests/                  # Validation and testing
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- 4GB RAM minimum

### Setup (example)
```bash
# Clone
git clone https://github.com/shizhf999/pcos-environmental-inequality-research.git
cd pcos-environmental-inequality-research

# Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r environment/requirements_minimal.txt
```

### Run a quick smoke test with sample data
```bash
python code/run_repro_example.py
```

### Run selected methods (examples)
```bash
python code/method3_concentration_index.py
python code/enhanced_method1_complete_shapley_analysis.py
python code/progressive_ml_layer1.py
```

## ⚙️ Configuration: Per-Source Coverage (Recommended)
Use `config/data_sources_coverage.yaml` to avoid hard-coding year ranges. Pipelines should:
- Load YAML at start (e.g., `yaml.safe_load`) 
- Define an analysis window (default 1990–2023)
- Mask data beyond each source’s valid `coverage_end` to prevent accidental extrapolation

```yaml
analysis_window:
  start_year: 1990
  end_year: 2023

sources:
  gbd:
    name: "Global Burden of Disease Study 2021 (IHME)"
    coverage_start: 1990
    coverage_end: 2021
    notes: "Outcomes available to 2021 per public release used."
  who_gho:
    name: "WHO Global Health Observatory"
    coverage_start: 1990
    coverage_end: 2023
  wdi:
    name: "World Bank World Development Indicators"
    coverage_start: 1990
    coverage_end: 2023
  era5:
    name: "ERA5 Reanalysis (ECMWF)"
    coverage_start: 1990
    coverage_end: 2023
  un_pop:
    name: "UN Population Division"
    coverage_start: 1990
    coverage_end: 2023
  pm25_satellite:
    name: "Satellite-derived PM2.5 (van Donkelaar et al., 2021)"
    coverage_start: 1990
    coverage_end: 2023
  co2_per_capita:
    name: "National CO₂ per-capita from inventory reports"
    coverage_start: 1990
    coverage_end: 2023
```

## 🎯 Analysis Methods

### Core Statistical Methods (1–10)
1. Shapley Value Analysis — Feature importance quantification
2. Oaxaca–Blinder Decomposition — Inequality decomposition
3. Concentration Index — Income-related health inequality
4. Theil Index Decomposition — Within/between group inequality
5. Instrumental Variables — Causal inference
6. Regression Discontinuity — Natural experiment design
7. Survival Analysis — Time-to-event modeling (if applicable)
8. Spatial Autocorrelation — Geographic dependency
9. Bayesian Hierarchical Modeling — Multi-level uncertainty
10. Time-Series Analysis — Temporal trend detection

### Progressive ML Framework (5 Layers)
- Layer 1: Baseline ML pipeline
- Layer 2: Advanced ensembles & variable selection
- Layer 3: Deep learning integration
- Layer 4: Spatial modeling integration
- Layer 5: Optimized performance framework

### Specialized Tools
- Inequality economics toolkit (Gini/Atkinson/Theil CI)
- DALY monetization with geographic mapping
- Risk factor analyzer with enhanced features
- Income classification system
- Interactive heatmaps and mapping utilities

## 📊 Sample Data

Lightweight datasets are provided for fast testing:
- Geographic coverage: a small set of countries across income groups
- Temporal range: 1990–2010 (for quick runs <1MB)
- Variables: PCOS outcomes (mocked/sample), environmental, socioeconomic

> The full pipeline accepts 1990–2023 data once you place real datasets per the data schema. Sample data are for smoke tests only and not intended for inference.

## 🔍 Data Sources

- PCOS outcomes: Global Burden of Disease (IHME) — 1990–2023
- Environmental: WHO Global Health Observatory — to 2023
- Economic: World Bank World Development Indicators — to 2023
- Climate: ERA5 Reanalysis (ECMWF) — to 2023
- Demographics: UN Population Division — to 2023
- Additional: Satellite-derived PM2.5 (van Donkelaar et al., 2021); national CO₂ per-capita from inventory reports — harmonized to 2023

## 📖 Documentation
- Getting Started: this README
- Data documentation: `data_sample/data_schema.json`
- Methods overview: `docs/METHODS_OVERVIEW.md`
- API/usage details: see docstrings in individual scripts

## 🧪 Testing
- Minimal smoke tests and examples in `tests/` and `code/run_repro_example.py`
- We welcome PRs adding unit tests for core modules

## 🏆 Citation

```bibtex
@software{pcos_inequality_2025,
  title   = {PCOS Environmental Health Inequality Analysis — Open Science Release},
  author  = {[Authors]},
  year    = {2025},
  url     = {https://github.com/shizhf999/pcos-environmental-inequality-research},
  license = {MIT}
}
```

Please also cite the associated research article (see manuscript for details).

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file.

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
- Bug reports: open an issue with reproduction steps
- Feature requests: open an issue describing the use case
- Pull requests: focus on modular changes and include brief tests where possible

## 📧 Contact
- Issues: GitHub Issues
- Research inquiries: [contact email]
- Collaboration: [Institution/Department]

## 🌟 Acknowledgments
- Global Burden of Disease Collaborative Network
- World Health Organization
- World Bank Open Data Initiative
- Open science community

---

**Keywords**: PCOS, environmental health, health inequality, concentration index, Shapley values, open science, reproducibility
