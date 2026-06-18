# Practical 2.3 - Implementing-mode-or-frequent-category-imputation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### [[Frequent Category Imputation]]  
**Definition**: A technique to replace missing values in categorical variables with the **mode** (most frequently occurring category) estimated from the training dataset. The mode is stored and applied to training, test, and future datasets to ensure consistency.  

**Formula**:  
Mode = \( \text{argmax}_k(\text{count of category } k \text{ in training set}) \)  

**Example**:  
- **Pandas**:  
  ```python  
  value = X_train[var].mode()[0]  
  X_train[var].fillna(value, inplace=True)  
  X_test[var].fillna(value, inplace=True)  
  ```  
- **Feature-engine**:  
  ```python  
  mode_imputer = mdi.CategoricalImputer(variables=['A4', 'A5'], imputation_method='frequent')  
  mode_imputer.fit(X_train)  
  X_train = mode_imputer.transform(X_train)  
  ```  
- **Scikit-learn**:  
  ```python  
  imputer = SimpleImputer(strategy='most_frequent')  
  X_train = imputer.fit_transform(X_train)  
  X_test = imputer.transform(X_test)  
  ```  

---

### [[Pandas Frequent Imputation]]  
**Definition**: Using Pandas' `fillna` method to manually replace missing categorical values with the mode computed from the training set.  

**Formula**:  
Mode = \( \text{X_train[var].mode()[0]} \)  

**Example**:  
```python  
for var in ['A4', 'A5']:  
    value = X_train[var].mode()[0]  
    X_train[var].fillna(value, inplace=True)  
    X_test[var].fillna(value, inplace=True)  
```  

---

### [[Feature-engine CategoricalImputer]]  
**Definition**: A transformer from the **Feature-engine** library that automates frequent category imputation by learning the mode during `fit` and storing it in `imputer_dict_`.  

**Formula**:  
\( \text{imputer_dict_} = \{\text{variable: mode for each variable}\} \)  

**Example**:  
```python  
mode_imputer = mdi.CategoricalImputer(variables=['A6', 'A7'], imputation_method='frequent')  
mode_imputer.fit(X_train)  
X_train = mode_imputer.transform(X_train)  
```  

---

### [[Scikit-learn SimpleImputer (most_frequent)]]  
**Definition**: Scikit-learn’s `SimpleImputer` with the `most_frequent` strategy, which replaces missing values in categorical features with the mode learned from the training set.  

**Formula**:  
\( \text{statistics_} = \text{mode of each feature in the training set} \)  

**Example**:  
```python  
imputer = SimpleImputer(strategy='most_frequent')  
X_train = imputer.fit_transform(X_train)  
X_test = imputer.transform(X_test)  
```  

--- 

**Key Concepts**:  
- [[Mode]]: Most frequent category in a dataset.  
- [[Training Set]]: Data used to learn imputation parameters (e.g., mode).  
- [[Test Set]]: Data imputed using parameters learned from the training set.