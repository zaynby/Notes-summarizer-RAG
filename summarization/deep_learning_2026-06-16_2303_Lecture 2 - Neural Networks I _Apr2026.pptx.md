# Lecture 2 - Neural Networks I _Apr2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the provided Deep Learning content:

---

## **Deep Learning Core Concepts**

### **1. Neural Network Anatomy**
- **Term**: Input, Hidden Layers, Output  
  - **Definition**:  
    - **Input Layer**: Receives raw data (e.g., pixel values, word embeddings).  
    - **Hidden Layers**: Intermediate layers between input and output that learn hierarchical representations.  
    - **Output Layer**: Produces final predictions (e.g., class probabilities, regression values).  
  - **Example**: In the MNIST digit classification, the input layer processes 28x28 pixel images, hidden layers extract features like edges/circles, and the output layer outputs 10 class probabilities.

---

### **2. Core Building Blocks**
- **Term**: Neurons, Weights, Bias  
  - **Definition**:  
    - **Neuron**: Basic computational unit that applies weights, adds bias, and uses an activation function.  
    - **Weights**: Parameters that scale input signals (learned during training).  
    - **Bias**: Scalar added to the neuron’s output to shift its activation.  
  - **Formula**: Output = Activation(Σ(Inputs × Weights) + Bias)  
  - **Example**: In loan approval prediction, weights might assign higher importance to "Income" than "Age".

---

### **3. Forward Propagation & Loss**
- **Term**: Forward Propagation, Loss Function  
  - **Definition**:  
    - **Forward Propagation**: Process of computing predictions from inputs.  
    - **Loss Function**: Quantifies the difference between predictions (Y’) and true targets (Y).  
  - **Formula**: Loss = Y − Y’ (e.g., Mean Squared Error: \( \frac{1}{n}\sum_{i=1}^{n}(Y_i - Y'_i)^2 \))  
  - **Example**: In the credit loan example, a loss score of 0.4671 indicates the model’s prediction error.

---

### **4. Backpropagation**
- **Term**: Backpropagation  
  - **Definition**: Algorithm to update weights by propagating gradients backward through the network.  
  - **Formula**: \( W_{\text{new}} = W_{\text{old}} - \eta \frac{\partial \text{Loss}}{\partial W} \) (η = learning rate)  
  - **Example**: If weights increase by 0.1 during backpropagation, the model reduces its loss.

---

### **5. Activation Functions**
- **Term**: Activation Function (e.g., Sigmoid, ReLU)  
  - **Definition**: Introduces non-linearity to enable learning complex patterns.  
  - **Formula**:  
    - **Sigmoid**: \( \sigma(x) = \frac{1}{1 + e^{-x}} \)  
    - **ReLU**: \( f(x) = \max(0, x) \)  
  - **Example**: A sigmoid activation in the output layer for binary classification (e.g., loan approve/reject).

---

### **6. Gradient Descent**
- **Term**: Gradient Descent, Mini-Batch SGD  
  - **Definition**: Optimization method to minimize loss by adjusting weights.  
  - **Challenges**:  
    - Local minima, saddle points, vanishing/exploding gradients.  
  - **Formula**: Weight update as in backpropagation.  
  - **Example**: Mini-batch SGD processes subsets of data (e.g., 32 samples at a time) for efficient training.

---

### **7. Keras Framework**
- **Term**: Keras, Sequential API, Functional API  
  - **Definition**:  
    - **Keras**: High-level API for building DL models (default backend: TensorFlow).  
    - **Sequential**: Linear stack of layers (e.g., `model.add(Dense(64, activation='relu'))`).  
    - **Functional API**: Supports complex architectures (e.g., multi-input models).  
  - **Compilation Parameters**:  
    - **Optimizer**: Adam, SGD  
    - **Loss**: `binary_crossentropy`, `mse`  
    - **Metrics**: Accuracy, MAE  
  - **Example**: Compiling a model: `model.compile(optimizer='adam', loss='binary_crossentropy')`.

---

### **8. Training Process**
- **Term**: Fit Method, Epochs, Batch Size  
  - **Definition**:  
    - **Fit Method**: Trains the model using `model.fit()`.  
    - **Epochs**: Number of passes through the entire dataset.  
    - **Batch Size**: Number of samples per forward/backward pass.  
  - **Example**: Training for 10 epochs with a batch size of 32.

---

### **9. Practical Applications**
#### **Binary Classification (IMDB Dataset)**
- **Task**: Predict positive/negative movie reviews.  
- **Steps**:  
  1. Text preprocessing (one-hot encoding).  
  2. Model: Dense layers with ReLU and a final Sigmoid layer.  
  3. Optimizer: Adam.  
  4. Metric: Accuracy.  

#### **Regression (Housing Prices)**
- **Task**: Predict median house prices.  
- **Steps**:  
  1. Feature normalization (mean=0, std=1).  
  2. Model: Dense layers with ReLU.  
  3. Loss: Mean Squared Error (MSE).  
  4. Validation: K-fold cross-validation (e.g., 5-fold).  

---

### **10. Evaluation Challenges**
- **Term**: Overfitting, Underfitting, K-Fold Validation  
  - **Definition**:  
    - **Overfitting**: Model memorizes training data but fails on new data.  
    - **Underfitting**: Model is too simple to capture patterns.  
    - **K-Fold Validation**: Splits data into K subsets for robust evaluation.  
  - **Example**: Using 5-fold validation on a small housing dataset (480 training samples).  

---

## **Key Equations Recap**
1. **Sigmoid Activation**: \( \sigma(x) = \frac{1}{1 + e^{-x}} \)  
2. **Weight Update**: \( W_{\text{new}} = W_{\text{old}} - \eta \frac{\partial \text{Loss}}{\partial W} \)  
3. **Mean Squared Error (MSE)**: \( \frac{1}{n}\sum_{i=1}^{n}(Y_i - Y'_i)^2 \)  

---

## **Linked Concepts**
- [[Neural Network]]  
- [[Activation Function]]  
- [[Gradient Descent]]  
- [[Keras]]  
- [[Overfitting]]  
- [[K-Fold Cross Validation]]  

This summary integrates foundational concepts, practical workflows, and challenges in deep learning, aligned with the provided lecture materials.