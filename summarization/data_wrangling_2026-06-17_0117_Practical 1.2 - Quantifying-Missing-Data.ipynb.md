# Practical 1.2 - Quantifying-Missing-Data.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### [[Missing Data]]
**Definition**: The absence of values for certain observations within a variable in a dataset, a common issue in real-world data sources.  
**Formula**: N/A  
**Example**: In the KDD-CUP-98 dataset, variables like `AGE` or `INCOME` may contain missing entries, which can be detected using `data.isnull().sum()`.

---

### [[Quantifying Missing Values]]
**Definition**: The process of measuring the extent of missing data in a dataset, often expressed as counts or percentages.  
**Formula**:  
Percentage of missing values = (Number of missing values / Total number of observations) × 100  
**Example**: Using `data.isnull().mean()` to calculate the percentage of missing values per variable (e.g., `0.15` indicates 15% missing values in a variable).

---

### [[Visualizing Missing Data]]
**Definition**: Representing the proportion of missing values graphically to enable intuitive interpretation of data quality issues.  
**Formula**: N/A  
**Example**: Generating a bar chart with `data.isnull().mean().plot.bar()` to visualize missing data percentages across variables, as shown in the practical.

---

### [[KDD-CUP-98 Dataset]]
**Definition**: A dataset from the UCI Machine Learning Repository, used in this practical to demonstrate missing data quantification and visualization.  
**Formula**: N/A  
**Example**: The dataset includes variables such as `AGE`, `NUMCHLD`, and `INCOME`, which are loaded using `pd.read_csv('./data/cup98LRN.txt', usecols=cols)` for analysis.  

---

This summary connects key concepts for handling missing data, with links to related techniques like [[Imputation]] (not covered in this practical but relevant for subsequent steps).