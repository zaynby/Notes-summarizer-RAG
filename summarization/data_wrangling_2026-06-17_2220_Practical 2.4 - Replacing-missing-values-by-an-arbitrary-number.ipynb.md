# Practical 2.4 - Replacing-missing-values-by-an-arbitrary-number.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Arbitrary Number Imputation

## [[Arbitrary Number Imputation]]
**Definition**: A technique where missing values in a dataset are replaced with a predefined arbitrary constant (e.g., 99, -1) that is not typically present in the data distribution. This method is suitable for numerical variables and avoids introducing values close to the mean/median of the data.

**Formula**:  
\[
\text{Imputed Value} = 
\begin{cases} 
x & \text{if } x \text{ is not missing} \\
c & \text{if } x \text{ is missing}
\end{cases}
\]  
where \( c \) is the chosen arbitrary constant.

**Example**:  
Replacing missing values in variables `A2`, `A3`, `A8`, `A11` with 99 using pandas:  
```python
for var in ['A2','A3', 'A8', 'A11']:
    X_train[var] = X_train[var].fillna(99)
    X_test[var] = X_test[var].fillna(99)
```

---

## [[Pandas Arbitrary Imputation]]
**Definition**: Implementation of arbitrary number imputation using pandas' `fillna()` method to replace missing values in a DataFrame.

**Formula**:  
`DataFrame[var].fillna(c, inplace=True)`  
where `c` is the arbitrary value.

**Example**:  
```python
# Replace missing values in specified columns with 99
for var in ['A2','A3', 'A8', 'A11']:
    X_train[var] = X_train[var].fillna(99)
    X_test[var] = X_test[var].fillna(99)
```

---

## [[Scikit-learn Arbitrary Imputation]]
**Definition**: Use of Scikit-learn's `SimpleImputer` class with `strategy='constant'` to impute missing values with a user-defined constant.

**Formula**:  
`SimpleImputer(strategy='constant', fill_value=c).fit_transform(X)`  
where `c` is the arbitrary constant.

**Example**:  
```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='constant', fill_value=99)
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## [[Feature-engine Arbitrary Imputation]]
**Definition**: Application of Feature-engine's `ArbitraryNumberImputer` transformer to replace missing values with a specified number, enabling pipeline integration.

**Formula**:  
`ArbitraryNumberImputer(arbitrary_number=c, variables=[vars]).fit_transform(X)`  
where `c` is the arbitrary constant and `vars` are target variables.

**Example**:  
```python
from feature_engine.imputation import ArbitraryNumberImputer

imputer = ArbitraryNumberImputer(
    arbitrary_number=99,
    variables=['A2','A3', 'A8', 'A11']
)
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## Key Considerations
- **Variable Selection**: Arbitrary imputation is typically applied to numerical variables. Categorical variables require separate handling (e.g., using frequent or missing category imputation).
- **Value Choice**: The arbitrary constant (e.g., 99) should not overlap with valid data values to avoid misinterpretation.
- **Pipeline Compatibility**: Feature-engine and Scikit-learn implementations are designed for integration into machine learning pipelines.