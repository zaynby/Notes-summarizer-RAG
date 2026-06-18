# Practical 3.5 - ordered-ordinal-encoding.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Ordered Integer Encoding for Linear Models

## **Ordered Integer Encoding**
**Definition**: A method of encoding categorical variables by assigning integers (0 to k-1) to categories based on their mean target value. Categories are ordered from lowest to highest mean target, ensuring a monotonic relationship with the target variable.  
**Formula**:  
Mean target per category:  
\[ \text{mean\_target} = \frac{\sum \text{target values in category}}{\text{number of observations in category}} \]  
**Example**:  
```python
# Create ordered mapping for 'A7' based on mean target
ordered_labels = X_train.groupby(['A7'])['A16'].mean().sort_values().index
ordinal_mapping = {k: i for i, k in enumerate(ordered_labels, 0)}
X_train['A7'] = X_train['A7'].map(ordinal_mapping)
```

## **Monotonic Relationship**
**Definition**: A consistent, step-wise relationship between the encoded integers and the target variable, where higher integers correspond to higher (or lower) target means. This is critical for linear models to interpret the encoded variables correctly.  
**Formula**: Sorted mean targets must follow a non-decreasing or non-increasing order.  
**Example**:  
```python
# Plot showing monotonic relationship after encoding
X_train.groupby(['A7'])['A16'].mean().plot()
plt.title('Monotonic Relationship Between A7 and Target')
```

## **OrdinalEncoder (Feature-engine)**
**Definition**: A class in the `Feature-engine` library that automates ordered integer encoding by fitting on the training data and target variable. It stores mappings for each categorical variable.  
**Formula**: N/A (Process involves fitting to target and transforming categories).  
**Example**:  
```python
from feature_engine.encoding import OrdinalEncoder
ordinal_enc = OrdinalEncoder(encoding_method='ordered')
ordinal_enc.fit(X_train, y_train)  # Requires target for ordering
X_train_enc = ordinal_enc.transform(X_train)
```

## **Target-Based Encoding**
**Definition**: A category encoding strategy that uses target variable information (e.g., mean, median) to assign values to categorical levels. Ordered integer encoding is a type of target-based encoding.  
**Formula**: Same as `mean_target` in Ordered Integer Encoding.  
**Example**:  
```python
# Calculate mean target per category for encoding
category_means = X_train.groupby(['A7'])['A16'].mean().sort_values()
```

---

### **Key Concept Links**  
- [[Ordinal Encoding]]: Arbitrary assignment of integers (previous method).  
- [[Linear Models]]: Benefit from monotonic relationships created by ordered encoding.  
- [[Target-Based Encoding]]: Broader category including ordered integer encoding.  

### **Comparison with Arbitrary Ordinal Encoding**  
| **Aspect**               | **Ordered Integer Encoding**                          | **Arbitrary Ordinal Encoding**          |  
|--------------------------|----------------------------------------------------------|-----------------------------------------|  
| **Basis for Assignment** | Mean target value of categories                         | Random or default order                |  
| **Suitability**          | Linear models (monotonic relationship)                  | Non-linear models (e.g., tree-based)   |  
| **Implementation**       | Requires target variable during fitting                 | No target dependency                   |  

This method ensures categorical variables are transformed in a way that aligns with the assumptions of linear models, enhancing their interpretability and performance.