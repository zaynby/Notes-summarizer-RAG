# Practical_2b-predicting-house-prices_Apr2026_[student_name].ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Predicting House Prices (Regression)  
**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

## **Regression**  
**Definition**: A type of supervised learning task where the goal is to predict continuous numerical values (e.g., house prices).  
**Formula**: N/A  
**Example**: Predicting median house prices in California using census data.  
**[[Wikilink]]**: [[Neural Network]], [[Mean Squared Error (MSE)]]  

---

## **Neural Network (for Regression)**  
**Definition**: A layered architecture with input, hidden, and output layers designed to learn complex patterns in data for regression tasks.  
**Formula**: Output = $ f(Wx + b) $, where $ f $ is the activation function.  
**Example**: A network with two hidden layers (64 ReLU units each) and a linear output layer (Code Cell 19).  
**[[Wikilink]]**: [[Regression], [Data Normalization]]  

---

## **Data Normalization (Z-Score Standardization)**  
**Definition**: Scaling features to have zero mean and unit variance using $ \frac{x - \mu}{\sigma} $.  
**Formula**: $ \text{Normalized Value} = \frac{x - \text{mean}}{\text{std}} $  
**Example**: Normalizing the California Housing dataset (Code Cell 13).  
**[[Wikilink]]**: [[Neural Network], [Regression]]  

---

## **Mean Squared Error (MSE)**  
**Definition**: Loss function measuring the average squared difference between predicted and true values.  
**Formula**: $ \text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_{\text{true}} - y_{\text{pred}})^2 $  
**Example**: Used as the loss function in the regression model (Code Cell 19).  
**[[Wikilink]]**: [[Mean Absolute Error (MAE)]], [[Regression]]  

---

## **Mean Absolute Error (MAE)**  
**Definition**: Metric measuring the average absolute difference between predicted and true values.  
**Formula**: $ \text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_{\text{true}} - y_{\text{pred}}| $  
**Example**: Monitored during training (Code Cell 21) and reported as ~0.05 (scaled targets).  
**[[Wikilink]]**: [[Mean Squared Error (MSE)]], [[Regression]]  

---

## **K-Fold Cross-Validation**  
**Definition**: Validation technique where data is split into K partitions, and the model is trained K times with each partition as validation once.  
**Formula**: N/A  
**Example**: 5-fold validation to determine optimal epochs (Code Cell 27).  
**[[Wikilink]]**: [[Overfitting], [Validation Data]]  

---

## **Overfitting**  
**Definition**: When a model performs well on training data but poorly on validation/test data due to memorizing noise.  
**Formula**: N/A  
**Example**: Training MAE decreases while validation MAE plateaus or increases (Code Cell 23).  
**[[Wikilink]]**: [[K-Fold Cross-Validation], [Data Normalization]]  

---

## **Batch Size**  
**Definition**: Number of samples processed before updating model weights during training.  
**Formula**: N/A  
**Example**: Increasing batch size from 1 to 128 (Scenario A, Code Cell 40).  
**[[Wikilink]]**: [[Learning Rate], [Optimizer]]  

---

## **Learning Rate**  
**Definition**: Hyperparameter controlling the step size of weight updates during optimization.  
**Formula**: N/A  
**Example**: Reducing Adam optimizer’s learning rate from 0.001 to 0.0005 (Scenario B, Code Cell 46).  
**[[Wikilink]]**: [[Batch Size], [[Adam Optimizer]]  

---

## **Adam Optimizer**  
**Definition**: Adaptive learning rate optimizer combining momentum and RMSProp for efficient weight updates.  
**Formula**: N/A (uses adaptive learning rates with parameters $ \beta_1 $ and $ \beta_2 $).  
**Example**: Default learning rate of 0.001 (Code Cell 19).  
**[[Wikilink]]**: [[Learning Rate], [Mean Squared Error (MSE)]]  

---

## **Key Observations**  
1. **Data Scaling**: Normalizing features and targets improved training stability (Code Cell 13, 17).  
2. **Overfitting**: The model quickly overfit with small batch sizes (batch=1) but showed better generalization with batch=128 (Scenario A).  
3. **Learning Rate Impact**: A lower learning rate (0.0005) slowed convergence but reduced validation MAE compared to the default (Scenario B).  
4. **K-Fold Validation**: Average validation MAE stabilized after 50 epochs, guiding early stopping (Code Cell 31).  

---

## **[[Wikilinks]]**  
- [[Regression]] → [[Neural Network]], [[Mean Squared Error (MSE)]]  
- [[Neural Network]] → [[Data Normalization], [K-Fold Cross-Validation]]  
- [[K-Fold Cross-Validation]] → [[Overfitting], [Validation Data]]  
- [[Batch Size]] → [[Learning Rate], [Adam Optimizer]]  
- [[Learning Rate]] → [[Batch Size], [[Adam Optimizer]]  
- [[Mean Squared Error (MSE)]] → [[Mean Absolute Error (MAE)]], [[Regression]]  
- [[Overfitting]] → [[K-Fold Cross-Validation], [Data Normalization]]  

This summary integrates regression concepts, data preprocessing, model training, and hyperparameter tuning for predicting continuous targets like house prices.