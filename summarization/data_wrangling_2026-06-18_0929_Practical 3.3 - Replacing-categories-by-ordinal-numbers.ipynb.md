# Practical 3.3 - Replacing-categories-by-ordinal-numbers.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Ordinal Encoding Techniques

## **Ordinal Encoding**
**Definition**: A method of converting categorical variables into numerical values by assigning each category an arbitrary integer (e.g., 0 to k-1 or 1 to k), where k is the number of unique categories.  
**Formula**:  
\[ \text{Mapping} = \{ k_i \rightarrow m_i \mid k_i \in \text{Categories}, m_i \in \mathbb{Z} \} \]  
**Example**:  
```python
ordinal_mapping = {k: i for i, k in enumerate(X_train['A7'].unique(), 0)}
X_train['A7'] = X_train['A7'].map(ordinal_mapping)
```

---

## **Pandas Ordinal Encoding**
**Definition**: Implementing ordinal encoding using pandas’ `map()` function and manual dictionary creation to replace categories with integers.  
**Formula**:  
\[ \text{Encoded Value} = \text{Category} \mapsto \text{Integer via Dictionary} \]  
**Example**:  
```python
def find_category_mappings(df, variable):
    return {k: i for i, k in enumerate(df[variable].unique(), 0)}

def integer_encode(train, test, variable, ordinal_mapping):
    train[variable] = train[variable].map(ordinal_mapping)
    test[variable] = test[variable].map(ordinal_mapping)
```

---

## **Scikit-learn OrdinalEncoder**
**Definition**: A scikit-learn class (`OrdinalEncoder`) that automatically maps categories to integers in a specified order.  
**Formula**:  
\[ X_{\text{encoded}} = \text{OrdinalEncoder().fit_transform}(X_{\text{categorical}}) \]  
**Example**:  
```python
from sklearn.preprocessing import OrdinalEncoder
le = OrdinalEncoder()
le.fit(X_train[vars_categorical])
X_train_enc = le.transform(X_train[vars_categorical])
```

---

## **Feature-engine OrdinalEncoder**
**Definition**: An encoder from the `feature_engine` library that applies arbitrary ordinal encoding while retaining category-to-integer mappings.  
**Formula**:  
\[ X_{\text{encoded}} = \text{OrdinalEncoder}(\text{encoding_method='arbitrary')}.transform(X) \]  
**Example**:  
```python
from feature_engine.encoding import OrdinalEncoder
ordinal_enc = OrdinalEncoder(encoding_method='arbitrary', variables=vars_categorical)
ordinal_enc.fit(X_train)
X_train = ordinal_enc.transform(X_train)
```

---

## **Integer Encoding**
**Definition**: Synonym for ordinal encoding, emphasizing the conversion of categorical labels to integers.  
**Formula**: Same as [[Ordinal Encoding]].  
**Example**:  
```python
for variable in vars_categorical:
    if variable != 'A7':
        mappings = find_category_mappings(X_train, variable)
        integer_encode(X_train, X_test, variable, mappings)
```

---

## **Category Mapping**
**Definition**: The dictionary that defines the relationship between original categories and their assigned integers.  
**Formula**:  
\[ \text{Mapping} = \{ \text{Category} : \text{Integer} \} \]  
**Example**:  
```python
ordinal_mapping = {k: i for i, k in enumerate(X_train['A7'].unique(), 0)}
# Output: {'A7_Category1': 0, 'A7_Category2': 1, ...}
```

---

## **Key Notes**
- **Use Case**: Preferred for non-linear models that can handle arbitrary integer assignments.  
- **Libraries**: [[Pandas]], [[Scikit-learn]], and [[Feature-engine]] provide distinct implementations.  
- **Caution**: Arbitrary mappings may not preserve ordinal relationships unless explicitly defined.  

[[Categorical Variables]] vs. [[Ordinal Variables]] distinctions are critical for choosing encoding methods.