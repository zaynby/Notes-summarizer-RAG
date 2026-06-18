# Practical 1a - Linear Regression.ipynb
**Module:** machine_learning
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