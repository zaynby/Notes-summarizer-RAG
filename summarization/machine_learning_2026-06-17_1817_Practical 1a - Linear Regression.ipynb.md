# Practical 1a - Linear Regression.ipynb
**Module:** machine_learning
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