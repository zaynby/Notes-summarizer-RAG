# Revision for DL CT_Theory.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided Deep Learning content:

---

### **Artificial Intelligence (AI)**  
**Definition**: Field of creating systems that automate intellectual tasks normally performed by humans. Encompasses ML, DL, and non-learning approaches (e.g., rule-based systems).  
**Formula**: N/A  
**Example**: Rule-based chatbots vs. learning-based image recognition systems.  

---

### **Machine Learning (ML)**  
**Definition**: Subset of AI focused on learning representations from data to predict outputs from inputs.  
**Formula**: N/A  
**Example**: Classifying images as "cat" or "dog" using labeled datasets.  

#### **Key Components of ML**  
1. **Inputs**  
   - **Definition**: Raw data points (e.g., image files).  
   - **Formula**: N/A  
   - **Example**: Pixel values of an image.  

2. **Labels**  
   - **Definition**: Expected outputs (e.g., "cat" or "dog").  
   - **Formula**: N/A  
   - **Example**: Binary labels (0 = reject, 1 = approve) for loan applications.  

3. **Loss Function**  
   - **Definition**: Measures the difference between predictions and true targets.  
   - **Formula**:  
     - Mean Absolute Error (MAE): $\frac{1}{n} \sum_{i=1}^n |y_{\text{true}} - y_{\text{pred}}|$  
     - Binary Crossentropy: $- \frac{1}{n} \sum_{i=1}^n [y_{\text{true}} \log(y_{\text{pred}}) + (1-y_{\text{true}}) \log(1-y_{\text{pred}})]$  
   - **Example**: Sigmoid + binary crossentropy for loan approval prediction.  

---

### **Deep Learning (DL)**  
**Definition**: Subset of ML using layered (hierarchical) representations to learn complex patterns.  
**Formula**: N/A  
**Example**: Stacked dense layers with ReLU activations for image classification.  

#### **Core Concepts**  
1. **Neural Network**  
   - **Definition**: Parameterized by weights, composed of input, hidden, and output layers.  
   - **Formula**: Forward propagation: $y_{\text{pred}} = \sigma(Wx + b)$  
   - **Example**: Loan approval model with inputs (credit score, age) and output (approve/reject).  

2. **Activation Functions**  
   - **Definition**: Introduce non-linearity (e.g., ReLU, Sigmoid).  
   - **Formula**:  
     - ReLU: $f(x) = \max(0, x)$  
     - Sigmoid: $f(x) = \frac{1}{1 + e^{-x}}$  
   - **Example**: Sigmoid for binary classification outputs (probability).  

3. **Gradient Descent**  
   - **Definition**: Optimization method to minimize loss by adjusting weights.  
   - **Formula**: $W_{\text{new}} = W_{\text{old}} - \eta \frac{\partial \text{Loss}}{\partial W}$  
   - **Example**: Adam optimizer with default learning rate (0.001).  

---

### **Model Training Workflow**  
1. **Generalization**  
   - **Definition**: Model’s ability to perform well on unseen data.  
   - **Formula**: N/A  
   - **Example**: Validating a model on a hold-out test set.  

2. **Overfitting/Underfitting**  
   - **Definition**: Overfitting = model memorizes training data; Underfitting = model too simple.  
   - **Formula**: N/A  
   - **Example**: Overfitting detected when validation loss increases while training loss decreases.  

3. **Bias-Variance Trade-off**  
   - **Definition**: Balance between model simplicity (high bias) and complexity (high variance).  
   - **Formula**: Total Error = Bias² + Variance + Irreducible Error  
   - **Example**: Reducing dropout rate to decrease variance.  

---

### **Convolutional Neural Networks (CNNs)**  
**Definition**: Specialized DL models for grid-like data (e.g., images).  
**Formula**: N/A  
**Example**: MNIST digit classification using convolution and max-pooling layers.  

#### **Key Operations**  
1. **Convolution**  
   - **Definition**: Applies filters to extract local features.  
   - **Formula**: Output size = $\frac{W - F + 2P}{S} + 1$ (W=width, F=filter size, P=padding, S=stride)  
   - **Example**: 5x5 image → 3x3 filter → 3x3 output (stride=1, padding=0).  

2. **Max-Pooling**  
   - **Definition**: Downsampling by taking maximum values in windows.  
   - **Formula**: N/A  
   - **Example**: Reducing 28x28 feature maps to 14x14 with 2x2 pooling.  

---

### **Transfer Learning**  
**Definition**: Reusing pre-trained models (e.g., VGG16) on new tasks.  
**Formula**: N/A  
**Example**: Fine-tuning VGG16’s convolutional layers for medical image classification.  

#### **Techniques**  
1. **Feature Extraction**  
   - **Definition**: Using pre-trained layers to extract features, then training a new classifier.  
   - **Formula**: N/A  
   - **Example**: Freezing VGG16 layers and adding a custom dense head.  

2. **Fine-Tuning**  
   - **Definition**: Unfreezing and retraining some pre-trained layers.  
   - **Formula**: N/A  
   - **Example**: Training Conv Block 5 of VGG16 on a new dataset.  

---

### **Regularization Techniques**  
1. **Dropout**  
   - **Definition**: Randomly deactivates neurons during training.  
   - **Formula**: N/A  
   - **Example**: Dropout rate of 0.5 in hidden layers.  

2. **L1/L2 Regularization**  
   - **Definition**: Penalizes large weights in loss function.  
   - **Formula**:  
     - L1: $\text{Loss} + \lambda \sum |W|$  
     - L2: $\text{Loss} + \lambda \sum W^2$  
   - **Example**: Adding L2 regularization to dense layers in Keras.  

---

### **Wikilinks**  
- [[Artificial Intelligence]] → [[Machine Learning]] → [[Deep Learning]]  
- [[Neural Networks]] → [[Convolutional Neural Networks]]  
- [[Loss Function]] → [[Optimizer]] (e.g., Adam)  
- [[Generalization]] ↔ [[Overfitting]]/[[Underfitting]]  
- [[Transfer Learning]] → [[Pre-trained ConvNet]]  

--- 

This summary integrates all key concepts from the slides, linking related terms and providing concise examples/formulas where applicable.