# 🚢 Titanic Dataset - Exploratory Data Analysis Report

**Generated on:** 2026-01-30 12:22:42  
**Author:** Titanic EDA Project  
**Dataset:** Titanic Passenger List (1912)

## 📋 Executive Summary

| Metric | Value |
|--------|-------|
| **Total Passengers** | 712 |
| **Overall Survival Rate** | 40.4% |
| **Female Survival Rate** | 75.3% |
| **Male Survival Rate** | 20.5% |
| **1st Class Survival Rate** | 65.2% |
| **3rd Class Survival Rate** | 23.9% |
| **Average Age** | 29.6 years |
| **Average Fare** | $34.57 |

## 📊 Dataset Overview

**Original Dataset:**
- Rows: 891
- Columns: 15
- Memory Usage: 0.27 MB

**Cleaned Dataset:**
- Rows: 712
- Columns: 18
- Missing Values Remaining: 0

## 🧹 Data Cleaning Process

1. **Age**: Filled 177 missing values with median (28.0)
2. **Embarked**: Filled 2 missing values with mode ('S')
3. **Deck**: Dropped column (77.1% missing values)
4. **New Features Created**:
   - Age Groups (Child, Teen, Young Adult, Adult, Senior)
   - Fare Groups (Low, Medium, High, Very High)
   - Family Size
   - Alone Status

## 📈 Key Visualizations

### 1. Survival Distribution
![Survival Distribution](CodeAlpha_DataAnalytics/CodeAlpha_EDA/images/01_survival_distribution.png)

### 2. Age Distribution
![Age Distribution](CodeAlpha_EDA/images/02_age_distribution.png)

### 3. Fare Distribution
![Fare Distribution](CodeAlpha_EDA/images/03_fare_distribution.png)

### 4. Survival by Gender
![Survival by Gender](CodeAlpha_EDA/images/04_survival_by_gender.png)

### 5. Survival by Passenger Class
![Survival by Class](CodeAlpha_EDA/images/05_survival_by_class.png)

### 6. Correlation Analysis
![Correlation Heatmap](CodeAlpha_EDA/images/06_correlation_heatmap.png)

### 7. Age vs Survival
![Age vs Survival](CodeAlpha_EDA/images/07_age_vs_survival.png)

### 8. Fare vs Survival
![Fare vs Survival](CodeAlpha_EDA/images/08_fare_vs_survival.png)

### 9. Gender Distribution
![Gender Distribution](CodeAlpha_EDA/images/09_gender_distribution.png)

### 10. Class Distribution
![Class Distribution](CodeAlpha_EDA/images/10_class_distribution.png)

## 🔍 Key Insights

### Gender Analysis
- **Female passengers** were 3.7x more likely to survive than male passengers
- **Survival rate by gender**:
  - Female: 75.3%
  - Male: 20.5%

### Class Analysis
- **1st class passengers** were 2.7x more likely to survive than 3rd class passengers
- **Survival rate by class**:
  - 1st Class: 65.2%
  - 2nd Class: 48.0%
  - 3rd Class: 23.9%

### Age Analysis
- **Children (≤12 years)**: 58.0% survival rate
- **Average age difference**:
  - Survivors: 28.2 years
  - Non-survivors: 30.6 years

### Economic Factors
- **Fare correlation with survival**: 0.266
- **Average fare difference**:
  - Survivors: $51.65
  - Non-survivors: $22.97

### Family & Companions
- **Traveling alone**: 31.8% survival rate
- **With family**: 51.6% survival rate

### Embarkation Port Analysis
- **Cherbourg (C)**: 60.8% survival
- **Queenstown (Q)**: 28.6% survival
- **Southampton (S)**: 36.3% survival

## 📋 Statistical Summary

### Survival Rates by Category

| Category | Subcategory | Survival Rate | Count |
|----------|-------------|---------------|-------|
| Gender | Female | 75.3% | 259 |
| Gender | Male | 20.5% | 453 |
| Class | First | 65.2% | 184 |
| Class | Second | 48.0% | 173 |
| Class | Third | 23.9% | 355 |
| Embarked | C | 60.8% | 130 |
| Embarked | Q | 28.6% | 28 |
| Embarked | S | 36.3% | 554 |

## 💡 Conclusions & Recommendations

### Key Conclusions
1. **Gender was the strongest predictor** of survival, with women having significantly higher survival rates
2. **Socioeconomic status** (as indicated by passenger class) played a crucial role in survival chances
3. **Age was a factor**, with children having better survival rates than adults
4. **Traveling with family** slightly increased survival chances compared to traveling alone
5. **Fare price correlated with survival**, indicating economic inequality in safety measures

### Historical Recommendations
1. **Prioritize vulnerable groups** - The "women and children first" policy was evident in the data
2. **Address class inequality** - Ensure equal access to safety equipment for all passenger classes
3. **Family coordination** - Develop family-based evacuation protocols
4. **Economic transparency** - Ensure safety measures aren't tied to ticket price

### Modern Implications
- Importance of equitable safety protocols in transportation
- Need for clear evacuation procedures that don't discriminate by demographics
- Value of historical data analysis for improving modern safety standards

## 📁 Project Structure
titanic_eda_project/
├── data/ # Data files
│ └── titanic_cleaned.csv
├── notebooks/ # Jupyter notebook
│ └── titanic_eda.ipynb
├── reports/ # Generated reports
│ └── TITANIC_EDA_REPORT.md
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
│ └── generate_report.py
├── requirements.txt # Python dependencies
├── environment.yml # Conda environment
└── README.md # Project documentation

## 🔗 References
1. Titanic dataset from Seaborn library
2. Historical records of RMS Titanic
3. Python Data Science Stack: Pandas, NumPy, Matplotlib, Seaborn

---
*Report generated automatically by Titanic EDA Analysis System*

