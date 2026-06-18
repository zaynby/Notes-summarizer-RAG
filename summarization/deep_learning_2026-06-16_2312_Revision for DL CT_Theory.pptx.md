# Revision for DL CT_Theory.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Comprehensive Summary of Deep Learning Concepts

## **AI (Artificial Intelligence)**
- **Definition**: Field of creating systems that automate intellectual tasks normally performed by humans.
- **Example**: Autonomous vehicles making decisions based on sensor data.

## **Machine Learning (ML)**
- **Definition**: Subset of AI focused on learning representations from data to predict outputs from inputs.
- **Components**:
  - **Inputs**: Data points (e.g., images).
  - **Labels**: Expected outputs (e.g., "cat" or "dog").
  - **Loss Function**: Measures algorithm performance (e.g., Mean Squared Error).
- **Example**: Classifying emails as spam or not spam.

## **Deep Learning (DL)**
- **Definition**: Subset of ML using layered (hierarchical) representations to learn complex patterns.
- **Example**: Image recognition systems identifying objects in photos.

## **Neural Network**
- **Definition**: Computational model parameterized by weights, consisting of layers of neurons.
- **Components**:
  - **Layers**: Input, hidden, output.
  - **Activation Functions**: Introduce non-linearity (e.g., ReLU, Sigmoid).
  - **Forward/Backpropagation**: Prediction and weight adjustment processes.
- **Example**: Predicting loan approval (1) or rejection (0) based on income and credit score.

## **Loss Function**
- **Definition**: Quantifies the difference between predicted and true outputs, guiding optimization.
- **Formula**: Varies by task (e.g., Binary Crossentropy: $ L = -(y \log(y') + (1-y) \log(1-y')) $).
- **Example**: Mean Absolute Error (MAE) in regression tasks.

## **Optimizer**
- **Definition**: Adjusts model weights to minimize the loss function.
- **Examples**: 
  - **Adam**: Adaptive learning rate optimizer.
  - **SGD**: Stochastic Gradient Descent.

## **Generalization**
- **Definition**: Model’s ability to perform well on unseen data by learning underlying patterns.
- **Trade-off**: Balancing optimization (training error) and generalization (test error).

## **Overfitting**
- **Definition**: Model memorizes training data but fails on new data.
- **Remedies**:
  - More data.
  - Dropout (randomly deactivating neurons).
  - Regularization (L1/L2).

## **Underfitting**
- **Definition**: Model is too simple to capture data patterns.
- **Remedies**:
  - Increase model capacity (add layers/neurons).
  - Train longer.

## **Bias-Variance Tradeoff**
- **Definition**: Balance between model simplicity (high bias) and complexity (high variance).
- **Formula**: Total Error = Bias² + Variance + Irreducible Error.
- **Example**: A linear model may have high bias for non-linear data.

## **Convolutional Neural Network (ConvNet)**
- **Definition**: Specialized DL architecture for grid-like data (e.g., images).
- **Key Operations**:
  - **Convolution**: Applies filters to extract features.
  - **Padding**: Adds zeros to preserve spatial dimensions.
  - **Strides**: Controls filter movement step size.
- **Formula for Output Width**: 
  $$
  \text{Output Width} = \frac{\text{Input Width} + 2 \times \text{Padding} - \text{Filter Width}}{\text{Strides}} + 1
  $$
- **Example**: MNIST digit classification using 32 filters.

## **Max-Pooling**
- **Definition**: Downsampling operation retaining maximum values in windows (e.g., 2x2).
- **Purpose**: Reduces computation and overfitting.
- **Example**: Reducing a 28x28 feature map to 14x14.

## **Transfer Learning**
- **Definition**: Reusing pre-trained models (e.g., VGG16) on new tasks.
- **Steps**:
  1. Freeze convolutional base.
  2. Train custom classifier.
- **Example**: Using ImageNet-trained models for medical image analysis.

## **Backpropagation**
- **Definition**: Algorithm to update weights using gradients of the loss function.
- **Example**: Adjusting weights to reduce prediction error from 0.4671.

## **Activation Function**
- **Definition**: Introduces non-linearity (e.g., ReLU: $ f(x) = \max(0, x) $).
- **Purpose**: Enables learning complex patterns.

## **K-Fold Cross-Validation**
- **Definition**: Evaluates model performance by partitioning data into k subsets.
- **Use Case**: Small datasets (e.g., k=5).

## **Data Preprocessing**
- **Steps**:
  - Scaling to ranges like [-1, 1].
  - Normalization (per-feature scaling).
  - Feature engineering (e.g., PCA).

## **Epoch & Batch Size**
- **Definitions**:
  - **Epoch**: One full pass over training data.
  - **Batch Size**: Number of samples per gradient update.
- **Example**: Training with batch size 32 for 10 epochs.

---

## **Key Links**
- [[AI]] → [[Machine Learning]] → [[Deep Learning]]
- [[Neural Network]] → [[Activation Function]], [[Backpropagation]]
- [[ConvNet]] → [[Convolution]], [[Max-Pooling]], [[Transfer Learning]]