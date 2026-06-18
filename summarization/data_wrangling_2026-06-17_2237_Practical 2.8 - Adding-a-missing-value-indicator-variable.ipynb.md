# Practical 2.8 - Adding-a-missing-value-indicator-variable.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

## Missing Value Indicator Variable  
**Definition**: A binary feature that indicates whether an observation's value was missing (1) or present (0) in the original dataset. It preserves information about missingness while allowing imputation (e.g., [[Mean/Median Imputation]]) to fill missing values.  

**Formula**:  
\[
\text{Indicator}_i = 
\begin{cases} 
1 & \text{if } x_i \text{ is missing} \\ 
0 & \text{otherwise} 
\end{cases}
\]

**Example**:  
```python
# Using pandas and numpy to create indicators
X_train[var+'_NA'] = np.where(X_train[var].isnull(), 1, 0)
X_test[var+'_NA'] = np.where(X_test[var].isnull(), 1, 0)
```

---

## AddMissingIndicator (Feature-engine)  
**Definition**: A transformer class in the `Feature-engine` library that automatically adds missing value indicator variables to columns with missing data.  

**Formula**: N/A (method-based implementation)  

**Example**:  
```python
from feature_engine.imputation import AddMissingIndicator
imputer = AddMissingIndicator()
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## MissingIndicator (Scikit-learn)  
**Definition**: A Scikit-learn transformer that generates binary indicators for missing values in the dataset. It identifies columns with missing values and creates corresponding indicator features.  

**Formula**: N/A (method-based implementation)  

**Example**:  
```python
from sklearn.impute import MissingIndicator
indicator = MissingIndicator(error_on_new=True, features='missing-only')
X_train_ind = indicator.fit_transform(X_train)
# Concatenate indicators to original data
indicator_cols = [c+'_NA' for c in X_train.columns[indicator.features_]]
X_train = pd.concat([X_train, pd.DataFrame(X_train_ind, columns=indicator_cols)], axis=1)
```

---

## Key Concepts & Links  
- **[[Missing Data Imputation Techniques]]**: Context for using indicators alongside imputation.  
- **[[Mean/Median Imputation]]**: Often paired with indicators to handle missing values.  
- **[[IQR Proximity Rule]]**: Alternative imputation method for non-normal distributions.  
- **[[Random Sample Imputation]]**: Another technique for filling missing data.