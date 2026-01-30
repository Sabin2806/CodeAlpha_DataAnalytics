#!/usr/bin/env python3
"""
Titanic EDA Report Generator
Generates a complete Exploratory Data Analysis report for Titanic dataset

Usage:
    python generate_report.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
from datetime import datetime
import sys

# Suppress warnings
warnings.filterwarnings('ignore')

class TitanicEDA:
    """Titanic Exploratory Data Analysis Class"""
    
    def __init__(self):
        """Initialize the EDA class"""
        self.df = None
        self.df_clean = None
        self.project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Set visualization style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.rcParams['font.size'] = 12
        
        # Create directories
        self._create_directories()
    
    def _create_directories(self):
        """Create necessary directories for the project"""
        directories = ['data', 'reports', 'images']
        for directory in directories:
            dir_path = os.path.join(self.project_dir, directory)
            os.makedirs(dir_path, exist_ok=True)
            print(f"✅ Created directory: {directory}/")
    
    def load_data(self):
        """Load Titanic dataset from Seaborn"""
        print("📊 Loading Titanic dataset...")
        try:
            self.df = sns.load_dataset('titanic')
            print(f"✅ Dataset loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
            return True
        except Exception as e:
            print(f"❌ Error loading dataset: {e}")
            return False
    
    def clean_data(self):
        """Clean and preprocess the dataset"""
        print("\n🧹 Cleaning data...")
        self.df_clean = self.df.copy()
        
        # Fill missing age with median
        age_median = self.df_clean['age'].median()
        self.df_clean['age'].fillna(age_median, inplace=True)
        
        # Fill missing embarked with mode
        embarked_mode = self.df_clean['embarked'].mode()[0]
        self.df_clean['embarked'].fillna(embarked_mode, inplace=True)
        
        # Drop deck column (too many missing values)
        self.df_clean.drop('deck', axis=1, inplace=True, errors='ignore')
        
        # Drop any remaining missing values
        self.df_clean.dropna(inplace=True)
        
        # Create new features
        self.df_clean['age_group'] = pd.cut(self.df_clean['age'], 
                                           bins=[0, 12, 18, 35, 60, 100],
                                           labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])
        
        self.df_clean['fare_group'] = pd.qcut(self.df_clean['fare'], q=4,
                                             labels=['Low', 'Medium', 'High', 'Very High'])
        
        self.df_clean['family_size'] = self.df_clean['sibsp'] + self.df_clean['parch'] + 1
        self.df_clean['is_alone'] = (self.df_clean['family_size'] == 1).astype(int)
        
        # Save cleaned data
        data_path = os.path.join(self.project_dir, 'data', 'titanic_cleaned.csv')
        self.df_clean.to_csv(data_path, index=False)
        print(f"✅ Data cleaned and saved to: data/titanic_cleaned.csv")
        print(f"   Before: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        print(f"   After:  {self.df_clean.shape[0]} rows, {self.df_clean.shape[1]} columns")
        
        return True
    
    def create_visualizations(self):
        """Create all visualizations for the report"""
        print("\n🎨 Creating visualizations...")
        images_dir = os.path.join(self.project_dir, 'images')
        
        # 1. Survival Distribution
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Count plot
        sns.countplot(data=self.df_clean, x='survived', ax=axes[0], palette='Set2')
        axes[0].set_title('Survival Count', fontsize=14, pad=20)
        axes[0].set_xlabel('Survived (0=No, 1=Yes)', fontsize=12)
        axes[0].set_ylabel('Count', fontsize=12)
        
        # Pie chart
        survival_counts = self.df_clean['survived'].value_counts()
        axes[1].pie(survival_counts.values, labels=['Died', 'Survived'], 
                   autopct='%1.1f%%', colors=['#ff6b6b', '#4ecdc4'], 
                   explode=[0, 0.1], startangle=90)
        axes[1].set_title('Survival Distribution', fontsize=14, pad=20)
        
        plt.tight_layout()
        plt.savefig(os.path.join(images_dir, '01_survival_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # 2. Age Distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df_clean, x='age', kde=True, bins=30)
        plt.axvline(self.df_clean['age'].mean(), color='red', linestyle='--', 
                   label=f'Mean: {self.df_clean["age"].mean():.1f}')
        plt.axvline(self.df_clean['age'].median(), color='green', linestyle='--', 
                   label=f'Median: {self.df_clean["age"].median():.1f}')
        plt.title('Age Distribution of Passengers', fontsize=16, pad=20)
        plt.xlabel('Age', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.legend()
        plt.savefig(os.path.join(images_dir, '02_age_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # 3. Fare Distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df_clean, x='fare', kde=True, bins=30)
        plt.axvline(self.df_clean['fare'].mean(), color='red', linestyle='--', 
                   label=f'Mean: ${self.df_clean["fare"].mean():.2f}')
        plt.title('Fare Distribution', fontsize=16, pad=20)
        plt.xlabel('Fare ($)', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.legend()
        plt.savefig(os.path.join(images_dir, '03_fare_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # 4. Survival by Gender
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df_clean, x='sex', hue='survived', palette='Set2')
        plt.title('Survival by Gender', fontsize=16, pad=20)
        plt.xlabel('Gender', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.legend(['Died', 'Survived'])
        plt.savefig(os.path.join(images_dir, '04_survival_by_gender.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # 5. Survival by Passenger Class
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df_clean, x='class', hue='survived', palette='Set2')
        plt.title('Survival by Passenger Class', fontsize=16, pad=20)
        plt.xlabel('Class', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.legend(['Died', 'Survived'])
        plt.savefig(os.path.join(images_dir, '05_survival_by_class.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # 6. Correlation Heatmap
        numerical_df = self.df_clean.select_dtypes(include=[np.number])
        plt.figure(figsize=(10, 8))
        corr_matrix = numerical_df.corr()
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
        plt.title('Correlation Matrix of Numerical Features', fontsize=16, pad=20)
        plt.tight_layout()
        plt.savefig(os.path.join(images_dir, '06_correlation_heatmap.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # 7. Age vs Survival Boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.df_clean, x='survived', y='age', palette='Set2')
        plt.title('Age Distribution by Survival Status', fontsize=16, pad=20)
        plt.xlabel('Survived (0=No, 1=Yes)', fontsize=12)
        plt.ylabel('Age', fontsize=12)
        plt.savefig(os.path.join(images_dir, '07_age_vs_survival.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # 8. Fare vs Survival Boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.df_clean, x='survived', y='fare', palette='Set2')
        plt.title('Fare Distribution by Survival Status', fontsize=16, pad=20)
        plt.xlabel('Survived (0=No, 1=Yes)', fontsize=12)
        plt.ylabel('Fare ($)', fontsize=12)
        plt.savefig(os.path.join(images_dir, '08_fare_vs_survival.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # 9. Gender Distribution
        plt.figure(figsize=(8, 6))
        gender_counts = self.df_clean['sex'].value_counts()
        plt.pie(gender_counts.values, labels=gender_counts.index, 
               autopct='%1.1f%%', colors=['#ff9999', '#66b3ff'], startangle=90)
        plt.title('Gender Distribution', fontsize=16, pad=20)
        plt.savefig(os.path.join(images_dir, '09_gender_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        # 10. Passenger Class Distribution
        plt.figure(figsize=(8, 6))
        class_counts = self.df_clean['class'].value_counts()
        plt.pie(class_counts.values, labels=class_counts.index, 
               autopct='%1.1f%%', colors=['#ffcc99', '#99ff99', '#99ccff'], startangle=90)
        plt.title('Passenger Class Distribution', fontsize=16, pad=20)
        plt.savefig(os.path.join(images_dir, '10_class_distribution.png'), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ 10 visualizations saved to: images/ folder")
        return True
    
    def calculate_statistics(self):
        """Calculate key statistics for the report"""
        print("\n📈 Calculating statistics...")
        
        stats = {}
        
        # Basic statistics
        stats['total_passengers'] = len(self.df_clean)
        stats['survival_rate'] = self.df_clean['survived'].mean() * 100
        
        # Gender statistics
        stats['female_survival'] = self.df_clean[self.df_clean['sex'] == 'female']['survived'].mean() * 100
        stats['male_survival'] = self.df_clean[self.df_clean['sex'] == 'male']['survived'].mean() * 100
        
        # Class statistics
        stats['first_class_survival'] = self.df_clean[self.df_clean['class'] == 'First']['survived'].mean() * 100
        stats['second_class_survival'] = self.df_clean[self.df_clean['class'] == 'Second']['survived'].mean() * 100
        stats['third_class_survival'] = self.df_clean[self.df_clean['class'] == 'Third']['survived'].mean() * 100
        
        # Age statistics
        stats['avg_age'] = self.df_clean['age'].mean()
        stats['child_survival'] = self.df_clean[self.df_clean['age'] <= 12]['survived'].mean() * 100
        
        # Fare statistics
        stats['avg_fare'] = self.df_clean['fare'].mean()
        stats['fare_survival_corr'] = self.df_clean['fare'].corr(self.df_clean['survived'])
        
        # Additional statistics
        stats['survivor_avg_age'] = self.df_clean[self.df_clean['survived'] == 1]['age'].mean()
        stats['non_survivor_avg_age'] = self.df_clean[self.df_clean['survived'] == 0]['age'].mean()
        stats['survivor_avg_fare'] = self.df_clean[self.df_clean['survived'] == 1]['fare'].mean()
        stats['non_survivor_avg_fare'] = self.df_clean[self.df_clean['survived'] == 0]['fare'].mean()
        
        # Family statistics
        stats['alone_survival'] = self.df_clean[self.df_clean['is_alone'] == 1]['survived'].mean() * 100
        stats['with_family_survival'] = self.df_clean[self.df_clean['is_alone'] == 0]['survived'].mean() * 100
        
        # Embarkation statistics
        for port in ['C', 'Q', 'S']:
            stats[f'embarked_{port}_survival'] = self.df_clean[self.df_clean['embarked'] == port]['survived'].mean() * 100
        
        print("✅ Statistics calculated")
        return stats
    
    def generate_markdown_report(self, stats):
        """Generate comprehensive markdown report"""
        print("\n📝 Generating markdown report...")
        
        # Calculate ratios
        gender_ratio = stats['female_survival'] / stats['male_survival'] if stats['male_survival'] > 0 else 0
        class_ratio = stats['first_class_survival'] / stats['third_class_survival'] if stats['third_class_survival'] > 0 else 0
        
        # Get basic statistics as string
        stats_summary = self.df_clean.describe().round(2).to_string()
        
        # Create report
        report = f"""# 🚢 Titanic Dataset - Exploratory Data Analysis Report

