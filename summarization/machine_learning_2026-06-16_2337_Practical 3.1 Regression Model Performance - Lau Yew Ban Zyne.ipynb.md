# Practical 3.1 Regression Model Performance - Lau Yew Ban Zyne.ipynb
**Module:** machine_learning
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