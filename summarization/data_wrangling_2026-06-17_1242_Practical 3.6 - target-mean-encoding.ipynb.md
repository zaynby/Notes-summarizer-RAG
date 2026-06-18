# Practical 3.6 - target-mean-encoding.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Target Mean Encoding

## Term: [[Target Mean Encoding]]  
**Definition**: A technique where categorical variables are replaced by the average value of the target variable associated with each category. This method leverages the relationship between categories and the target to create numerical features.  
**Formula**:  
\[
\text{Mean Encoding} = \frac{\sum_{i=1}^{n} y_i}{n} \quad \text{for category } c
\]  
Where \( y_i \) are target values for category \( c \), and \( n \) is the number of observations in \( c \).  
**Example**:  
```python
# Using pandas to compute and apply target means
ordered_labels = X_train.groupby(['A7'])['A16'].mean().to_dict()
X_train['A7'] = X_train['A7'].map(ordered_labels)
X_test['A7'] = X_test['A7'].map(ordered_labels)
```

---

## Term: [[MeanEncoder (Feature-engine)]]  
**Definition**: A class from the `Feature-engine` library that automates target mean encoding. It encodes categorical variables by fitting to the training data and applying the learned means to the test set.  
**Formula**: Same as Target Mean Encoding.  
**Example**:  
```python
# Using Feature-engine's MeanEncoder
mean_enc = MeanEncoder(variables=None)  # Encode all categorical variables
mean_enc.fit(X_train, y_train)         # Fit using target
X_train_enc = mean_enc.transform(X_train)
X_test_enc = mean_enc.transform(X_test)
```

---

## Term: [[Manual Mean Encoding with Pandas]]  
**Definition**: A manual approach to target mean encoding using pandas, involving calculating category means and mapping them to original categories.  
**Formula**: Same as Target Mean Encoding.  
**Example**:  
```python
# Calculate target mean per category
X_train[["A7", "A16"]][X_train["A7"]=="n"]  # Inspect data
ordered_labels = X_train.groupby(['A7'])['A16'].mean().to_dict()
# Apply encoding
X_train['A7'] = X_train['A7'].map(ordered_labels)
X_test['A7'] = X_test['A7'].map(ordered_labels)
```

---

## Key Concepts and Links  
- **[[Categorical Variable]]**: Non-numeric feature requiring encoding (e.g., `A7` in the dataset).  
- **[[Target Variable]]**: The variable to predict (e.g., `A16` in the dataset).  
- **[[Scikit-learn]]**: Integration with libraries like `Feature-engine` for pipeline compatibility.  
- **[[Overfitting Risk]]**: Target mean encoding may introduce overfitting if not properly regularized.  

This summary aligns with the notebook’s focus on encoding categorical variables using target means, demonstrating both manual and automated methods.