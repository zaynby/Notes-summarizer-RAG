# Lecture 2 - Neural Networks I _Apr2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

```markdown
## Neural Networks Fundamentals

### Term -> Definition -> Formula -> Example

#### 1. Input, Hidden Layers, Output
**Definition**: These are the key components of a neural network.
- **Input Layer**: Receives raw data.
- **Hidden Layers**: Process and transform data through layers of neurons.
- **Output Layer**: Produces final predictions.

**Example**: 
- Input: Features like age, salary, education level.
- Hidden Layers: Stacks of dense layers with ReLU activations.
- Output: Prediction (e.g., loan approval).

#### 2. Neurons
**Definition**: Basic building blocks that process inputs and produce outputs through weighted connections.
- **Formula**: \( y = f(w_1x_1 + w_2x_2 + b) \)
  - Where \( x_i \) are input features, \( w_i \) are weights, \( b \) is bias, and \( f \) is the activation function.

**Example**: 
- Neuron with input \( [x_1, x_2] \), weight vector \( [w_1, w_2] \), and bias \( b = 0.5 \). If \( f(x) = \text{ReLU}(x) \):
  - For input \( [1, 2] \): \( y = \max(0, (1*1 + 2*2 + 0.5)) = 5.5 \).

#### 3. Weight, Bias
**Definition**: Parameters that influence the output of a neuron.
- **Formula**: 
  - **Weight**: Adjusted during training to minimize error.
  - **Bias**: Shifts the activation function.

**Example**: 
- Initial weights \( w = [0.5, -1] \), bias \( b = 2 \).
- For input \( x = [3, 4] \):
  - Output: \( y = f(0.5*3 + (-1)*4 + 2) = f(-0.5) \).

#### 4. Activation Function (Threshold Function)
**Definition**: Introduces non-linearity to the network.
- **Formula**: 
  - **ReLU**: \( f(x) = \max(0, x) \).
  - **Sigmoid**: \( f(x) = \frac{1}{1 + e^{-x}} \).

**Example**: 
- For input \( x = 2 \):
  - ReLU: \( y = \max(0, 2) = 2 \).
  - Sigmoid: \( y = \frac{1}{1 + e^{-2}} \approx 0.88 \).

#### 5. Forward Propagation, Backpropagation
**Definition**: 
- **Forward Propagation**: Passes data through the network to produce an output.
- **Backpropagation**: Adjusts weights based on error.

**Example**: 
- For a simple model with input \( x = [1, 2] \), hidden layer ReLU activation, and output Sigmoid:
  - Forward: Predicted output \( y' = f(w_1x_1 + w_2x_2 + b) \).
  - Backward: Adjust weights based on error \( E = Y - Y' \).

#### 6. Loss Functions
**Definition**: Measures the difference between predicted and actual values.
- **Formula**: 
  - Mean Squared Error (MSE): \( L(y, y') = \frac{1}{n} \sum_{i=1}^{n} (y_i - y'_i)^2 \).
  - Binary Cross Entropy: \( L(y, y') = -[y \log(y') + (1-y) \log(1-y')] \).

**Example**: 
- Predicted output \( y' = 0.4671 \), true target \( Y = 1.0 \):
  - MSE: \( L = \frac{1}{2} (1.0 - 0.4671)^2 \approx 0.3085 \).
  - Binary Cross Entropy: \( L = -(1.0 \log(0.4671) + (1-1.0) \log(1-0.4671)) \approx 0.994 \).

#### 7. Optimizers
**Definition**: Algorithms that update weights to minimize loss.
- **Formula**: 
  - Adam: \( w_{t+1} = w_t - \alpha \frac{\hat{g}_t}{\sqrt{\hat{v}_t} + \epsilon} \)
    - Where \( \hat{g}_t \) is the estimated gradient, \( \hat{v}_t \) is the moving average of squared gradients.

**Example**: 
- Initial weights \( w = [0.5] \), learning rate \( \alpha = 0.1 \).
- Gradient \( g_t = -2(y - y')x \):
  - Updated weight: \( w_{t+1} = 0.5 - 0.1 \times (-2(1 - 0.4671) \times 1) = 0.6934 \).

#### 8. Preprocessing
**Definition**: Transforming raw data into tensors suitable for neural networks.
- **Formula**: 
  - One-hot encoding: \( x_i = 1 \text{ if } i = j, 0 \text{ otherwise} \).
  - Normalization: \( x' = \frac{x - \mu}{\sigma} \).

**Example**: 
- Input data: "positive", "negative".
- One-hot encoded: [1, 0], [0, 1].
- Normalized feature values: subtract mean and divide by standard deviation.

#### 9. Keras
**Definition**: High-level API for building deep learning models.
- **Key Features**: 
  - Easy to use with multiple backends (TensorFlow, Theano).
  - Supports various network architectures.

**Example**: 
- Define a model using `Sequential` or `Functional API`.
- Compile the model: specify loss function, optimizer, and metrics.
- Train the model: fit() method on training data.
- Evaluate the model: predict() method on testing data.

#### 10. Challenges in Gradient Descent
**Definition**: Issues that can hinder effective optimization.
- **Local Minima**: Algorithm gets stuck at a local minimum.
- **Saddle Points**: Flat regions where gradients are small.
- **Vanishing/Exploding Gradients**: Slow or unstable learning.

**Example**: 
- Local minima: Stuck at \( x = 0 \) if gradient is zero.
- Saddle point: Gradient is small, but not zero.
- Vanishing gradient: \( e^{-10} \approx 4.54 \times 10^{-5} \).

#### 11. Overfitting and Underfitting
**Definition**: 
- **Overfitting**: Model performs well on training data but poorly on unseen data.
- **Underfitting**: Model is too simple to capture underlying patterns.

**Example**: 
- Monitor validation loss: overfitting if training loss decreases while validation loss increases.
- Use techniques like dropout, early stopping, and regularization to prevent overfitting.

#### 12. Practical Applications
**Definition**: Real-world examples of neural network usage.
- **Loan Approval Prediction**: Binary classification using ReLU activations and Sigmoid output.
- **House Price Prediction**: Regression using Mean Squared Error (MSE) loss function.

**Example**: 
- Loan approval model: Predicts loan approval based on features like age, salary, education level.
- House price prediction model: Uses 13 features to predict median home prices in Boston suburbs.
```

This structured breakdown covers the fundamental concepts and practical applications of neural networks, providing clear definitions, formulas, examples, and key steps for implementation.