# Practical 7.3 - MinMaxScaling.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Min-Max Scaling and Data Transformation

## [[MinMax Scaling]]  
**Definition**: A feature scaling technique that rescales data to a fixed range, typically [0, 1], by subtracting the minimum value and dividing by the range (max - min).  
**Formula**:  
\[ x_{\text{scaled}} = \frac{x - \min(x)}{\max(x) - \min(x)} \]  
**Example**:  
Applied to the Boston Housing dataset to normalize features like `RM` (average number of rooms) and `LSTAT` (percentage of lower status population).  

---

## [[MinMaxScaler (Scikit-learn)]]  
**Definition**: A class in `sklearn.preprocessing` used to implement Min-Max scaling. It learns scaling parameters (min, max) from the training data and applies them to both training and test sets.  
**Attributes**:  
- `data_max_`: Maximum values of each feature (learned from training data).  
- `min_`: Minimum values of each feature.  
- `data_range_`: Range (max - min) of each feature.  
**Example**:  
```python  
from sklearn.preprocessing import MinMaxScaler  
scaler = MinMaxScaler()  
scaler.fit(X_train)  # Learns parameters  
X_train_scaled = scaler.transform(X_train)  # Scales training data  
X_test_scaled = scaler.transform(X_test)     # Scales test data  
```  

---

## [[Data Transformation (NumPy to DataFrame)]]  
**Definition**: Conversion of scaled NumPy arrays (output of `MinMaxScaler.transform`) into pandas DataFrames to preserve feature names and structure.  
**Example**:  
```python  
# Convert scaled arrays to DataFrames  
X_train_scaled = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns)  
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)  
```  

---

## [[Distribution Visualization (KDE Plots)]]  
**Definition**: Use of Kernel Density Estimation (KDE) plots to compare feature distributions before and after scaling. This visualizes the impact of scaling on data spread and shape.  
**Example**:  
```python  
import matplotlib.pyplot as plt  
import seaborn as sns  

# Compare distributions of 'RM', 'LSTAT', and 'CRIM'  
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))  
sns.kdeplot(X_train['RM'], ax=ax1, label='RM (Before)')  
sns.kdeplot(X_train_scaled['RM'], ax=ax2, label='RM (After)')  
ax1.set_title('Before Scaling')  
ax2.set_title('After Scaling')  
plt.show()  
```  

---

## Key Concepts Linked  
- [[Feature Scaling]]: General term for techniques like Min-Max Scaling and Standardization.  
- [[Scikit-learn]]: Library providing implementations of scaling methods (e.g., `MinMaxScaler`).  
- [[Data Preprocessing]]: Broader category including scaling, transformation, and visualization.