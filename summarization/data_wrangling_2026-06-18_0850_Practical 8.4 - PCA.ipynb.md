# Practical 8.4 - PCA.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Summary: Principal Component Analysis (PCA)

#### [[Principal Component Analysis (PCA)]]
**Definition**: A dimensionality reduction technique that transforms high-dimensional data into a lower-dimensional subset of **Principal Components (PCs)**. These PCs are linear combinations of the original variables, orthogonal to each other, and ordered by the amount of variance they explain in the data.  
**Formula**:  
The transformation is derived from the eigenvalues and eigenvectors of the data’s covariance matrix. For a standardized dataset \( X \), the PCs are defined by:  
\[
\text{PC}_i = X \cdot w_i
\]  
where \( w_i \) is the eigenvector corresponding to the \( i \)-th largest eigenvalue of the covariance matrix. The **explained variance ratio** for each PC is:  
\[
\text{Explained Variance Ratio}_i = \frac{\lambda_i}{\sum_{j=1}^n \lambda_j}
\]  
where \( \lambda_i \) is the eigenvalue for the \( i \)-th PC.  
**Example**:  
In the provided code, PCA is applied to the Boston housing dataset after standardization:  
```python
# Initialize and train PCA
pca = PCA()
pca.fit(X_train_scaled)  # Fit to training data

# Transform data into principal components
train_t = pca.transform(X_train_scaled)
test_t = pca.transform(X_test_scaled)
```

---

#### [[Principal Components (PCs)]]
**Definition**: Linear combinations of the original features that capture the maximum variance in the data. Each PC is orthogonal to all others, ensuring no correlation between components.  
**Formula**:  
The first PC (\( \text{PC}_1 \)) maximizes the variance:  
\[
\text{PC}_1 = w_{1,1}x_1 + w_{1,2}x_2 + \dots + w_{1,n}x_n
\]  
Subsequent PCs maximize residual variance under the constraint of orthogonality to previous PCs.  
**Example**:  
The code extracts PCs and their explained variance:  
```python
# Access explained variance ratio
print(pca.explained_variance_ratio_)  # Output: Array of variance ratios for each PC
```

---

#### [[Explained Variance Ratio]]
**Definition**: The proportion of total variance in the data explained by each principal component. Used to determine the number of PCs needed to retain meaningful information.  
**Formula**:  
\[
\text{Explained Variance Ratio}_i = \frac{\lambda_i}{\sum \lambda}
\]  
where \( \lambda_i \) is the eigenvalue of the \( i \)-th PC.  
**Example**:  
The code visualizes the variance explained by each PC:  
```python
# Plot explained variance ratio
plt.plot(pca.explained_variance_ratio_, linewidth=2)
plt.title('Percentage of Variance Explained')
plt.xlabel('PC Index')
plt.ylabel('Variance Ratio')
plt.show()
```

---

#### [[Standardization]]
**Definition**: A preprocessing step that centers the data (mean = 0) and scales it to unit variance (std = 1). Critical for PCA since it ensures all features contribute equally to the variance.  
**Formula**:  
\[
z = \frac{x - \mu}{\sigma}
\]  
where \( \mu \) is the mean and \( \sigma \) the standard deviation.  
**Example**:  
The code standardizes the dataset using `StandardScaler`:  
```python
# Initialize and apply StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on training data
X_test_scaled = scaler.transform(X_test)        # Transform test data
```

---

### Key Workflow Integration
1. **Standardization** → **PCA Training** → **Component Extraction** → **Variance Analysis**  
2. **Wikilinks**: [[Standardization]] → [[Principal Component Analysis (PCA)]] → [[Explained Variance Ratio]] → [[Principal Components (PCs)]]