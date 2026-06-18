# Practical 2.5 - Capturing-missing-values-in-a-bespoke-category.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Bespoke Category Imputation for Missing Data  

## [[Bespoke Category Imputation]]  
**Definition**: A technique for handling missing values in categorical variables by replacing them with a custom category (e.g., "Missing"). This approach treats missingness as a distinct category, preserving the variable’s categorical nature.  

**Formula**:  
\[
\text{Missing value} \rightarrow \text{"Missing"}
\]

**Example**:  
```python
# Using pandas to replace missing values with "Missing"
for var in ['A4', 'A5', 'A6', 'A7']:
    X_train[var] = X_train[var].fillna('Missing')
    X_test[var] = X_test[var].fillna('Missing')
```  

---

## [[CategoricalImputer (Feature-engine)]]  
**Definition**: A transformer from the `feature_engine` library designed to impute missing categorical values with a specified bespoke category (e.g., "Missing"). It learns the imputation value from the training set.  

**Formula**:  
\[
\text{Missing value} \rightarrow \text{User-defined category (e.g., "Missing")}
\]

**Example**:  
```python
# Initialize and apply CategoricalImputer
imputer = CategoricalImputer(variables=['A4', 'A5', 'A6', 'A7'], fill_with='Missing')
imputer.fit(X_train)
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)
```  

---

## [[SimpleImputer (scikit-learn)]]  
**Definition**: Scikit-learn’s `SimpleImputer` with a `constant` strategy allows replacing missing values with a user-specified value (e.g., "Missing"). Note that it returns a NumPy array.  

**Formula**:  
\[
\text{Missing value} \rightarrow \text{Constant (e.g., "Missing")}
\]

**Example**:  
```python
# Using SimpleImputer with constant strategy
imputer = SimpleImputer(strategy='constant', fill_value='Missing')
imputer.fit(X_train)
X_train = imputer.transform(X_train)  # Returns NumPy array
X_test = imputer.transform(X_test)
```  

---

## Key Workflow Steps  
1. **Data Splitting**: Use `train_test_split` to separate data into training and testing sets.  
2. **Imputation**: Apply imputation technique (pandas, Feature-engine, or scikit-learn) to replace missing values.  
3. **Validation**: Verify absence of missing values using `isnull().sum()` or `isnull().mean()`.  

**Context**: Demonstrated on the `creditApprovalUCI.csv` dataset, targeting categorical variables (e.g., `A4`, `A5`, `A6`, `A7`).  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).  

--- 

[[Imputation Methods]] | [[Missing Data Handling]] | [[Categorical Variables]]