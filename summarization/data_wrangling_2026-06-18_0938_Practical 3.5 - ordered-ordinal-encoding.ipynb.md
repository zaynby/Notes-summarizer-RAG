# Practical 3.5 - ordered-ordinal-encoding.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the content:

---

### **Ordered Integer Encoding**  
**Definition**: A technique where categorical variables are encoded as integers based on the mean value of the target variable for each category. Categories are sorted by their target mean and assigned digits from `0` to `k-1` (where `k` is the number of categories), creating a monotonic relationship with the target.  
**Formula**:  
Mean target per category = \(\frac{\text{Sum of target values in category}}{\text{Number of observations in category}}\)  
**Example**:  
```python  
# Sort categories by target mean and create mappings  
ordered_labels = X_train.groupby(['A7'])['A16'].mean().sort_values().index  
ordinal_mapping = {k: i for i, k in enumerate(ordered_labels, 0)}  
```  

---

### **Monotonic Relationship**  
**Definition**: A relationship where the encoded integer values of a categorical variable consistently increase or decrease alongside the target variable’s mean values. This ensures linear models can interpret the encoded values meaningfully.  
**Formula**: N/A (Conceptual)  
**Example**:  
```python  
# Plot after encoding shows ordered target means  
X_train.groupby(['A7'])['A16'].mean().plot()  
plt.title('Monotonic relationship between A7 and target')  
```  

---

### **Target-Based Encoding**  
**Definition**: Encoding categorical variables by leveraging the target variable’s distribution. Categories are ranked by their association with the target (e.g., mean target value) to assign integers.  
**Formula**:  
Sorted categories = \( \text{Categories ordered by } \frac{\sum y}{n} \) (where \(y\) = target, \(n\) = observations per category)  
**Example**:  
```python  
# Calculate target mean per category and sort  
X_train.groupby(['A7'])['A16'].mean().sort_values()  
```  

---

### **Feature-engine OrdinalEncoder**  
**Definition**: A scikit-learn-compatible transformer from the `Feature-engine` library that performs ordered integer encoding by fitting on the training data and the target variable.  
**Formula**: N/A (Algorithmic)  
**Example**:  
```python  
ordinal_enc = OrdinalEncoder(encoding_method='ordered')  
ordinal_enc.fit(X_train, y_train)  # Requires target for ordering  
X_train_enc = ordinal_enc.transform(X_train)  
```  

---

### **Key Connections**  
- [[Ordinal Encoding]] (previous method) assigns arbitrary integers, while **Ordered Integer Encoding** uses target-based ordering.  
- **Monotonic Relationship** is critical for linear models, as it ensures encoded values align with the target’s trend.  
- **Feature-engine OrdinalEncoder** automates the ordered encoding process, integrating with scikit-learn pipelines.  

--- 

This summary links encoding techniques to their mathematical foundations and practical implementations, emphasizing their suitability for different model types (linear vs. non-linear).