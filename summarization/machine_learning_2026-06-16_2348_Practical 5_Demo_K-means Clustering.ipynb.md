# Practical 5_Demo_K-means Clustering.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here's a structured summary of the provided K-means clustering practical:

---

### [[K-means Clustering]]
**Definition**: An iterative vector quantization algorithm used to partition observations into `k` clusters based on distances to cluster centroids.  
**Formula**: Objective function to minimize:  
$$ \text{SSE} = \sum_{i=1}^{k} \sum_{x \in C_i} \|x - \mu_i\|^2 $$  
where \(C_i\) = cluster, \(\mu_i\) = centroid  
**Example**:  
```python
kmeans = KMeans(n_clusters=5, random_state=1)
y_pred = kmeans.fit_predict(X_scaled)
```

---

### [[Sum of Squared Errors (SSE)]]
**Definition**: Metric measuring total squared distance between data points and their cluster centroids. Lower values indicate better clustering.  
**Formula**:  
$$ \text{SSE} = \sum_{i=1}^{n} (x_i - \mu_{c(i)})^2 $$  
**Example**:  
```python
print(kmeans.inertia_)  # Outputs SSE value for the model
```

---

### [[Elbow Method]]
**Definition**: Technique to determine optimal number of clusters (`k`) by plotting SSE against varying `k` values. The "elbow" point indicates where SSE improvement diminishes.  
**Formula**: N/A (Visual interpretation method)  
**Example**:  
```python
sse = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)
plt.plot(range(1,11), sse)
```

---

### [[StandardScaler]]
**Definition**: Preprocessing technique that standardizes features by removing mean and scaling to unit variance using z-score normalization.  
**Formula**:  
$$ z = \frac{x - \mu}{\sigma} $$  
**Example**:  
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
```

---

### [[Cluster Centroids]]
**Definition**: Representative central points of clusters calculated as mean of all data points in the cluster.  
**Formula**:  
$$ \mu = \frac{1}{n} \sum_{i=1}^{n} x_i $$  
**Example**:  
```python
print(kmeans.cluster_centers_)  # Outputs centroid coordinates
```

---

### [[Customer Segmentation]]
**Definition**: Marketing strategy that divides customers into groups based on behavioral characteristics (e.g., income, spending).  
**Example**:  
```python
dat['Cluster'] = y_pred  # Assigning cluster labels to customers
```
**Insight**: Identified 5 segments including:
- Cluster 0: Low income, high spending
- Cluster 3: High income, high spending

---

### [[Visual Cluster Analysis]]
**Techniques**:  
1. **Scatter Plots**: Visualize cluster distribution and centroids  
   ```python
   plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y_pred)
   ```
2. **Boxplots**: Compare feature distributions across clusters  
   ```python
   plt.boxplot([dat[col][dat.Cluster==i] for i in range(5)])
   ```

This structured approach enables data-driven marketing strategies by identifying distinct customer groups through quantitative analysis.