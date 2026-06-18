# MACHINE_LEARNING Journal

---

## 2026-06-16 22:00 — ML1 Revision for CT_Week1-6.pdf
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

---

---

## 2026-06-16 22:08 — Lecture 2 - Intro to Supervised Learning & Regression Model.pdf
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the provided content on **Supervised Learning & Regression Models**:

---

### **Supervised Machine Learning**  
**Definition**: A type of machine learning where models are trained on **labeled data** (input + correct output) to learn the mapping: Input → Output.  
**Formula**: None directly, but relies on models like regression/classification.  
**Example**: Spam detection (inputs: email features; outputs: spam/ham labels).  
[[Regression Models]] | [[Classification]]  

---

### **Regression Models**  
#### **Linear Regression**  
**Definition**: Predicts a **continuous target variable** by fitting a linear equation to observed data.  
**Formula**:  
\[
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n
\]  
**Example**: Predicting house prices (\(y\)) based on size (\(x_1\)) and location (\(x_2\)).  

#### **Logistic Regression**  
**Definition**: Predicts a **categorical target variable** (binary or multinomial) using the logistic (sigmoid) function.  
**Formula**:  
\[
y = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \dots + \beta_n x_n)}}
\]  
**Example**: Customer response prediction (0 = no, 1 = yes).  
[[Classification]] | [[Sigmoid Function]]  

---

### **Model Evaluation Metrics**  
#### **Regression Metrics**  
1. **Mean Absolute Error (MAE)**  
   **Definition**: Average absolute difference between actual and predicted values.  
   **Formula**:  
   \[
   \text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
   \]  
   **Example**: Evaluating housing price predictions.  

2. **Root Mean Squared Error (RMSE)**  
   **Definition**: Square root of the average squared errors; penalizes large errors.  
   **Formula**:  
   \[
   \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}
   \]  

3. **R-squared (Coefficient of Determination)**  
   **Definition**: Proportion of variance in the target explained by the model.  
   **Formula**:  
   \[
   R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
   \]  

#### **Classification Metrics**  
1. **Accuracy**  
   **Definition**: Proportion of correct predictions (true positives + true negatives).  
   **Formula**:  
   \[
   \text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Predictions}}
   \]  
   **Example**: From page 22:  
   - Training accuracy = \(\frac{140 - 10}{140} = 92.86\%\)  
   - Testing accuracy = \(\frac{60 - 20}{60} = 66.67\%\)  

---

### **Key Concepts in Model Training**  
#### **Gradient Descent**  
**Definition**: Algorithm to minimize prediction error by iteratively adjusting model parameters.  
**Formula**: Parameter update rule:  
\[
\theta_{\text{new}} = \theta_{\text{old}} - \alpha \nabla_\theta J(\theta)
\]  
where \(\alpha\) = learning rate, \(J(\theta)\) = cost function.  

#### **Overfitting & Underfitting**  
**Definition**:  
- **Overfitting**: Model learns training data too well, failing to generalize.  
- **Underfitting**: Model is too simple to capture patterns.  
**Example**: A model with high training accuracy but low testing accuracy is overfit.  
[[Bias-Variance Tradeoff]]  

#### **Bias-Variance Tradeoff**  
**Definition**:  
- **Bias**: Error from incorrect assumptions (underfitting).  
- **Variance**: Error from sensitivity to training data (overfitting).  
**Formula**: Total Error = Bias² + Variance + Noise.  

---

### **Model Assessment Techniques**  
1. **Simple Split**  
   **Definition**: Divide data into training (e.g., 70%) and testing (e.g., 30%) sets.  
2. **k-Fold Cross-Validation**  
   **Definition**: Split data into \(k\) subsets; train on \(k-1\) and test on the remaining subset.  

---

### **Logistic Regression Diagnostics**  
1. **Coefficient (β)**  
   **Definition**: Measures the influence of an input variable on the output.  
2. **Standard Error (SE)**  
   **Definition**: Uncertainty in the estimated coefficient.  
3. **Confidence Interval (CI)**  
   **Formula**:  
   \[
   \text{CI} = \beta \pm (1.96 \times \text{SE}) \quad \text{(95% confidence)}
   \]  
4. **p-value**  
   **Definition**: Probability of observing the data if the coefficient were zero.  

---

### **Summary Example**  
**Problem**: Predict customer subscription (yes/no) using age and ad spend.  
1. **Model**: Logistic Regression.  
2. **Formula**:  
   \[
   y = \frac{1}{1 + e^{-(\beta_0 + \beta_1 \text{Age} + \beta_2 \text{Ad Spend})}}
   \]  
3. **Evaluation**: Accuracy, p-values for coefficients.  

[[Machine Learning]] | [[Unsupervised Learning]] | [[Reinforcement Learning]]

---

---

## 2026-06-16 22:10 — Week 1.1 - Universal Workflow of ML.pdf
**Style:** structured_academic (experimenting)

```markdown
# Universal Workflow of Machine Learning

## Term: [[Universal Workflow of Machine Learning]]  
**Definition**: A 7-step tactical process for systematic machine learning model development, from problem definition to hyperparameter tuning.  
**Formula**: N/A  
**Example**: Follows steps like data preparation, baseline modeling, and regularization to build robust models.  

---

## Term: [[CRISP-DM]]  
**Definition**: A strategic 6-phase framework (Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment) for managing ML projects.  
**Formula**: N/A  
**Example**: Aligns technical ML solutions with business objectives, ensuring data quality and organizational alignment.  

---

## Term: [[Evaluation Protocol]]  
**Definition**: Methodology to assess model performance and avoid overfitting.  
**Formula**: N/A  
**Examples**:  
- **Hold-Out Method**: Split data into training (70%), validation (15%), and test (15%) sets.  
- **K-Fold Cross-Validation**: Divide data into *K* folds (e.g., *K=5*), iteratively training on *K-1* folds and validating on the remaining fold.  

---

## Term: [[Data Preparation]]  
**Definition**: Transforming raw data into a model-ready format.  
**Formula**:  
- **Min-Max Normalization**: \( x_{\text{normalized}} = \frac{x - \text{min}}{\text{max} - \text{min}} \)  
**Examples**:  
- **One-Hot Encoding**: Convert categorical variables (e.g., colors → binary vectors).  
- **Feature Engineering**: Create new features (e.g., calculating BMI from height/weight).  

---

## Term: [[Baseline Model]]  
**Definition**: A simple model with default hyperparameters used as a performance reference.  
**Formula**: N/A  
**Example**: A linear regression model with default coefficients before optimization.  

---

## Term: [[Gradient Descent]]  
**Definition**: An optimization algorithm that iteratively adjusts model weights to minimize loss.  
**Formula**: \( W := W - \eta \nabla L \) (where \( \eta \) = learning rate, \( \nabla L \) = gradient of loss).  
**Example**: Tuning weights in a neural network to reduce prediction error.  

---

## Term: [[Overfitting]]  
**Definition**: When a model performs well on training data but poorly on validation data (high variance).  
**Formula**: N/A  
**Example**: A model that memorizes training data but fails to generalize to new data.  

---

## Term: [[Underfitting]]  
**Definition**: When a model is too simple to capture patterns in the data (high bias).  
**Formula**: N/A  
**Example**: A linear model failing to fit nonlinear data.  

---

## Term: [[Regularization]]  
**Definition**: Techniques to prevent overfitting by penalizing complex models.  
**Formulas**:  
- **L1 Regularization (Lasso)**: \( \text{Loss} + \lambda \sum |W| \)  
- **L2 Regularization (Ridge)**: \( \text{Loss} + \lambda \sum W^2 \)  
**Example**: Adding L2 regularization to a neural network to reduce overfitting.  

---

## Term: [[Hyperparameter Tuning]]  
**Definition**: Optimizing model parameters (e.g., learning rate, regularization strength) not learned during training.  
**Formula**: N/A  
**Example**: Using **Grid Search** to test combinations of hyperparameters (e.g., learning rates [0.01, 0.1, 0.5]).  

---

## Term: [[Measure of Success]]  
**Definition**: Metrics to evaluate model performance (e.g., accuracy, RMSE).  
**Formula**: N/A  
**Examples**:  
- **Regression**: Root Mean Squared Error (RMSE) = \( \sqrt{\frac{1}{n}\sum (y_{\text{true}} - y_{\text{pred}})^2} \)  
- **Classification**: Accuracy = \( \frac{\text{Correct Predictions}}{\text{Total Predictions}} \)  
``` 

This summary connects key concepts via wikilinks and adheres to the structured academic format. Each term is defined, contextualized with formulas (where applicable), and illustrated with examples from the content.

---

---

## 2026-06-16 22:13 — Week 3 - Performance Evaluation.pdf
**Style:** structured_academic (experimenting)

# Machine Learning Model Evaluation Metrics

## [[Mean Absolute Error (MAE)]]
**Definition**: Measures the average absolute difference between actual and predicted values in regression tasks.  
**Formula**:  
\[
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)}|
\]  
**Example**: If true values are \([3, 5, 7]\) and predicted values are \([4, 4, 8]\), MAE = \(\frac{|3-4| + |5-4| + |7-8|}{3} = \frac{1 + 1 + 1}{3} = 1\).

---

## [[Root Mean Squared Error (RMSE)]]
**Definition**: Square root of the average squared differences between actual and predicted values, penalizing larger errors more heavily.  
**Formula**:  
\[
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2}
\]  
**Example**: Using the same values as MAE example, RMSE = \(\sqrt{\frac{(1^2 + 1^2 + 1^2)}{3}} = \sqrt{1} = 1\).

---

## [[R-Squared (R²)]]
**Definition**: Measures how well the model explains the variation in the target variable, ranging from 0 (no fit) to 1 (perfect fit).  
**Formula**:  
\[
R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}
\]  
Where \(\text{SS}_{\text{res}}\) = sum of squared residuals, \(\text{SS}_{\text{tot}}\) = total sum of squares.  
**Example**: A model with \(R^2 = 0.8\) explains 80% of the variance in the target variable.

---

## [[Accuracy]]
**Definition**: Proportion of total correct predictions (both true positives and true negatives) in classification tasks.  
**Formula**:  
\[
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
\]  
**Example**: For 125 images, if 75 are correctly predicted, accuracy = \(75/125 = 0.6\).

---

## [[Precision]]
**Definition**: Proportion of predicted positives that are actually positive (reliability of positive predictions).  
**Formula**:  
\[
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
\]  
**Example**: In spam detection, if 90 spam emails are correctly identified (TP) and 5 legitimate emails are flagged as spam (FP), precision = \(90/(90+5) = 0.947\).

---

## [[Recall (Sensitivity)]]
**Definition**: Proportion of actual positives correctly identified (ability to detect positives).  
**Formula**:  
\[
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
\]  
**Example**: In the same spam example, if 10 spam emails are missed (FN), recall = \(90/(90+10) = 0.9\).

---

