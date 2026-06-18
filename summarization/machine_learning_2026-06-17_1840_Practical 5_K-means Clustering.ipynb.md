# Practical 5_K-means Clustering.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

# Summary: K-means Clustering

## [[K-means Clustering]]
**Definition**: An iterative clustering algorithm that partitions data into *k* distinct clusters based on distances. It initializes centroids, assigns data points to the nearest cluster, updates centroids, and repeats until convergence or a maximum number of iterations is reached.  
**Formula**: Objective function to minimize:  
\[ \text{SSE} = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (x_i - \mu_j)^2 \]  
**Example**:  
```python
kmeans = KMeans(n_clusters=3, n_init=20, max_iter=300, random_state=1)
kmeans.fit(X_scaled)
```

---

## [[Sum of Squared Errors (SSE)]]
**Definition**: A metric to evaluate clustering performance, representing the sum of squared distances between data points and their assigned cluster centroids. Lower SSE indicates better clustering.  
**Formula**:  
\[ \text{SSE} = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (x_i - \mu_j)^2 \]  
**Example**:  
```python
sse = kmeans.inertia_
print(f"Sum of Squared Errors (SSE): {sse}")
```

---

## [[Elbow Method]]
**Definition**: A technique to determine the optimal number of clusters (*k*) by plotting SSE values against varying *k*. The "elbow" point (where SSE decreases less sharply) indicates the optimal *k*.  
**Formula**: No direct formula; relies on visual interpretation.  
**Example**:  
```python
sse = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=1)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)
plt.plot(range(1, 11), sse, 'b-*')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.show()
```

---

## [[StandardScaler]]
**Definition**: A preprocessing method that standardizes features by removing the mean and scaling to unit variance, ensuring equal contribution of all features to distance calculations.  
**Formula**:  
\[ X_{\text{scaled}} = \frac{X - \mu}{\sigma} \]  
**Example**:  
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## [[Centroids]]
**Definition**: The central point of a cluster, representing the average position of all data points assigned to that cluster.  
**Formula**:  
\[ \mu_j = \frac{1}{n_j} \sum_{i=1}^{n_j} x_i \]  
**Example**:  
```python
centroids = kmeans.cluster_centers_
```

---

## [[Cluster]]
**Definition**: A group of data points that are more similar to each other than to points in other clusters, as determined by the K-means algorithm.  
**Formula**: Not applicable.  
**Example**:  
```python
y_pred = kmeans.predict(X_scaled)
```

---

## Key Concepts Interconnection
- [[K-means Clustering]] uses [[Centroids]] to group data into [[Cluster]]s.  
- Model performance is evaluated using [[Sum of Squared Errors (SSE)]].  
- The [[Elbow Method]] aids in selecting the optimal number of clusters (*k*) by analyzing SSE trends.  
- Features are normalized using [[StandardScaler]] to ensure robust distance calculations.