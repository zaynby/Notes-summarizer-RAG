# Practical 3.4 - replacing-categories-by-counts-frequency.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured summary of the content following the requested format:

---

### **Count Encoding**  
**Definition**: A technique where categorical variable categories are replaced with their **occurrence counts** in the dataset. This captures the frequency of each category as a numerical value.  
**Formula**:  
\[ \text{Count}(c) = \text{Number of observations with category } c \]  
**Example**:  
```python
# Using pandas to create count mappings
count_map = X_train['A7'].value_counts().to_dict()
X_train['A7'] = X_train['A7'].map(count_map)
```  
**Wikilinks**: [[Frequency Encoding]], [[Categorical Variable]]

---

### **Frequency Encoding**  
**Definition**: A method where categories are replaced with their **relative frequency** (proportion of total observations). This normalizes counts to a [0,1] scale.  
**Formula**:  
\[ \text{Frequency}(c) = \frac{\text{Count}(c)}{\text{Total Observations}} \]  
**Example**:  
```python
# Calculating frequency mappings
frequency_map = (X_train['A6'].value_counts() / len(X_train)).to_dict()
X_train['A6'] = X_train['A6'].map(frequency_map)
```  
**Wikilinks**: [[Count Encoding]], [[Data Normalization]]

---

### **CountFrequencyEncoder (Feature-engine)**  
**Definition**: A class from the `Feature-engine` library that automates count or frequency encoding. It stores mappings and applies them to training/test sets.  
**Formula**:  
- **Count Mode**: \( \text{Encoded Value} = \text{Count}(c) \)  
- **Frequency Mode**: \( \text{Encoded Value} = \frac{\text{Count}(c)}{N} \)  
**Example**:  
```python
# Using Feature-engine for count encoding
count_enc = CountFrequencyEncoder(encoding_method='count')
count_enc.fit(X_train)
X_train_enc = count_enc.transform(X_train)
```  
**Wikilinks**: [[Pandas]], [[One-Hot Encoding]]

---

### **Key Functions for Encoding**  
**Definition**: Custom functions to streamline encoding workflows:  
1. **`count_mappings`**: Generates count dictionaries.  
2. **`frequency_mappings`**: Generates frequency dictionaries.  
3. **`encode`**: Applies mappings to train/test sets.  
**Example**:  
```python
# Applying encoding to multiple variables
for variable in vars_categorical:
    mappings = count_mappings(X_train, variable)
    encode(X_train, X_test, variable, mappings)
```  
**Wikilinks**: [[Data Preprocessing]]

---

### **Applications**  
- **Advantages**:  
  - Reduces dimensionality compared to [[One-Hot Encoding]].  
  - Captures category representation patterns.  
- **Use Cases**: Predictive modeling where category frequency correlates with the target (e.g., credit approval datasets).  

**Wikilinks**: [[Rare Categories]], [[Ordinal Encoding]]  

--- 

This summary links to related concepts (e.g., [[One-Hot Encoding]], [[Ordinal Encoding]]) for cross-referencing. Let me know if further refinements are needed!