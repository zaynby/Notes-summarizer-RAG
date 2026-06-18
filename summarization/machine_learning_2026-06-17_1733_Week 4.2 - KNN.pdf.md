# Week 4.2 - KNN.pdf
**Module:** machine_learning
**Style:** structured_academic (experimenting)

# K-Nearest Neighbors (KNN)  

## Term -> Definition -> Formula -> Example  

### **K-Nearest Neighbors (KNN)**  
**Definition**: A supervised machine learning algorithm used for classification and regression tasks. It predicts outcomes based on the proximity of data points in the feature space.  
**Formula**:  
- **Euclidean Distance**: \( d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2} \)  
- **Manhattan Distance**: \( d(x, y) = \sum_{i=1}^{n} |x_i - y_i| \)  
- **Hamming Distance**: Count of differing categorical features between two data points.  
**Example**:  
- **Classification**: A new sample is classified as "DERMASON" bean if 10 nearest neighbors (K=10) in the Dry Bean Dataset are all DERMASON.  
- **Regression**: Predicts a continuous value (e.g., price) as the mean of the K nearest neighbors’ values.  

---

### **Supervised Learning**  
**Definition**: A learning approach where the algorithm is trained on labeled data (input-output pairs) to predict outputs for new inputs.  
**Formula**: \( y = f(x) \), where \( x \) is the input and \( y \) is the predicted output.  
**Example**:  
- KNN uses labeled bean images (e.g., "Seker," "Barbunya") to classify new unlabeled bean images.  

---

### **Classification**  
**Definition**: A type of supervised learning where outputs are categorical labels.  
**Formula**: \( \text{Class}(x_{\text{new}}) = \text{Mode}\{\text{Labels of K nearest neighbors}\} \)  
**Example**:  
- Classifying a new bean image as "Cali" based on the majority class among its K nearest neighbors.  

---

### **Regression**  
**Definition**: A type of supervised learning where outputs are continuous values.  
**Formula**: \( \text{Value}(x_{\text{new}}) = \frac{1}{K} \sum_{i=1}^{K} y_i \), where \( y_i \) are the values of K nearest neighbors.  
**Example**:  
- Predicting the perimeter of a bean image as the average perimeter of its K nearest neighbors.  

---

### **Distance Metric**  
**Definition**: A mathematical function to measure the distance between data points.  
**Formula**:  
- **Euclidean**: \( \sqrt{\sum (x_i - y_i)^2} \)  
- **Manhattan**: \( \sum |x_i - y_i| \)  
- **Hamming**: \( \text{Count of differing categorical features} \)  
**Example**:  
- Euclidean distance is used to compare the 16 features of bean images in the Dry Bean Dataset.  

---

### **Choosing K Value**  
**Definition**: Selecting the optimal number of neighbors (K) for KNN.  
**Formula**: Default \( K = \sqrt{n} \), where \( n \) is the number of training samples.  
**Example**:  
- For a dataset with 100 samples, start with \( K = 10 \) (since \( \sqrt{100} = 10 \)).  

---

### **Principal Component Analysis (PCA)**  
**Definition**: A dimensionality reduction technique to visualize high-dimensional data.  
**Formula**: \( \text{Reduced dimensions} = \text{Linear combinations of original features} \)  
**Example**:  
- PCA reduces the 16-dimensional Dry Bean Dataset to 2D for visualization.  

---

### **Advantages of KNN**  
1. Simple to implement.  
2. No explicit training phase.  
3. Effective for multi-class problems.  

### **Disadvantages of KNN**  
1. Computationally expensive for large datasets (brute force).  
2. Suffers from the **curse of dimensionality**.  
3. Requires feature normalization.  

---

### **Scikit-Learn Implementation**  
**Definition**: KNN is implemented via `KNeighborsClassifier` or `KNeighborsRegressor` in Python.  
**Formula**: N/A  
**Example**:  
```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
```  

---

[[Supervised Learning]] | [[Classification]] | [[Regression]] | [[Distance Metric]] | [[Principal Component Analysis (PCA)]] | [[Curse of Dimensionality]]