# Practical 2.9 - Assembling-an-imputation-pipeline-with-Scikit-learn.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

## Summary: Assembling an Imputation Pipeline with Scikit-Learn

### [[Imputation Pipeline]]
**Definition**: A structured workflow that chains multiple data preprocessing steps (e.g., imputation strategies) to handle missing values in different subsets of a dataset.  
**Formula**: N/A  
**Example**:  
```python
preprocessor = ColumnTransformer(transformers=[
    ('imp_num_arbitrary', imputer_num_arbitrary, features_num_arbitrary),
    ('imp_num_median', imputer_num_median, features_num_median),
    ('imp_cat_frequent', imputer_cat_frequent, features_cat_frequent),
    ('imp_cat_missing', imputer_cat_missing, features_cat_missing)
])
```

---

### [[ColumnTransformer]]
**Definition**: A scikit-learn class that applies distinct transformers to specific columns of a dataset, enabling tailored preprocessing for numerical and categorical features.  
**Formula**: N/A  
**Example**:  
```python
preprocessor = ColumnTransformer(
    transformers=[
        ('imp_num_arbitrary', Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value=99))]), ['A3', 'A8'])
    ],
    remainder='passthrough'
)
```

---

### [[SimpleImputer]]
**Definition**: A scikit-learn class for filling missing values using strategies like mean, median, most frequent, or constant values.  
**Formula**:  
- **Median Imputation**: \( \text{Replace missing values with } \mu = \text{median}(x) \)  
- **Most Frequent Imputation**: \( \text{Replace missing values with mode}(x) \)  
**Example**:  
```python
imputer_num_median = Pipeline(steps=[('imputer', SimpleImputer(strategy='median'))])
```

---

### [[Arbitrary Number Imputation]]
**Definition**: Replaces missing numerical values with a user-defined constant (e.g., 99).  
**Formula**: \( x_{\text{missing}} \rightarrow c \) (where \( c \) is a constant)  
**Example**:  
```python
SimpleImputer(strategy='constant', fill_value=99)
```

---

### [[Median Imputation]]
**Definition**: Replaces missing numerical values with the median of the column.  
**Formula**: \( x_{\text{missing}} \rightarrow \mu = \text{median}(x) \)  
**Example**:  
```python
SimpleImputer(strategy='median')
```

---

### [[Most Frequent Imputation (Categorical)]]
**Definition**: Replaces missing categorical values with the most frequent category in the column.  
**Formula**: \( x_{\text{missing}} \rightarrow \text{mode}(x) \)  
**Example**:  
```python
SimpleImputer(strategy='most_frequent')
```

---

### [[Missing Category Imputation]]
**Definition**: Adds a new category (e.g., "Missing") to represent missing values in categorical variables.  
**Formula**: N/A  
**Example**:  
```python
SimpleImputer(strategy='constant', fill_value='Missing')
```

---

### [[Train-Test Split]]
**Definition**: Divides a dataset into training and testing subsets to evaluate model performance without data leakage.  
**Formula**: N/A  
**Example**:  
```python
X_train, X_test, y_train, y_test = train_test_split(
    data.drop('A16', axis=1), data['A16'], test_size=0.3, random_state=0
)
```

---

### [[Handling Missing Data]]
**Definition**: The process of addressing missing values in a dataset through imputation, deletion, or other methods to ensure data quality for analysis.  
**Formula**: N/A  
**Example**:  
```python
# Identifying missing values
X_train.isnull().mean()
# Imputing missing values
X_train = preprocessor.transform(X_train)
``` 

---

### Key Notes:
1. **Column Order**: Scikit-learn transformers may reorder columns and return NumPy arrays instead of DataFrames.  
2. **Strategies by Variable Type**:  
   - **Numerical**: Arbitrary number, median.  
   - **Categorical**: Most frequent, "Missing" category.  
3. **Pipeline Integration**: Combines preprocessing steps (e.g., imputation) with model training in a single workflow.  

[[Data Leakage]] should be avoided by fitting the pipeline only on the training data before transforming test data.