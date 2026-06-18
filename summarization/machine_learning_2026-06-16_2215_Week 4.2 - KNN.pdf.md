# Week 4.2 - KNN.pdf
**Module:** machine_learning
**Style:** structured_academic (experimenting)

# K-Nearest Neighbors (KNN) Summary

## **K-Nearest Neighbors (KNN)**  
**Definition**: A supervised machine learning algorithm used for classification and regression tasks. It predicts outcomes based on the proximity of data points in the feature space.  
**Formula**:  
- **Classification**: Majority vote among the *K* nearest neighbors.  
- **Regression**: Mean value of the *K* nearest neighbors.  
**Example**: In the Dry Bean dataset, a new sample was classified as "DERMASON" because its 10 nearest neighbors were all DERMASON beans.  

---

## **Classification in KNN**  
**Definition**: Assigns the most frequent class label among the *K* nearest neighbors to a new sample.  
**Formula**:  
$$
\text{Class} = \text{Argmax}_{c \in \text{Classes}} \sum_{i=1}^{K} \mathbb{I}(y_i = c)
$$  
**Example**: A new sample is classified as "Seker" if 7 out of 10 nearest neighbors are labeled "Seker".  

---

## **Regression in KNN**  
**Definition**: Predicts a continuous value as the mean of the *K* nearest neighbors.  
**Formula**:  
$$
\hat{y} = \frac{1}{K} \sum_{i=1}^{K} y_i
$$  
**Example**: Predicting the price of a house based on the average price of the *K* nearest similar houses.  

---

## **Dry Bean Dataset**  
**Definition**: A dataset containing 13,611 images of 7 bean types (e.g., Seker, DERMASON) with 16 extracted features (e.g., Area, Perimeter).  
**Example**: Used to demonstrate KNN classification by visualizing high-dimensional data via [[Principal Component Analysis (PCA)]] for 2D representation.  

---

## **Brute Force Method**  
**Definition**: Computes distances between the new sample and all training data points to find nearest neighbors.  
**Formula**: Euclidean distance between points $x$ and $y$:  
$$
d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
$$  
**Example**: Calculating distances from a new bean sample to all 13,611 samples in the Dry Bean dataset.  

---

## **Choosing K Value**  
**Definition**: Selecting the optimal number of neighbors (*K*) to balance bias and variance.  
**Formula**: Common heuristic: $K = \sqrt{n}$, where $n$ is the number of training samples.  
**Example**: For a dataset with 100 samples, start with $K = 10$.  

---

## **Distance Metrics**  
### **Euclidean Distance**  
**Definition**: Measures straight-line distance between two points in Euclidean space.  
**Formula**:  
$$
d_{\text{Euclidean}} = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
$$  
**Example**: Used in the Dry Bean dataset to compare bean shapes.  

### **Manhattan Distance**  
**Definition**: Measures distance as the sum of absolute differences along axes.  
**Formula**:  
$$
d_{\text{Manhattan}} = \sum_{i=1}^{n} |x_i - y_i|
$$  
**Example**: Preferred for grid-based pathfinding problems.  

### **Hamming Distance**  
**Definition**: Counts the number of differing positions between categorical sequences.  
**Formula**:  
$$
d_{\text{Hamming}} = \sum_{i=1}^{n} \mathbb{I}(x_i \neq y_i)
$$  
**Example**: Comparing categorical labels like bean types.  

---

## **Scikit-Learn Implementation**  
**Definition**: Utilizes `KNeighborsClassifier` or `KNeighborsRegressor` with parameters like `n_neighbors`, `algorithm`, and `metric`.  
**Example**:  
```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
model.fit(X_train, y_train)
```  

---

## **Advantages and Disadvantages**  
### **Advantages**  
- Simple to implement and interpret.  
- No explicit training phase; instance-based learning.  
- Effective for multi-class problems.  

### **Disadvantages**  
- Computationally expensive for large datasets (e.g., brute force).  
- Sensitive to high dimensionality ([[Curse of Dimensionality]]).  
- Requires feature normalization.  
- Poor performance on imbalanced datasets.  

---

## **Linked Concepts**  
- [[Supervised Learning]]  
- [[Principal Component Analysis (PCA)]]  
- [[Curse of Dimensionality]]  
- [[Euclidean Distance]]  
- [[Manhattan Distance]]  
- [[Hamming Distance]]