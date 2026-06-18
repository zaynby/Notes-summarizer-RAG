# Lecture 2 - Neural Networks I _Apr2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Here’s a structured summary of the key concepts from the provided deep learning lecture materials:

---

### **Neural Network (NN)**  
**Definition**: A computational model inspired by biological neural networks, consisting of interconnected layers of nodes (neurons) that process data.  
**Formula**: Output \( y = \sigma\left(\sum w_i x_i + b\right) \), where \( \sigma \) is the activation function, \( w_i \) are weights, \( x_i \) are inputs, and \( b \) is bias.  
**Example**: Image classification where input pixels are transformed through hidden layers to produce class probabilities.  
[[Link to Activation Function]], [[Link to Forward Propagation]]

---

### **Forward Propagation**  
**Definition**: The process of passing input data through the network to generate predictions.  
**Formula**: For a single neuron: \( y' = \sigma(Wx + b) \). For a network, this is applied layer-wise.  
**Example**: In the loan approval example (Slide 7), input features (credit score, age) are used to predict a binary output (approve/reject).  
[[Link to Backpropagation]], [[Link to Loss Function]]

---

### **Backpropagation**  
**Definition**: The method of computing gradients of the loss function with respect to weights by applying the chain rule, enabling weight updates.  
**Formula**: Gradient of loss \( \mathcal{L} \) w.r.t. weight \( w \): \( \frac{\partial \mathcal{L}}{\partial w} = \frac{\partial \mathcal{L}}{\partial y'} \cdot \frac{\partial y'}{\partial w} \).  
**Example**: Adjusting weights in the loan approval model to reduce prediction error (Slide 8).  
[[Link to Optimizer]], [[Link to Gradient Descent]]

---

### **Activation Function**  
**Definition**: Introduces non-linearity to enable learning of complex patterns.  
**Formula**:  
- **ReLU**: \( \sigma(x) = \max(0, x) \)  
- **Sigmoid**: \( \sigma(x) = \frac{1}{1 + e^{-x}} \)  
**Example**: ReLU in hidden layers for housing price prediction (Slide 29), Sigmoid for binary classification (IMDB reviews).  
[[Link to Neural Network]], [[Link to Forward Propagation]]

---

### **Optimizer**  
**Definition**: Algorithm that updates weights to minimize the loss function.  
**Formula**: Weight update rule for **Adam**: \( w_{t+1} = w_t - \eta \cdot \hat{g} \), where \( \eta \) is learning rate and \( \hat{g} \) is estimated gradient.  
**Example**: Adam optimizer used in IMDB sentiment analysis (Slide 21) and housing price prediction (Slide 27).  
[[Link to Gradient Descent]], [[Link to Loss Function]]

---

### **Loss Function**  
**Definition**: Quantifies the difference between predicted and actual values.  
**Formula**:  
- **Mean Squared Error (MSE)**: \( \mathcal{L} = \frac{1}{n}\sum (y - y')^2 \) (regression)  
- **Binary Cross-Entropy**: \( \mathcal{L} = -\frac{1}{n}\sum [y \log(y') + (1-y)\log(1-y')] \) (classification)  
**Example**: MSE for Boston housing prices (Slide 31), binary cross-entropy for IMDB reviews (Slide 22).  
[[Link to Optimizer]], [[Link to Backpropagation]]

---

### **Keras**  
**Definition**: A high-level API for building and training deep learning models, typically running on TensorFlow.  
**Key Features**:  
- Sequential API for linear stacks of layers.  
- Functional API for complex architectures.  
**Example**: Building a dense network for movie review classification (Slide 23).  
[[Link to Neural Network]], [[Link to Optimizer]]

---

### **Overfitting**  
**Definition**: When a model performs well on training data but poorly on unseen data.  
**Mitigation**: Monitor validation loss (Slide 26), use regularization, or reduce network complexity.  
**Example**: Neural networks overfitting on training data in Practical 2a (Slide 26).  
[[Link to Validation]], [[Link to K-Fold Validation]]

---

### **K-Fold Validation**  
**Definition**: A technique where data is split into \( k \) subsets, with \( k-1 \) used for training and 1 for validation, repeated \( k \) times.  
**Use Case**: Evaluating regression models with limited data (Boston housing, Slide 30).  
[[Link to Overfitting]], [[Link to Dataset]]

---

### **Dataset Preprocessing**  
**Definition**: Transforming raw data into a format suitable for neural networks (e.g., normalization, one-hot encoding).  
**Example**:  
- IMDB reviews: Converted to vectors via one-hot encoding (Slide 22).  
- Boston housing: Feature-wise normalization (Slide 28).  
[[Link to Tensor]], [[Link to Neural Network]]

---

### **Tensor**  
**Definition**: A multidimensional array used to represent data in deep learning (e.g., images as 3D tensors).  
**Example**: Input tensors for movie reviews (Slide 22) and housing features (Slide 28).  
[[Link to Dataset Preprocessing]], [[Link to Keras]]

---

This summary connects core concepts in deep learning, emphasizing their roles in building, training, and evaluating neural networks. For deeper dives, refer to the linked topics or the provided [Further Reading](https://medium.com/deep-learning-demystified/loss-functions-explained-3098e8ff2b27).