**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Author:** Titanic EDA Project  
**Dataset:** Titanic Passenger List (1912)

## 📋 Executive Summary

| Metric | Value |
|--------|-------|
| **Total Passengers** | {stats['total_passengers']:,} |
| **Overall Survival Rate** | {stats['survival_rate']:.1f}% |
| **Female Survival Rate** | {stats['female_survival']:.1f}% |
| **Male Survival Rate** | {stats['male_survival']:.1f}% |
| **1st Class Survival Rate** | {stats['first_class_survival']:.1f}% |
| **3rd Class Survival Rate** | {stats['third_class_survival']:.1f}% |
| **Average Age** | {stats['avg_age']:.1f} years |
| **Average Fare** | ${stats['avg_fare']:.2f} |

## 📊 Dataset Overview

**Original Dataset:**
- Rows: {self.df.shape[0]:,}
- Columns: {self.df.shape[1]}
- Memory Usage: {self.df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB

**Cleaned Dataset:**
- Rows: {self.df_clean.shape[0]:,}
- Columns: {self.df_clean.shape[1]}
- Missing Values Remaining: {self.df_clean.isnull().sum().sum()}

## 🧹 Data Cleaning Process

1. **Age**: Filled {self.df['age'].isnull().sum()} missing values with median ({self.df_clean['age'].median():.1f})
2. **Embarked**: Filled {self.df['embarked'].isnull().sum()} missing values with mode ('{self.df_clean['embarked'].mode()[0]}')
3. **Deck**: Dropped column (77.1% missing values)
4. **New Features Created**:
   - Age Groups (Child, Teen, Young Adult, Adult, Senior)
   - Fare Groups (Low, Medium, High, Very High)
   - Family Size
   - Alone Status

## 📈 Key Visualizations

### 1. Survival Distribution
![Survival Distribution](images/01_survival_distribution.png)

### 2. Age Distribution
![Age Distribution](images/02_age_distribution.png)

### 3. Fare Distribution
![Fare Distribution](images/03_fare_distribution.png)

### 4. Survival by Gender
![Survival by Gender](images/04_survival_by_gender.png)

### 5. Survival by Passenger Class
![Survival by Class](images/05_survival_by_class.png)

### 6. Correlation Analysis
![Correlation Heatmap](images/06_correlation_heatmap.png)

### 7. Age vs Survival
![Age vs Survival](images/07_age_vs_survival.png)

### 8. Fare vs Survival
![Fare vs Survival](images/08_fare_vs_survival.png)

### 9. Gender Distribution
![Gender Distribution](images/09_gender_distribution.png)

### 10. Class Distribution
![Class Distribution](images/10_class_distribution.png)

## 🔍 Key Insights

### Gender Analysis
- **Female passengers** were {gender_ratio:.1f}x more likely to survive than male passengers
- **Survival rate by gender**:
  - Female: {stats['female_survival']:.1f}%
  - Male: {stats['male_survival']:.1f}%

### Class Analysis
- **1st class passengers** were {class_ratio:.1f}x more likely to survive than 3rd class passengers
- **Survival rate by class**:
  - 1st Class: {stats['first_class_survival']:.1f}%
  - 2nd Class: {stats['second_class_survival']:.1f}%
  - 3rd Class: {stats['third_class_survival']:.1f}%

### Age Analysis
- **Children (≤12 years)**: {stats['child_survival']:.1f}% survival rate
- **Average age difference**:
  - Survivors: {stats['survivor_avg_age']:.1f} years
  - Non-survivors: {stats['non_survivor_avg_age']:.1f} years

### Economic Factors
- **Fare correlation with survival**: {stats['fare_survival_corr']:.3f}
- **Average fare difference**:
  - Survivors: ${stats['survivor_avg_fare']:.2f}
  - Non-survivors: ${stats['non_survivor_avg_fare']:.2f}

### Family & Companions
- **Traveling alone**: {stats['alone_survival']:.1f}% survival rate
- **With family**: {stats['with_family_survival']:.1f}% survival rate

### Embarkation Port Analysis
- **Cherbourg (C)**: {stats['embarked_C_survival']:.1f}% survival
- **Queenstown (Q)**: {stats['embarked_Q_survival']:.1f}% survival
- **Southampton (S)**: {stats['embarked_S_survival']:.1f}% survival

## 📋 Statistical Summary

### Survival Rates by Category

| Category | Subcategory | Survival Rate | Count |
|----------|-------------|---------------|-------|
| Gender | Female | {stats['female_survival']:.1f}% | {len(self.df_clean[self.df_clean['sex'] == 'female']):,} |
| Gender | Male | {stats['male_survival']:.1f}% | {len(self.df_clean[self.df_clean['sex'] == 'male']):,} |
| Class | First | {stats['first_class_survival']:.1f}% | {len(self.df_clean[self.df_clean['class'] == 'First']):,} |
| Class | Second | {stats['second_class_survival']:.1f}% | {len(self.df_clean[self.df_clean['class'] == 'Second']):,} |
| Class | Third | {stats['third_class_survival']:.1f}% | {len(self.df_clean[self.df_clean['class'] == 'Third']):,} |
| Embarked | C | {stats['embarked_C_survival']:.1f}% | {len(self.df_clean[self.df_clean['embarked'] == 'C']):,} |
| Embarked | Q | {stats['embarked_Q_survival']:.1f}% | {len(self.df_clean[self.df_clean['embarked'] == 'Q']):,} |
| Embarked | S | {stats['embarked_S_survival']:.1f}% | {len(self.df_clean[self.df_clean['embarked'] == 'S']):,} |

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
"""
        
        # Save report
        report_path = os.path.join(self.project_dir, 'reports', 'TITANIC_EDA_REPORT.md')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ Markdown report saved to: reports/TITANIC_EDA_REPORT.md")
        return report_path
    
    def run_analysis(self):
        """Run complete analysis pipeline"""
        print("=" * 60)
        print("🚢 TITANIC EXPLORATORY DATA ANALYSIS")
        print("=" * 60)
        
        # Step 1: Load data
        if not self.load_data():
            return False
        
        # Step 2: Clean data
        if not self.clean_data():
            return False
        
        # Step 3: Create visualizations
        if not self.create_visualizations():
            return False
        
        # Step 4: Calculate statistics
        stats = self.calculate_statistics()
        
        # Step 5: Generate report
        report_path = self.generate_markdown_report(stats)
        
        # Display summary
        print("\n" + "=" * 60)
        print("✅ ANALYSIS COMPLETE!")
        print("=" * 60)
        print("\n📁 Generated Files:")
        print(f"   1. Cleaned Data: data/titanic_cleaned.csv")
        print(f"   2. Visualizations: images/ (10 charts)")
        print(f"   3. Report: {report_path}")
        
        print("\n📊 Key Statistics:")
        print(f"   • Total Passengers: {stats['total_passengers']:,}")
        print(f"   • Survival Rate: {stats['survival_rate']:.1f}%")
        print(f"   • Female Survival: {stats['female_survival']:.1f}%")
        print(f"   • Male Survival: {stats['male_survival']:.1f}%")
        
        print("\n🎯 To view the report:")
        print(f"   1. Open '{report_path}' in any markdown viewer")
        print(f"   2. Or view it directly on GitHub")
        
        return True

def main():
    """Main function"""
    try:
        # Check dependencies
        required_packages = ['pandas', 'numpy', 'matplotlib', 'seaborn']
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package)
            except ImportError:
                missing_packages.append(package)
        
        if missing_packages:
            print(f"❌ Missing packages: {', '.join(missing_packages)}")
            print("Please install using: pip install " + " ".join(missing_packages))
            return
        
        # Run analysis
        eda = TitanicEDA()
        success = eda.run_analysis()
        
        if success:
            print("\n✨ Titanic EDA completed successfully!")
            print("   All files have been generated in the project directory.")
        else:
            print("\n❌ Analysis failed. Please check the error messages above.")
            
    except KeyboardInterrupt:
        print("\n\n⚠️ Analysis interrupted by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()


