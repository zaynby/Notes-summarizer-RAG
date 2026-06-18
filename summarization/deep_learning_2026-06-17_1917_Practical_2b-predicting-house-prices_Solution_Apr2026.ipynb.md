# Practical_2b-predicting-house-prices_Solution_Apr2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Predicting House Prices  
**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

## **California Housing Dataset**  
**Definition**: A regression dataset containing median house prices and 8 features (e.g., longitude, latitude, median income) from the 1990 California census.  
**Formula**: N/A  
**Example**: Small version used in the practical with 480 training samples and 120 test samples.  
**[[Wikilink]]**: [[Data Normalization]], [[Regression]]  

---

## **Data Normalization (Z-Score Standardization)**  
**Definition**: Technique to scale features by subtracting the mean and dividing by the standard deviation, ensuring zero mean and unit variance.  
**Formula**:  
$$
\text{Normalized } x = \frac{x - \mu}{\sigma}
$$  
**Example**: Applied to both training and test data using `train_data.mean(axis=0)` and `train_data.std(axis=0)`.  
**[[Wikilink]]**: [[Data Preprocessing]], [[California Housing Dataset]]  

---

## **Neural Network (Regression)**  
**Definition**: A model with two hidden layers (64 units each, ReLU activation) and a linear output layer for predicting continuous house prices.  
**Formula**: N/A  
**Example**: Model built in Code Cell 19 with `keras.Sequential` and compiled with `mse` loss.  
**[[Wikilink]]**: [[Mean Squared Error (MSE)]], [[Overfitting]]  

---

## **Mean Squared Error (MSE)**  
**Definition**: Loss function measuring the average squared difference between predicted and actual values.  
**Formula**:  
$$
\text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_{\text{true}} - y_{\text{pred}})^2
$$  
**Example**: Used as the loss function in model compilation (Code Cell 19).  
**[[Wikilink]]**: [[Loss Functions]], [[Neural Network (Regression)]]  

---

## **Mean Absolute Error (MAE)**  
**Definition**: Metric measuring the average absolute difference between predicted and actual values.  
**Formula**:  
$$
\text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_{\text{true}} - y_{\text{pred}}|
$$  
**Example**: Monitored during training; 1 MAE unit ≈ \$100,000 house price error.  
**[[Wikilink]]**: [[Model Evaluation]], [[Neural Network (Regression)]]  

---

## **K-Fold Cross-Validation**  
**Definition**: Validation technique splitting data into *k* partitions, training on *k-1*, and validating on the remaining partition.  
**Formula**: N/A  
**Example**: 5-fold validation used to determine optimal epochs (Code Cell 27).  
**[[Wikilink]]**: [[Overfitting]], [[Model Training]]  

---

## **Batch Size**  
**Definition**: Number of samples processed before updating model weights.  
**Formula**: N/A  
**Example**: **Scenario A** increased batch size from 1 to 128 (Code Cell 40), resulting in smoother MAE curves but slower convergence.  
**[[Wikilink]]**: [[Learning Rate]], [[Model Training]]  

---

## **Learning Rate**  
**Definition**: Hyperparameter controlling the step size of weight updates during optimization.  
**Formula**: N/A (Adam optimizer uses adaptive rates with `beta_1` and `beta_2`).  
**Example**: **Scenario B** reduced learning rate from 0.001 to 0.0002 (Code Cell 46), slowing initial training but improving stability.  
**[[Wikilink]]**: [[Adam Optimizer]], [[Batch Size]]  

---

## **Overfitting**  
**Definition**: Phenomenon where the model performs well on training data but poorly on validation/test data.  
**Formula**: N/A  
**Example**: Observed in initial training (Code Cell 21) where validation MAE plateaued while training MAE decreased.  
**[[Wikilink]]**: [[K-Fold Cross-Validation]], [[Neural Network (Regression)]]  

---

## **Model Training**  
**Definition**: Process of optimizing model weights using training data and evaluating performance on validation data.  
**Formula**: N/A  
**Example**: Training for 50 epochs based on K-fold results (Code Cell 33) to balance overfitting and performance.  
**[[Wikilink]]**: [[Batch Size]], [[Learning Rate]]  

---

## **Key Observations**  
1. **Data Normalization**: Critical for stable training with heterogeneous features.  
2. **K-Fold Validation**: Identified optimal training duration (50 epochs) to mitigate overfitting.  
3. **Batch Size (Scenario A)**: Larger batches (128) reduced noise in MAE curves but required more epochs for convergence.  
4. **Learning Rate (Scenario B)**: Smaller learning rate (0.0002) improved training stability but slowed initial progress.  

---

## **[[Wikilinks]]**  
- [[California Housing Dataset]] → [[Data Normalization]], [[Regression]]  
- [[Neural Network (Regression)]] → [[Mean Squared Error (MSE)]], [[Overfitting]]  
- [[K-Fold Cross-Validation]] → [[Overfitting]], [[Model Training]]  
- [[Batch Size]] → [[Learning Rate]], [[Model Training]]  
- [[Learning Rate]] → [[Adam Optimizer]], [[Batch Size]]  
- [[Mean Absolute Error (MAE)]] → [[Model Evaluation]]  
- [[Overfitting]] → [[K-Fold Cross-Validation]], [[Neural Network (Regression)]]  

This summary connects practical implementation (e.g., data normalization, hyperparameter tuning) with theoretical concepts (e.g., overfitting, cross-validation) for a comprehensive understanding of regression modeling in deep learning.