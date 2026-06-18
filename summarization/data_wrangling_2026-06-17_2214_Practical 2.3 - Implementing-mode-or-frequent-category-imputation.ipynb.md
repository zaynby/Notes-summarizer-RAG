# Practical 2.3 - Implementing-mode-or-frequent-category-imputation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Frequent Category Imputation

## [[Frequent Category Imputation]]
**Definition**: A method for handling missing values in categorical variables by replacing them with the **mode** (most frequently occurring category) of the training dataset. This ensures consistency across train, test, and future datasets by storing the learned mode values.  
**Formula**: Mode = The value with the highest frequency in the training set.  
**Example**:  
```python
# Using pandas
for var in ['A4', 'A5', 'A6', 'A7']:
    value = X_train[var].mode()[0]
    X_train[var] = X_train[var].fillna(value)
    X_test[var] = X_test[var].fillna(value)
```

---

## [[Mode Imputation]]
**Definition**: Synonymous with Frequent Category Imputation; replaces missing values with the mode. Often used interchangeably but may apply to both categorical and numerical data (though less common for the latter).  
**Formula**: Same as Frequent Category Imputation.  
**Example**:  
```python
# Using scikit-learn's SimpleImputer
imputer = SimpleImputer(strategy='most_frequent')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## [[SimpleImputer (scikit-learn)]]
**Definition**: A scikit-learn class for imputation that supports strategies like `most_frequent` for categorical data. Learns the mode during `.fit()` and applies it during `.transform()`.  
**Formula**: N/A (method-based).  
**Example**:  
```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='most_frequent')
imputer.fit(X_train)  # Learns mode values
X_train = imputer.transform(X_train)
```

---

## [[CategoricalImputer (Feature-engine)]]
**Definition**: A Feature-engine transformer specifically designed for categorical imputation, including `frequent` strategy. Stores imputation mappings in `imputer_dict_`.  
**Formula**: N/A (method-based).  
**Example**:  
```python
from feature_engine.imputation import CategoricalImputer
mode_imputer = CategoricalImputer(variables=['A4', 'A5', 'A6', 'A7'], imputation_method='frequent')
mode_imputer.fit(X_train)
X_train = mode_imputer.transform(X_train)
```

---

## [[Train/Test Split]]
**Definition**: The process of dividing data into training and testing subsets to evaluate model performance. Critical for imputation to avoid data leakage.  
**Formula**: N/A (process-based).  
**Example**:  
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=0)
```

---

## [[Mode Calculation]]
**Definition**: The process of identifying the most frequent category in a dataset. Used in Frequent Category Imputation to determine replacement values.  
**Formula**:  
\[
\text{Mode} = \text{Value with } \max(\text{Frequency})
\]  
**Example**:  
```python
# Extract mode for a variable
mode_value = X_train['A4'].mode()[0]
```

---

## Key Links
- [[Data Wrangling]]  
- [[Missing Data Imputation]]  
- [[Scikit-learn Pipeline]]  
- [[Feature-engine Transformers]]