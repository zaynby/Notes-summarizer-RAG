# Practical 2.8 - Adding-a-missing-value-indicator-variable.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Adding Missing Value Indicator Variables

## [[Missing Value Indicator]]
### Definition
A binary variable that flags whether an observation originally had a missing value (1) for the respective feature or not (0). It preserves information about missingness, which can be informative for downstream models.

### Formula
Binary assignment:  
$$
\text{Indicator} = 
\begin{cases} 
1 & \text{if original value was missing} \\
0 & \text{otherwise}
\end{cases}
$$

### Example (Pandas Implementation)
```python
# Using NumPy to create indicators for specified columns
for var in ['A1', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']:
    X_train[var+'_NA'] = np.where(X_train[var].isnull(), 1, 0)
    X_test[var+'_NA'] = np.where(X_test[var].isnull(), 1, 0)
```

---

## [[Pandas Implementation]]
### Definition
Manual creation of missing indicators using Pandas and NumPy for specified columns.

### Formula
`np.where(condition, value_if_true, value_if_false)`  
- **Condition**: `X_train[var].isnull()`  
- **Value if true**: `1` (missing)  
- **Value if false**: `0` (not missing)

### Example
```python
# Check alignment between missing rate and indicator mean
X_train['A3'].isnull().mean(), X_train['A3_NA'].mean()
# Output: (0.05, 0.05)  # Example alignment
```

---

## [[Feature-engine Implementation]]
### Definition
Using the `AddMissingIndicator` class from the **Feature-engine** library to automate indicator creation.

### Formula
1. Initialize imputer: `imputer = AddMissingIndicator()`  
2. Fit to training data: `imputer.fit(X_train)`  
3. Transform data: `X_train = imputer.transform(X_train)`

### Example
```python
imputer = AddMissingIndicator()
imputer.fit(X_train)
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)
```

---

## [[Scikit-learn Implementation]]
### Definition
Using `MissingIndicator` from **Scikit-learn** to generate indicators, requiring manual concatenation with the original dataset.

### Formula
1. Initialize indicator: `indicator = MissingIndicator()`  
2. Fit to training data: `indicator.fit(X_train)`  
3. Transform data: `indicator.transform(X_train)`  
4. Concatenate indicators to original data.

### Example
```python
indicator = MissingIndicator()
indicator.fit(X_train)
indicator_cols = [c+'_NA' for c in X_train.columns[indicator.features_]]
X_train = pd.concat([
    X_train.reset_index(),
    pd.DataFrame(indicator.transform(X_train), columns=indicator_cols)
], axis=1)
```

---

## Key Considerations
- **Purpose**: Combines with imputation methods (e.g., [[Mean Imputation]], [[Median Imputation]]) to retain information about missingness.
- **Best Practice**: Always fit the imputer/indicator on the **training set** to avoid data leakage.
- **Libraries**: [[Feature-engine]] and [[Scikit-learn]] provide streamlined implementations compared to manual Pandas approaches.