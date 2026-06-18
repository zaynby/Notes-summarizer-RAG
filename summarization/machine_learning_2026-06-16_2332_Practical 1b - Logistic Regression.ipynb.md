# Practical 1b - Logistic Regression.ipynb
**Module:** machine_learning
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