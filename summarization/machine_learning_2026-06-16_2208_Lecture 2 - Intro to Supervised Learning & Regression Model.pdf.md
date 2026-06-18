# Lecture 2 - Intro to Supervised Learning & Regression Model.pdf
**Module:** machine_learning
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