# Practical 5_K-means Clustering.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

# Summary: K-means Clustering and Cluster Analysis

## [[K-means Clustering]]  
**Definition**: An iterative unsupervised learning algorithm that partitions data into *K* clusters based on distances between data points and cluster centroids.  
**Formula**: Objective function to minimize:  
\[ \text{SSE} = \sum_{i=1}^{K} \sum_{x \in C_i} (x - \mu_i)^2 \]  
where \( \mu_i \) is the centroid of cluster \( C_i \).  
**Example**:  
```python
kmeans = KMeans(n_clusters=3, n_init=20, max_iter=300, random_state=1)
kmeans.fit(X_scaled)
y_pred = kmeans.predict(X_scaled)
```

---

## [[Sum of Squared Errors (SSE)]]  
**Definition**: A metric to evaluate clustering quality, representing the total squared distance between data points and their cluster centroids.  
**Formula**:  
\[ \text{SSE} = \sum_{i=1}^{K} \sum_{j=1}^{N_i} (x_{ij} - \mu_i)^2 \]  
where \( x_{ij} \) is the \( j \)-th point in cluster \( i \), and \( \mu_i \) is the centroid.  
**Example**:  
```python
sse = kmeans.inertia_  # Access SSE directly from KMeans model
print(f"SSE: {sse}")
```

---

## [[Elbow Method]]  
**Definition**: A technique to determine the optimal number of clusters (*K*) by identifying the "elbow" point in the SSE vs. *K* plot, where SSE decreases marginally.  
**Formula**: No direct formula; iterative computation of SSE for varying *K*:  
\[ \text{SSE}(K) = \text{Compute SSE for } K \text{ clusters} \]  
**Example**:  
```python
sse = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=1)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)
plt.plot(range(1, 11), sse, 'b-*')  # Plot SSE vs. K
```

---

## [[StandardScaler]]  
**Definition**: A preprocessing tool that standardizes features by removing the mean and scaling to unit variance.  
**Formula**:  
\[ z = \frac{x - \mu}{\sigma} \]  
where \( \mu \) = mean, \( \sigma \) = standard deviation.  
**Example**:  
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scales dataset X
```

---

## [[Hierarchical Clustering]]  
**Definition**: A method that builds nested clusters either agglomeratively (bottom-up) or divisively (top-down). Agglomerative clustering merges closest pairs iteratively.  
**Formula**: Proximity matrix updates using linkage criteria (e.g., single, complete, average).  
**Example**:  
```python
# Agglomerative steps (conceptual):
1. Initialize each point as a cluster.
2. Merge closest clusters using a linkage criterion.
3. Repeat until one cluster remains.
```

---

## Key Links  
- [[K-means Clustering]] uses [[Sum of Squared Errors (SSE)]] for evaluation and the [[Elbow Method]] to optimize *K*.  
- Data preprocessing with [[StandardScaler]] ensures robust clustering.  
- [[Hierarchical Clustering]] provides an alternative to K-means for exploring nested cluster structures.