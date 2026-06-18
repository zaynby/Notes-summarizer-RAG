# Lecture 1 - Introduction to DL_Apr 2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary: Introduction to Deep Learning  

## **Artificial Intelligence (AI)**  
**Definition**: Field of creating systems that automate intellectual tasks normally performed by humans.  
**Formula**: N/A  
**Example**: Self-driving cars, chatbots, and virtual assistants.  
**Link**: [[Artificial Intelligence]]  

---

## **Machine Learning (ML)**  
**Definition**: Subset of AI where systems learn from data to make predictions or decisions.  
**Key Components**:  
1. **Inputs**: Training data (e.g., images, text).  
2. **Labels**: Expected outputs (e.g., "cat" or "dog" for image classification).  
3. **Loss Function**: Measures algorithm performance (e.g., RMSE for regression, Accuracy for classification).  
**Formula**: Loss \( L = \frac{1}{n} \sum_{i=1}^n (y_{\text{pred}} - y_{\text{true}})^2 \) (Mean Squared Error example).  
**Example**: Classifying emails as spam or not spam.  
**Link**: [[Machine Learning]]  

---

## **Deep Learning (DL)**  
**Definition**: Subset of ML using layered (hierarchical) neural networks to learn complex patterns.  
**Formula**: N/A  
**Example**: Detecting COVID-19 in X-ray images.  
**Link**: [[Deep Learning]]  

---

## **Evaluation Protocols**  
1. **Hold-Out Validation**  
   - **Definition**: Split data into training and validation sets (e.g., 80%-20%).  
   - **Use Case**: When ample data is available.  
2. **K-Fold Cross-Validation**  
   - **Definition**: Split data into \( k \) subsets, train on \( k-1 \), validate on 1.  
   - **Use Case**: Limited data.  
3. **Iterated K-Fold**  
   - **Definition**: Repeat K-fold multiple times for robust evaluation.  
   - **Use Case**: Highly accurate validation with minimal data.  
**Link**: [[Cross-Validation]]  

---

## **Neural Network Fundamentals**  
1. **Tensor**  
   - **Definition**: Multidimensional array storing data.  
   - **Attributes**: Rank (number of axes), shape (dimensions), data type.  
   - **Examples**:  
     - 4D tensor: Images (batch, height, width, channels).  
     - 3D tensor: Video frames (batch, frames, height, width).  
   - **Link**: [[Tensor]]  

2. **Weight (W) and Bias (b)**  
   - **Definition**: Trainable parameters adjusting input data to predict outputs.  
   - **Formula**: Output \( = W \cdot X + b \) (linear transformation).  
   - **Example**: Image classification weights mapping pixels to classes.  
   - **Link**: [[Neural Network]]  

3. **Activation Function**  
   - **Definition**: Introduces non-linearity (e.g., ReLU, Sigmoid).  
   - **Formula**: \( \text{ReLU}(x) = \max(0, x) \).  
   - **Example**: Hidden layers in MNIST digit classification.  
   - **Link**: [[Activation Function]]  

---

## **Training Workflow**  
1. **Forward Pass**  
   - **Definition**: Compute predictions \( y_{\text{pred}} \) from inputs \( X \).  
2. **Loss Computation**  
   - **Definition**: Compare \( y_{\text{pred}} \) to true labels \( y_{\text{true}} \).  
3. **Backward Pass (Optimization)**  
   - **Definition**: Update weights using gradient descent (e.g., Adam optimizer).  
   - **Formula**: \( W_{\text{new}} = W_{\text{old}} - \eta \cdot \nabla W \) (gradient update).  
   - **Example**: Adjusting weights in a CNN for better image recognition.  

---

## **Overfitting vs. Underfitting**  
1. **Overfitting**  
   - **Definition**: Model memorizes training data but fails on new data.  
   - **Mitigation**: Dropout, L1/L2 regularization, reduce model complexity.  
2. **Underfitting**  
   - **Definition**: Model too simple to capture patterns.  
   - **Mitigation**: Add layers, increase nodes, train longer.  
**Link**: [[Overfitting]], [[Underfitting]]  

---

## **Real-World Applications**  
1. **Medical Imaging**  
   - **Example**: Detecting COVID-19 in X-rays using CNNs.  
2. **Natural Language Processing (NLP)**  
   - **Example**: Customer review sentiment analysis with RNNs.  
**Link**: [[Applications of Deep Learning]]  

---

## **Key Hyperparameters**  
1. **Batch Size**  
   - **Definition**: Number of samples per training iteration.  
2. **Learning Rate (\( \eta \))**  
   - **Definition**: Step size for weight updates.  
3. **Epochs**  
   - **Definition**: Number of times the model sees the entire dataset.  
**Link**: [[Hyperparameters]]  

--- 

This summary connects foundational concepts in AI, ML, and DL, emphasizing practical workflows and theoretical underpinnings. Use [[Wikilinks]] to explore related topics in detail.