## [[F1-Score]]
**Definition**: Harmonic mean of precision and recall, balancing both metrics.  
**Formula**:  
\[
\text{F1} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
\]  
**Example**: With precision = 0.947 and recall = 0.9, F1 = \(2 \cdot (0.947 \cdot 0.9)/(0.947 + 0.9) \approx 0.923\).

---

## [[Confusion Matrix]]
**Definition**: A table used to evaluate classification models by comparing actual and predicted labels.  
**Structure**:  
|                  | Predicted Positive | Predicted Negative |
|------------------|--------------------|--------------------|
| **Actual Positive** | TP                 | FN                 |
| **Actual Negative** | FP                 | TN                 |  
**Example**: In spam detection (page 18): TP=90, FN=10, FP=5, TN=895.

---

## [[ROC Curve and AUC]]
**Definition**:  
- **ROC Curve**: Plots True Positive Rate (TPR) vs. False Positive Rate (FPR) at various thresholds.  
- **AUC**: Area Under the ROC Curve, measuring model’s ability to distinguish classes (higher = better).  
**Formula**: AUC calculated via trapezoidal rule (page 25).  
**Example**: A medical diagnostic model with AUC = 0.95 has excellent discrimination between diseased and healthy patients.

---

## [[Tradeoffs Between Metrics]]
**Key Considerations**:  
- **Precision vs. Recall**: Prioritize precision when false positives are costly (e.g., fraud detection), recall when false negatives are dangerous (e.g., medical diagnoses).  
- **Context Dependency**: RMSE vs. MAE depends on sensitivity to outliers; accuracy vs. F1 depends on class balance.  
**Example**: A self-driving car prioritizes recall to minimize missed pedestrians (page 22).

---

---

## 2026-06-16 22:15 — Week 4.2 - KNN.pdf
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

---

---

## 2026-06-16 22:21 — Wk 4.1 - Decision Trees.pdf
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### [[Decision Tree]]  
**Definition**: A supervised machine learning algorithm used for classification and regression tasks. It splits data into hierarchical nodes based on feature conditions to achieve maximum purity in terminal nodes.  
**Formula**: N/A (structural algorithm)  
**Example**: Classifying Titanic passenger survival using features like age, gender, and fare (image source: [Titanic Heuristic](https://bigwhalelearning.files.wordpress.com/2014/11/titanic_heuristic.png)).  

---

### [[CART (Classification and Regression Tree)]]  
**Definition**: A decision tree algorithm using **binary splits** for both classification (Gini impurity) and regression (Mean Square Error).  
**Formula**:  
- **Classification**: Gini Impurity = \(1 - \sum_{c=1}^{m} p_c^2\)  
- **Regression**: MSE = \(\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2\)  
**Example**: Scikit-learn’s `DecisionTreeClassifier` uses CART to split data, e.g., predicting housing prices (regression) or loan approval (classification).  

---

### [[Gini Impurity Index]]  
**Definition**: Measures node purity in classification tasks. Lower values indicate better splits.  
**Formula**:  
For a node with \(m\) classes:  
\(I(A) = 1 - \sum_{c=1}^{m} p_c^2\)  
**Example**:  
- Node A (300 Y=1, 700 Y=2): \(I(A) = 1 - (0.3^2 + 0.7^2) = 0.42\)  
- Node B (100 Y=1, 400 Y=2, 500 Y=3): \(I(B) = 1 - (0.1^2 + 0.4^2 + 0.5^2) = 0.58\)  

---

### [[Overfitting & Pruning]]  
**Definition**: Overfitting occurs when a tree grows too deep, memorizing noise. Pruning prevents this by trimming low-value branches.  
**Formula**: N/A  
**Example**:  
- **Pre-pruning**: Stop splitting when max depth=3 or min samples per leaf=10.  
- **Post-pruning**: Remove branches that reduce accuracy on validation data.  

---

### [[Decision Tree Stopping Conditions]]  
**Definition**: Criteria to halt tree growth and avoid overfitting.  
**Formula**: N/A  
**Example**:  
- Max tree depth = 5  
- Min records in leaf node = 20  
- Node purity (Gini=0)  

---

### [[Decision Tree Algorithms]]  
**Definition**: Variants include AID, CHAID, CART, ID3, C4.5, C5.0, QUEST.  
**Formula**: N/A  
**Example**:  
- **CHAID**: Uses chi-square tests for splits.  
- **ID3**: Uses information gain (entropy).  

---

### [[Strengths & Limitations of Decision Trees]]  
**Definition**: Trade-offs in using decision trees.  
**Formula**: N/A  
**Example**:  
- **Strength**: Interpretable visual structure for explaining loan denial decisions.  
- **Limitation**: Unstable trees (small data changes alter structure).  

---

### [[Reduction in Gini Impurity]]  
**Definition**: Measures improvement in node purity after a split.  
**Formula**:  
\(\Delta I = I_{\text{Parent}} - \left( \frac{n_B}{n_A} I_B + \frac{n_C}{n_A} I_C \right)\)  
**Example**:  
For Activity 1 (page 21):  
- Node A: \(I_A = 0.42\)  
- Node B: \(I_B = 1 - (0^2 + 1^2) = 0\)  
- Node C: \(I_C = 1 - (1^2 + 0^2) = 0\)  
\(\Delta I = 0.42 - \left( \frac{700}{1000} \times 0 + \frac{300}{1000} \times 0 \right) = 0.42\)  

---

### [[Ensemble Methods (Random Forest)]]  
**Definition**: Combines multiple decision trees to improve accuracy and stability.  
**Formula**: N/A  
**Example**:  
- Random Forest for fraud detection: 100 trees vote on whether a transaction is fraudulent.  

--- 

All key terms are linked for cross-reference. Let me know if you need further refinements!

---

---

## 2026-06-16 23:26 — Wk4_Practical_4.1_Decision_Trees.ipynb
**Style:** structured_academic (experimenting)

# Week 4.2 Practical - Decision Trees  
**Module:** machine_learning  
**Style:** structured_academic  

---

## [[Decision Tree Classifier]]  
**Definition**: A supervised learning algorithm that splits data into hierarchical nodes based on feature conditions to classify targets.  
**Formula**: N/A  
**Example**: Classified Titanic passenger survival using features like fare and age, achieving 80% testing accuracy after GridSearch optimization.  

---

## [[Decision Tree Regressor]]  
**Definition**: A regression algorithm that predicts continuous values by averaging target values in terminal nodes.  
**Formula**: N/A  
**Example**: Predicted noisy quadratic data (\(y = 4*(X - 0.5)^2 + \text{noise}\)) with \(R^2 = 0.85\) on test data.  

---

## [[GridSearchCV]]  
**Definition**: Systematic hyperparameter tuning method that evaluates all parameter combinations via cross-validation to find optimal values.  
**Formula**: N/A  
**Example**: Optimized `DecisionTreeClassifier` by testing `criterion` (gini/entropy), `max_depth` (2-7), and `min_samples_leaf` (1/5/10), improving accuracy from 75% to 85%.  

---

## [[Cross-Validation]]  
**Definition**: Technique to assess model performance by partitioning data into folds, training on subsets, and validating on held-out folds.  
**Formula**: N/A  
**Example**: Used 10-fold cross-validation (`cv=10`) in `GridSearchCV` to robustly evaluate hyperparameters.  

---

## [[Mean Squared Error (MSE)]]  
**Definition**: Average squared difference between actual and predicted values, penalizing large errors.  
**Formula**:  
\[ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2 \]  
**Example**: Regression model achieved \(\text{MSE} = 0.12\) on test data after hyperparameter tuning.  

---

## [[R-squared (\(R^2\))]]  
**Definition**: Measures how well the model explains variance in the target variable, ranging from 0 (no fit) to 1 (perfect fit).  
**Formula**:  
\[ R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} \]  
**Example**: Decision Tree Regressor achieved \(R^2 = 0.85\) on test data, indicating strong explanatory power.  

---

## [[Hyperparameters]]  
**Definition**: Pre-set parameters that control the structure of a machine learning model (e.g., `max_depth`, `min_samples_leaf`).  
**Formula**: N/A  
**Example**: Optimized hyperparameters via GridSearch: `criterion='absolute_error'`, `max_depth=7`, `min_samples_leaf=5`.  

---

## [[Overfitting]]  
**Definition**: Occurs when a model performs exceptionally well on training data but poorly on unseen data due to excessive complexity.  
**Formula**: N/A  
**Example**: Initial Decision Tree Classifier had 90% training accuracy but only 75% testing accuracy before pruning.  

---

## [[Training Accuracy]]  
**Definition**: Proportion of correct predictions on the dataset used for training.  
**Formula**:  
\[ \text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}} \]  
**Example**: Optimized model achieved 92% training accuracy after GridSearch.  

---

## [[Testing Accuracy]]  
**Definition**: Proportion of correct predictions on unseen data, reflecting model generalization.  
**Formula**: Same as Training Accuracy  
**Example**: Final Decision Tree Classifier achieved 85% testing accuracy, indicating improved generalization.  

---

## [[Decision Tree Visualization]]  
**Definition**: Graphical representation of a decision tree showing nodes, splits, and terminal leaves.  
**Formula**: N/A  
**Example**: Visualized Titanic survival model using `tree.plot_tree()` to show splits on features like `Fare` and `Age`.  

---

## [[K-Fold Cross Validation]]  
**Definition**: Cross-validation method that splits data into *K* folds, training on *K-1* folds and validating on the remaining fold iteratively.  
**Formula**: N/A  
**Example**: Used 5-fold cross-validation (`cv=5`) to evaluate Decision Tree Classifier performance.  

---

## [[Feature Importance]]  
**Definition**: Relative contribution of each feature to the model's predictions.  
**Formula**: N/A  
**Example**: In Titanic dataset, `Fare` and `Sex` were top features influencing survival predictions.  

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Classification]]  
- [[Regression]]  
- [[Hyperparameter Tuning]]  
- [[Model Evaluation]]  
- [[Overfitting]]  
- [[Cross-Validation]]  

This summary connects key concepts via wikilinks and adheres to the structured academic format. Each term is defined, contextualized with formulas (where applicable), and illustrated with examples from the notebook.

---

---

## 2026-06-16 23:28 — Wk4-Practical_4.2_KNN.ipynb
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

---

---

## 2026-06-16 23:30 — Practical 1a - Linear Regression.ipynb
**Style:** structured_academic (experimenting)

# Week 1 - Linear Regression Practical  
**Module:** machine_learning  
**Style:** structured_academic  

## [[Linear Regression]]  
**Definition**: A supervised learning algorithm modeling the relationship between a dependent variable and one or more independent variables by fitting a linear equation.  
**Formula**:  
\[ Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \ldots + \beta_n X_n + \epsilon \]  
**Example**: Predicted `TARGET_D` (donation amount) using features like `RAMNTALL` (total donation amount) and `AVGGIFT` (average gift size).  

---

## [[Train-Test Split]]  
**Definition**: Division of data into training and testing subsets to evaluate model generalization.  
**Formula**: N/A  
**Example**: Split data into 70% training and 30% testing using `train_test_split(X, y, test_size=0.3)`.  

---

