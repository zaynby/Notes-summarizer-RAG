# Lecture 3 - Neural Networks II _Apr2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Here’s a structured summary of the provided Deep Learning lecture content:

---

### **Generalization**  
**Definition**: Model’s ability to learn underlying patterns in data to make accurate predictions on unseen data.  
**Formula**: —  
**Example**: A model trained on diverse image datasets generalizes well to new, unseen images of the same class.  

---

### **Optimization**  
**Definition**: Process of minimizing error on training data by adjusting model parameters to improve performance.  
**Formula**: —  
**Example**: Using gradient descent to reduce the loss function’s value during training.  

---

### **Underfitting**  
**Definition**: Occurs when a model is too simple to capture patterns in the training data, leading to high training and test errors.  
**Formula**: —  
**Example**: A linear regression model applied to nonlinear data (e.g., predicting curved relationships with a straight line).  

---

### **Overfitting**  
**Definition**: Occurs when a model is too complex and memorizes training data, including noise, leading to poor performance on new data.  
**Formula**: —  
**Example**: A neural network with excessive layers memorizing pixel-level details in training images but failing on slightly altered test images.  

---

### **Bias-Variance Trade-off**  
**Definition**: Balancing model simplicity (low variance) and complexity (low bias) to minimize total error.  
**Formula**: Total Error = Bias² + Variance + Irreducible Error  
**Example**: A simple linear model has high bias (underfits), while a deep neural network has high variance (overfits).  

---

### **Bias**  
**Definition**: Error due to overly simplistic model assumptions, leading to underfitting.  
**Formula**: —  
**Example**: A model assuming all apples are red, ignoring variations in color.  

---

### **Variance**  
**Definition**: Error due to model sensitivity to training data fluctuations, leading to overfitting.  
**Formula**: —  
**Example**: A model that performs perfectly on training data but fails when given slightly different inputs.  

---

### **L1 Regularization (Lasso)**  
**Definition**: Adds penalty proportional to the absolute value of weights, encouraging sparsity.  
**Formula**: Loss + λ∑|w| (λ = regularization strength)  
**Example**: Many weights in a neural network become zero, simplifying the model.  

---

### **L2 Regularization (Ridge Regression)**  
**Definition**: Adds penalty proportional to the square of weights, encouraging small weights.  
**Formula**: Loss + λ∑w²  
**Example**: Weights in a model are kept small but non-zero, reducing overfitting.  

---

### **Dropout**  
**Definition**: Technique to randomly deactivate a fraction of neurons during training to prevent overfitting.  
**Formula**: —  
**Example**: Dropout rate of 0.5 disables 50% of neurons in a layer during each training iteration.  

---

### **Data Augmentation**  
**Definition**: Artificially expanding dataset diversity by applying transformations (e.g., rotations, flips).  
**Formula**: —  
**Example**: Flipping or cropping images to simulate new training examples.  

---

### **Model Capacity**  
**Definition**: Total number of learnable parameters (layers, units per layer) determining model complexity.  
**Formula**: —  
**Example**: A network with 10 layers and 256 units per layer has higher capacity than one with 3 layers and 64 units.  

---

### **Weight Regularization**  
**Definition**: Constraining weight values during training to prevent overfitting (via L1/L2 penalties).  
**Formula**: —  
**Example**: Applying L2 regularization to a dense layer in Keras using `kernel_regularizer`.  

---

### **Remedies for Overfitting**  
1. **More Training Data**: Improves generalization.  
2. **Reduce Network Size**: Fewer layers/units.  
3. **Regularization (L1/L2)**: Penalize large weights.  
4. **Dropout**: Randomly deactivate neurons.  
5. **Data Augmentation**: Increase data diversity.  

---

### **Remedies for Underfitting**  
1. **Increase Model Capacity**: Add layers/units.  
2. **Train Longer**: More epochs.  
3. **Reduce Regularization**: Loosen constraints.  

---

**[[Wikilinks]]**:  
- [[Generalization]] → [[Overfitting]], [[Underfitting]]  
- [[Bias-Variance Trade-off]] → [[Bias]], [[Variance]]  
- [[Regularization]] → [[L1 Regularization]], [[L2 Regularization]]  
- [[Model Capacity]] → [[Overfitting]], [[Underfitting]]  

This summary balances conciseness with thoroughness, linking core concepts for easy cross-reference.