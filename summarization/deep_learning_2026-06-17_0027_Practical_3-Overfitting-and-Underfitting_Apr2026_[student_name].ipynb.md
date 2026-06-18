# Practical_3-Overfitting-and-Underfitting_Apr2026_[student_name].ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Preventing Overfitting in Neural Networks  
**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

### **Overfitting**  
**Definition**: A phenomenon where a model learns training data too well, including noise, leading to poor performance on validation/test data.  
**Formula**: N/A  
**Example**: The "bigger_model" (512 units) achieved near-zero training loss but validation loss increased sharply (e.g., from 0.30 to 0.98 over 20 epochs).  
**[[Wikilink]]**: [[Underfitting]], [[Weight Regularization]], [[Dropout]]  

---

### **Underfitting**  
**Definition**: A model is too simple to capture underlying patterns in the data, resulting in poor performance on both training and validation data.  
**Formula**: N/A  
**Example**: The "smaller_model" (4 units) showed slower convergence and higher validation loss compared to the original model.  
**[[Wikilink]]**: [[Overfitting]], [[Model Capacity]]  

---

### **Reducing Network Capacity**  
**Definition**: Decreasing the number of layers or units in a neural network to reduce overfitting.  
**Formula**: N/A  
**Example**: Replacing the original 16-unit layers with 4-unit layers in `smaller_model` delayed overfitting but degraded performance.  
**[[Wikilink]]**: [[Overfitting]], [[Model Capacity]]  

---

### **Weight Regularization (L2)**  
**Definition**: Adds a penalty to the loss function to constrain weight values, preventing overly complex models.  
**Formula**: Loss += `0.002 * (sum of squared weights)`  
**Example**: `l2_model` used `kernel_regularizer=l2(0.002)` in dense layers, improving validation loss stability.  
**[[Wikilink]]**: [[Overfitting]], [[Dropout]]  

---

### **Dropout**  
**Definition**: A regularization technique that randomly deactivates a fraction of neurons during training to prevent overfitting.  
**Formula**: N/A  
**Example**: Adding `Dropout(0.5)` after dense layers in `dpt_model` reduced validation loss from 0.98 to 0.52 over 20 epochs.  
**[[Wikilink]]**: [[Overfitting], [Weight Regularization]]  

---

### **Validation Loss**  
**Definition**: The loss computed on the validation set during training, used to monitor overfitting.  
**Formula**: N/A  
**Example**: Comparing `original_val_loss` (red) vs. `l2_model_val_loss` (green) showed regularization reduced validation loss divergence.  
**[[Wikilink]]**: [[Overfitting], [Model Evaluation]]  

---

### **Adam Optimizer**  
**Definition**: Adaptive learning rate optimizer combining momentum and RMSProp for efficient weight updates.  
**Formula**: N/A (uses adaptive learning rates with parameters `beta_1` and `beta_2`).  
**Example**: Compiled with `learning_rate=1e-3` in the custom model (`model_hist`).  
**[[Wikilink]]**: [[Learning Rate]]  

---

### **Binary Crossentropy Loss**  
**Definition**: Loss function for binary classification problems, measuring the difference between predicted probabilities and true labels.  
**Formula**:  
$$
\text{Loss} = -\frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]
$$  
**Example**: Used in model compilation (Code Cell 41) for IMDB review classification.  
**[[Wikilink]]**: [[Loss Functions]]  

---

### **Batch Size**  
**Definition**: Number of samples processed before updating model weights during training.  
**Formula**: N/A  
**Example**: Training with `batch_size=512` in all models (Code Cells 12, 13, 19, 41).  
**[[Wikilink]]**: [[Learning Rate]]  

---

### **Model Generalization**  
**Definition**: A model’s ability to perform well on unseen data by learning robust patterns.  
**Formula**: N/A  
**Example**: The combined dropout and L2 regularized model (`model_hist`) achieved a smaller training-validation loss gap.  
**[[Wikilink]]**: [[Overfitting], [Underfitting]]  

---

### **Key Observations**  
1. **Overfitting Mitigation**:  
   - Reducing capacity (smaller_model) delayed overfitting but degraded performance.  
   - L2 regularization (0.002) and dropout (0.5) improved validation stability.  
2. **Model Capacity Trade-offs**:  
   - Larger models (bigger_model) overfit rapidly (validation loss spiked after 1 epoch).  
   - Smaller models underfit, struggling to capture patterns.  
3. **Regularization Synergy**:  
   - Combining dropout and L2 regularization balanced training and validation loss.  

---

## **[[Wikilinks]]**  
- [[Overfitting]] → [[Dropout]], [[Weight Regularization]], [[Reducing Network Capacity]]  
- [[Underfitting]] → [[Model Capacity]]  
- [[Weight Regularization]] → [[L2 Regularization]]  
- [[Dropout]] → [[Model Generalization]]  
- [[Model Generalization]] → [[Validation Loss]]  
- [[Adam Optimizer]] → [[Learning Rate]]  
- [[Batch Size]] → [[Learning Rate]]  
- [[Binary Crossentropy Loss]] → [[Loss Functions]]