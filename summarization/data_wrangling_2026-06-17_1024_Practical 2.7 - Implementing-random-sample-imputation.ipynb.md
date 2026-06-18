# Practical 2.7 - Implementing-random-sample-imputation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Random Sample Imputation  

## [[Random Sample Imputation]]  
**Definition**: A technique that replaces missing values by randomly sampling from the observed values in the dataset, preserving the original data distribution. Suitable for both numerical and categorical variables.  

**Formula**:  
For a variable with *n* missing values:  
1. Extract a random sample of size *n* from the observed data.  
2. Assign this sample to the missing value positions.  

**Example**:  
```python  
# Using pandas  
number_missing = X_train['A2'].isnull().sum()  
random_sample = X_train['A2'].dropna().sample(number_missing, random_state=0)  
X_train.loc[X_train['A2'].isnull(), 'A2'] = random_sample.values  
```  

---

## [[Pandas Implementation]]  
**Definition**: Manual implementation of random sample imputation using pandas functions to handle missing data.  

**Formula**:  
1. Calculate missing values per variable.  
2. Sample observed data to match the number of missing values.  
3. Reindex the sample to align with missing positions.  
4. Replace missing values in both training and test sets.  

**Example**:  
```python  
for var in ['A1', 'A3', 'A4']:  
    # Train set  
    sample_train = X_train[var].dropna().sample(X_train[var].isnull().sum(), random_state=0)  
    sample_train.index = X_train[X_train[var].isnull()].index  
    X_train.loc[X_train[var].isnull(), var] = sample_train.values  
    # Repeat for test set  
```  

---

## [[Feature-engine Implementation]]  
**Definition**: Uses the `RandomSampleImputer` class from the `feature_engine` library to streamline the imputation process.  

**Formula**:  
1. Fit the imputer on the training data to learn the sampling distribution.  
2. Transform both training and test sets to replace missing values.  

**Example**:  
```python  
from feature_engine.imputation import RandomSampleImputer  
imputer = RandomSampleImputer()  
imputer.fit(X_train)  
X_train = imputer.transform(X_train)  
X_test = imputer.transform(X_test)  
```  

---

## Key Links  
- [[Missing Data]]: Absence of values in a dataset.  
- [[Imputation Techniques]]: Methods to replace missing data (e.g., mean, median, mode).  
- [[SimpleImputer]]: Scikit-learn’s basic imputation tool.  
- [[Data Preprocessing]]: General steps for preparing data for analysis.  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).