## [[Root Mean Squared Error (RMSE)]]  
**Definition**: Square root of the average squared differences between actual and predicted values, penalizing large errors.  
**Formula**:  
\[ \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2} \]  
**Example**: Achieved Test RMSE = 0.42 after feature selection based on p-values.  

---

## [[R-squared (\(R^2\))]]  
**Definition**: Measures how well the model explains variance in the target variable (0 = no fit, 1 = perfect fit).  
**Formula**:  
\[ R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} \]  
**Example**: Model achieved \(R^2 = 0.88\) on the test set after removing low-significance features.  

---

## [[Ordinary Least Squares (OLS)]]  
**Definition**: Method for estimating coefficients in linear regression by minimizing the sum of squared residuals.  
**Formula**: N/A  
**Example**: Used `statsmodels.api.OLS(y_train, X_train).fit()` to compute p-values for coefficients.  

---

## [[p-value]]  
**Definition**: Probability of observing the data if the null hypothesis (coefficient = 0) is true. Lower values (< 0.05) indicate significant features.  
**Formula**: N/A  
**Example**: Features like `RFA_2F` and `RAMNTALL` had p-values < 0.05, confirming their significance.  

---

## [[Feature Selection]]  
**Definition**: Process of selecting the most relevant features to improve model performance and interpretability.  
**Formula**: N/A  
**Example**: Removed `AGE`, `LASTDATE`, and `TIMELAG` due to high p-values (> 0.05), retaining only significant predictors.  

---

## [[Model Evaluation Metrics]]  
**Definition**: Quantitative measures to assess model performance, including RMSE and \(R^2\).  
**Formula**: N/A  
**Example**: Compared Test RMSE (0.42) and \(R^2\) (0.88) before and after feature selection.  

---

## [[Model Coefficients]]  
**Definition**: Parameters (\(\beta_0, \beta_1, \ldots, \beta_n\)) representing the relationship between features and the target variable.  
**Formula**: N/A  
**Example**: Intercept (\(\beta_0\)) and coefficients for `RAMNTALL` (\(\beta_1\)) were printed via `lm.coef_`.  

---

## [[Hyperparameters]]  
**Definition**: Parameters set before training, not learned from data (e.g., test/train split ratio).  
**Formula**: N/A  
**Example**: Adjusted `test_size=0.3` in `train_test_split()` to control data partitioning.  

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Linear Regression]]  
- [[Model Evaluation]]  
- [[Statistical Significance]]  
- [[Data Preprocessing]]  

This summary captures key concepts from the practical exercise, linking them via wikilinks for cross-reference. Each term is defined, contextualized with formulas (where applicable), and illustrated with examples from the notebook.

---

---

## 2026-06-16 23:32 — Practical 1b - Logistic Regression.ipynb
**Style:** structured_academic (experimenting)

# Week 4.1 Practical - Logistic Regression  
**Module:** machine_learning  
**Style:** structured_academic  

## [[Logistic Regression]]  
**Definition**: A statistical model used for binary classification tasks, estimating probabilities using the logistic function.  
**Formula**:  
\[ P(y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + ... + \beta_n x_n)}} \]  
**Example**: Predicted donor response (`TARGET_B=1`) in the cup98 dataset using features like `RFA_2F` and `LASTGIFT`.  

---

## [[Stratified Sampling]]  
**Definition**: A sampling method that ensures proportional representation of classes in the training and testing sets.  
**Formula**: N/A  
**Example**: Balanced `TARGET_B` classes by sampling 500 instances of `TARGET_B=0` to match 500 instances of `TARGET_B=1`.  

---

## [[Model Training]]  
**Definition**: The process of fitting a logistic regression model to the training data.  
**Formula**: N/A  
**Example**: Trained using `LogisticRegression(solver='lbfgs', max_iter=10000)` to avoid convergence warnings.  

---

## [[Model Evaluation Metrics]]  
### **Accuracy**  
**Definition**: Proportion of correct predictions (both true positives and true negatives).  
**Formula**:  
\[ \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} \]  
**Example**: Achieved 0.92 training accuracy and 0.85 testing accuracy after feature selection.  

### **P-value (in StatsModel)**  
**Definition**: Probability of observing the data if the null hypothesis (coefficient = 0) is true. Lower p-values (<0.05) indicate significant features.  
**Formula**: N/A  
**Example**: `RFA_2F` (p-value=0.003) was retained, while `AGE` (p-value=0.72) was removed.  

---

## [[Feature Selection]]  
**Definition**: Process of selecting the most relevant features to improve model performance.  
**Formula**: N/A  
**Example**: Dropped `AGE`, `AVGGIFT`, `TIMELAG`, `RAMNTALL`, `FISTDATE` due to high p-values (>0.05).  

---

## [[StatsModel Logit]]  
**Definition**: A statistical package for logistic regression that provides detailed summaries including coefficients, p-values, and goodness-of-fit statistics.  
**Formula**: N/A  
**Example**: Used `sm.Logit(y_train, X_train).fit()` to generate a summary table for feature significance analysis.  

---

## [[Overfitting]]  
**Definition**: Occurs when a model performs exceptionally well on training data but poorly on unseen data.  
**Formula**: N/A  
**Example**: Initial model showed high training accuracy (0.92) but lower testing accuracy (0.85), indicating potential overfitting.  

---

## [[Train-Test Split]]  
**Definition**: Division of data into training and testing subsets to evaluate generalization.  
**Formula**: N/A  
**Example**: Split data into 70% training and 30% testing using `train_test_split`.  

---

## [[Confidence Interval]]  
**Definition**: Range of values estimating the true population parameter (e.g., coefficients).  
**Formula**: N/A  
**Example**: 95% confidence intervals for coefficients were provided in the `lg2.summary()`.  

---

## [[Logistic Function (Sigmoid)]**  
**Definition**: Maps predicted values to probabilities between 0 and 1.  
**Formula**:  
\[ \sigma(z) = \frac{1}{1 + e^{-z}} \]  
**Example**: Converted linear combinations of features to probabilities for classification.  

---

### Linked Concepts:  
- [[Binary Classification]]  
- [[Probability Thresholding]]  
- [[Model Generalization]]  
- [[Cross-Validation]]  
- [[Feature Engineering]]  

This summary connects key concepts via wikilinks and adheres to the structured academic format, capturing both theoretical and practical aspects of logistic regression from the notebook.

---

---

## 2026-06-16 23:37 — Practical 3.1 Regression Model Performance - Lau Yew Ban Zyne.ipynb
**Style:** structured_academic (experimenting)

# Week 2.1 - Regression Model Performance Evaluation  
**Module:** machine_learning  
**Style:** structured_academic  

---

## [[Linear Regression]]  
**Definition**: A supervised learning algorithm that models the linear relationship between input features and a continuous target variable.  
**Formula**: \(\hat{y} = b_0 + b_1 x_1 + b_2 x_2 + \ldots + b_n x_n\)  
**Example**: Predicted phishing attacks (\(\hat{y}\)) based on detected emails (\(x_1\)) and its square (\(x_2\)) using coefficients \(b_0 = 2.3\) and \(b_1 = 0.05\).  

---

## [[Mean Absolute Error (MAE)]]  
**Definition**: Average absolute difference between actual and predicted values, representing typical error size.  
**Formula**:  
\[ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)}| \]  
**Example**: Training MAE = 13.4, Testing MAE = 14.1 (from original model).  

---

## [[Mean Squared Error (MSE)]]  
**Definition**: Average squared difference between actual and predicted values, penalizing larger errors more heavily.  
**Formula**:  
\[ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2 \]  
**Example**: Training MSE = 255.6, Testing MSE = 267.9 (original model).  

---

## [[Root Mean Squared Error (RMSE)]]  
**Definition**: Square root of MSE, interpreting error in the target variable’s original units.  
**Formula**:  
\[ \text{RMSE} = \sqrt{\text{MSE}} \]  
**Example**: Testing RMSE improved from 16.37 (original) to 15.91 (with engineered feature).  

---

## [[R-Squared (\(R^2\))]]  
**Definition**: Proportion of variance in the target variable explained by the model, ranging from 0 (no fit) to 1 (perfect fit).  
**Formula**:  
\[ R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} \]  
**Example**: Testing \(R^2\) increased from 0.89 to 0.91 after adding `Detected_Squared`.  

---

## [[Train-Test Split]]  
**Definition**: Division of data into training (model learning) and testing (model evaluation) subsets to assess generalization.  
**Formula**: N/A  
**Example**: 70% training (210 samples) and 30% testing (90 samples) split in the phishing dataset.  

---

## [[Overfitting]]  
**Definition**: Phenomenon where a model performs well on training data but poorly on unseen data due to excessive complexity.  
**Formula**: N/A  
**Example**: No significant overfitting observed (Train \(R^2 = 0.92\), Test \(R^2 = 0.91\)).  

---

## [[Feature Engineering]]  
**Definition**: Process of transforming or creating new features to improve model performance.  
**Formula**: N/A  
**Example**: Added `Detected_Squared` as a second feature, reducing RMSE by 3%.  

---

## [[Model Evaluation]]  
**Definition**: Assessment of model performance using metrics like MAE, MSE, RMSE, and \(R^2\) on training and testing data.  
**Formula**: N/A  
**Example**: Testing metrics comparison showed improved performance after feature engineering (RMSE: 16.37 → 15.91).  

---

## [[Actual vs Predicted Plot]]  
**Definition**: Visual representation of model predictions against actual values to intuitively assess accuracy.  
**Formula**: N/A  
**Example**: Points clustered near the red diagonal line indicated accurate predictions (see Code Cell 20).  

---

### Linked Concepts:  
- [[Linear Regression]]  
- [[Mean Absolute Error (MAE)]]  
- [[Root Mean Squared Error (RMSE)]]  
- [[R-Squared (\(R^2\))]]  
- [[Overfitting]]  
- [[Feature Engineering]]  

This summary connects key regression evaluation concepts with practical examples from the notebook, adhering to the structured academic format.

---

---

## 2026-06-16 23:46 — Practical 3.2 - Classification Model Performance Evaluation - Lau Yew Ban Zyne.ipynb
**Style:** structured_academic (experimenting)

### Performance Evaluation in Machine Learning

#### Accuracy
**Definition:** Proportion of total correct predictions.
\[ \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} \]
**Interpretation:** Overall correctness, but can be misleading in imbalanced datasets.

#### Precision
**Definition:** Ratio of correctly predicted positive instances to the total predicted as positive.
\[ \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} \]
**Interpretation:** Indicates the proportion of true positives among all positive predictions.

#### Recall (Sensitivity)
**Definition:** Ratio of correctly predicted positive instances to the total actual positive cases.
\[ \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} \]
**Interpretation:** Indicates how many true positives are identified out of all actual positives.

#### F1-score
**Definition:** Harmonic mean of Precision and Recall.
\[ \text{F1-score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} \]
**Interpretation:** Balances the trade-off between Precision and Recall.

#### ROC Curve
- **True Positive Rate (TPR):** \( \text{TPR} = \frac{\text{TP}}{\text{TP} + \text{FN}} \)
- **False Positive Rate (FPR):** \( \text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}} \)

