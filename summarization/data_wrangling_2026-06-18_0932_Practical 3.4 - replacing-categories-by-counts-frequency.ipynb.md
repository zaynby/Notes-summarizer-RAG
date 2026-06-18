# Practical 3.4 - replacing-categories-by-counts-frequency.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Summary: Count and Frequency Encoding in Categorical Variable Processing

---

#### [[Count Encoding]]  
**Definition**: A technique in categorical variable encoding where each category is replaced by the number of times it appears in the dataset. This method assumes that the frequency of a category may correlate with the target variable.  
**Formula**:  
\[
\text{Count}(c) = \text{Number of occurrences of category } c \text{ in the dataset}
\]  
**Example**:  
```python  
# Using pandas to perform count encoding on column 'A7'  
count_map = X_train['A7'].value_counts().to_dict()  
X_train['A7'] = X_train['A7'].map(count_map)  
X_test['A7'] = X_test['A7'].map(count_map)  
```  
**Link**: [[Frequency Encoding]], [[Categorical Variable Encoding]]  

---

#### [[Frequency Encoding]]  
**Definition**: A variant of count encoding where categories are replaced by their relative frequency (proportion) in the dataset. This normalization helps in comparing categories across datasets of different sizes.  
**Formula**:  
\[
\text{Frequency}(c) = \frac{\text{Count}(c)}{\text{Total number of observations}} = \frac{\text{Count}(c)}{N}
\]  
**Example**:  
```python  
# Calculating frequency map for column 'A6'  
frequency_map = (X_train['A6'].value_counts() / len(X_train)).to_dict()  
X_train['A6'] = X_train['A6'].map(frequency_map)  
X_test['A6'] = X_test['A6'].map(frequency_map)  
```  
**Link**: [[Count Encoding]], [[Categorical Variable Encoding]]  

---

#### [[CountFrequencyEncoder]]  
**Definition**: A class from the `Feature-engine` library that automates count or frequency encoding. It allows specification of the encoding method (`'count'` or `'frequency'`) and handles fitting/transforming datasets.  
**Formula**: Same as [[Count Encoding]] or [[Frequency Encoding]], depending on the `encoding_method` parameter.  
**Example**:  
```python  
# Using Feature-engine for count encoding  
count_enc = CountFrequencyEncoder(encoding_method='count')  
count_enc.fit(X_train)  
X_train_enc = count_enc.transform(X_train)  
X_test_enc = count_enc.transform(X_test)  
```  
**Link**: [[Count Encoding]], [[Frequency Encoding]]  

---

#### [[Categorical Variable Encoding]]  
**Definition**: The general process of converting categorical variables into numerical representations to enable use in machine learning models. Includes techniques like [[Count Encoding]], [[Frequency Encoding]], one-hot encoding, and ordinal encoding.  
**Formula**: N/A (umbrella term for encoding methods).  
**Example**:  
- Applying [[Count Encoding]] to variables `['A1', 'A4', 'A5', ...]` in a dataset.  
**Link**: [[Count Encoding]], [[Frequency Encoding]], [[Ordinal Encoding]], [[One-Hot Encoding]]  

---

### Key Concepts Recap  
- **Count vs. Frequency Encoding**: Count uses raw frequencies, while frequency normalizes by total observations.  
- **Implementation Tools**: Pandas (manual mapping) and `Feature-engine` (automated via `CountFrequencyEncoder`).  
- **Use Case**: Reduces dimensionality compared to one-hot encoding and retains category importance.  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).