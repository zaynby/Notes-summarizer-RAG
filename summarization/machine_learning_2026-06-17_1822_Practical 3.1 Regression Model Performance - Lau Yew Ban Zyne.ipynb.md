# Practical 3.1 Regression Model Performance - Lau Yew Ban Zyne.ipynb
**Module:** machine_learning
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