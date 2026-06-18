# Practical 7.2 - Mean-normalization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Mean Normalization in Data Preprocessing

## [[Mean Normalization]]
**Definition**: A technique to rescale features by centering data at zero and adjusting the range to [-1, 1] using the formula:  
**Formula**:  
\[ x_{\text{scaled}} = \frac{x - \text{mean}(x)}{\text{max}(x) - \text{min}(x)} \]  
**Example**:  
```python
X_train_scaled = (X_train - means) / ranges
X_test_scaled = (X_test - means) / ranges  # Code Cell 8
```

---

## [[Training Set]]
**Definition**: Subset of data used to compute scaling parameters (e.g., mean, range) for normalization.  
**Example**:  
```python
X_train, X_test, y_train, y_test = train_test_split(...)  # Code Cell 4
means = X_train.mean(axis=0)  # Code Cell 5
ranges = X_train.max(axis=0) - X_train.min(axis=0)  # Code Cell 6
```

---

## [[Test Set]]
**Definition**: Subset of data used for evaluation, scaled using parameters derived from the training set.  
**Example**:  
```python
X_test_scaled = (X_test - means) / ranges  # Code Cell 8
```

---

## [[Value Range]]
**Definition**: The difference between the maximum and minimum values of a feature.  
**Formula**:  
\[ \text{range}(x) = \text{max}(x) - \text{min}(x) \]  
**Example**:  
```python
ranges = X_train.max(axis=0) - X_train.min(axis=0)  # Code Cell 6
```

---

## [[Centering Data]]
**Definition**: Adjusting data by subtracting the mean to center the distribution at zero.  
**Formula**:  
\[ x_{\text{centered}} = x - \text{mean}(x) \]  
**Example**:  
```python
(X_train - means)  # Part of Code Cell 8
```

---

## [[Kernel Density Estimate (KDE) Plot]]
**Definition**: A statistical visualization tool to compare distributions before and after scaling.  
**Example**:  
```python
sns.kdeplot(X_train['RM'], ax=ax1, label='RM')  # Code Cells 13 & 14
```

---

## [[Feature Scaling]]
**Definition**: General process of standardizing the range of features to improve model performance.  
**Example**:  
Mean normalization implemented in Code Cell 8, visualized in Code Cells 13–14.

---

**Key Concepts**:  
- Mean normalization ensures features are on a comparable scale.  
- Parameters (mean, range) are learned from the **training set** to avoid data leakage.  
- **KDE plots** validate the effectiveness of scaling by showing distribution shifts.