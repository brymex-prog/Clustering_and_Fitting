# Used Car Data Analysis – Clustering, Line Fitting & Statistical Insights

## Overview
This project explores **patterns, relationships, and trends** within a used car dataset using a combination of:
- Statistical analysis  
- Data visualisation  
- Clustering methods  
- Line fitting techniques  

The goal is to understand how different features (e.g., price, mileage, age, brand, engine size) influence each other and identify meaningful segments within the dataset.

---

## Objectives
- Analyse the distribution and trends in used car pricing.
- Identify relationships between car features such as mileage, age, engine size, and brand.
- Apply clustering techniques to segment used cars into meaningful groups.
- Use line fitting (regression) to model relationships between variables.
- Visualise the dataset to support interpretation and insights.

---

## Dataset
The dataset contains various attributes of used cars, such as:
- Price  
- Mileage  
- Make/Model  
- Engine size  
- Fuel type  
- Transmission  
- Other car specifications  

Data was cleaned and prepared before analysis.

---

## Tools & Libraries Used
- **Python**
- **Pandas** (data cleaning & manipulation)
- **NumPy** (numerical computations)
- **Matplotlib / Seaborn** (visualisation)
- **Scikit-Learn** (clustering & modelling)
- **Jupyter Notebook**

---

## Analysis Workflow

### 1. **Data Cleaning**
- Removed duplicates  
- Handled missing values  
- Converted data types  
- Standardised categorical values  

### 2. **Exploratory Data Analysis (EDA)**
- Summary statistics  
- Distribution plots  
- Correlation analysis  
- Brand/price comparisons  

### 3. **Clustering**
- Applied clustering algorithms (e.g., K-Means)  
- Identified segments such as:
  - High-priced, low-mileage vehicles  
  - Older, low-cost vehicles  
  - Mid-range standard cars  
- Visualised clusters to understand group characteristics  

### 4. **Line Fitting / Regression**
- Fitted regression lines to explore relationships such as:
  - Mileage vs Price  
  - Age vs Price  
- Assessed strength of relationships using metrics  

### 5. **Visualisation**
- Scatter plots  
- Heatmaps  
- Cluster plots  
- Regression/line fitting graphs  


- Price tends to decrease significantly as **mileage increases**.  
- Newer vehicles generally retain **higher value** regardless of brand.  
- Clustering reveals clear groupings based on mileage, and engine features.  
- Line fitting confirms strong negative correlation between price and mileage.  
- Some brands show more stable pricing trends than others.

---

## Conclusion
The analysis highlights how statistical methods, clustering, and regression can be combined to uncover valuable insights from automotive datasets.  
Understanding these relationships can support pricing strategies, customer segmentation, and predictive modelling for used-car markets.

