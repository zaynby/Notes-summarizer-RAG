# Practical 2.6 - Replacing-missing-values-by-a-value-at-the-end-of-the-distribution.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content following the requested format:

---

### **End-of-Tail Imputation**  
**Definition**: A method to replace missing values with statistically derived extreme values from the variable's distribution, using either the interquartile range (IQR) or standard deviation. This avoids arbitrary value selection while preserving data distribution characteristics.  
**Formula**:  
- For IQR-based imputation (right tail): \( \text{Value} = Q3 + 1.5 \times \text{IQR} \)  
- For IQR-based imputation (left tail): \( \text{Value} = Q1 - 1.5 \times \text{IQR} \)  
- IQR calculation: \( \text{IQR} = Q3 - Q1 \)  
**Example**:  
```python  
# Using pandas to replace missing values in variables ['A2', 'A3', 'A8', 'A11', 'A15']  
for var in ['A2', 'A3', 'A8', 'A11', 'A15']:  
    IQR = X_train[var].quantile(0.75) - X_train[var].quantile(0.25)  
    value = X_train[var].quantile(0.75) + 1.5 * IQR  # Right tail  
    X_train[var].fillna(value, inplace=True)  
    X_test[var].fillna(value, inplace=True)  
```  

---

### **Interquartile Range (IQR)**  
**Definition**: A measure of statistical dispersion, representing the range between the 25th percentile (Q1) and 75th percentile (Q3) of a dataset.  
**Formula**:  
\[ \text{IQR} = Q3 - Q1 \]  
**Example**:  
```python  
# Calculating IQR for variable 'A2'  
Q1 = X_train['A2'].quantile(0.25)  
Q3 = X_train['A2'].quantile(0.75)  
IQR = Q3 - Q1  
```  

---

### **IQR Proximity Rule**  
**Definition**: A criterion to identify extreme values (potential outliers or imputation targets) based on the IQR. Values beyond \( Q1 - 1.5 \times \text{IQR} \) (left tail) or \( Q3 + 1.5 \times \text{IQR} \) (right tail) are considered extreme.  
**Formula**:  
- Right tail threshold: \( Q3 + 1.5 \times \text{IQR} \)  
- Left tail threshold: \( Q1 - 1.5 \times \text{IQR} \)  
**Example**:  
```python  
# Using IQR proximity rule for right tail imputation  
value = Q3 + 1.5 * IQR  
print(f"Imputation value for right tail: {value}")  
```  

---

### **EndTailImputer (Feature-engine)**  
**Definition**: A class in the Feature-engine library that automates end-of-tail imputation. It learns imputation values from the training set and applies them to test/future data.  
**Formula**: N/A (implementation-specific)  
**Example**:  
```python  
from feature_engine.imputation import EndTailImputer  

imputer = EndTailImputer(  
    imputation_method='iqr',  
    tail='right',  
    fold=1.5,  
    variables=['A2', 'A3', 'A8', 'A11', 'A15']  
)  
imputer.fit(X_train)  
X_train = imputer.transform(X_train)  
X_test = imputer.transform(X_test)  
```  

---

### **Train/Test Split**  
**Definition**: The process of dividing a dataset into training and testing subsets to evaluate machine learning models. The training set is used for imputation parameter estimation, while the test set simulates unseen data.  
**Formula**: N/A  
**Example**:  
```python  
from sklearn.model_selection import train_test_split  

X_train, X_test, y_train, y_test = train_test_split(  
    data.drop('A16', axis=1),  
    data['A16'],  
    test_size=0.3,  
    random_state=0  
)  
```  

---

### **Key Links**  
- [[Imputation Techniques]]  
- [[Feature-engine]]  
- [[Interquartile Range (IQR)]]  
- [[Train/Test Split]]  

This summary integrates theoretical concepts and practical implementations from the notebook, emphasizing statistical foundations and code-based workflows.