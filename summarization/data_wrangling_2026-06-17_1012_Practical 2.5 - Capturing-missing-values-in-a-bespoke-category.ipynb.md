# Practical 2.5 - Capturing-missing-values-in-a-bespoke-category.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Summary: Bespoke Category Imputation

#### Term: [[Bespoke Category Imputation]]  
**Definition**: A strategy for handling missing values in categorical variables by replacing them with a user-defined category (e.g., "Missing"). This treats missingness as a distinct group, preserving its potential informational value.  

**Formula**: N/A (categorical replacement strategy)  

**Examples**:  
1. **Pandas Implementation**:  
   ```python  
   for var in ['A4', 'A5', 'A6', 'A7']:  
       X_train[var] = X_train[var].fillna('Missing')  
       X_test[var] = X_test[var].fillna('Missing')  
   ```  
2. **Scikit-learn (`SimpleImputer`)**:  
   ```python  
   imputer = SimpleImputer(strategy='constant', fill_value='Missing')  
   X_train = imputer.fit_transform(X_train)  
   X_test = imputer.transform(X_test)  
   ```  
3. **Feature-engine (`CategoricalImputer`)**:  
   ```python  
   imputer = CategoricalImputer(variables=['A4', 'A5', 'A6', 'A7'])  
   X_train = imputer.fit_transform(X_train)  
   X_test = imputer.transform(X_test)  
   ```  

---

#### Term: [[SimpleImputer (Constant Strategy)]]  
**Definition**: Scikit-learn’s `SimpleImputer` with `strategy='constant'` allows users to fill missing values with a predefined constant (e.g., "Missing").  

**Formula**:  
$$ \text{Imputed Value} = \text{fill\_value} \quad \text{(user-specified constant)} $$  

**Example**:  
```python  
imputer = SimpleImputer(strategy='constant', fill_value='Missing')  
imputer.fit(X_train)  
X_train = imputer.transform(X_train)  
```  

---

#### Term: [[CategoricalImputer (Feature-engine)]]  
**Definition**: Feature-engine’s `CategoricalImputer` is designed to replace missing values in categorical variables with a specified category (e.g., "Missing"), learned from the training data.  

**Formula**: N/A (applies predefined category)  

**Example**:  
```python  
imputer = CategoricalImputer(variables=['A4', 'A5', 'A6', 'A7'])  
imputer.fit(X_train)  
X_train = imputer.transform(X_train)  
```  

---

#### Term: [[Pandas `fillna()` for Imputation]]  
**Definition**: Pandas’ `fillna()` method is used to replace missing values in DataFrame columns with a specified value (e.g., "Missing").  

**Formula**: N/A (direct value replacement)  

**Example**:  
```python  
X_train["A4"] = X_train["A4"].fillna('Missing')  
X_test["A4"] = X_test["A4"].fillna('Missing')  
```  

---

### Related Concepts  
- [[Missing Data Imputation]]  
- [[Categorical Variables]]  
- [[Scikit-learn]]  
- [[Feature-engine]]  
- [[Pandas]]  

This summary integrates methods for handling missing categorical data using bespoke categories, with implementations across pandas, scikit-learn, and Feature-engine.