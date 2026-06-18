# Practical 6_Demo_Hierarchical Clustering.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided Hierarchical Clustering content:

---

### [[Hierarchical Clustering]]  
**Definition**: An unsupervised machine learning method that builds a hierarchy of clusters by either iteratively merging (agglomerative) or splitting (divisive) data points.  
**Formula**: N/A  
**Example**: Customer segmentation using age and annual salary to identify groups like "young low-income" and "senior low-income" (Section 5).  

---

### [[Dendrogram]]  
**Definition**: A tree-like diagram that visualizes the hierarchical structure of clusters, showing merge distances between data points or clusters.  
**Formula**: N/A  
**Example**: Visualized cluster linkages using `shc.dendrogram(Z)` to determine optimal cluster count (Code Cell 23).  

---

### [[Agglomerative Clustering]]  
**Definition**: A bottom-up hierarchical clustering approach where each data point starts as its own cluster, iteratively merging closest pairs until one cluster remains.  
**Formula**: N/A  
**Example**: Implemented with `AgglomerativeClustering(n_clusters=3)` for initial customer segmentation (Code Cell 26).  

---

### [[StandardScaler]]  
**Definition**: A feature scaling technique that standardizes data by removing the mean and scaling to unit variance.  
**Formula**: \( x_{\text{scaled}} = \frac{x - \mu}{\sigma} \)  
**Example**: Scaled age and annual salary features to comparable ranges before clustering (Code Cell 12).  

---

### [[Silhouette Score]]  
**Definition**: A metric to evaluate cluster separation and cohesion, ranging from -1 (poor) to 1 (excellent).  
**Formula**:  
\[ \text{Silhouette Score} = \frac{\text{Between-cluster distance} - \text{Within-cluster distance}}{\max(\text{Between}, \text{Within})} \]  
**Example**: Improved score from 0.38 (3 clusters) to 0.40 (5 clusters) (Code Cells 32 & 42).  

---

### [[Linkage Methods]]  
**Definition**: Criteria for merging clusters in hierarchical clustering. Common methods include:  
- **Single**: Minimum distance between clusters.  
- **Complete**: Maximum distance between clusters.  
- **Average**: Mean distance between clusters.  
- **Ward**: Minimizes variance increase from merging.  
**Formula**: N/A  
**Example**: Used Ward’s method (`method='ward'`) for customer segmentation (Code Cell 20).  

---

### [[Condensed Distance Matrix]]  
**Definition**: A compact representation of pairwise distances between clusters, used in hierarchical clustering.  
**Formula**: N/A  
**Example**: Generated via `cdist(X_scaled, X_scaled)` (Code Cell 16), resulting in a (n(n-1)/2) dimensional array.  

---

### [[Cluster Evaluation]]  
**Definition**: Assessing cluster quality using metrics like Silhouette Score to determine optimal number of clusters.  
**Formula**: N/A  
**Example**: Compared Silhouette Scores for 2–10 clusters, identifying 5 as optimal (Code Cells 35–37).  

---

### [[Feature Scaling]]  
**Definition**: Rescaling features to a standard range to prevent bias toward higher-magnitude features.  
**Formula**: N/A  
**Example**: Applied to age (25–70) and annual salary (10k–29k) to ensure equal contribution (Markdown Cell 11).  

---

### [[Outliers in Clustering]]  
**Definition**: Data points that deviate significantly from the majority, often forming isolated clusters.  
**Formula**: N/A  
**Example**: Identified "young low-income" (red) and "senior low-income" (yellow) clusters as outliers (Markdown Cell 43).  

---

### Linked Concepts:  
- [[Unsupervised Learning]]  
- [[Distance Metrics]]  
- [[Model Evaluation]]  
- [[Principal Component Analysis (PCA)]]  

This summary connects key hierarchical clustering concepts via wikilinks, adheres to the structured academic format, and integrates practical examples from the notebook.