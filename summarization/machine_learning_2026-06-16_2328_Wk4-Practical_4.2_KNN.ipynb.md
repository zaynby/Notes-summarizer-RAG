# Wk4-Practical_4.2_KNN.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

# Week 4.2 Practical - KNN  
**Module:** machine_learning  
**Style:** structured_academic  

## [[K-Nearest Neighbors (KNN)]]  
**Definition**: A supervised learning algorithm that classifies or regresses data points based on the majority vote or average of their *K* nearest neighbors in the feature space.  
**Formula**:  
- **Classification**: \( \text{Class} = \text{Argmax}_{c} \sum_{i=1}^{K} \mathbb{I}(y_i = c) \)  
- **Regression**: \( \hat{y} = \frac{1}{K} \sum_{i=1}^{K} y_i \)  
**Example**: Classified URL types (Benign, Phishing, etc.) in the Canadian Institute for Cybersecurity dataset using *K=1* and achieved 85% testing accuracy with *K=5* in the Social Network Ads dataset.  

---

## [[StandardScaler]]  
**Definition**: A feature scaling technique that standardizes data by removing the mean and scaling to unit variance.  
**Formula**: \( x_{\text{scaled}} = \frac{x - \mu}{\sigma} \)  
**Example**: Scaled features like `EstimatedSalary` and `Age` in the Social Network Ads dataset to improve KNN performance.  

---

## [[Train-Test Split]]  
**Definition**: Divides data into training and testing subsets to evaluate model generalization.  
**Formula**: N/A  
**Example**: Split the URL dataset into 75% training and 25% testing data using `train_test_split`.  

---

## [[Confusion Matrix]]  
**Definition**: A table quantifying correct and incorrect predictions for classification models.  
**Structure**:  
| | Predicted Positive | Predicted Negative |  
|----------------------|--------------------|--------------------|  
| **Actual Positive** | TP | FN |  
| **Actual Negative** | FP | TN |  
**Example**: For phishing detection, the matrix showed 120 True Positives (TP) and 30 False Negatives (FN).  

---

## [[Accuracy Score]]  
**Definition**: Proportion of correct predictions (both true positives and true negatives).  
**Formula**: \( \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} \)  
**Example**: Achieved 0.85 accuracy with KNN (*K=5*) on the Social Network Ads dataset.  

---

## [[Elbow Method]]  
**Definition**: A technique to determine the optimal number of clusters (*K*) by plotting distortion (sum of squared distances) against *K*.  
**Formula**: Distortion = \( \sum_{i=1}^{n} \min_{j=1}^{K} \|x_i - \mu_j\|^2 \)  
**Example**: Identified *K=7* as optimal for clustering in the Social Network Ads dataset using inertia values.  

---

## [[Feature Scaling]]  
**Definition**: Rescaling features to a standard range to prevent bias toward higher-magnitude features.  
**Formula**: N/A  
**Example**: Applied `StandardScaler` to normalize URL features like `Destination_Portal`, `Count_of_Dots`, etc.  

---

## [[Data Preprocessing]]  
**Definition**: Steps to clean and transform raw data into a model-ready format.  
**Formula**: N/A  
**Example**:  
- Removed leading whitespaces from column names in the URL dataset.  
- Dropped rows with null values using `df.dropna()`.  
- Removed infinite values with `np.isfinite()`.  

---

## [[Hyperparameter Tuning]]  
**Definition**: Optimizing model parameters (e.g., *K* in KNN) not learned during training.  
**Formula**: N/A  
**Example**: Tested *K=1* to *K=9* using the Elbow method and selected *K=7* for optimal performance.  

---

## [[Classification Report]]  
**Definition**: Metrics (precision, recall, F1-score) evaluating classifier performance per class.  
**Formula**:  
- **Precision**: \( \frac{\text{TP}}{\text{TP} + \text{FP}} \)  
- **Recall**: \( \frac{\text{TP}}{\text{TP} + \text{FN}} \)  
- **F1-Score**: \( 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} \)  
**Example**: For the URL dataset, the report showed precision=0.92 for Phishing class.  

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Distance Metrics]]  
- [[Model Evaluation]]  
- [[Curse of Dimensionality]]  
- [[Principal Component Analysis (PCA)]]  

This summary connects key concepts via wikilinks and adheres to the structured academic format, capturing practical KNN implementation steps and theoretical foundations.