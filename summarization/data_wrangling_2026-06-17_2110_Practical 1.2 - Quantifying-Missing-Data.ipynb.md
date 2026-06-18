# Practical 1.2 - Quantifying-Missing-Data.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary of Key Concepts in Data Wrangling

## [[Missing Data]]
**Definition**: The absence of values for certain observations within a variable, commonly encountered in real-world datasets.  
**Formula**: Not applicable (descriptive concept).  
**Example**:  
```python
# Detect missing values in the dataset
data.isnull().sum()  # Quantify total missing values per variable
data.isnull().mean()  # Calculate percentage of missing values per variable
```

---

## [[Quantifying Missing Values]]
**Definition**: The process of measuring the extent of missing data in a dataset, either as absolute counts or relative percentages.  
**Formula**:  
- Absolute count: \( \text{Total Missing} = \sum (\text{isnull()}) \)  
- Percentage: \( \text{Percentage Missing} = \frac{\text{Total Missing}}{\text{Total Observations}} \times 100 \)  
**Example**:  
```python
# Calculate percentage of missing values per variable
data.isnull().mean().plot.bar(figsize=(12,6))
plt.ylabel('Percentage of Missing Values')
plt.xlabel('Variables')
plt.title('Quantifying Missing Data')
```

---

## [[Visualizing Missing Data]]
**Definition**: Representing the distribution and proportion of missing values graphically to identify patterns or outliers.  
**Formula**: Not applicable (visualization technique).  
**Example**:  
```python
# Bar plot of missing value percentages
data.isnull().mean().plot.bar(figsize=(12,6))
plt.ylabel('Percentage of Missing Values')
plt.xlabel('Variables')
plt.title('Visualizing Missing Data')
plt.show()
```

---

## [[Variables]]
**Definition**: Characteristics or attributes measured in a dataset, categorized into numerical or categorical types.  
**Subtypes**:  
- **Numerical Variables**: Discrete (countable, e.g., `NUMCHLD`) or continuous (measurable, e.g., `INCOME`).  
- **Categorical Variables**: Represented by labels (e.g., `MBCRAFT`).  
**Example**:  
```python
# Select and load specific variables from the dataset
cols = ['AGE', 'NUMCHLD', 'INCOME', 'WEALTH1', 'MBCRAFT', 'MBGARDEN', 'MBBOOKS', 'MBCOLECT', 'MAGFAML', 'MAGFEM', 'MAGMALE']
data = pd.read_csv('./data/cup98LRN.txt', usecols=cols)
```

---

## [[Imputation]]
**Definition**: The process of replacing missing values with statistical estimates to create a complete dataset for machine learning models.  
**Formula**: Not applicable (process-dependent, e.g., mean imputation: \( \text{Imputed Value} = \text{Mean of Observed Values} \)).  
**Example**:  
```python
# Example of mean imputation (not shown in provided code)
data['COLUMN_NAME'].fillna(data['COLUMN_NAME'].mean(), inplace=True)
```

---

## Related Concepts  
- [[Scikit-learn]]: A Python library that requires complete numerical data, necessitating imputation or removal of missing values.  
- [[Outliers]]: Data points significantly deviating from the norm, often addressed alongside missing data.  

This summary integrates concepts from the provided notebooks, emphasizing practical implementation in Python.