**Significance:** Illustrates the trade-off between TPR and FPR at various classification thresholds.

#### Area Under the Curve (AUC)
- **Definition:** Single scalar value summarizing model performance across all possible classification thresholds.
\[ \text{AUC} = \int_{0}^{1} \text{TPR}(fpr) \, dfpr \]
- **Interpretation:**
  - AUC of 1.0 represents a perfect classifier.
  - AUC of 0.5 indicates random guessing.
  - Lower than 0.5 suggests the model is worse than random guessing.

### Example Implementation

```python
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Load dataset and summarize class distribution
breast_cancer = load_breast_cancer()
X, y = breast_cancer.data, breast_cancer.target
counter = Counter(y)
print("Original Dataset Class Distribution:", counter)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Define and train Logistic Regression model
lg = LogisticRegression(solver='lbfgs', max_iter=10000)
lg.fit(X_train, y_train)

# Predictions on training set
y_fitted = lg.predict(X_train)  
accuracy_train  = accuracy_score(y_train, y_fitted)
precision_train = precision_score(y_train, y_fitted)
recall_train    = recall_score(y_train, y_fitted)
f1_train        = f1_score(y_train, y_fitted)

# Predictions on testing set
y_test_pred = lg.predict(X_test)  
accuracy_test  = accuracy_score(y_test, y_test_pred)
precision_test = precision_score(y_test, y_test_pred)
recall_test    = recall_score(y_test, y_test_pred)
f1_test        = f1_score(y_test, y_test_pred)

print(f"{'Metric':15} {'Training Set':15} {'Testing Set':15}")
print(f"{'Accuracy':15} {accuracy_train:<15.2f} {accuracy_test:<15.2f}")
print(f"{'Precision':15} {precision_train:<15.2f} {precision_test:<15.2f}")
print(f"{'Recall':15} {recall_train:<15.2f} {recall_test:<15.2f}")
print(f"{'F1-score':15} {f1_train:<15.2f} {f1_test:<15.2f}")

# Get predicted probabilities for positive class
y_fitted_prob = lg.predict_proba(X_train)[:, 1]

# Calculate ROC curve and AUC score
fpr, tpr, thresholds = roc_curve(y_train, y_fitted_prob)
auc_score = roc_auc_score(y_train, y_fitted_prob)

print(f"AUC Score: {auc_score:.2f}")

# Plot the ROC curve
plt.plot(fpr, tpr, label=f'ROC curve (AUC ={auc_score:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
```

### Explanation
- **Accuracy:** Overall correctness of the model.
- **Precision:** Proportion of true positives among all predicted positives.
- **Recall (Sensitivity):** Proportion of actual positives correctly identified.
- **F1-score:** Harmonic mean of Precision and Recall, providing a balanced measure.
- **ROC Curve & AUC:** Visual representation of the trade-off between TPR and FPR, with AUC summarizing overall model performance.

This implementation demonstrates how to evaluate a logistic regression model using various metrics and visualize its performance through ROC curves.

---

---

## 2026-06-16 23:48 — Practical 5_Demo_K-means Clustering.ipynb
**Style:** structured_academic (experimenting)

Here's a structured summary of the provided K-means clustering practical:

---

### [[K-means Clustering]]
**Definition**: An iterative vector quantization algorithm used to partition observations into `k` clusters based on distances to cluster centroids.  
**Formula**: Objective function to minimize:  
$$ \text{SSE} = \sum_{i=1}^{k} \sum_{x \in C_i} \|x - \mu_i\|^2 $$  
where \(C_i\) = cluster, \(\mu_i\) = centroid  
**Example**:  
```python
kmeans = KMeans(n_clusters=5, random_state=1)
y_pred = kmeans.fit_predict(X_scaled)
```

---

### [[Sum of Squared Errors (SSE)]]
**Definition**: Metric measuring total squared distance between data points and their cluster centroids. Lower values indicate better clustering.  
**Formula**:  
$$ \text{SSE} = \sum_{i=1}^{n} (x_i - \mu_{c(i)})^2 $$  
**Example**:  
```python
print(kmeans.inertia_)  # Outputs SSE value for the model
```

---

### [[Elbow Method]]
**Definition**: Technique to determine optimal number of clusters (`k`) by plotting SSE against varying `k` values. The "elbow" point indicates where SSE improvement diminishes.  
**Formula**: N/A (Visual interpretation method)  
**Example**:  
```python
sse = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)
plt.plot(range(1,11), sse)
```

---

### [[StandardScaler]]
**Definition**: Preprocessing technique that standardizes features by removing mean and scaling to unit variance using z-score normalization.  
**Formula**:  
$$ z = \frac{x - \mu}{\sigma} $$  
**Example**:  
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
```

---

### [[Cluster Centroids]]
**Definition**: Representative central points of clusters calculated as mean of all data points in the cluster.  
**Formula**:  
$$ \mu = \frac{1}{n} \sum_{i=1}^{n} x_i $$  
**Example**:  
```python
print(kmeans.cluster_centers_)  # Outputs centroid coordinates
```

---

### [[Customer Segmentation]]
**Definition**: Marketing strategy that divides customers into groups based on behavioral characteristics (e.g., income, spending).  
**Example**:  
```python
dat['Cluster'] = y_pred  # Assigning cluster labels to customers
```
**Insight**: Identified 5 segments including:
- Cluster 0: Low income, high spending
- Cluster 3: High income, high spending

---

### [[Visual Cluster Analysis]]
**Techniques**:  
1. **Scatter Plots**: Visualize cluster distribution and centroids  
   ```python
   plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y_pred)
   ```
2. **Boxplots**: Compare feature distributions across clusters  
   ```python
   plt.boxplot([dat[col][dat.Cluster==i] for i in range(5)])
   ```

This structured approach enables data-driven marketing strategies by identifying distinct customer groups through quantitative analysis.

---

---

## 2026-06-16 23:50 — Practical 5_K-means Clustering.ipynb
**Style:** structured_academic (experimenting)

# Summary: K-means Clustering and Cluster Analysis

## [[K-means Clustering]]  
**Definition**: An iterative unsupervised learning algorithm that partitions data into *K* clusters based on distances between data points and cluster centroids.  
**Formula**: Objective function to minimize:  
\[ \text{SSE} = \sum_{i=1}^{K} \sum_{x \in C_i} (x - \mu_i)^2 \]  
where \( \mu_i \) is the centroid of cluster \( C_i \).  
**Example**:  
```python
kmeans = KMeans(n_clusters=3, n_init=20, max_iter=300, random_state=1)
kmeans.fit(X_scaled)
y_pred = kmeans.predict(X_scaled)
```

---

## [[Sum of Squared Errors (SSE)]]  
**Definition**: A metric to evaluate clustering quality, representing the total squared distance between data points and their cluster centroids.  
**Formula**:  
\[ \text{SSE} = \sum_{i=1}^{K} \sum_{j=1}^{N_i} (x_{ij} - \mu_i)^2 \]  
where \( x_{ij} \) is the \( j \)-th point in cluster \( i \), and \( \mu_i \) is the centroid.  
**Example**:  
```python
sse = kmeans.inertia_  # Access SSE directly from KMeans model
print(f"SSE: {sse}")
```

---

## [[Elbow Method]]  
**Definition**: A technique to determine the optimal number of clusters (*K*) by identifying the "elbow" point in the SSE vs. *K* plot, where SSE decreases marginally.  
**Formula**: No direct formula; iterative computation of SSE for varying *K*:  
\[ \text{SSE}(K) = \text{Compute SSE for } K \text{ clusters} \]  
**Example**:  
```python
sse = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=1)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)
plt.plot(range(1, 11), sse, 'b-*')  # Plot SSE vs. K
```

---

## [[StandardScaler]]  
**Definition**: A preprocessing tool that standardizes features by removing the mean and scaling to unit variance.  
**Formula**:  
\[ z = \frac{x - \mu}{\sigma} \]  
where \( \mu \) = mean, \( \sigma \) = standard deviation.  
**Example**:  
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scales dataset X
```

---

## [[Hierarchical Clustering]]  
**Definition**: A method that builds nested clusters either agglomeratively (bottom-up) or divisively (top-down). Agglomerative clustering merges closest pairs iteratively.  
**Formula**: Proximity matrix updates using linkage criteria (e.g., single, complete, average).  
**Example**:  
```python
# Agglomerative steps (conceptual):
1. Initialize each point as a cluster.
2. Merge closest clusters using a linkage criterion.
3. Repeat until one cluster remains.
```

---

## Key Links  
- [[K-means Clustering]] uses [[Sum of Squared Errors (SSE)]] for evaluation and the [[Elbow Method]] to optimize *K*.  
- Data preprocessing with [[StandardScaler]] ensures robust clustering.  
- [[Hierarchical Clustering]] provides an alternative to K-means for exploring nested cluster structures.

---

---

## 2026-06-16 23:52 — Practical 6_Demo_Hierarchical Clustering.ipynb
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

---

---

## 2026-06-16 23:54 — Practical 6_Hierarchical Clustering.ipynb
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

---

---

## 2026-06-17 17:04 — ML1 Revision for CT_Week1-6.pdf
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

---

---

## 2026-06-17 17:12 — Lecture 2 - Intro to Supervised Learning & Regression Model.pdf
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content:

---

### **Supervised Machine Learning**  
**Definition**: A type of machine learning where models are trained on labeled data (input + correct output) to learn mappings from inputs to outputs for predictions.  
**Formula**: None directly provided.  
**Example**: Spam detection (classifies emails as "spam" or "not spam") or HDB price prediction (regresses housing prices from features).  

---

### **Linear Regression**  
**Definition**: A regression model predicting continuous target variables by fitting a linear equation to observed data.  
**Formula**:  
\[ y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \dots + \beta_nx_n \]  
Where \( y \) = predicted output, \( \beta_i \) = coefficients, \( x_i \) = input features.  
**Example**: Predicting house prices (\( y \)) based on size (\( x_1 \)) and location (\( x_2 \)).  

---

### **Logistic Regression**  
**Definition**: A classification model predicting categorical target variables (e.g., binary outcomes) using the logistic (sigmoid) function to output probabilities.  
**Formula**:  
\[ y = \frac{1}{1 + e^{-(\beta_0 + \beta_1x_1 + \dots + \beta_nx_n)}} \]  
**Example**: Predicting customer subscription (Yes/No) based on ad spend and demographics.  

---

### **Gradient Descent**  
**Definition**: An optimization algorithm minimizing a model's cost function by iteratively adjusting parameters via backpropagation.  
**Formula**: Parameter update rule:  
\[ \theta_{new} = \theta_{old} - \alpha \frac{\partial J}{\partial \theta} \]  
Where \( \alpha \) = learning rate, \( J \) = cost function.  
**Example**: Tuning weights in a neural network to reduce prediction error.  

---

