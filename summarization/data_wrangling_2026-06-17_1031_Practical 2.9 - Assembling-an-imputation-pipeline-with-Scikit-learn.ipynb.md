# Practical 2.9 - Assembling-an-imputation-pipeline-with-Scikit-learn.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured summary of the content using the requested format:

---

### [[Imputation Pipeline]]
**Definition**: A sequence of data preprocessing steps designed to handle missing values in a dataset using different strategies for various feature types.  
**Formula**: N/A (process-oriented concept)  
**Example**:  
```python
preprocessor = ColumnTransformer([...])
preprocessor.fit(X_train)
X_train = preprocessor.transform(X_train)
```

---

### [[ColumnTransformer]]
**Definition**: A scikit-learn class that applies different column-specific transformers to subsets of data features.  
**Formula**: N/A (structural component)  
**Example**:  
```python
preprocessor = ColumnTransformer(
    transformers=[
        ('imp_num_arbitrary', imputer_num_arbitrary, features_num_arbitrary),
        ('imp_num_median', imputer_num_median, features_num_median)
    ]
)
```

---

### [[SimpleImputer]]
**Definition**: A scikit-learn class for filling missing values using specified strategies.  
**Formula**:  
- For numerical: \( \text{Imputed value} = \begin{cases} 
  \text{median}(X) & \text{if strategy='median'} \\
  c & \text{if strategy='constant'} 
\end{cases} \)  
- For categorical: \( \text{Imputed value} = \text{mode}(X) \) (most frequent)  
**Example**:  
```python
imputer_num_median = Pipeline([('imputer', SimpleImputer(strategy='median'))])
```

---

### [[Constant Imputation]]
**Definition**: Replaces missing values with a user-defined constant.  
**Formula**: \( \text{Imputed value} = c \) (where \( c \) is the specified constant)  
**Example**:  
```python
SimpleImputer(strategy='constant', fill_value=99)
```

---

### [[Median Imputation]]
**Definition**: Replaces missing values with the median of the observed data.  
**Formula**: \( \text{Median} = \text{middle value of sorted observations} \)  
**Example**:  
```python
SimpleImputer(strategy='median')
```

---

### [[Most Frequent Imputation]]
**Definition**: Replaces missing values with the most frequent category or value.  
**Formula**: \( \text{Mode} = \text{most frequently occurring value} \)  
**Example**:  
```python
SimpleImputer(strategy='most_frequent')
```

---

### [[Feature Engineering]]
**Definition**: The process of transforming raw data into features suitable for modeling.  
**Formula**: N/A (broad concept)  
**Example**:  
```python
features_num_arbitrary = ['A3', 'A8']  # Custom feature grouping
```

---

### [[Pipeline (scikit-learn)]]
**Definition**: Chains multiple preprocessing steps or models into a single unit.  
**Formula**: N/A (methodological concept)  
**Example**:  
```python
imputer_num_arbitrary = Pipeline([('imputer', SimpleImputer(...))])
```

---

### Key Workflow Steps:
1. **Data Splitting**: `train_test_split` for training/testing sets.  
2. **Feature Categorization**: Separate numerical/categorical features.  
3. **Imputer Initialization**: Define strategies for specific feature groups.  
4. **ColumnTransformer Assembly**: Combine imputers for parallel execution.  
5. **Fit/Transform**: Apply pipeline to training/test data.  

All concepts are interconnected through [[Feature Engineering]] and [[Imputation Pipeline]] design.