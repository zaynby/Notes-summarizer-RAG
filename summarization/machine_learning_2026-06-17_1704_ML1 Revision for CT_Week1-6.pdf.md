# ML1 Revision for CT_Week1-6.pdf
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided Machine Learning content:

---

### **CRISP-DM Framework**  
**Definition**: Cross-Industry Standard Process for Data Mining that bridges business and technical work, encourages iteration, and is tool/industry-agnostic.  
**Formula**: N/A  
**Example**: Phases include Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation, and Deployment.  

---

### **Universal Workflow of ML**  
**Definition**: A systematic approach to building ML models, from problem definition to deployment.  
**Steps**:  
1. **Define Problem & Collect Data**: Identify inputs/outputs and data availability.  
2. **Choose Success Metric**: E.g., RMSE for regression, accuracy for classification.  
3. **Evaluation Protocol**: Train/validation/test split or k-fold cross-validation.  
4. **Prepare Data**: Feature encoding (one-hot), normalization, and selection.  
5. **Build Baseline Model**: Outperform random guessing.  
6. **Scale Up**: Train until overfitting occurs (monitor validation metrics).  
7. **Regularize & Tune**: Adjust hyperparameters (learning rate, dropout) to reduce overfitting.  
**Formula**: N/A  
**Example**: Use k-fold cross-validation for small datasets to evaluate model performance.  

---

### **Supervised Learning Models**  
#### **Linear Regression**  
**Definition**: Predicts continuous target variables using a linear equation.  
**Formula**:  
- Simple: \( y = \beta_0 + \beta_1x \)  
- Multiple: \( y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \dots + \beta_nx_n \)  
**Example**: Predicting house prices based on size and location.  

#### **Logistic Regression**  
**Definition**: Predicts categorical target variables (classifier).  
**Formula**: Sigmoid function \( P(y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1x_1 + \dots + \beta_nx_n)}} \).  
**Example**: Classifying emails as spam (1) or not spam (0).  

---

### **Model Evaluation Metrics**  
#### **Classification**  
- **Accuracy**: \( \frac{TP + TN}{TP + TN + FP + FN} \)  
- **Precision**: \( \frac{TP}{TP + FP} \)  
- **Recall (Sensitivity)**: \( \frac{TP}{TP + FN} \)  
- **F1 Score**: \( 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \)  
- **ROC-AUC**: Area under the ROC curve (1.0 = perfect, 0.5 = random).  
**Example**: In a medical test, high recall reduces false negatives (missed diagnoses).  

#### **Regression**  
- **MAE**: \( \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i| \)  
- **MSE**: \( \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2 \)  
- **RMSE**: \( \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2} \)  
- **R-squared**: \( 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2} \)  
**Example**: RMSE quantifies average error in housing price predictions.  

---

### **Decision Trees**  
**Definition**: A tree-like model that splits data based on feature values to maximize node purity.  
**Key Concepts**:  
- **Gini Impurity**: \( I = 1 - \sum_{c=1}^m p_c^2 \) (lower = purer node).  
- **Stopping Conditions**: Max depth, min samples per leaf, statistical tests.  
- **CART Algorithm**: Binary splits using Gini reduction.  
**Example**: Splitting customer data by age and income to predict loan defaults.  

---

### **K-Nearest Neighbors (KNN)**  
**Definition**: A lazy learner that classifies/regresses based on nearest training examples.  
**Distance Metrics**:  
- **Euclidean**: \( d = \sqrt{\sum (x_i - y_i)^2} \)  
- **Manhattan**: \( d = \sum |x_i - y_i| \)  
**Choosing K**: \( K = \sqrt{n} \) (n = training samples).  
**Example**: Classifying flowers as Iris Setosa or Versicolor using K=5.  

---

### **Unsupervised Learning: Clustering**  
#### **K-Means Clustering**  
**Definition**: Partitions data into k clusters based on similarity.  
**Steps**:  
1. Initialize centroids.  
2. Assign data points to nearest centroid.  
3. Update centroids.  
4. Repeat until convergence.  
**Example**: Customer segmentation for targeted marketing.  

#### **Hierarchical Clustering**  
**Definition**: Builds nested clusters via agglomerative (bottom-up) or divisive (top-down) approaches.  
**Linkage Criteria**: Single, complete, average, centroid.  
**Example**: Gene expression analysis to identify disease subtypes.  

#### **Silhouette Coefficient**  
**Definition**: Measures how well a data point fits its cluster (\( -1 \leq s(o) \leq 1 \)).  
**Formula**: \( s(o) = \frac{b(o) - a(o)}{\max(a(o), b(o))} \) (a = intra-cluster distance, b = nearest cluster distance).  
**Example**: Higher silhouette scores indicate better cluster quality.  

---

### **Key Concepts**  
- **Overfitting**: Model performs well on training data but poorly on validation data.  
- **Underfitting**: Model fails to capture underlying patterns (high bias).  
- **Cross-Validation**: k-fold splits data into training/testing subsets to reduce variance.  
- **Feature Scaling**: Normalizes features (e.g., min-max, z-score) to ensure equal contribution.  

---

All terms are interconnected via [[wikilinks]] for contextual navigation (e.g., [[Decision Tree]] links to [[Gini Impurity]] and [[Overfitting]]). This structure ensures clarity and alignment with polytechnic-level ML curricula.