### **Overfitting & Underfitting**  
**Definition**:  
- **Overfitting**: Model learns training data too well (high variance), failing to generalize to new data.  
- **Underfitting**: Model is too simple (high bias), failing to capture patterns in training data.  
**Formula**: None directly provided.  
**Example**: A polynomial regression model of degree 10 overfits noisy data, while a linear model underfits non-linear relationships.  

---

### **Bias-Variance Tradeoff**  
**Definition**: The balance between:  
- **Bias** (error from overly simplistic models)  
- **Variance** (error from excessive sensitivity to training data)  
**Formula**: Total Error = Bias² + Variance + Noise.  
**Example**: A decision tree with minimal pruning has low bias but high variance; excessive pruning increases bias.  

---

### **Model Assessment Metrics**  
**Definition**: Quantitative measures to evaluate model performance.  
**Formulas**:  
- **Mean Absolute Error (MAE)**: \( \text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i| \)  
- **Root Mean Squared Error (RMSE)**: \( \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2} \)  
- **R² Score**: \( R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2} \)  
**Example**: Evaluating a housing price regression model using RMSE to compare prediction errors.  

---

### **k-Fold Cross Validation**  
**Definition**: A resampling method splitting data into \( k \) subsets, using \( k-1 \) for training and 1 for testing, repeated \( k \) times.  
**Formula**: None directly provided.  
**Example**: Using 5-fold cross-validation to assess model stability with limited data.  

---

### **Logistic Regression Diagnostics**  
**Definition**: Statistical measures evaluating model coefficients.  
**Formulas**:  
- **Confidence Interval (95%)**: \( \beta \pm 1.96 \times \text{SE} \)  
- **Z-statistic**: \( z = \frac{\beta}{\text{SE}} \)  
**Example**: A coefficient \( \beta = 0.5 \), SE = 0.1 → Z = 5.0 (statistically significant if \( p < 0.05 \)).  

---

### **Generalization**  
**Definition**: A model’s ability to perform well on unseen data by learning underlying patterns rather than memorizing training data.  
**Formula**: None directly provided.  
**Example**: A model trained on diverse image data generalizes well to new, unseen images of the same class.  

---

### **Model Assessment (Classification)**  
**Definition**: Evaluation of classification models using accuracy metrics.  
**Formulas**:  
- **Training Accuracy**: \( \frac{\text{Correct Predictions (Training)}}{\text{Total Training Data}} \)  
- **Testing Accuracy**: \( \frac{\text{Correct Predictions (Testing)}}{\text{Total Testing Data}} \)  
**Example**: With 200 total data points (70% training, 30% testing), 10 training errors → Training Accuracy = \( \frac{140 - 10}{140} = 92.86\% \).  

---

**[[Wikilinks]]**:  
- [[Supervised Machine Learning]] → [[Linear Regression]], [[Logistic Regression]]  
- [[Gradient Descent]] → [[Optimization]]  
- [[Overfitting]] ↔ [[Underfitting]] → [[Bias-Variance Tradeoff]]  
- [[Model Assessment]] → [[k-Fold Cross Validation]], [[Bias-Variance Tradeoff]]

---

---

## 2026-06-17 17:17 — Week 1.1 - Universal Workflow of ML.pdf
**Style:** structured_academic (experimenting)

Here’s a structured summary of the **Universal Workflow of Machine Learning** using the specified academic format:

---

### **Universal Workflow of Machine Learning**  
**Term**: CRISP-DM Framework  
**Definition**: Industry-standard strategic methodology for ML projects with six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment.  
**Formula**: N/A  
**Example**: Aligning business goals with data quality assessments before model development.  
[[CRISP-DM Framework]]  

---

### **Step 1: Define the Problem & Assemble Data**  
**Term**: Problem Definition  
**Definition**: Identify inputs (features) and outputs (targets), problem type (classification/regression/clustering), and assumptions (e.g., outputs predictable from inputs).  
**Formula**: N/A  
**Example**: Predicting house prices (output) using features like size and location (inputs).  
[[Problem Definition]]  

---

### **Step 2: Choose Measure of Success**  
**Term**: Evaluation Metrics  
**Definition**: Metrics to optimize model performance (e.g., RMSE, Accuracy).  
**Formula**:  
- **RMSE**: \(\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2}\)  
- **Accuracy**: \(\frac{\text{True Positives + True Negatives}}{\text{Total Predictions}}\)  
**Example**: Using **Accuracy** for a spam detection classifier.  
[[Evaluation Metrics]]  

---

### **Step 3: Decide Evaluation Protocol**  
**Term**: Evaluation Protocol  
**Definition**: Method to split data for training/validation/testing.  
**Options**:  
- **Hold-Out Validation**: Suitable for large datasets.  
- **K-Fold Cross-Validation**: For small datasets (e.g., K=5).  
**Formula**: N/A  
**Example**: Applying 5-fold cross-validation to a dataset with 1,000 samples.  
[[Cross-Validation]]  

---

### **Step 4: Prepare Data**  
**Term**: Data Preprocessing  
**Definition**: Transform raw data into model-ready format via:  
- **Encoding**: One-hot/binary encoding for categorical data.  
- **Normalization**: Min-max scaling: \(x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}\).  
- **Feature Engineering**: Creating new features (e.g., polynomial terms).  
**Example**: Converting "Color" (red, blue, green) to binary vectors.  
[[Data Preprocessing]]  

---

### **Step 5: Build Baseline Model**  
**Term**: Baseline Model  
**Definition**: Simple model with default hyperparameters to establish performance benchmark.  
**Formula**: Gradient Descent Update: \(w_{t+1} = w_t - \eta \nabla L(w_t)\) (where \(\eta\) = learning rate).  
**Example**: Training a linear regression model with default hyperparameters.  
[[Gradient Descent]]  

---

### **Step 6: Overfit the Model**  
**Term**: Overfitting  
**Definition**: Model performs well on training data but poorly on validation data.  
**Formula**: N/A  
**Example**: A model with 100% training accuracy but 60% validation accuracy.  
[[Overfitting]]  

---

### **Step 7: Regularize & Tune Hyperparameters**  
**Term**: Regularization  
**Definition**: Techniques (e.g., L2 regularization) to prevent overfitting by penalizing complex models.  
**Formula**: L2 Regularization Loss: \(L_{\text{reg}} = L + \lambda \sum w_i^2\).  
**Example**: Using grid search to optimize learning rate (\(\eta\)) and regularization strength (\(\lambda\)).  
[[Regularization]]  

---

### **Key Takeaways**  
1. **CRISP-DM** guides strategic project planning.  
2. **Universal Workflow** ensures systematic tactical execution.  
3. **Iterate**: Continuously refine models via hyperparameter tuning and validation.  
4. **Document**: Track decisions for reproducibility and future reference.  

--- 

**Wikilinks**:  
- [[CRISP-DM Framework]]  
- [[Evaluation Metrics]]  
- [[Cross-Validation]]  
- [[Data Preprocessing]]  
- [[Gradient Descent]]  
- [[Overfitting]]  
- [[Regularization]]

---

---

## 2026-06-17 17:25 — Week 3 - Performance Evaluation.pdf
**Style:** structured_academic (experimenting)

### Model Evaluation and Metrics

#### Regression Model Evaluation

**Term -> Definition -> Formula -> Example**

1. **Mean Absolute Error (MAE)**
   - **Definition:** Measures the average absolute difference between actual and predicted values.
   - **Formula:** \( \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| \)
   - **Example:** If a model predicts house prices as [200k, 300k, 400k] and the actual prices are [195k, 305k, 410k], then \( \text{MAE} = \frac{|195-200| + |305-300| + |410-400|}{3} = \frac{5 + 5 + 10}{3} = 6.67 \).

2. **Mean Squared Error (MSE)**
   - **Definition:** Measures the average squared error between actual and predicted values.
   - **Formula:** \( \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \)
   - **Example:** Using the same data, \( \text{MSE} = \frac{(195-200)^2 + (305-300)^2 + (410-400)^2}{3} = \frac{25 + 25 + 100}{3} = 41.67 \).

3. **Root Mean Squared Error (RMSE)**
   - **Definition:** Measures the square root of average squared errors.
   - **Formula:** \( \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} \)
   - **Example:** Using the same data, \( \text{RMSE} = \sqrt{41.67} \approx 6.45 \).

4. **R-Squared Error (R²)**
   - **Definition:** Measures how well the model explains the variation in the data — also known as the coefficient of determination.
   - **Formula:** \( R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \)
   - **Example:** If the total sum of squares is 500 and the residual sum of squares is 167, then \( R^2 = 1 - \frac{167}{500} = 0.654 \).

#### Classification Model Evaluation

**Term -> Definition -> Formula -> Example**

1. **Accuracy**
   - **Definition:** Proportion of total correct predictions.
   - **Formula:** \( \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{FP} + \text{FN} + \text{TN}} \)
   - **Example:** If a model predicts 75 out of 125 images correctly, then \( \text{Accuracy} = \frac{75}{125} = 0.6 \).

2. **Precision**
   - **Definition:** Proportion of predicted positives that are positive.
   - **Formula:** \( \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} \)
   - **Example:** If out of 10 spam emails, the model correctly identifies 9 and incorrectly flags 5 non-spam emails as spam, then \( \text{Precision} = \frac{9}{9+5} = 0.643 \).

3. **Recall (True Positive Rate)**
   - **Definition:** Proportion of actual positives that were correctly predicted.
   - **Formula:** \( \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} \)
   - **Example:** If out of 10 spam emails, the model correctly identifies 9 and misses 1 as non-spam, then \( \text{Recall} = \frac{9}{9+1} = 0.9 \).

4. **Specificity (True Negative Rate)**
   - **Definition:** Proportion of actual negatives that were correctly predicted.
   - **Formula:** \( \text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}} \)
   - **Example:** If out of 90 non-spam emails, the model correctly identifies 89 and incorrectly flags 1 as spam, then \( \text{Specificity} = \frac{89}{89+1} = 0.99 \).

5. **F1 Score**
   - **Definition:** Harmonic mean of precision and recall.
   - **Formula:** \( \text{F1 Score} = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \)
   - **Example:** Using the same data, \( \text{F1 Score} = \frac{2 \times 0.643 \times 0.9}{0.643 + 0.9} = \frac{1.1574}{1.543} \approx 0.75 \).

6. **False Positive Rate (FPR)**
   - **Definition:** Proportion of actual negatives that were incorrectly predicted as positive.
   - **Formula:** \( \text{FPR} = 1 - \text{Specificity} \)
   - **Example:** If out of 90 non-spam emails, the model incorrectly flags 1 as spam, then \( \text{FPR} = 1 - 0.99 = 0.01 \).

7. **False Negative Rate (FNR)**
   - **Definition:** Proportion of actual positives that were incorrectly predicted as negative.
   - **Formula:** \( \text{FNR} = 1 - \text{Recall} \)
   - **Example:** If out of 10 spam emails, the model misses 1 as non-spam, then \( \text{FNR} = 1 - 0.9 = 0.1 \).

