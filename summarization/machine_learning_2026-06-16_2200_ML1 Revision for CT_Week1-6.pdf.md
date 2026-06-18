# ML1 Revision for CT_Week1-6.pdf
**Module:** machine_learning
**Style:** structured_academic (experimenting)

It seems like you have a detailed outline of clustering techniques and their applications in unsupervised machine learning. Here are some key points to summarize, expand upon, or correct:

### K-Means Clustering

**Key Points:**
- **Objective:** Cluster data points into \(k\) groups.
- **Feature Scaling:** Essential for attributes with larger magnitudes; use Min-max normalization, z-score standardization.

**Steps:**
1. Define the number of clusters (\(k\)).
2. Choose initial centroids randomly.
3. Assign each data point to the nearest centroid.
4. Update centroids by calculating the mean vector of members in each cluster.
5. Repeat steps 3 and 4 until cluster membership stabilizes.

**Choosing \(k\) Value:**
- **Sum of Squares:** Minimize within-cluster spread and maximize between-cluster separation.
- **Elbow Method:** Plot within-cluster sum of squares vs. \(k\); look for the bend.
- **Silhouette Analysis:** Measure how well each point fits its cluster; choose \(k\) that maximizes mean silhouette coefficient.

### Hierarchical Clustering

**Agglomerative Clustering:**
1. Start with each data point as a single cluster.
2. Compute proximity matrix.
3. Merge the two closest clusters iteratively.
4. Repeat until only one cluster remains.

**Linkage Criteria:**
- **Single Linkage:** Minimum dissimilarity between merged pairs.
- **Complete Linkage:** Maximum dissimilarity between merged pairs.
- **Average Linkage:** Average dissimilarity between merged pairs.
- **Centroid Linkage:** Dissimilarity based on centroids.

### K-Means Variants

**K-Medoids:**
- Used for noisy data; replaces mean with medoid (most centrally located object).

**K-Modes:**
- Suitable for categorical data; uses mode as cluster representative instead of mean.

### Strengths and Weaknesses of Hierarchical Clustering:
- **Strengths:** Deterministic results, flexible granularity, no need to pre-specify \(k\), interpretable structure.
- **Weaknesses:** Does not scale well with large datasets.

### Silhouette Coefficient
- **Range:** \(-1\) to \(1\).
  - \(≈ 1\): Well-clustered (close to own cluster, far from others) – Best.
  - \(≈ 0\): On or near decision boundary between two clusters.
  - < \(0\): Likely assigned to wrong cluster.
  - = \(0\): Cluster contains only one point.

### Summary
- **K-Means Clustering:** Good for large datasets but sensitive to initial centroids and outliers.
- **Hierarchical Clustering:** Provides nested structure, flexible granularity but less scalable with larger datasets.
- **K-Medoids/K-Modes:** Useful when dealing with noisy or categorical data.

If you need further details on any specific topic or more examples, feel free to ask!