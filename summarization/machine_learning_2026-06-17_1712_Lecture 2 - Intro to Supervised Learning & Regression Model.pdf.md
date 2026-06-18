# Lecture 2 - Intro to Supervised Learning & Regression Model.pdf
**Module:** machine_learning
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