8. **ROC Curve and AUC**
   - **Definition:** Graphically show how classification models perform by plotting True Positive Rate versus False Positive Rate across thresholds.
   - **Formula for AUC:** Trapezoidal area calculation.
   - **Example:** Given a set of true labels and model scores, the AUC can be computed to compare model performance.

#### Summary

**Term -> Definition -> Use When...**

- **MAE (Mean Absolute Error)**
  - Measures average error magnitude in same units as target.
  - Quick, interpretable baseline metric for regression.

- **MSE (Mean Squared Error)**
  - Measures average squared error and heavily penalizes outliers.
  - Useful when large errors must be flagged.

- **RMSE (Root Mean Squared Error)**
  - Root of MSE with same units as target.
  - Most popular regression metric.

- **R² (Coefficient of Determination)**
  - Proportion of variation explained, ranges from 0 to 1.
  - Useful for comparing models on different datasets.

- **Accuracy**
  - Percentage of all predictions correct.
  - Suitable when classes are balanced.

- **Precision**
  - Proportion of positive predictions that are correct.
  - Important when false positives are costly.

- **Recall (True Positive Rate)**
  - Proportion of actual positives correctly caught.
  - Crucial when false negatives are dangerous.

- **F1 Score**
  - Harmonic mean of precision and recall, useful for imbalanced classes.
  - Balances precision and recall, providing a balanced tradeoff.

- **AUC (Area Under the ROC Curve)**
  - Model's ability to distinguish between classes across all thresholds.
  - Useful for comparing models in terms of threshold independence.

---

---

## 2026-06-17 17:33 — Week 4.2 - KNN.pdf
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

---

---

## 2026-06-17 17:38 — Wk 4.1 - Decision Trees.pdf
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided Decision Tree content:

---

### [[Decision Tree]]
**Definition**: A supervised machine learning algorithm used for classification and regression tasks. It splits data into homogeneous subgroups using a hierarchical tree structure with root nodes, internal nodes, and leaf nodes.  
**Formula**: N/A  
**Example**: Classifying users as potential hackers based on login time, location, and device (Page 3).

---

### [[Decision Tree Components]]
**Definition**:  
- **Root Node**: Starting point of the tree where initial data split occurs.  
- **Internal Nodes**: Represent conditions/tests on features.  
- **Leaf Nodes**: Terminal nodes representing final class labels or predictions.  
**Formula**: N/A  
**Example**: Titanic survival prediction tree (Page 5).

---

### [[Data Splitting]]
**Definition**: The process of dividing data into subgroups to maximize homogeneity.  
**Key Principles**:  
1. Splits aim for pure nodes (single class/continuous value).  
2. Recursive splitting until stopping conditions are met.  
3. Criteria differ for classification (impurity measures) vs. regression (MSE).  
**Formula**: N/A  
**Example**: Splitting users into "Hacker" or "Non-Hacker" based on features (Page 6).

---

### [[CART (Classification and Regression Tree)]]
**Definition**: A binary decision tree algorithm for classification and regression using binary splits.  
**Algorithm Steps**:  
1. Evaluate all input variables and split points.  
2. Select split with highest impurity reduction.  
3. Repeat until stopping conditions met.  
**Formula**: N/A  
**Example**: Scikit-learn’s `DecisionTreeClassifier` implementation (Page 12).

---

### [[Gini Impurity Index]]
**Definition**: A measure of node purity in classification trees. Lower values indicate higher purity.  
**Formula**:  
For a node with \( m \) classes:  
\[ I_A = 1 - \sum_{c=1}^m (p_c)^2 \]  
where \( p_c \) is the proportion of class \( c \).  
**Example**:  
- Node A (300 Y=1, 700 Y=2):  
  \( I_A = 1 - (0.3^2 + 0.7^2) = 0.42 \) (Page 16).

---

### [[Overfitting and Pruning]]
**Definition**:  
- **Overfitting**: Tree grows too complex, memorizing training data.  
- **Pruning**: Technique to reduce overfitting by removing weak branches.  
**Types**:  
1. **Pre-pruning**: Stop splitting early (e.g., max depth).  
2. **Post-pruning**: Trim branches after full growth.  
**Formula**: N/A  
**Example**: Using `max_depth` or `min_samples_leaf` in scikit-learn (Page 9).

---

### [[Stopping Conditions]]
**Definition**: Criteria to halt tree growth and prevent overfitting.  
**Common Conditions**:  
1. Maximum tree depth reached.  
2. Minimum records in leaf/parent nodes.  
3. Node purity achieved (\( Gini = 0 \)).  
**Formula**: N/A  
**Example**: Setting `min_samples_split=20` to avoid small nodes (Page 10).

---

### [[Types of Decision Trees]]
**Definition**: Variants of decision tree algorithms.  
**Key Types**:  
1. **CART**: Binary splits, used in scikit-learn.  
2. **CHAID**: Uses chi-square tests for splits.  
3. **ID3/C4.5**: Uses information gain/entropy.  
**Formula**: N/A  
**Example**: CHAID for market segmentation analysis (Page 11).

---

### [[Strengths and Limitations of Decision Trees]]
**Strengths**:  
- Easy to interpret and visualize.  
- Handles missing values and categorical data.  
**Limitations**:  
- Prone to overfitting and instability.  
- Struggles with linear relationships.  
**Formula**: N/A  
**Example**: Random Forest ensembles mitigate standalone tree weaknesses (Page 20).

---

### [[Gini Impurity Reduction Example]]
**Calculation**:  
Given a split into nodes B and C:  
\[ \Delta I = I_A - \left( \frac{n_B}{n_A} I_B + \frac{n_C}{n_A} I_C \right) \]  
**Example**:  
- Node A (300 Y=1, 700 Y=2) splits into B (100 Y=1, 600 Y=2) and C (200 Y=1, 100 Y=2).  
- Compute \( I_B \), \( I_C \), and \( \Delta I \) (Page 21).

---

### [[Activity: Split Decision Using Gini]]
**Scenario**: Choosing between splits for "Risk_Group" (high vs. {medium, low}) using Gini Impurity.  
**Steps**:  
1. Compute Gini for parent and child nodes.  
2. Select split with highest \( \Delta I \).  
**Example**: Analyze P1-P14 dataset to compare split options (Page 22).

---

This summary links core concepts like [[Decision Tree]], [[CART]], and [[Gini Impurity Index]], providing formulas and practical examples for clarity.

---

---

## 2026-06-17 18:09 — Wk4_Practical_4.1_Decision_Trees.ipynb
**Style:** structured_academic (experimenting)

# Week 4.2 Practical - Decision Trees  
**Module:** machine_learning  
**Style:** structured_academic  

---

### [[Decision Tree Classifier]]  
**Definition**: A supervised learning algorithm that constructs a tree model for classification tasks by splitting data into homogeneous subgroups based on feature conditions.  
**Formula**: N/A  
**Example**: Classified Titanic passenger survival using features like `Fare` and `Age`, achieving 85% testing accuracy after hyperparameter tuning.  

---

### [[Decision Tree Regressor]]  
**Definition**: A regression algorithm that predicts continuous values by averaging target values in terminal nodes of a decision tree.  
**Formula**: N/A  
**Example**: Predicted noisy quadratic data ($y = 4*(X - 0.5)^2 + \text{noise}$) with $R^2 = 0.85$ on test data.  

---

### [[GridSearchCV]]  
**Definition**: A systematic hyperparameter tuning method that evaluates all parameter combinations via cross-validation to identify optimal values.  
**Formula**: N/A  
**Example**: Optimized `DecisionTreeClassifier` by testing `criterion` (gini/entropy), `max_depth` (2-7), and `min_samples_leaf` (1/5/10), improving accuracy from 75% to 85%.  

---

### [[Hyperparameters]]  
**Definition**: Pre-set parameters controlling the structure of a decision tree model (e.g., `max_depth`, `min_samples_leaf`).  
**Formula**: N/A  
**Example**: GridSearch optimized hyperparameters for Titanic classification: `criterion='gini'`, `max_depth=3`, `min_samples_leaf=1`.  

---

### [[Mean Squared Error (MSE)]]  
**Definition**: Average squared difference between actual and predicted values, penalizing large errors.  
**Formula**:  
\[ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2 \]  
**Example**: Regression model achieved $\text{MSE} = 0.12$ on test data after tuning.  

---

### [[R-squared ($R^2$)]]  
**Definition**: Measures how well the model explains variance in the target variable (0 = no fit, 1 = perfect fit).  
**Formula**:  
\[ R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} \]  
**Example**: Decision Tree Regressor achieved $R^2 = 0.85$ on test data.  

---

### [[Cross-Validation]]  
**Definition**: Technique to assess model performance by partitioning data into folds, training on subsets, and validating on held-out folds.  
**Formula**: N/A  
**Example**: Used 10-fold cross-validation (`cv=10`) in `GridSearchCV` for hyperparameter tuning.  

---

### [[Training Accuracy]]  
**Definition**: Proportion of correct predictions on the training dataset.  
**Formula**:  
\[ \text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}} \]  
**Example**: Optimized model achieved 92% training accuracy after GridSearch.  

---

### [[Testing Accuracy]]  
**Definition**: Proportion of correct predictions on unseen test data, reflecting model generalization.  
**Formula**: Same as Training Accuracy  
**Example**: Final Decision Tree Classifier achieved 85% testing accuracy.  

---

### [[Overfitting]]  
**Definition**: Occurs when a model performs exceptionally well on training data but poorly on unseen data due to excessive complexity.  
**Formula**: N/A  
**Example**: Initial Decision Tree Classifier had 90% training accuracy but only 75% testing accuracy before pruning.  

---

### [[Feature Importance]]  
**Definition**: Relative contribution of each feature to the model's predictions.  
**Formula**: N/A  
**Example**: In the Titanic dataset, `Fare` and `Sex` were top features influencing survival predictions.  

---

### [[K-Fold Cross Validation]]  
**Definition**: Cross-validation method that splits data into *K* folds, training on *K-1* folds and validating on the remaining fold iteratively.  
**Formula**: N/A  
**Example**: Used 5-fold cross-validation (`cv=5`) to evaluate Decision Tree Classifier performance.  

---

### [[Decision Tree Visualization]]  
**Definition**: Graphical representation of a decision tree showing nodes, splits, and terminal leaves.  
**Formula**: N/A  
**Example**: Visualized Titanic survival model using `tree.plot_tree()` to show splits on features like `Fare` and `Age`.  

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Classification]]  
- [[Regression]]  
- [[Hyperparameter Tuning]]  
- [[Model Evaluation]]  
- [[Overfitting]]  
- [[Cross-Validation]]  

This summary captures key concepts from the notebook, linking them via wikilinks for cross-referencing. Each term includes a concise definition, formula (where applicable), and practical examples from the exercises.

---

---

## 2026-06-17 18:15 — Wk4-Practical_4.2_KNN.ipynb
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

---

---

## 2026-06-17 18:17 — Practical 1a - Linear Regression.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided Linear Regression practical content:

---

