# Practical_2b-predicting-house-prices_Solution_Apr2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Predicting House Prices (California Housing Dataset)  
**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

### **California Housing Price Dataset**  
**Definition**: A regression dataset containing median house prices and 8 features (e.g., longitude, latitude, median income) for districts in California.  
**Formula**: N/A  
**Example**: Small version used with 480 training samples and 120 test samples (`train_data.shape = (480, 8)`).  
**[[Wikilink]]**: [[Data Preprocessing]]  

---

### **Data Preprocessing**  
**Definition**: Standardization of input features to have zero mean and unit variance, and scaling of target values for stable training.  
**Formula**:  
- Standardization: \( x_{\text{normalized}} = \frac{x - \mu}{\sigma} \)  
- Target scaling: \( y_{\text{scaled}} = \frac{y}{100,000} \)  
**Example**:  
- Features normalized using `train_data.mean(axis=0)` and `train_data.std(axis=0)`.  
- Targets scaled by dividing by 100,000 (e.g., \$60,000 → 0.6).  
**[[Wikilink]]**: [[Neural Network Architecture]]  

---

### **Neural Network Architecture**  
**Definition**: A Sequential model with two hidden layers (64 units each, ReLU activation) and a linear output layer for regression.  
**Formula**: N/A  
**Example**:  
```python  
model = keras.Sequential([  
    Input(shape=(8,)),  
    layers.Dense(64, activation="relu"),  
    layers.Dense(64, activation="relu"),  
    layers.Dense(1)  
])  
```  
**[[Wikilink]]**: [[Mean Squared Error (MSE)]]  

---

### **Mean Squared Error (MSE)**  
**Definition**: Loss function measuring the average squared difference between predicted and true values.  
**Formula**:  
\[ \text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2 \]  
**Example**: Used in model compilation (`loss='mse'`).  
**[[Wikilink]]**: [[Mean Absolute Error (MAE)]]  

---

### **Mean Absolute Error (MAE)**  
**Definition**: Metric measuring the average absolute difference between predicted and true values.  
**Formula**:  
\[ \text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i| \]  
**Example**: Monitored during training (`metrics=['mae']`).  
**[[Wikilink]]**: [[K-Fold Cross-Validation]]  

---

### **K-Fold Cross-Validation**  
**Definition**: Validation technique splitting data into *k* partitions, training on *k-1* folds, and validating on the remaining fold.  
**Formula**: N/A  
**Example**: 5-fold validation (`k=5`) to determine optimal epochs (50 epochs chosen).  
**[[Wikilink]]**: [[Overfitting]]  

---

### **Overfitting**  
**Definition**: Phenomenon where the model performs well on training data but poorly on validation/test data.  
**Formula**: N/A  
**Example**: Training MAE decreases rapidly, but validation MAE plateaus after 50 epochs.  
**[[Wikilink]]**: [[Batch Size]], [[Learning Rate]]  

---

### **Batch Size**  
**Definition**: Number of samples processed before updating model weights.  
**Formula**: N/A  
**Example**:  
- **Scenario A**: Batch size increased from 1 to 128.  
- **Observation**: Smoother MAE curves but slower convergence.  
**[[Wikilink]]**: [[Learning Rate]]  

---

### **Learning Rate**  
**Definition**: Hyperparameter controlling the step size of weight updates during optimization.  
**Formula**: N/A  
**Example**:  
- **Scenario B**: Learning rate reduced from 0.001 (Adam default) to 0.0002.  
- **Observation**: Slower initial training but steadier convergence.  
**[[Wikilink]]**: [[Adam Optimizer]]  

---

### **Adam Optimizer**  
**Definition**: Adaptive learning rate optimizer combining momentum and RMSProp.  
**Formula**: N/A  
**Example**: Compiled with `optimizer='adam'` (default learning rate 0.001).  
**[[Wikilink]]**: [[Neural Network Architecture]]  

---

## **Key Observations**  
1. **Data Preprocessing**: Normalization and target scaling improved training stability.  
2. **K-Fold Validation**: Identified 50 epochs as optimal to prevent overfitting.  
3. **Batch Size (Scenario A)**: Larger batches (128) reduced gradient noise but slowed convergence.  
4. **Learning Rate (Scenario B)**: Reduced learning rate (0.0002) stabilized training but required more epochs.  

## **[[Wikilinks]]**  
- [[California Housing Price Dataset]] → [[Data Preprocessing]]  
- [[Neural Network Architecture]] → [[Mean Squared Error (MSE)]], [[Adam Optimizer]]  
- [[Overfitting]] → [[K-Fold Cross-Validation]], [[Batch Size]]  
- [[Batch Size]] → [[Learning Rate]]  
- [[Learning Rate]] → [[Adam Optimizer]]