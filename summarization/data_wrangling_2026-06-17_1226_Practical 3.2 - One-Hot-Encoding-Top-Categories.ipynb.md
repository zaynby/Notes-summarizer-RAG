# Practical 3.2 - One-Hot-Encoding-Top-Categories.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### One-Hot Encoding  
**Definition:** A technique to represent categorical variables as binary variables, where each category is assigned a binary column (1 if present, 0 otherwise).  
**Formula:** For a categorical variable with \( N \) categories, \( N \) binary columns are created. When limiting to top \( K \) categories, only \( K \) binary columns are generated.  
**Example:**  
```python  
# Create binary variables for top 5 categories in 'A6'  
top_5 = X_train['A6'].value_counts().sort_values(ascending=False).head(5).index  
for label in top_5:  
    X_train[f'A6_{label}'] = np.where(X_train['A6'] == label, 1, 0)  
```  

---

### Top Categories Encoding  
**Definition:** A variant of one-hot encoding that encodes only the most frequent categories to reduce dimensionality, grouping less frequent categories into a single "Other" category.  
**Formula:** Select top \( K \) categories by frequency, encode them as binary variables, and treat remaining categories as a collective group.  
**Example:**  
```python  
# Select top 5 categories for 'A6'  
top_5 = X_train['A6'].value_counts().sort_values(ascending=False).head(5).index  
# Encode top categories in train and test sets  
for label in top_5:  
    X_train[f'A6_{label}'] = np.where(X_train['A6'] == label, 1, 0)  
    X_test[f'A6_{label}'] = np.where(X_test['A6'] == label, 1, 0)  
```  

---

### Feature-engine OneHotEncoder  
**Definition:** A class from the [[Feature-engine]] library that performs one-hot encoding for specified variables, with options to limit encoding to top frequent categories.  
**Formula:** Initialized with parameters such as `top_categories` (number of categories to encode) and `variables` (columns to encode).  
**Example:**  
```python  
# Initialize encoder for top 5 categories in 'A6' and 'A7'  
ohe_enc = OneHotEncoder(  
    top_categories=5,  
    variables=['A6', 'A7'],  
    drop_last=False  
)  
# Fit and transform data  
ohe_enc.fit(X_train)  
X_train_enc = ohe_enc.transform(X_train)  
```  

---

### Frequency-based Category Selection  
**Definition:** The process of identifying the most frequent categories in a dataset using frequency counts, often for dimensionality reduction in encoding.  
**Formula:** \( \text{Top } K \text{ categories} = \text{Sort categories by frequency in descending order and select first } K \).  
**Example:**  
```python  
# Get top 5 most frequent categories in 'A6'  
top_5 = X_train['A6'].value_counts().sort_values(ascending=False).head(5).index  
print(top_5)  
```  

---

### Dimensionality Reduction in Encoding  
**Definition:** Techniques to minimize the number of features generated during encoding, such as limiting one-hot encoding to frequent categories.  
**Formula:** Reduces \( N \) categories to \( K \) binary columns (\( K < N \)).  
**Example:**  
```python  
# Before: 'A6' has 10 categories → 10 binary columns  
# After: Encode only top 5 categories → 5 binary columns  
```  

---

### [[Feature-engine]]  
**Definition:** A Python library for feature engineering tasks, including encoding, imputation, and transformation.  
**Formula:** N/A (library/tool).  
**Example:**  
```python  
# Import OneHotEncoder from Feature-engine  
from feature_engine.encoding import OneHotEncoder  
```  

---

### [[Grouping Rare or Infrequent Categories]]  
**Definition:** A method to combine less frequent categories into a single "Other" category to reduce noise and dimensionality.  
**Formula:** \( \text{Rare categories} \rightarrow \text{Grouped as "Other"} \).  
**Example:**  
```python  
# Implicitly achieved by encoding only top categories; remaining categories are treated as a group.  
```  

--- 

This summary connects key concepts like [[One-Hot Encoding]], [[Feature-engine]], and [[Grouping Rare or Infrequent Categories]] for cohesive understanding.