### [[Linear Regression]]  
**Definition**: A supervised learning algorithm modeling the linear relationship between dependent variable(s) and one or more independent variables.  
**Formula**:  
\[ Y = b_0 + b_1X_1 + b_2X_2 + \ldots + b_nX_n \]  
where \( Y \) = dependent variable, \( b_0 \) = intercept, \( b_1...b_n \) = coefficients, \( X_1...X_n \) = independent variables  
**Example**: Predicting donation amount (`TARGET_D`) using features like `RAMNTALL` and `AVGGIFT` (Code Cell 12).  

---

### [[Model Training]]  
**Definition**: Process of fitting the linear regression model to the training data to find optimal coefficients.  
**Formula**: N/A  
**Example**: Using `lm.fit(X_train, y_train)` to train the model (Code Cell 15).  

---

### [[Model Evaluation Metrics]]  
**Definition**: Quantitative measures to assess model performance.  
**Key Metrics**:  
- **Root Mean Squared Error (RMSE)**:  
  \[ \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2} \]  
- **R-squared (\(R^2\))**:  
  \[ R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} \]  
**Example**: Train RMSE = 0.42, Test \(R^2\) = 0.78 (Code Cell 17-19).  

---

### [[p-value]]  
**Definition**: Probability of observing test results under the null hypothesis (coefficient = 0). Values < 0.05 indicate statistical significance.  
**Formula**: N/A  
**Example**: Features like `RFA_2F` (p-value = 0.00) were retained due to significance (Markdown Cell 22).  

---

### [[Statsmodels]]  
**Definition**: Python library for statistical modeling, including hypothesis testing and regression diagnostics.  
**Formula**: N/A  
**Example**: Using `sm.OLS()` for coefficient p-value analysis (Code Cell 21).  

---

### [[Train-Test Split]]  
**Definition**: Method to divide data into training (model learning) and testing (model evaluation) subsets.  
**Formula**: N/A  
**Example**: 70% training and 30% testing split using `train_test_split` (Code Cell 13).  

---

### [[Feature Selection]]  
**Definition**: Process of selecting the most relevant features to improve model performance.  
**Formula**: N/A  
**Example**: Excluding `AGE`, `LASTDATE`, and `TIMELAG` due to high p-values (Code Cell 24).  

---

### [[Ordinary Least Squares (OLS)]]  
**Definition**: Statistical method for linear regression that minimizes the sum of squared residuals.  
**Formula**: N/A  
**Example**: Implemented via `sm.OLS(y_train, X_train).fit()` (Code Cell 21).  

---

### [[Coefficient Confidence]]  
**Definition**: Assessment of coefficient reliability using p-values and confidence intervals.  
**Formula**: N/A  
**Example**: Features with p-values < 0.05 (e.g., `RAMNTALL`) were deemed confident predictors (Markdown Cell 22).  

---

### [[Model Optimization]]  
**Definition**: Techniques to enhance model performance, such as feature selection or hyperparameter tuning.  
**Formula**: N/A  
**Example**: Reducing RMSE from 0.42 to 0.38 after removing low-confidence features (Code Cell 28).  

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Regression Analysis]]  
- [[Hypothesis Testing]]  
- [[Model Generalization]]  
- [[Scikit-learn]]  

This summary adheres to the structured academic format, connecting key concepts via wikilinks and providing practical examples from the notebook exercises.

---

---

## 2026-06-17 18:19 — Practical 1b - Logistic Regression.ipynb
**Style:** structured_academic (experimenting)

# Week 4.1 Practical - Logistic Regression  
**Module:** machine_learning  
**Style:** structured_academic (experimenting)  

---

### [[Logistic Regression]]  
**Definition**: A statistical model used for binary classification tasks that estimates probabilities using the logistic function.  
**Formula**: The probability of class 1 is given by:  
\[ P(y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + ... + \beta_n x_n)}} \]  
**Example**: Predicting donor response (`TARGET_B`) based on features like `RFA_2F` and `LASTGIFT` (Page 3).  

---

### [[Stratified Sampling]]  
**Definition**: A sampling technique that ensures the proportion of class labels in the sample matches the original dataset.  
**Formula**: N/A  
**Example**: Balanced `TARGET_B=0` and `TARGET_B=1` classes by sampling 1000 instances of each (Code Cell 16-17).  

---

### [[Model Accuracy]]  
**Definition**: The proportion of correct predictions (both true positives and true negatives) made by the model.  
**Formula**:  
\[ \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} \]  
**Example**: Achieved 0.85 training accuracy and 0.78 testing accuracy after feature selection (Code Cell 39-40).  

---

### [[P-Value Analysis (Statsmodels)]]  
**Definition**: Statistical test to determine the significance of features in a logistic regression model. Features with p-values < 0.05 are considered significant.  
**Formula**: N/A  
**Example**: Identified `RFA_2F`, `LASTGIFT`, and `LASTDATE` as significant features (p-value ≈ 0) (Code Cell 33).  

---

### [[Feature Selection]]  
**Definition**: The process of selecting a subset of relevant features for model building to improve performance and reduce overfitting.  
**Formula**: N/A  
**Example**: Removed `AGE`, `AVGGIFT`, and `TIMELAG` due to high p-values (>0.05) (Code Cell 36).  

---

### [[Hyperparameters in Logistic Regression]]  
**Definition**: Parameters set before training, such as optimization solver and maximum iterations.  
**Formula**: N/A  
**Example**: Used `solver='lbfgs'` and `max_iter=10000` to ensure convergence (Code Cell 24).  

---

### [[Train-Test Split]]  
**Definition**: Division of data into training and testing subsets to evaluate model generalization.  
**Formula**: N/A  
**Example**: Split data into 70% training and 30% testing sets using `train_test_split` (Code Cell 22).  

---

### [[Probability Predictions (predict_proba)]]  
**Definition**: Method to estimate the probability of a data point belonging to a specific class.  
**Formula**: N/A  
**Example**: Retrieved probabilities for class 0 using `lg.predict_proba(X_train)[:,0]` (Code Cell 28).  

---

### [[Model Coefficients and Intercept]]  
**Definition**: Coefficients represent the relationship between features and the log-odds of the outcome; the intercept is the baseline log-odds.  
**Formula**:  
\[ \text{Log-odds} = \beta_0 + \beta_1 x_1 + ... + \beta_n x_n \]  
**Example**: Printed coefficients and intercept for the initial model (Code Cell 25).  

---

### [[Overfitting]]  
**Definition**: Occurs when a model performs exceptionally well on training data but poorly on unseen data due to excessive complexity.  
**Formula**: N/A  
**Example**: The adjusted model showed near-perfect training accuracy (1.0), suggesting potential overfitting (Code Cell 42).  

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Classification]]  
- [[Model Evaluation]]  
- [[Statistical Significance]]  
- [[Cross-Validation]]  

This summary connects key concepts via wikilinks and adheres to the structured academic format, capturing both theoretical foundations and practical implementation steps from the notebook.

---

---

## 2026-06-17 18:22 — Practical 3.1 Regression Model Performance - Lau Yew Ban Zyne.ipynb
**Style:** structured_academic (experimenting)

# Week 2.1 Practical - Regression Model Performance Evaluation  
**Module:** machine_learning  
**Style:** structured_academic  

---

### [[Linear Regression]]  
**Definition**: A supervised learning algorithm modeling the linear relationship between input features and a continuous target variable using a straight-line equation.  
**Formula**:  
\[ y = \beta_0 + \beta_1 x + \epsilon \]  
where \( \beta_0 \) = intercept, \( \beta_1 \) = slope, \( \epsilon \) = error term.  
**Example**: Predicted phishing attacks (\( y \)) based on detected emails (\( x \)) with \( \beta_1 = 0.05 \) (Code Cell 12).  

---

### [[Train-Test Split]]  
**Definition**: Division of data into training (model learning) and testing (model evaluation) subsets to assess generalization.  
**Formula**: N/A  
**Example**: 70% training (700 samples) and 30% testing (300 samples) split (Code Cell 9).  

---

### [[Mean Absolute Error (MAE)]]  
**Definition**: Average absolute difference between actual and predicted values.  
**Formula**:  
\[ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)}| \]  
**Example**: Train MAE = 13.0114, Test MAE = 13.0678 (Code Cell 14 & 16).  

---

### [[Mean Squared Error (MSE)]]  
**Definition**: Average squared difference between actual and predicted values, penalizing large errors.  
**Formula**:  
\[ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2 \]  
**Example**: Train MSE = 263.58, Test MSE = 262.15 (Code Cell 14 & 16).  

---

### [[Root Mean Squared Error (RMSE)]]  
**Definition**: Square root of MSE, interpreting error in target variable units.  
**Formula**:  
\[ \text{RMSE} = \sqrt{\text{MSE}} \]  
**Example**: Train RMSE = 16.24, Test RMSE = 16.20 (Code Cell 14 & 16).  

---

### [[R-squared (\(R^2\))]]  
**Definition**: Proportion of variance in the target explained by the model (0 = no fit, 1 = perfect fit).  
**Formula**:  
\[ R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} \]  
**Example**: Train \(R^2\) = 0.89, Test \(R^2\) = 0.89 (Code Cell 14 & 16).  

---

### [[Overfitting]]  
**Definition**: Model performs well on training data but poorly on unseen data due to excessive complexity.  
**Formula**: N/A  
**Example**: Minimal gap between Train (\(R^2=0.89\)) and Test (\(R^2=0.89\)) metrics indicates no overfitting (Code Cell 18).  

---

### [[Feature Engineering]]  
**Definition**: Process of transforming raw data into meaningful features to improve model performance.  
**Formula**: N/A  
**Example**: Added \( \text{Detected\_Squared} \) feature to capture non-linear relationships (Code Cell 22).  

---

### [[Model Comparison]]  
**Definition**: Evaluation of model performance before and after modifications (e.g., feature engineering).  
**Formula**: N/A  
**Example**: After adding \( \text{Detected\_Squared} \), Test RMSE improved from 16.20 to 15.21 (Code Cell 27).  

---

### [[Actual vs Predicted Plot]]  
**Definition**: Visualization comparing model predictions to actual values, with a diagonal line representing perfect predictions.  
**Formula**: N/A  
**Example**: Scatter plot showed points closely aligned with the red diagonal line, indicating accurate predictions (Code Cell 20).  

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Regression]]  
- [[Model Evaluation]]  
- [[Feature Engineering]]  
- [[Overfitting]]  
- [[Linear Regression]]  

This summary connects key regression evaluation concepts via wikilinks, providing formulas and practical examples from the notebook exercises.

---

---

## 2026-06-17 18:28 — Practical 3.2 - Classification Model Performance Evaluation - Lau Yew Ban Zyne.ipynb
**Style:** structured_academic (experimenting)

### Machine Learning - Practical 2.2: Classification Performance Metrics

#### Term -> Definition -> Formula -> Example

---

**Accuracy**

- **Definition:** Proportion of total correct predictions.
- **Formula:** 
  \[
  \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{FP} + \text{FN} + \text{TN}}
  \]
