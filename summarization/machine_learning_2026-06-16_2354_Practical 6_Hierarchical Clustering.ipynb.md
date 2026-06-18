# Practical 6_Hierarchical Clustering.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

# Summary: Hierarchical Clustering  

## [[Hierarchical Clustering]]  
**Definition**: A method of cluster analysis which seeks to build a hierarchy of clusters. It can be either **agglomerative** (bottom-up, merging clusters) or **divisive** (top-down, splitting clusters).  
**Formula**: None directly, but relies on distance metrics (e.g., Euclidean) and linkage criteria.  
**Example**:  
```python  
Z = shc.linkage(X_scaled, method='average')  # Agglomerative clustering with average linkage  
plt.figure(figsize=(12, 12))  
shc.dendrogram(Z)  # Visualize hierarchy  
```  

---

## [[Agglomerative Clustering]]  
**Definition**: A bottom-up hierarchical clustering approach where each data point starts as its own cluster, and iteratively merges the closest pairs based on a linkage criterion.  
**Formula**: Proximity matrix updates after each merge using linkage methods (e.g., single, average, ward).  
**Example**:  
```python  
ac3 = AgglomerativeClustering(n_clusters=3, linkage='average')  
clusters = ac3.fit_predict(X_scaled)  
```  

---

## [[Linkage Methods]]  
**Definition**: Criteria to measure distance between clusters during merging. Common types include:  
- **Single (Nearest Neighbor)**: Minimum distance between clusters.  
- **Complete (Farthest Neighbor)**: Maximum distance between clusters.  
- **Average**: Mean distance between all points in two clusters.  
- **Ward**: Minimizes variance increase within clusters.  
**Formula**:  
- Ward’s method minimizes \( \sum \text{variance within clusters} \).  
**Example**:  
```python  
# Using average linkage  
ac_i = AgglomerativeClustering(n_clusters=i, linkage='average')  

# Default Ward method in previous demo  
ac_ward = AgglomerativeClustering(n_clusters=5, linkage='ward')  
```  

---

## [[Dendrogram]]  
**Definition**: A tree-like diagram that visualizes the hierarchical clustering structure, showing merge points and distances.  
**Formula**: Derived from the condensed distance matrix.  
**Example**:  
```python  
Z = shc.linkage(X_scaled, method='average')  
shc.dendrogram(Z)  # Plot dendrogram  
```  

---

## [[Silhouette Score]]  
**Definition**: A metric to evaluate clustering quality, ranging from -1 (poor) to 1 (excellent). Measures how similar a data point is to its own cluster compared to others.  
**Formula**:  
\[ \text{Silhouette Score} = \frac{\text{Inter-cluster distance} - \text{Intra-cluster distance}}{\max(\text{Inter-cluster}, \text{Intra-cluster})} \]  
**Example**:  
```python  
silhouette_scores = []  
for i in range(2, 11):  
    ac_i = AgglomerativeClustering(n_clusters=i, linkage='average')  
    score = silhouette_score(X_scaled, ac_i.fit_predict(X_scaled))  
    silhouette_scores.append(score)  
plt.bar(range(2, 11), silhouette_scores)  # Compare scores  
```  

---

## [[Condensed Distance Matrix]]  
**Definition**: A compact representation of pairwise distances between clusters, used to build dendrograms.  
**Formula**: Computed using distance metrics like Euclidean:  
\[ d_{ij} = \sqrt{\sum (x_i - x_j)^2} \]  
**Example**:  
```python  
from scipy.spatial.distance import cdist  
print(cdist(X_scaled, X_scaled))  # Generate pairwise distances  
```  

---

## [[StandardScaler]]  
**Definition**: A preprocessing tool to standardize features by removing mean and scaling to unit variance.  
**Formula**:  
\[ z = \frac{x - \mu}{\sigma} \]  
**Example**:  
```python  
scaler = StandardScaler()  
X_scaled = scaler.fit_transform(df.values())  # Scale dataset  
```  

---

## [[Cluster Evaluation (Elbow Method)]]  
**Definition**: A technique to determine the optimal number of clusters by observing where the improvement in cluster quality (e.g., silhouette score) diminishes (the "elbow" point).  
**Formula**: None, but uses metrics like silhouette score or distortion.  
**Example**:  
```python  
# Silhouette score bar plot to identify optimal K  
plt.bar(k_range, silhouette_scores)  
plt.xlabel('Number of Clusters')  
plt.ylabel('Silhouette Score')  
```  

---

### Key Comparison: Average vs. Ward Linkage  
- **Average Linkage**: Silhouette score peaked at **9 clusters**.  
- **Ward Linkage**: Silhouette score peaked at **5 clusters** (from previous demo).  
**Implication**: Linkage method significantly impacts cluster structure and optimal cluster count.  

```python  
# Final model with average linkage (9 clusters)  
ac5 = AgglomerativeClustering(n_clusters=9, linkage='average')  
plt.scatter(X_scaled[:,0], X_scaled[:,1], c=ac5.fit_predict(X_scaled))  
```  

--- 

This summary connects clustering theory, evaluation metrics, and practical implementation steps for hierarchical clustering. Use [[Wikilinks]] to explore related concepts like [[K-means Clustering]] or [[Distance Metrics]].