# Week 1.1 - Universal Workflow of ML.pdf
**Module:** machine_learning
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