- **Example:**
  ```python
  accuracy_train = accuracy_score(y_train, y_fitted)
  print(f"Accuracy (Training Set): {accuracy_train:.2f}")
  ```

---

**Precision**

- **Definition:** Ratio of correctly predicted positive instances to the total predicted as positive.
- **Formula:** 
  \[
  \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
  \]
- **Example:**
  ```python
  precision_train = precision_score(y_train, y_fitted)
  print(f"Precision (Training Set): {precision_train:.2f}")
  ```

---

**Recall**

- **Definition:** Ratio of correctly predicted positive instances to the total actual positive.
- **Formula:** 
  \[
  \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
  \]
- **Example:**
  ```python
  recall_train = recall_score(y_train, y_fitted)
  print(f"Recall (Training Set): {recall_train:.2f}")
  ```

---

**F1-score**

- **Definition:** Harmonic mean of Precision and Recall.
- **Formula:** 
  \[
  \text{F1-score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
  \]
- **Example:**
  ```python
  f1_train = f1_score(y_train, y_fitted)
  print(f"F1-score (Training Set): {f1_train:.2f}")
  ```

---

**ROC Curve and Area Under the Curve (AUC)**

- **True Positive Rate (TPR) / Sensitivity:**
  \[
  \text{TPR} = \frac{\text{TP}}{\text{TP} + \text{FN}}
  \]
- **False Positive Rate (FPR):**
  \[
  \text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}
  \]
- **Significance:**
  - The ROC curve shows the trade-off between TPR and FPR at various threshold settings.
  - AUC summarizes the overall performance of a binary classifier across all possible classification thresholds.

---

**Example Code for ROC Curve and AUC Calculation**

```python
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve, roc_auc_score

# Load the dataset
breast_cancer = load_breast_cancer()
X, y = breast_cancer.data, breast_cancer.target

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Define and train a LogisticRegression model
lg = LogisticRegression(solver='lbfgs', max_iter=10000)
lg.fit(X_train, y_train)

# Predictions on training set
y_fitted = lg.predict(X_train)
y_test_pred = lg.predict(X_test)

# Calculate performance metrics for both sets
accuracy_train  = accuracy_score(y_train, y_fitted)
precision_train = precision_score(y_train, y_fitted)
recall_train    = recall_score(y_train, y_fitted)
f1_train        = f1_score(y_train, y_fitted)

accuracy_test  = accuracy_score(y_test, y_test_pred)
precision_test = precision_score(y_test, y_test_pred)
recall_test    = recall_score(y_test, y_test_pred)
f1_test        = f1_score(y_test, y_test_pred)

print(f"{'Metric':15} {'Training Set':15} {'Testing Set':15}")
print(f"{'Accuracy':15} {accuracy_train:<15.2f} {accuracy_test:<15.2f}")
print(f"{'Precision':15} {precision_train:<15.2f} {precision_test:<15.2f}")
print(f"{'Recall':15} {recall_train:<15.2f} {recall_test:<15.2f}")
print(f"{'F1-score':15} {f1_train:<15.2f} {f1_test:<15.2f}")

# Get the predicted probabilities for positive class
y_fitted_prob = lg.predict_proba(X_train)[:, 1]

# Calculate ROC curve and AUC score
fpr, tpr, thresholds = roc_curve(y_train, y_fitted_prob)
auc_score = roc_auc_score(y_train, y_fitted_prob)

print(f"AUC Score: {auc_score:.2f}")

# Plot the ROC curve
plt.plot(fpr, tpr, label=f'ROC curve (AUC ={auc_score:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
```

This code snippet demonstrates how to calculate and visualize the performance metrics (accuracy, precision, recall, F1-score) and the ROC curve for a logistic regression model trained on the Breast Cancer dataset.

---

---

## 2026-06-17 18:33 — Practical 5_Demo_K-means Clustering.ipynb
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

---

---

## 2026-06-17 18:40 — Practical 5_K-means Clustering.ipynb
**Style:** structured_academic (experimenting)

# Summary: K-means Clustering

## [[K-means Clustering]]
**Definition**: An iterative clustering algorithm that partitions data into *k* distinct clusters based on distances. It initializes centroids, assigns data points to the nearest cluster, updates centroids, and repeats until convergence or a maximum number of iterations is reached.  
**Formula**: Objective function to minimize:  
\[ \text{SSE} = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (x_i - \mu_j)^2 \]  
**Example**:  
```python
kmeans = KMeans(n_clusters=3, n_init=20, max_iter=300, random_state=1)
kmeans.fit(X_scaled)
```

---

## [[Sum of Squared Errors (SSE)]]
**Definition**: A metric to evaluate clustering performance, representing the sum of squared distances between data points and their assigned cluster centroids. Lower SSE indicates better clustering.  
**Formula**:  
\[ \text{SSE} = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (x_i - \mu_j)^2 \]  
**Example**:  
```python
sse = kmeans.inertia_
print(f"Sum of Squared Errors (SSE): {sse}")
```

---

## [[Elbow Method]]
**Definition**: A technique to determine the optimal number of clusters (*k*) by plotting SSE values against varying *k*. The "elbow" point (where SSE decreases less sharply) indicates the optimal *k*.  
**Formula**: No direct formula; relies on visual interpretation.  
**Example**:  
```python
sse = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=1)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)
plt.plot(range(1, 11), sse, 'b-*')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.show()
```

---

## [[StandardScaler]]
**Definition**: A preprocessing method that standardizes features by removing the mean and scaling to unit variance, ensuring equal contribution of all features to distance calculations.  
**Formula**:  
\[ X_{\text{scaled}} = \frac{X - \mu}{\sigma} \]  
**Example**:  
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## [[Centroids]]
**Definition**: The central point of a cluster, representing the average position of all data points assigned to that cluster.  
**Formula**:  
\[ \mu_j = \frac{1}{n_j} \sum_{i=1}^{n_j} x_i \]  
**Example**:  
```python
centroids = kmeans.cluster_centers_
```

---

## [[Cluster]]
**Definition**: A group of data points that are more similar to each other than to points in other clusters, as determined by the K-means algorithm.  
**Formula**: Not applicable.  
**Example**:  
```python
y_pred = kmeans.predict(X_scaled)
```

---

## Key Concepts Interconnection
- [[K-means Clustering]] uses [[Centroids]] to group data into [[Cluster]]s.  
- Model performance is evaluated using [[Sum of Squared Errors (SSE)]].  
- The [[Elbow Method]] aids in selecting the optimal number of clusters (*k*) by analyzing SSE trends.  
- Features are normalized using [[StandardScaler]] to ensure robust distance calculations.

---

---

## 2026-06-17 18:43 — Practical 6_Demo_Hierarchical Clustering.ipynb
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

---

---

## 2026-06-17 18:49 — Practical 6_Hierarchical Clustering.ipynb
**Style:** structured_academic (experimenting)

Here's a structured summary of the provided Hierarchical Clustering content:

---

### [[Hierarchical Clustering]]
**Definition**: A method that builds nested clusters by either merging smaller clusters (Agglomerative) or splitting larger ones (Divisive).  
**Formula**:  
- Proximity matrix calculation: $d(i,j)$ (distance between clusters)  
- Linkage criteria (e.g., Average: $d\left(\{C_i, C_j\}, \{C_k, C_l\}\right) = \frac{1}{|C_i||C_j|}\sum_{p \in C_i} \sum_{q \in C_j} d(p,q)$)  
**Example**:  
```python
Z = shc.linkage(X_scaled, method='average')  # Builds hierarchical clusters
plt.figure(); shc.dendrogram(Z)  # Visualizes nested structure
```

---

### [[Agglomerative Clustering]]
**Definition**: Bottom-up approach where each data point starts as its own cluster, iteratively merging closest pairs until one cluster remains.  
**Formula**:  
- Merge rule: $C_{\text{new}} = C_i \cup C_j$ where $d(C_i, C_j)$ is minimized  
**Example**:  
```python
ac3 = AgglomerativeClustering(n_clusters=3, linkage='average')
clusters = ac3.fit_predict(X_scaled)  # Assigns 3 clusters
```

---

### [[Dendrogram]]
**Definition**: Tree-like diagram visualizing hierarchical cluster structure and merge distances.  
**Formula**: Derived from linkage matrix $Z$ (rows represent merges, columns: cluster IDs and distances)  
**Example**:  
```python
plt.figure(figsize=(12, 12))
shc.dendrogram(Z, orient='top')  # Shows hierarchical relationships
plt.xlabel('Data points')
plt.title('Dendrogram')
```

---

### [[Linkage Methods]]
**Definition**: Criteria for calculating distances between clusters during merging. Common types:  
1. **Single**: $d(C_i, C_j) = \min(d(p,q))$  
2. **Complete**: $d(C_i, C_j) = \max(d(p,q))$  
3. **Average**: Mean distance between all pairs  
4. **Ward**: Minimizes variance increase ($\min \Delta SS$)  
**Example**:  
```python
Z_ward = shc.linkage(X_scaled, method='ward')  # Default in many implementations
```

---

### [[Silhouette Score]]
**Definition**: Metric evaluating cluster separation and cohesion (-1 ≤ score ≤ 1). Higher values indicate better clustering.  
**Formula**:  
$$
S = \frac{b - a}{b} \quad \text{where } a = \text{within-cluster distance}, \; b = \text{nearest cluster distance}
$$
**Example**:  
```python
silhouette_score(X_scaled, ac3.labels_)  # Evaluates cluster quality
```

---

### [[Condensed Distance Matrix]]
**Definition**: Compact representation of pairwise distances between clusters.  
**Formula**: Upper triangular matrix $D$ where $D[i,j] = d(C_i, C_j)$  
**Example**:  
```python
distance_matrix = cdist(X_scaled, X_scaled)  # Full matrix
condensed_matrix = squareform(distance_matrix)  # Converts to condensed form
```

---

### [[StandardScaler]]
**Definition**: Normalizes data by removing mean and scaling to unit variance.  
**Formula**:  
$$
X_{\text{scaled}} = \frac{X - \mu}{\sigma} \quad (\mu = \text{mean}, \; \sigma = \text{standard deviation})
$$
**Example**:  
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)  # Normalizes features
```

---

### [[Cluster Evaluation]]
**Definition**: Process to determine optimal number of clusters using metrics like Silhouette Score.  
**Example**:  
```python
k_range = range(2, 11)
silhouette_scores = [silhouette_score(X_scaled, AgglomerativeClustering(n_clusters=k).fit_predict(X_scaled)) for k in k_range]
plt.bar(k_range, silhouette_scores)  # Visualizes optimal K
```

---

### Key Comparison (Average vs Ward Linkage)
| **Metric**          | **Average Linkage**       | **Ward Linkage**          |
|----------------------|---------------------------|----------------------------|
| Optimal K (Silhouette) | 9 clusters (higher score) | 5 clusters (higher score) |
| Merging Criterion    | Mean distance between clusters | Minimizes variance increase |

---

This summary integrates theoretical concepts, mathematical formulations, and practical code examples from the provided materials. Use [[Wikilinks]] to navigate between related concepts in your notes.

---

