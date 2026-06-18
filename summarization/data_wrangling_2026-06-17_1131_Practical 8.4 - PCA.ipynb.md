# Practical 8.4 - PCA.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Principal Component Analysis (PCA)

## [[Principal Component Analysis (PCA)]]
**Definition**: A dimensionality reduction technique that transforms a high-dimensional dataset into a smaller set of orthogonal (uncorrelated) principal components (PCs), which capture the maximum variance in the data.  
**Formula**:  
PCA involves eigenvalue decomposition of the covariance (or correlation) matrix of the standardized data. The PCs are the eigenvectors, and the eigenvalues represent the variance explained by each PC:  
\[
\text{Cov}(X_{\text{scaled}}) = V \Lambda V^T
\]  
where \(V\) is the matrix of eigenvectors (PCs) and \(\Lambda\) is the diagonal matrix of eigenvalues.  
**Example**:  
In the provided code, PCA is implemented using `sklearn.decomposition.PCA` on the Boston Housing dataset after standardization:  
```python
pca = PCA()
pca.fit(X_train_scaled)  # Training PCA on scaled data
train_t = pca.transform(X_train_scaled)  # Projecting data onto PCs
```

---

## [[Principal Components (PCs)]]
**Definition**: Linear combinations of the original features that are orthogonal to each other and sequentially maximize the variance in the data.  
**Formula**:  
The \(i\)-th principal component is given by:  
\[
\text{PC}_i = w_{i1}X_1 + w_{i2}X_2 + \dots + w_{in}X_n
\]  
where \(w_{i1}, \dots, w_{in}\) are the eigenvectors (weights) from the covariance matrix.  
**Example**:  
After fitting PCA, the transformed data `train_t` and `test_t` represent the original data projected onto the principal components.

---

## [[Explained Variance Ratio]]
**Definition**: The proportion of variance in the data explained by each principal component, often used to determine the optimal number of PCs to retain.  
**Formula**:  
\[
\text{Explained Variance Ratio}_i = \frac{\lambda_i}{\sum_{j=1}^n \lambda_j}
\]  
where \(\lambda_i\) is the eigenvalue corresponding to the \(i\)-th PC.  
**Example**:  
The code extracts and visualizes the explained variance ratio:  
```python
print(pca.explained_variance_ratio_)  # Output: Array of variance ratios
plt.plot(pca.explained_variance_ratio_, linewidth=2)  # Plotting variance decay
```

---

## [[Standardization]]
**Definition**: A preprocessing step that centers the data (mean = 0) and scales it to unit variance (std = 1), ensuring PCA is not dominated by features with large scales.  
**Formula**:  
\[
z = \frac{x - \mu}{\sigma}
\]  
where \(\mu\) is the mean and \(\sigma\) is the standard deviation.  
**Example**:  
The code uses `StandardScaler` to standardize the training and test sets:  
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## [[Orthogonality in PCA]]
**Definition**: The property that all principal components are mutually orthogonal (perpendicular), meaning their covariance is zero.  
**Formula**:  
For two distinct PCs \( \text{PC}_i \) and \( \text{PC}_j \):  
\[
\text{Cov}(\text{PC}_i, \text{PC}_j) = 0 \quad \text{for} \quad i \neq j
\]  
**Example**:  
Orthogonality ensures that the transformed data `train_t` has uncorrelated columns, as seen in the PCA output.

---

## [[Variance Maximization]]
**Definition**: The principle that the first PC captures the maximum variance in the data, with subsequent PCs capturing the largest remaining variance under the constraint of orthogonality.  
**Formula**:  
The optimization problem for the first PC is:  
\[
\max_{\mathbf{w}} \mathbf{w}^T \Sigma \mathbf{w}
\]  
subject to \(\mathbf{w}^T \mathbf{w} = 1\), where \(\Sigma\) is the covariance matrix.  
**Example**:  
The plot of explained variance ratios (Code Cell 12) illustrates the decay in variance captured by each subsequent PC, guiding the selection of components.