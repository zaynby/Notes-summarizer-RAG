# Wk4-Practical_4.2_KNN.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided KNN practical content:

---

### [[K-Nearest Neighbors (KNN)]]
**Definition**: A supervised learning algorithm that classifies or regresses data points based on the majority vote (classification) or average (regression) of their *K* nearest neighbors in the feature space.  
**Formula**:  
- **Classification**: \( \text{Class} = \text{Argmax}_{c} \sum_{i=1}^{K} \mathbb{I}(y_i = c) \)  
- **Regression**: \( \hat{y} = \frac{1}{K} \sum_{i=1}^{K} y_i \)  
**Example**: Classified URLs into Benign/Phishing (85% accuracy with *K=5*) and predicted ad purchases in Social Network Ads dataset.

---

### [[StandardScaler]]
**Definition**: A feature scaling technique that standardizes data by removing the mean and scaling to unit variance.  
**Formula**: \( x_{\text{scaled}} = \frac{x - \mu}{\sigma} \)  
**Example**: Scaled `EstimatedSalary` and `Age` in Social Network Ads dataset to improve KNN performance.

---

### [[Train-Test Split]]
**Definition**: Divides data into training and testing subsets to evaluate model generalization.  
**Formula**: N/A  
**Example**: Split URL dataset into 75% training and 25% testing data using `train_test_split`.

---

### [[Confusion Matrix]]
**Definition**: A table quantifying correct and incorrect predictions for classification models.  
**Structure**:  
| | Predicted Positive | Predicted Negative |  
|----------------------|--------------------|--------------------|  
| **Actual Positive** | TP | FN |  
| **Actual Negative** | FP | TN |  
**Example**: Phishing detection showed 120 TP and 30 FN in the URL dataset.

---

### [[Accuracy Score]]
**Definition**: Proportion of correct predictions (both true positives and true negatives).  
**Formula**: \( \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} \)  
**Example**: Achieved 0.85 accuracy with KNN (*K=5*) on Social Network Ads dataset.

---

### [[Classification Report]]
**Definition**: Metrics (precision, recall, F1-score) evaluating classifier performance per class.  
**Formulas**:  
- **Precision**: \( \frac{\text{TP}}{\text{TP} + \text{FP}} \)  
- **Recall**: \( \frac{\text{TP}}{\text{TP} + \text{FN}} \)  
- **F1-Score**: \( 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} \)  
**Example**: URL dataset showed precision=0.92 for Phishing class.

---

### [[Elbow Method]]
**Definition**: A technique to determine optimal *K* by plotting distortion (sum of squared distances) against *K*.  
**Formula**: Distortion = \( \sum_{i=1}^{n} \min_{j=1}^{K} \|x_i - \mu_j\|^2 \)  
**Example**: Identified *K=7* as optimal for Social Network Ads clustering (used to guide KNN's *K*).

---

### [[Feature Scaling]]
**Definition**: Rescaling features to a standard range to prevent bias toward higher-magnitude features.  
**Formula**: N/A  
**Example**: Applied `StandardScaler` to normalize URL features like `Destination_Portal`.

---

### [[Data Preprocessing]]
**Definition**: Steps to clean and transform raw data into a model-ready format.  
**Formula**: N/A  
**Example**: Removed whitespace from column names, dropped null values, and removed infinite values in the URL dataset.

---

### [[Hyperparameter Tuning]]
**Definition**: Optimizing model parameters (e.g., *K* in KNN) not learned during training.  
**Formula**: N/A  
**Example**: Tested *K=1* to *K=9* using the Elbow method and selected *K=7* for optimal performance.

---

### [[Curse of Dimensionality]]
**Definition**: The issue where high-dimensional data spaces lead to sparsity, making distance metrics less meaningful.  
**Formula**: N/A  
**Example**: KNN performance degraded with too many features in the URL dataset.

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Distance Metrics]]  
- [[Model Evaluation]]  
- [[Principal Component Analysis (PCA)]]  

This summary connects key concepts via wikilinks and adheres to the structured academic format, capturing practical KNN implementation steps and theoretical foundations.