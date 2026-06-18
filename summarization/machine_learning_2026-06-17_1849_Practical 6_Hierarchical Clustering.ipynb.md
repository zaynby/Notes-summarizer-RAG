# Practical 6_Hierarchical Clustering.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here's a structured summary of the provided Hierarchical Clustering content:

---

### [[Hierarchical Clustering]]
**Definition**: A method that builds nested clusters by either merging smaller clusters (Agglomerative) or splitting larger ones (Divisive).  
**Formula**:  
- Proximity matrix calculation: $d(i,j)$ (distance between clusters)  
- Linkage criteria (e.g., Average: $d\left(\{C_i, C_j\}, \{C_k, C_l\}\right) = \frac{1}{|C_i||C_j|}\sum_{p \in C_i} \sum_{q \in C_j} d(p,q)$)  
**Example**:  
```python
Z = shc.linkage(X_scaled, method='average')  # Builds hierarchical clusters
plt.figure(); shc.dendrogram(Z)  # Visualizes nested structure
```

---

### [[Agglomerative Clustering]]
**Definition**: Bottom-up approach where each data point starts as its own cluster, iteratively merging closest pairs until one cluster remains.  
**Formula**:  
- Merge rule: $C_{\text{new}} = C_i \cup C_j$ where $d(C_i, C_j)$ is minimized  
**Example**:  
```python
ac3 = AgglomerativeClustering(n_clusters=3, linkage='average')
clusters = ac3.fit_predict(X_scaled)  # Assigns 3 clusters
```

---

### [[Dendrogram]]
**Definition**: Tree-like diagram visualizing hierarchical cluster structure and merge distances.  
**Formula**: Derived from linkage matrix $Z$ (rows represent merges, columns: cluster IDs and distances)  
**Example**:  
```python
plt.figure(figsize=(12, 12))
shc.dendrogram(Z, orient='top')  # Shows hierarchical relationships
plt.xlabel('Data points')
plt.title('Dendrogram')
```

---

### [[Linkage Methods]]
**Definition**: Criteria for calculating distances between clusters during merging. Common types:  
1. **Single**: $d(C_i, C_j) = \min(d(p,q))$  
2. **Complete**: $d(C_i, C_j) = \max(d(p,q))$  
3. **Average**: Mean distance between all pairs  
4. **Ward**: Minimizes variance increase ($\min \Delta SS$)  
**Example**:  
```python
Z_ward = shc.linkage(X_scaled, method='ward')  # Default in many implementations
```

---

### [[Silhouette Score]]
**Definition**: Metric evaluating cluster separation and cohesion (-1 ≤ score ≤ 1). Higher values indicate better clustering.  
**Formula**:  
$$
S = \frac{b - a}{b} \quad \text{where } a = \text{within-cluster distance}, \; b = \text{nearest cluster distance}
$$
**Example**:  
```python
silhouette_score(X_scaled, ac3.labels_)  # Evaluates cluster quality
```

---

### [[Condensed Distance Matrix]]
**Definition**: Compact representation of pairwise distances between clusters.  
**Formula**: Upper triangular matrix $D$ where $D[i,j] = d(C_i, C_j)$  
**Example**:  
```python
distance_matrix = cdist(X_scaled, X_scaled)  # Full matrix
condensed_matrix = squareform(distance_matrix)  # Converts to condensed form
```

---

### [[StandardScaler]]
**Definition**: Normalizes data by removing mean and scaling to unit variance.  
**Formula**:  
$$
X_{\text{scaled}} = \frac{X - \mu}{\sigma} \quad (\mu = \text{mean}, \; \sigma = \text{standard deviation})
$$
**Example**:  
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)  # Normalizes features
```

---

### [[Cluster Evaluation]]
**Definition**: Process to determine optimal number of clusters using metrics like Silhouette Score.  
**Example**:  
```python
k_range = range(2, 11)
silhouette_scores = [silhouette_score(X_scaled, AgglomerativeClustering(n_clusters=k).fit_predict(X_scaled)) for k in k_range]
plt.bar(k_range, silhouette_scores)  # Visualizes optimal K
```

---

### Key Comparison (Average vs Ward Linkage)
| **Metric**          | **Average Linkage**       | **Ward Linkage**          |
|----------------------|---------------------------|----------------------------|
| Optimal K (Silhouette) | 9 clusters (higher score) | 5 clusters (higher score) |
| Merging Criterion    | Mean distance between clusters | Minimizes variance increase |

---

This summary integrates theoretical concepts, mathematical formulations, and practical code examples from the provided materials. Use [[Wikilinks]] to navigate between related concepts in your notes.