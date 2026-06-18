# Practical 3.6 - target-mean-encoding.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here is a structured academic summary of the content:

---

### **Target Mean Encoding**  
**Definition**: A technique where categorical variable categories are replaced by the average target value observed for each category. This method leverages the relationship between categorical features and the target variable to create informative numerical representations.  

**Formula**:  
For a categorical feature \( X \) with category \( c \) and target variable \( y \):  
\[
\text{Encoded value} = \mu_c = \frac{\sum_{i: X_i = c} y_i}{N_c}
\]  
where \( N_c \) is the number of observations in category \( c \).  

**Example**:  
- **Pandas Implementation**:  
  ```python
  # Calculate target mean per category for 'A7'
  ordered_labels = X_train.groupby(['A7'])['A16'].mean().to_dict()
  # Replace categories with target means
  X_train['A7'] = X_train['A7'].map(ordered_labels)
  X_test['A7'] = X_test['A7'].map(ordered_labels)
  ```  
- **Feature-engine Implementation**:  
  ```python
  # Initialize and fit MeanEncoder
  mean_enc = MeanEncoder(variables=None)
  mean_enc.fit(X_train, y_train)
  # Transform datasets
  X_train_enc = mean_enc.transform(X_train)
  X_test_enc = mean_enc.transform(X_test)
  ```  

---

### **MeanEncoder (Feature-engine)**  
**Definition**: A class from the `Feature-engine` library that automates target mean encoding. It calculates the mean of the target variable for each category during fitting and applies the transformation to the data.  

**Formula**: Same as [[Target Mean Encoding]].  

**Example**:  
```python
# After splitting data into X_train, X_test, y_train, y_test:
mean_enc = MeanEncoder(variables=None)
mean_enc.fit(X_train, y_train)  # Learns category means
X_train_enc = mean_enc.transform(X_train)  # Applies encoding
```  

---

### **Key Considerations**  
1. **Data Splitting**: Always fit the encoder on the training data only to prevent data leakage.  
2. **Handling Unseen Categories**: The encoder assigns a default value (e.g., mean of target) to unseen categories in the test set.  
3. **Related Concepts**: [[Categorical Variables]], [[Target Encoding]], [[Feature Engineering]], [[Mean Normalization]].  

--- 

This summary integrates theoretical definitions, mathematical formulations, and practical code examples for implementing target mean encoding using both pandas and Feature-engine.