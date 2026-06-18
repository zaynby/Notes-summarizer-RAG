# Exercise_7 - Performing Feature Scaling.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Feature Scaling Techniques Summary

## [[Feature Scaling]]
### Definition
Process of standardizing the range of independent variables (features) in a dataset to ensure algorithms perform optimally. Critical for models sensitive to feature magnitude, such as linear regression, clustering, and principal component analysis (PCA).

### Formula
Varies by technique (see specific methods below)

### Example
```python
# Example from Exercise 7 (airbnb_sg dataset)
from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()
X_train_scaled = scaler.fit_transform(X_train)
```

---

## [[Standard Scaling (Z-score Normalization)]]
### Definition
Rescales data to have a mean (μ) of 0 and standard deviation (σ) of 1. Robust to outliers but assumes normal distribution.

### Formula
\[ z = \frac{x - \mu}{\sigma} \]

### Example
```python
# From Practical 7.1 - Standardization.ipynb
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Visualization
sns.kdeplot(X_train['RM'], label='Before')
sns.kdeplot(X_train_scaled['RM'], label='After')
```

---

## [[Robust Scaling]]
### Definition
Scales data using median and interquartile range (IQR), making it suitable for datasets with outliers.

### Formula
\[ x' = \frac{x - \text{median}(x)}{\text{IQR}(x)} \]
where IQR = Q3 - Q1

### Example
```python
# From Practical 7.5 - Robust-Scaling.ipynb
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Visualization for 'AGE' feature
sns.kdeplot(X_train['AGE'], label='Before')
sns.kdeplot(X_train_scaled['AGE'], label='After')
```

---

## [[Min-Max Scaling]]
### Definition
Scales data to a fixed range (typically [0, 1]) by adjusting to the minimum and maximum values.

### Formula
\[ x' = \frac{x - \min(x)}{\max(x) - \min(x)} \]

### Example
```python
# From Practical 7.3 - MinMaxScaling.ipynb
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Visualization for 'NOX' feature
sns.kdeplot(X_train['NOX'], label='Before')
sns.kdeplot(X_train_scaled['NOX'], label='After')
```

---

## [[MaxAbs Scaling]]
### Definition
Scales data by the maximum absolute value in the feature, preserving sparsity and useful for datasets with mixed positive/negative values.

### Formula
\[ x' = \frac{x}{\max(|x|)} \]

### Example
```python
# From Exercise 7 (airbnb_sg dataset)
scaler = MaxAbsScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Visualization for 'id' feature
sns.kdeplot(X_train['id'], label='Before')
sns.kdeplot(X_train_scaled['id'], label='After')
```

---

## [[KDE Plot (Kernel Density Estimate)]]
### Definition
Visualization tool used to compare feature distributions before and after scaling. Shows probability densities of continuous features.

### Formula
Non-parametric estimate of the probability density function:
\[ \hat{f}(x) = \frac{1}{n h} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right) \]
where \( K \) = kernel function, \( h \) = bandwidth

### Example
```python
# From Practical 7.4 - Maximum-Absolute-Scaling.ipynb
fig, (ax1, ax2) = plt.subplots(ncols=2)
sns.kdeplot(X_train['AGE'], ax=ax1)
sns.kdeplot(X_train_scaled['AGE'], ax=ax2)
```