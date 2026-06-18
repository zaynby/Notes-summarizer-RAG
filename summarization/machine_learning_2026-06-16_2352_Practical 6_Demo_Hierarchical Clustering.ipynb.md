# Practical 6_Demo_Hierarchical Clustering.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here is a structured academic summary of the provided Hierarchical Clustering practical exercise:

# Week 6 - Hierarchical Clustering  
**Module:** machine_learning  
**Style:** structured_academic  

## [[Hierarchical Clustering]]  
**Definition**: An unsupervised machine learning method that builds a hierarchy of clusters through either agglomerative (bottom-up) or divisive (top-down) approaches.  
**Formula**: N/A  
**Example**: Used to segment bank customers based on age and annual salary, revealing 5 optimal clusters including low-income outliers.  

---

## [[Dendrogram]]  
**Definition**: A tree-like diagram that visualizes the hierarchical clustering process, showing the distance between merged clusters.  
**Formula**: N/A  
**Example**: Illustrated the merging pattern of customer data points, with colors indicating cluster separation at a 70% distance threshold.  

---

## [[Agglomerative Clustering]]  
**Definition**: A bottom-up hierarchical clustering method where each data point starts as its own cluster, with iteratively merged clusters based on proximity.  
**Formula**: N/A  
**Example**: Implemented using `AgglomerativeClustering` with Ward's linkage to group customers into 3 or 5 clusters.  

---

## [[Ward's Linkage]]  
**Definition**: A linkage method that minimizes the variance within clusters during hierarchical clustering.  
**Formula**: N/A  
**Example**: Used as the default method in `shc.linkage` for customer segmentation, prioritizing compact clusters.  

---

## [[Feature Scaling]]  
**Definition**: Standardizing features to a comparable range (e.g., Z-score) to prevent bias in distance calculations.  
**Formula**: \( z = \frac{x - \mu}{\sigma} \)  
**Example**: Applied `StandardScaler` to normalize age and annual salary before clustering.  

---

## [[Silhouette Score]]  
**Definition**: A metric evaluating cluster quality, ranging from -1 (poor) to 1 (excellent), based on intra-cluster distance and inter-cluster separation.  
**Formula**: \( s = \frac{b - a}{\max(a, b)} \) where \( a \) = mean intra-cluster distance, \( b \) = mean nearest-cluster distance.  
**Example**: Improved from 0.38 (3 clusters) to 0.40 (5 clusters) after hyperparameter tuning.  

---

## [[Cluster Evaluation]]  
**Definition**: Assessing cluster quality using metrics like silhouette score to determine the optimal number of clusters.  
**Formula**: N/A  
**Example**: Evaluated clusters 2–10 using silhouette scores, identifying 5 clusters as optimal.  

---

## [[Outlier Detection]]  
**Definition**: Identifying data points that significantly deviate from the majority of the data.  
**Formula**: N/A  
**Example**: Revealed two outlier clusters: young customers with low income (red) and seniors with low income (yellow).  

---

## [[Distance Matrix]]  
**Definition**: A matrix containing pairwise distances between all data points.  
**Formula**: \( D = \{d_{ij} = \text{distance}(x_i, x_j)\} \)  
**Example**: Generated using `cdist` for scaled customer data, showing pairwise distances between 25 data points.  

---

## [[Linkage]]  
**Definition**: A method to determine the distance between clusters in hierarchical clustering (e.g., single, complete, average, Ward).  
**Formula**: N/A  
**Example**: Ward's linkage minimized variance during customer cluster merging.  

---

### Linked Concepts:  
- [[Unsupervised Learning]]  
- [[Cluster Analysis]]  
- [[Data Preprocessing]]  
- [[Model Evaluation]]  
- [[Outlier Detection]]  

This summary adheres to the structured academic format, linking key concepts for cross-reference and illustrating practical applications from the banking customer segmentation example.