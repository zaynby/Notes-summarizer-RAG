# Practical_3-Overfitting-and-Underfitting_Solution_Apr2026.ipynb
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

### **Weight Regularization (L1/L2)**  
**Definition**: Adding penalties to the loss function to constrain weight values, preventing overly complex models.  
**Formula**:  
- **L2 Regularization**: Loss += `0.002 * (sum of squared weights)`  
- **L1 Regularization**: Loss += `0.001 * (sum of absolute weights)`  
**Example**: `l2_model` used `kernel_regularizer=l2(0.002)` in dense layers, improving validation loss stability.  
**[[Wikilink]]**: [[Overfitting]], [[Dropout]]  

---

### **Dropout**  
**Definition**: A regularization technique that randomly deactivates a fraction of neurons during training to prevent overfitting.  
**Formula**: N/A  
**Example**: Adding `layers.Dropout(0.5)` after dense layers in `dpt_model` reduced validation loss from 0.98 to 0.52 over 20 epochs.  
**[[Wikilink]]**: [[Overfitting], [Weight Regularization]]  

---

### **Validation Loss**  
**Definition**: The loss computed on the validation set during training, used to monitor overfitting.  
**Formula**: N/A  
**Example**: Comparing `original_val_loss` (red) vs. `l2_model_val_loss` (green) showed regularization reduced validation loss divergence.  
**[[Wikilink]]**: [[Overfitting], [Model Evaluation]]  

---

### **Model Generalization**  
**Definition**: A model’s ability to perform well on unseen data by learning robust patterns.  
**Formula**: N/A  
**Example**: The combined dropout and L2 regularized model (`s_model`) achieved a smaller training-validation loss gap (42% vs. 98% in the original model).  
**[[Wikilink]]**: [[Overfitting], [Underfitting]]  

---

### **Adam Optimizer**  
**Definition**: An adaptive learning rate optimizer combining momentum and RMSProp for efficient weight updates.  
**Formula**: N/A  
**Example**: Used with `learning_rate=1e-3` in `s_model` for stable training.  
**[[Wikilink]]**: [[Optimization], [Learning Rate]]  

---

### **Key Outcomes**  
1. **Overfitting Mitigation**: Reducing capacity, adding dropout (e.g., 0.5 rate), and L2 regularization (0.002) improved validation performance.  
2. **Trade-offs**: Smaller models underfit, while overly large models overfit rapidly.  
3. **Regularization Synergy**: Combining dropout and L2 regularization balanced training and validation loss.  

## **[[Wikilinks]]**  
- [[Overfitting]] → [[Dropout]], [[Weight Regularization]], [[Reducing Network Capacity]]  
- [[Underfitting]] → [[Model Capacity]]  
- [[Weight Regularization]] → [[L1 Regularization]], [[L2 Regularization]]  
- [[Dropout]] → [[Model Generalization]]  
- [[Model Generalization]] → [[Validation Loss]]