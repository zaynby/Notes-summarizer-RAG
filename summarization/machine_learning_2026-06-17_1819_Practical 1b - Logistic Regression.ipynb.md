# Practical 1b - Logistic Regression.ipynb
**Module:** machine_learning
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