# Practical 7.4 - Maximum-Absolute-Scaling.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured summary of the content using the requested academic format:

---

### [[Maximum Absolute Scaling]]  
**Definition**: A data scaling technique that normalizes features by dividing each value by the maximum absolute value of that feature, resulting in values within the range [-1, 1]. Recommended for zero-centered or sparse data.  
**Formula**:  
\[ x_{\text{scaled}} = \frac{x}{\max(|x|)} \]  
**Example**:  
```python
from sklearn.preprocessing import MaxAbsScaler
scaler = MaxAbsScaler()
X_train_scaled = scaler.fit_transform(X_train)
```

---

### [[StandardScaler]] (Centering)  
**Definition**: A scaler that removes the mean (centers data at zero) but does not scale by standard deviation when configured appropriately. Used here as a preprocessing step before maximum absolute scaling.  
**Formula**:  
\[ x_{\text{centered}} = x - \mu \]  
where \( \mu \) is the mean of the feature.  
**Example**:  
```python
from sklearn.preprocessing import StandardScaler
scaler_mean = StandardScaler(with_mean=True, with_std=False)
X_centered = scaler_mean.fit_transform(X_train)
```

---

### [[Centering (Data Preprocessing)]]  
**Definition**: The process of subtracting the mean value from a dataset to ensure it is centered at zero, often used before applying scaling techniques like maximum absolute scaling.  
**Formula**: Same as [[StandardScaler]] (centering).  
**Example**: Combining centering with maximum absolute scaling:  
```python
X_train_scaled = scaler_maxabs.transform(scaler_mean.transform(X_train))
```

---

### [[Kernel Density Estimation (KDE)]]  
**Definition**: A non-parametric way to estimate the probability density function of a variable, used here to visualize the distribution of features before and after scaling.  
**Formula**:  
\[ \hat{f}(x) = \frac{1}{n h} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right) \]  
where \( K \) is the kernel function and \( h \) is the bandwidth.  
**Example**:  
```python
import seaborn as sns
sns.kdeplot(X_train['RM'], label='Before Scaling')
sns.kdeplot(X_train_scaled['RM'], label='After Scaling')
```

---

### Key Workflow Integration  
**Definition**: The process of combining centering and scaling for optimal data transformation.  
**Formula**: Sequential application of centering followed by maximum absolute scaling.  
**Example**:  
```python
# Center data
X_centered = StandardScaler(with_mean=True, with_std=False).fit_transform(X_train)
# Apply maximum absolute scaling
X_scaled = MaxAbsScaler().fit_transform(X_centered)
```

---

This summary connects data preprocessing techniques, their mathematical foundations, and practical implementations using Python. Use [[Wikilinks]] to explore related concepts like [[Feature Scaling]], [[Data Standardization]], or [[Probability Density Plots]].