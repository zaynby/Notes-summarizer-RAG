# Practical 2.4 - Replacing-missing-values-by-an-arbitrary-number.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Imputation Techniques for Missing Data

## [[Imputation]]
**Definition**: The process of replacing missing values in a dataset with statistically estimated or predefined values to create a complete dataset for analysis or modeling.  
**Formula**: N/A  
**Example**:  
```python
# Imputing missing values using pandas
X_train[var] = X_train[var].fillna(99)
```

---

## [[Missing Data]]
**Definition**: Absence of values for certain observations in a dataset, often due to collection errors, non-response, or other factors.  
**Formula**: N/A  
**Example**:  
```python
# Checking percentage of missing values per variable
X_train.isnull().mean()
```

---

## [[Arbitrary Number Imputation]]
**Definition**: A technique where missing values are replaced with a predefined arbitrary constant (e.g., 99, -1) not close to the distribution’s mean/median.  
**Formula**:  
\[ \text{Imputed Value} = c \]  
where \( c \) is the arbitrary constant (e.g., 99).  
**Example**:  
```python
# Using Feature-engine's ArbitraryNumberImputer
imputer = ArbitraryNumberImputer(arbitrary_number=99, variables=['A2','A3', 'A8', 'A11'])
imputer.fit(X_train)
X_train = imputer.transform(X_train)
```

---

## [[Pandas Imputation]]
**Definition**: Using Pandas' `fillna()` method to replace missing values in a DataFrame.  
**Formula**: N/A  
**Example**:  
```python
# Replacing missing values with 99 in specified columns
for var in ['A2','A3', 'A8', 'A11']:
    X_train[var] = X_train[var].fillna(99)
    X_test[var] = X_test[var].fillna(99)
```

---

## [[Feature-engine]]
**Definition**: An open-source Python library for feature engineering tasks, including advanced imputation methods.  
**Formula**: N/A  
**Example**:  
```python
# Transforming data with Feature-engine imputer
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)
```

---

## [[Scikit-learn SimpleImputer (Constant Strategy)]]
**Definition**: Scikit-learn’s `SimpleImputer` class with `strategy='constant'` to fill missing values with a user-defined constant.  
**Formula**: N/A  
**Example**:  
```python
# Using Scikit-learn's SimpleImputer
imputer = SimpleImputer(strategy='constant', fill_value=99)
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## Verification of Imputation
**Definition**: Checking for the absence of missing values post-imputation.  
**Formula**: N/A  
**Example**:  
```python
# Confirming no missing values remain
X_train[['A2','A3', 'A8', 'A11']].isnull().sum()
```