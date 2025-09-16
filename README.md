# PCOS Environmental Health Inequality Analysis - Open Science Release

This repository provides complete reproduction code for comprehensive analysis of PCOS environmental health inequality using 10+ advanced statistical methods.

## 🔬 Research Overview

**Objective**: Analyze the relationship between environmental factors and PCOS health inequality across 247 countries (1990-2021)

**Key Findings**:
- Environmental factors explain **42.3%** of PCOS prevalence variation
- Concentration index improved from **-0.122** to **-0.029** (inequality reduction)
- Significant disparities across income groups and geographic regions

## 📁 Repository Structure

```
├── code/                    # Complete analysis suite (41 Python scripts)
│   ├── method1-10_*.py     # Core statistical methods
│   ├── progressive_ml_*.py # Machine learning frameworks (5 layers)
│   └── specialized_*.py    # Domain-specific analyses
├── data_sample/            # Lightweight sample datasets
│   ├── sample_pcos_data.csv
│   ├── sample_environmental_data.csv
│   └── data_schema.json
├── environment/            # Dependencies and setup
│   └── requirements_minimal.txt
├── docs/                   # Documentation and methodology
├── results_samples/        # Example analysis outputs
└── tests/                  # Validation and testing
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- 4GB RAM minimum
- Internet connection for package installation

### Installation
```bash
# Clone repository
git clone https://github.com/[username]/pcos-environmental-inequality-research.git
cd pcos-environmental-inequality-research

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r environment/requirements_minimal.txt
```

### Running Analysis
```bash
# Test with sample data
python code/run_repro_example.py

# Run specific methods
python code/method3_concentration_index.py
python code/enhanced_method1_complete_shapley_analysis.py
python code/progressive_ml_layer1.py
```

## 🎯 Analysis Methods

### Core Statistical Methods (1-10)
1. **Shapley Value Analysis** - Feature importance quantification
2. **Oaxaca-Blinder Decomposition** - Inequality decomposition  
3. **Concentration Index** - Health inequality measurement
4. **Theil Index Decomposition** - Between/within group inequality
5. **Instrumental Variable Analysis** - Causal inference
6. **Regression Discontinuity** - Natural experiment design
7. **Survival Analysis** - Time-to-event modeling
8. **Spatial Autocorrelation** - Geographic dependency analysis
9. **Bayesian Hierarchical Modeling** - Multi-level uncertainty
10. **Time Series Analysis** - Temporal trend detection

### Progressive ML Framework (5 Layers)
- **Layer 1**: Basic machine learning pipeline
- **Layer 2**: Advanced ensemble methods
- **Layer 3**: Deep learning implementation
- **Layer 4**: Spatial modeling integration
- **Layer 5**: Optimized performance framework

### Specialized Tools
- Health inequality economics analysis
- DALY monetization with geographic mapping
- Risk factor analyzer with enhanced features
- Income classification system
- Interactive heatmap generation

## 📊 Sample Data

**Lightweight datasets** for method testing and development:
- **Geographic coverage**: 7 countries across all income groups
- **Temporal range**: 1990-2010 (representative sample)
- **Variables**: PCOS prevalence, environmental factors, socioeconomic indicators
- **Size**: <1MB total (vs. 395MB full dataset)

See `data_sample/README_DATA_SAMPLE.md` for detailed usage instructions.

## 🔍 Data Sources

- **PCOS Data**: Global Burden of Disease Study 2021 (IHME)
- **Environmental**: WHO Global Health Observatory
- **Economic**: World Bank World Development Indicators  
- **Climate**: ERA5 Reanalysis Data
- **Demographics**: UN Population Division

## 📖 Documentation

- **Getting Started**: This README
- **Data Documentation**: `data_sample/data_schema.json`
- **Methods Overview**: `docs/METHODS_OVERVIEW.md`
- **API Reference**: Individual script docstrings

## 🏆 Citation

```bibtex
@software{pcos_inequality_2025,
  title={PCOS Environmental Health Inequality Analysis - Open Science Release},
  author={[Author Names]},
  year={2025},
  url={https://github.com/[username]/pcos-environmental-inequality-research},
  license={MIT}
}
```

Please cite the original research paper: [Paper Title, Journal, Year]

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Code and documentation are open source. Some data may require permission from original sources.

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- **Bug Reports**: Open an issue with reproduction steps
- **Feature Requests**: Suggest improvements via issues
- **Pull Requests**: Submit code improvements
- **Academic Collaboration**: Contact authors for research partnerships

## 📧 Contact

- **Issues**: Use GitHub Issues for technical questions
- **Research Inquiries**: [Contact email]
- **Collaboration**: [Institution/Department]

## 🌟 Acknowledgments

- Global Burden of Disease Collaborative Network
- World Health Organization
- World Bank Open Data Initiative  
- Open science community

---

**Keywords**: PCOS, health inequality, environmental health, concentration index, Shapley values, open science, reproducibility
