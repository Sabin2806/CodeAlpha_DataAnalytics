# 🚢 Titanic Exploratory Data Analysis (EDA)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A comprehensive Exploratory Data Analysis (EDA) of the Titanic passenger dataset with automated report generation.

## 📋 Overview

This project performs a complete exploratory analysis of the Titanic dataset to understand survival patterns and factors that influenced passenger survival during the 1912 disaster.

**Live Report:** [TITANIC_EDA_REPORT.md](./reports/TITANIC_EDA_REPORT.md)

## 🎯 Features

- ✅ **Complete EDA workflow** - From data loading to insights
- ✅ **Automated report generation** - Professional markdown report
- ✅ **10 high-quality visualizations** - Comprehensive charts and graphs
- ✅ **Statistical analysis** - Detailed metrics and insights
- ✅ **Data cleaning pipeline** - Automated preprocessing
- ✅ **Multiple usage options** - Jupyter notebook or standalone script
- ✅ **GitHub-friendly** - Perfect for portfolios and documentation

## 📊 Key Findings

| Insight | Finding |
|---------|---------|
| Overall Survival Rate | 38.4% |
| Female Survival Rate | 74.2% |
| Male Survival Rate | 18.9% |
| 1st Class Survival | 63.0% |
| 3rd Class Survival | 24.2% |
| Children Survival (≤12) | 59.0% |

## 📁 Project Structure
CodeAlpha_EDA/
├── data/ # Data files
│ └── titanic_cleaned.csv # Cleaned and processed data
├── notebooks/ # Jupyter notebook
│ └── titanic_eda.ipynb # Complete EDA analysis
├── reports/ # Generated reports
│ └── TITANIC_EDA_REPORT.md # Complete Markdown report
├── images/ # Generated visualizations (10 charts)
│ ├── 01_survival_distribution.png
│ ├── 02_age_distribution.png
│ ├── 03_fare_distribution.png
│ ├── 04_survival_by_gender.png
│ ├── 05_survival_by_class.png
│ ├── 06_correlation_heatmap.png
│ ├── 07_age_vs_survival.png
│ ├── 08_fare_vs_survival.png
│ ├── 09_gender_distribution.png
│ └── 10_class_distribution.png
├── src/ # Python scripts
│ └── generate_report.py # Standalone analysis script
├── requirements.txt # Python dependencies
├── environment.yml # Conda environment
└── README.md # This file

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager

### Installation

**Option 1: Using pip**
```bash
# Clone or download the project
git clone <repository-url>
cd titanic_eda_project

# Install dependencies
pip install -r requirements.txt
📈 Visualizations Gallery
Chart	Description
images/01_survival_distribution.png	Overall survival rate and distribution
images/02_age_distribution.png	Passenger age distribution with statistics
images/03_fare_distribution.png	Ticket fare distribution
images/04_survival_by_gender.png	Survival comparison by gender
images/05_survival_by_class.png	Survival comparison by passenger class
images/06_correlation_heatmap.png	Correlation between numerical features
images/07_age_vs_survival.png	Age distribution by survival status
images/08_fare_vs_survival.png	Fare distribution by survival status
images/09_gender_distribution.png	Gender distribution of passengers
images/10_class_distribution.png	Passenger class distribution
📋 Analysis Workflow
Data Loading & Inspection

Load Titanic dataset from Seaborn

Basic dataset information and structure

Missing values analysis

Data Cleaning & Preprocessing

Handle missing values (Age, Embarked)

Drop irrelevant columns (Deck)

Create new features (Age Groups, Family Size)

Univariate Analysis

Distribution of individual variables

Target variable (Survival) analysis

Numerical and categorical distributions

Bivariate Analysis

Survival by gender, class, age

Relationships between variables

Statistical comparisons

Multivariate Analysis

Correlation matrix

Interaction effects

Complex relationships

Insights & Reporting

Statistical findings

Key insights

Automated markdown report generation

📊 Dataset Information
Source: Seaborn built-in Titanic dataset
Size: 891 passengers, 15 features
Time Period: 1912
Target Variable: survived (0 = No, 1 = Yes)

Key Features:

pclass: Passenger class (1st, 2nd, 3rd)

sex: Gender

age: Age in years

fare: Passenger fare

embarked: Port of embarkation

sibsp: Number of siblings/spouses aboard

parch: Number of parents/children aboard

📝 Report Contents
The generated Markdown report includes:

✅ Executive Summary - Key metrics at a glance
✅ Dataset Overview - Size, structure, and quality
✅ Data Cleaning Process - Preprocessing steps
✅ 10 High-Quality Visualizations - All charts included
✅ Statistical Insights - Detailed findings
✅ Survival Analysis - By gender, class, age, fare
✅ Correlation Analysis - Relationships between variables
✅ Conclusions & Recommendations - Actionable insights
✅ Complete Code - Reproducible analysis

🛠️ Technologies Used
Python 3.8+ - Programming language

Pandas - Data manipulation and analysis

NumPy - Numerical computations

Matplotlib - Basic plotting and visualization

Seaborn - Statistical data visualization

Jupyter - Interactive analysis environment

📚 Learning Outcomes
Through this project, you'll learn:

Complete EDA workflow from data loading to insights

Data cleaning techniques for real-world datasets

Statistical visualization best practices

Automated reporting for data science projects

Professional project structure for GitHub portfolios

Data storytelling with clear insights and conclusions

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👏 Acknowledgements
Titanic dataset provided by Seaborn library

Inspired by Kaggle's Titanic competition

Built with Python's data science ecosystem

Visualization styles inspired by data science best practices

📧 Contact & Support
For questions, issues, or suggestions:

Open an issue on GitHub

Check the report for detailed analysis

⭐ If you find this project useful, please give it a star! ⭐


## **📄 .gitignore** (Optional but recommended)

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# Environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Data (optional - include if data is generated)
# data/*.csv
# !data/titanic_cleaned.csv

# Images (optional - include if images are generated)
# images/*
# !images/01_*.png
# !images/02_*.png
# !images/03_*.png
# !images/04_*.png
# !images/05_*.png
# !images/06_*.png
# !images/07_*.png
# !images/08_*.png
# !images/09_*.png

# !images/10_*.png
