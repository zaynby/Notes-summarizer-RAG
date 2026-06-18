# Practical 2.10 - Assembling-an-imputation-pipeline-with-Feature-Engine.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

## Summary: Imputation Techniques with Feature-engine

### [[Arbitrary Number Imputer]]  
**Definition**: Replaces missing values in numerical features with a user-specified arbitrary constant (e.g., 0, -999).  
**Formula**: \( X_{\text{missing}} = c \) (where \( c \) is the chosen constant).  
**Example**:  
```python
('imp_num_arbitrary', mdi.ArbitraryNumberImputer(variables = features_num_arbitrary))
```

---

### [[Mean/Median Imputer]]  
**Definition**: Imputes missing values in numerical features using either the mean or median of the observed data.  
**Formula**:  
- Median: \( X_{\text{missing}} = \text{median}(X) \)  
- Mean: \( X_{\text{missing}} = \text{mean}(X) \)  
**Example**:  
```python
('imp_num_median', mdi.MeanMedianImputer(imputation_method = 'median', variables=features_num_median))
```

---

### [[Categorical Imputer (Frequent)]]  
**Definition**: Fills missing values in categorical features with the most frequent category (mode) observed in the data.  
**Formula**: \( X_{\text{missing}} = \text{mode}(X) \)  
**Example**:  
```python
('imp_cat_frequent', mdi.CategoricalImputer(variables = features_cat_frequent, imputation_method='frequent'))
```

---

### [[Categorical Imputer (Missing)]]  
**Definition**: Replaces missing values in categorical features with a placeholder value (e.g., "Missing").  
**Formula**: \( X_{\text{missing}} = \text{"Missing"} \)  
**Example**:  
```python
('imp_cat_missing', mdi.CategoricalImputer(variables=features_cat_missing, imputation_method='missing'))
```

---

### [[Pipeline (Scikit-learn)]]  
**Definition**: A sequential workflow that chains multiple preprocessing steps (e.g., imputers) into a single object. Each step is applied in order.  
**Formula**: \( \text{Pipeline} = \text{Step1} \rightarrow \text{Step2} \rightarrow \ldots \rightarrow \text{StepN} \)  
**Example**:  
```python
pipe = Pipeline(steps=[ 
    ('imp_num_arbitrary', mdi.ArbitraryNumberImputer(variables = features_num_arbitrary)),
    ('imp_num_median', mdi.MeanMedianImputer(imputation_method = 'median', variables=features_num_median)),
    ('imp_cat_frequent', mdi.CategoricalImputer(variables = features_cat_frequent, imputation_method='frequent')),
    ('imp_cat_missing', mdi.CategoricalImputer(variables=features_cat_missing, imputation_method='missing'))
])
```

---

### [[Credit Approval Dataset]]  
**Definition**: A dataset used for demonstrating imputation techniques, containing numerical and categorical features with missing values.  
**Example**:  
```python
data = pd.read_csv("./data/creditApprovalUCI.csv")
```

---

### Key Workflow Steps  
1. **Data Splitting**:  
   ```python
   X_train, X_test, y_train, y_test = train_test_split(data.drop('A16', axis=1), data['A16'], test_size=0.3, random_state=0)
   ```
2. **Imputation Pipeline**:  
   - Fit the pipeline to training data: `pipe.fit(X_train)`  
   - Transform train/test data: `X_train = pipe.transform(X_train)`  

---

### Outcome  
- Missing values are replaced based on feature type (numerical/categorical) and imputation strategy.  
- Final dataset retains original column order (as per Feature-engine behavior).