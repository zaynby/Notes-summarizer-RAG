# Practical 3.3 - Replacing-categories-by-ordinal-numbers.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Ordinal Encoding in Data Preprocessing

## [[Ordinal Encoding]]  
**Definition**: A technique to convert categorical variables into numerical values by assigning each category an arbitrary integer (e.g., 0 to \( k-1 \), where \( k \) is the number of unique categories). Suitable for non-linear models.  
**Formula**:  
\[ \text{Assigned Value} = i \quad \text{for category } k \text{ at index } i \]  
**Example**:  
```python
# Using pandas to map categories to integers
ordinal_mapping = {k: i for i, k in enumerate(X_train['A7'].unique(), 0)}
X_train['A7'] = X_train['A7'].map(ordinal_mapping)
```

---

## [[Nominal Categorical Variables]]  
**Definition**: Categorical variables without intrinsic order (e.g., "Gender", "City").  
**Formula**: N/A  
**Example**:  
```python
# Example of nominal variable 'A7' in the dataset
print(X_train['A7'].unique())  # Outputs: ['A', 'B', 'C', ...] (no inherent order)
```

---

## [[Ordinal Categorical Variables]]  
**Definition**: Categorical variables with a meaningful order (e.g., "Grade: A > B > C").  
**Formula**: N/A  
**Example**:  
```python
# Hypothetical ordinal variable mapping
grade_mapping = {'Fail': 0, 'C': 1, 'B': 2, 'A': 3}
```

---

## [[Category Mapping]]  
**Definition**: The process of creating a dictionary to map category labels to numerical values.  
**Formula**:  
\[ \text{Mapping} = \{k: i\} \quad \forall \text{categories } k \text{ in variable} \]  
**Example**:  
```python
# Manual mapping for variable 'A7'
ordinal_mapping = {k: i for i, k in enumerate(X_train['A7'].unique(), 0)}
# Output: {'A': 0, 'B': 1, 'C': 2, ...}
```

---

## [[Scikit-learn OrdinalEncoder]]  
**Definition**: A class from `sklearn.preprocessing` for ordinal encoding.  
**Formula**: N/A  
**Example**:  
```python
from sklearn.preprocessing import OrdinalEncoder
le = OrdinalEncoder()
le.fit(X_train[vars_categorical])  # Learn mappings
X_train_enc = le.transform(X_train[vars_categorical])  # Apply encoding
```

---

## [[Feature-engine OrdinalEncoder]]  
**Definition**: An encoder from the `Feature-engine` library for ordinal encoding.  
**Formula**: N/A  
**Example**:  
```python
from feature_engine.encoding import OrdinalEncoder
ordinal_enc = OrdinalEncoder(encoding_method='arbitrary', variables=vars_categorical)
ordinal_enc.fit(X_train)  # Fit to training data
X_train = ordinal_enc.transform(X_train)  # Transform datasets
```

---

## [[Train-Test Split]]  
**Definition**: Dividing a dataset into training and testing subsets to evaluate model performance.  
**Formula**:  
\[ \text{Test Size} \in (0, 1) \quad \text{(e.g., 0.3 for 30% test data)} \]  
**Example**:  
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    data.drop('A16', axis=1),  # Features
    data['A16'],               # Target
    test_size=0.3,             # 30% for testing
    random_state=0             # Reproducibility
)
```

---

## Key Concepts Interconnectivity  
- **Ordinal Encoding** is applied to **Nominal** or **Ordinal Categorical Variables**.  
- **Category Mapping** is the core step in **Ordinal Encoding**.  
- **Scikit-learn** and **Feature-engine** provide implementations of **Ordinal Encoding**.  
- **Train-Test Split** ensures encoding is fit only on training data to prevent data leakage.