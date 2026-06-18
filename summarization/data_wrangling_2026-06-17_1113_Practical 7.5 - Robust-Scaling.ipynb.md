# Practical 7.5 - Robust-Scaling.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Robust Scaling and Related Concepts

## [[Robust Scaling]]  
**Definition**: A data preprocessing technique that transforms features by removing the median and scaling by the interquartile range (IQR). It is robust to outliers compared to mean-based scaling methods.  
**Formula**:  
\[
x_{\text{scaled}} = \frac{x - \text{median}(x)}{\text{IQR}} = \frac{x - \text{median}(x)}{Q3 - Q1}
\]  
**Example**:  
In the provided code, `RobustScaler` from scikit-learn is applied to the Boston Housing dataset. After fitting to the training data, features like `RM`, `LSTAT`, and `CRIM` are transformed to reduce the impact of outliers.  

---

## [[Median]]  
**Definition**: The middle value of a sorted dataset. If the dataset has an even number of observations, it is the average of the two middle values.  
**Formula**:  
For a sorted dataset \( x_1, x_2, \ldots, x_n \):  
- If \( n \) is odd: \( \text{median} = x_{(n+1)/2} \)  
- If \( n \) is even: \( \text{median} = \frac{x_{n/2} + x_{n/2 + 1}}{2} \)  
**Example**:  
The `RobustScaler` stores the median of each feature in the `center_` attribute (e.g., `scaler.center_` retrieves medians for `RM`, `LSTAT`, etc.).  

---

## [[Interquartile Range (IQR)]]  
**Definition**: The range between the first quartile (Q1, 25th percentile) and the third quartile (Q3, 75th percentile), representing the spread of the central 50% of the data.  
**Formula**:  
\[
\text{IQR} = Q3 - Q1
\]  
**Example**:  
In the code, the `scale_` attribute of `RobustScaler` stores the IQR for each feature (e.g., `scaler.scale_` returns IQR values for `AGE`, `DIS`, etc.).  

---

## [[RobustScaler]]  
**Definition**: A scikit-learn class that implements robust scaling using median and IQR. It is less sensitive to outliers than `StandardScaler`.  
**Key Parameters**:  
- No parameters required for default implementation.  
**Example**:  
```python
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
scaler.fit(X_train)  # Learns medians and IQRs
X_train_scaled = scaler.transform(X_train)  # Applies scaling
```  

---

## [[Boston Housing Dataset]]  
**Definition**: A classic dataset used for regression tasks, containing features like crime rate (`CRIM`), room size (`RM`), and pollution levels (`NOX`) to predict house prices (`MEDV`).  
**Example**:  
The dataset is loaded and split into training/testing sets in the code:  
```python
data = pd.read_csv("./data/boston_local.csv")
X_train, X_test, y_train, y_test = train_test_split(data.drop('MEDV', axis=1), data['MEDV'], test_size=0.3, random_state=0)
```  

---

## Visualization of Scaled Data  
**Example**:  
Kernel Density Estimation (KDE) plots compare feature distributions before and after scaling:  
```python
sns.kdeplot(X_train['RM'], label='Before Scaling')
sns.kdeplot(X_train_scaled['RM'], label='After Robust Scaling')
```  
This visualizes the effect of robust scaling on reducing outlier influence.  

--- 

**Related Concepts**:  
- [[Standardization]] (mean = 0, std = 1)  
- [[Min-Max Scaling]] (scales to a fixed range, e.g., [0, 1])  
- [[Data Preprocessing]] (general category for scaling techniques)