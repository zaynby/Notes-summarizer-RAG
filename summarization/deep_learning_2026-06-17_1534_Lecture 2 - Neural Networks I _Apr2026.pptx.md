# Lecture 2 - Neural Networks I _Apr2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the lecture content on **Deep Learning**:

---

### **Deep Learning (DL)**  
**Definition**: A subfield of machine learning that uses multi-layered neural networks to learn hierarchical representations of data.  
**Formula**: N/A  
**Example**: MNIST handwritten digit classification (60k training images, 10k test images).  
**Link**: [[Machine Learning]], [[Neural Network]]

---

### **Neural Network (NN)**  
**Definition**: A computational model composed of layers of interconnected nodes (neurons) that process input data through weighted connections and activation functions.  
**Formula**:  
$$ \text{Output} = f\left(\sum (W \cdot X) + b\right) $$  
Where \( W \) = weights, \( X \) = input, \( b \) = bias, \( f \) = activation function.  
**Example**: Loan approval prediction (Input: credit score, age; Output: approve/reject).  
**Link**: [[Activation Function]], [[Forward Propagation]]

---

### **Activation Function**  
**Definition**: Introduces non-linearity to enable learning of complex patterns. Determines if a neuron "fires" based on input.  
**Formula**:  
- Sigmoid: \( \sigma(x) = \frac{1}{1 + e^{-x}} \)  
- ReLU: \( f(x) = \max(0, x) \)  
**Example**: Sigmoid used in binary classification (output probability between 0 and 1).  
**Link**: [[Neural Network]], [[Binary Classification]]

---

### **Forward Propagation**  
**Definition**: The process of passing input data through the network to compute predictions.  
**Formula**:  
$$ \hat{Y} = f(W \cdot X + b) $$  
Where \( \hat{Y} \) = predicted output.  
**Example**: Predicting loan approval ( \( \hat{Y} = 0.532 \) for a given input).  
**Link**: [[Backpropagation]], [[Loss Function]]

---

### **Backpropagation**  
**Definition**: Algorithm to update weights by propagating the error gradient backward through the network.  
**Formula**:  
$$ W_{\text{new}} = W_{\text{old}} - \eta \cdot \frac{\partial L}{\partial W} $$  
Where \( \eta \) = learning rate, \( L \) = loss.  
**Example**: Adjusting weights by +0.1 to reduce loss in a loan approval model.  
**Link**: [[Gradient Descent]], [[Loss Function]]

---

### **Loss Function**  
**Definition**: Quantifies the difference between predicted and actual values. Guides optimization.  
**Formula**:  
- Mean Squared Error (MSE): \( L = \frac{1}{n} \sum (Y - \hat{Y})^2 \)  
- Binary Crossentropy: \( L = -\frac{1}{n} \sum [Y \log(\hat{Y}) + (1-Y) \log(1-\hat{Y})] \)  
**Example**: Loss score = 0.4671 in loan approval prediction.  
**Link**: [[Optimizer]], [[Gradient Descent]]

---

### **Optimizer**  
**Definition**: Algorithm that adjusts model parameters (weights/biases) to minimize loss.  
**Formula**: N/A  
**Example**: Adam optimizer for binary classification (IMDB movie reviews).  
**Link**: [[Gradient Descent]], [[Keras]]

---

### **Keras**  
**Definition**: High-level API for building and training deep learning models.  
**Formula**: N/A  
**Example**:  
```python
model = Sequential([Dense(64, activation='relu', input_shape=(100,)), 
                    Dense(1, activation='sigmoid')]) 
model.compile(optimizer='adam', loss='binary_crossentropy')
```  
**Link**: [[TensorFlow]], [[Neural Network]]

---

### **Gradient Descent (GD)**  
**Definition**: Iterative optimization algorithm to find the minimum of a loss function.  
**Formula**:  
$$ W_{\text{new}} = W_{\text{old}} - \eta \cdot \nabla L $$  
**Example**: Learning rate too high causes divergence; too low causes slow progress.  
**Link**: [[Backpropagation]], [[Local Minima]]

---

### **Mini-Batch SGD**  
**Definition**: Variant of GD that uses random subsets (mini-batches) of data for gradient updates.  
**Formula**: N/A  
**Example**: Training on 32 samples per batch for IMDB sentiment analysis.  
**Link**: [[Gradient Descent]], [[Batch Size]]

---

### **Challenges in Gradient Descent**  
**Definition**: Issues like local minima, saddle points, vanishing/exploding gradients, and learning rate sensitivity.  
**Formula**: N/A  
**Example**: Vanishing gradients slow training in deep networks.  
**Link**: [[Gradient Descent]], [[Activation Function]]

---

### **Binary Classification**  
**Definition**: Task where the output is a binary label (0/1, positive/negative).  
**Formula**: N/A  
**Example**: Classifying movie reviews as positive (1) or negative (0) using IMDB dataset.  
**Link**: [[Loss Function]], [[Activation Function]]

---

### **Regression**  
**Definition**: Predicting continuous values (e.g., house prices).  
**Formula**:  
- Mean Absolute Error (MAE): \( \text{MAE} = \frac{1}{n} \sum |\hat{Y} - Y| \)  
**Example**: Predicting median house prices in California using normalized features.  
**Link**: [[Loss Function]], [[Feature Normalization]]

---

### **Feature Normalization**  
**Definition**: Scaling input features to a similar range (e.g., mean 0, std 1) to improve training.  
**Formula**:  
$$ X_{\text{normalized}} = \frac{X - \mu}{\sigma} $$  
**Example**: Normalizing median income and house age in housing price prediction.  
**Link**: [[Regression]], [[Deep Learning]]

---

### **K-Fold Validation**  
**Definition**: Technique to evaluate model performance by splitting data into k subsets.  
**Formula**: N/A  
**Example**: Using 5-fold validation for housing price prediction with limited data.  
**Link**: [[Regression]], [[Overfitting]]

---

This summary connects foundational concepts in deep learning, neural networks, and practical applications. Use [[Wikilinks]] to navigate related topics.