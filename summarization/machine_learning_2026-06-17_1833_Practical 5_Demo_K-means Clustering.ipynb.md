# Practical 5_Demo_K-means Clustering.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here’s a structured summary of the provided K-means clustering practical exercise:

---

### **K-means Clustering**  
**Definition**: An iterative unsupervised learning algorithm that partitions data into *K* distinct clusters based on feature similarity.  
**Formula**:  
Minimize the Sum of Squared Errors (SSE):  
$$
\text{SSE} = \sum_{i=1}^{K} \sum_{x \in C_i} \|x - \mu_i\|^2
$$  
Where:  
- \(C_i\): Cluster \(i\)  
- \(\mu_i\): Centroid of cluster \(i\)  
**Example**:  
```python
kmeans = KMeans(n_clusters=3, random_state=1)
kmeans.fit(X_scaled)
y_pred = kmeans.predict(X_scaled)
```

---

### **Sum of Squared Errors (SSE)**  
**Definition**: Measures the total squared distance between all data points in a cluster and their assigned centroid. Lower SSE indicates tighter clusters.  
**Formula**:  
$$
\text{SSE} = \sum_{j=1}^{N} \|x_j - \mu_{c(j)}\|^2
$$  
Where:  
- \(x_j\): Data point \(j\)  
- \(\mu_{c(j)}\): Centroid of the cluster assigned to \(x_j\)  
**Example**:  
```python
print(kmeans.inertia_)  # Outputs the SSE value
```

---

### **Elbow Method**  
**Definition**: A technique to determine the optimal number of clusters (*K*) by plotting SSE against varying *K* values. The "elbow" point (where SSE curve bends) suggests the optimal *K*.  
**Formula**: None (visual heuristic).  
**Example**:  
```python
sse = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)
plt.plot(range(1, 11), sse)
plt.xlabel("K"); plt.ylabel("SSE")
```  
**Result**: Optimal \(K=5\) identified from the plot.

---

### **StandardScaler**  
**Definition**: Normalizes data by removing the mean and scaling to unit variance, ensuring features contribute equally to distance calculations.  
**Formula**:  
$$
z = \frac{x - \mu}{\sigma}
$$  
Where:  
- \(\mu\): Mean of the feature  
- \(\sigma\): Standard deviation of the feature  
**Example**:  
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scales "Annual Income" and "Spending Score"
```

---

### **Cluster Centroids**  
**Definition**: The mean feature values of all data points in a cluster, representing the cluster’s "center".  
**Formula**:  
$$
\mu_i = \frac{1}{|C_i|} \sum_{x \in C_i} x
$$  
**Example**:  
```python
kmeans.cluster_centers_  # Outputs centroid coordinates (e.g., [[-0.85, 0.45], ...])
```

---

### **Inertia**  
**Definition**: Synonym for SSE in Scikit-learn, quantifying the compactness of clusters.  
**Formula**: Same as [[Sum of Squared Errors (SSE)]].  
**Example**:  
```python
kmeans.inertia_  # Directly returns the SSE value
```

---

### **Grouped Boxplots**  
**Definition**: Visualizations comparing the distribution of features across clusters to interpret cluster characteristics.  
**Example**:  
```python
dat['Cluster'] = y_pred
plt.boxplot([dat['Annual Income'][dat.Cluster == 0], ...])
plt.ylabel("Annual Income")
```  
**Insight**: Cluster 0 = low income, high spending; Cluster 3 = high income, high spending.

---

### **Marketing Insights**  
**Key Segments Identified**:  
1. **Cluster 0**: Low income, high spending (target with discounts).  
2. **Cluster 1**: High income, low spending (encourage higher spending).  
3. **Cluster 2**: Average income/spending (maintain engagement).  
4. **Cluster 3**: High income/spending (retain with premium services).  
5. **Cluster 4**: Low income/spending (cost-sensitive offers).  

---

**Linked Concepts**:  
[[K-means Clustering]] → [[Sum of Squared Errors (SSE)]] → [[Elbow Method]] → [[StandardScaler]] → [[Cluster Analysis]]