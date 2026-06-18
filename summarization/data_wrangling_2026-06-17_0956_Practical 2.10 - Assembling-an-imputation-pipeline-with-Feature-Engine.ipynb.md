# Practical 2.10 - Assembling-an-imputation-pipeline-with-Feature-Engine.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Imputing Missing Data with Feature-engine

## [[Missing Data Imputation]]
**Definition**: The process of replacing missing values in a dataset with statistically estimated values to enable machine learning model training.  
**Formula**: N/A  
**Example**:  
```python
pipe = Pipeline(steps=[  
    ('imp_num_arbitrary', mdi.ArbitraryNumberImputer(variables=features_num_arbitrary)),  
    ('imp_num_median', mdi.MeanMedianImputer(imputation_method='median', variables=features_num_median)),  
    ...  
])  
```

---

## [[Feature-engine]]
**Definition**: An open-source Python library for feature engineering, providing tools for imputation, encoding, and discretization.  
**Formula**: N/A  
**Example**:  
```python  
import feature_engine.imputation as mdi  # Importing imputation module  
```

---

## [[Arbitrary Number Imputer]]
**Definition**: Replaces missing values with a user-specified constant (e.g., 0).  
**Formula**:  
\[ \text{Imputed Value} = c \]  
where \( c \) is a constant.  
**Example**:  
```python  
SimpleImputer(strategy='constant', fill_value=0)  
# or  
mdi.ArbitraryNumberImputer(variables=features_num_arbitrary)  
```

---

## [[Mean/Median Imputer]]
**Definition**: Replaces missing values with the mean or median of the feature.  
**Formula**:  
- **Mean**:  
\[ \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i \]  
- **Median**: Middle value of ordered data.  
**Example**:  
```python  
SimpleImputer(strategy='median')  
# or  
mdi.MeanMedianImputer(imputation_method='median', variables=features_num_median)  
```

---

## [[Categorical Imputer]]
**Definition**: Replaces missing categorical values with the most frequent category or a 'missing' placeholder.  
**Formula**: N/A  
**Example**:  
```python  
mdi.CategoricalImputer(variables=features_cat_frequent, imputation_method='frequent')  
# or  
mdi.CategoricalImputer(variables=features_cat_missing, imputation_method='missing')  
```

---

## [[Pipeline]]
**Definition**: A sequence of data transformation steps combined into a single workflow.  
**Formula**: N/A  
**Example**:  
```python  
pipe = Pipeline(steps=[  
    ('imp_num_arbitrary', mdi.ArbitraryNumberImputer(...)),  
    ('imp_num_median', mdi.MeanMedianImputer(...)),  
])  
```

---

## [[ColumnTransformer]]
**Definition**: Applies different preprocessing steps to specific columns of a dataset.  
**Formula**: N/A  
**Example**:  
```python  
preprocessor = ColumnTransformer(transformers=[  
    ('num_arb', imputer_num_arb, num_arbitrary),  
    ('num_med', imputer_num_med, num_median),  
])  
```

---

## [[Train-Test Split]]
**Definition**: Dividing a dataset into training and testing subsets to evaluate model performance.  
**Formula**: N/A  
**Example**:  
```python  
X_train, X_test, y_train, y_test = train_test_split(  
    data.drop('A16', axis=1), data['A16'], test_size=0.3, random_state=0  
)  
```

---

## [[Handling Different Variable Types]]
**Definition**: Applying appropriate imputation techniques based on whether variables are numerical or categorical.  
**Formula**: N/A  
**Example**:  
```python  
cat_cols = [c for c in data.columns if data[c].dtypes == 'O']  # Categorical  
num_cols = [c for c in data.columns if data[c].dtypes != 'O']  # Numerical  
```

---

## [[Imputation Strategy]]
**Definition**: Selection of imputation methods based on data characteristics (e.g., missingness pattern, variable type) and model requirements.  
**Formula**: N/A  
**Example**:  
- Using **median imputation** for numerical variables with low missingness.  
- Using **'missing'** imputation for categorical variables with high missingness.  

---

**Wikilinks**:  
- [[Missing Data Imputation]] → [[Data Wrangling]]  
- [[Pipeline]] → [[Machine Learning Workflow]]  
- [[Feature-engine]] → [[Python Libraries for Data Science]]  
- [[ColumnTransformer]] → [[Scikit-learn]]