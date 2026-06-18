# Lecture 3 - Neural Networks II _Apr2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Here’s a structured summary of the provided content using the requested academic format:

---

## **Generalization**  
**Definition**: Model’s ability to learn underlying data patterns and make accurate predictions on unseen data.  
**Formula**: Not directly quantifiable; evaluated via validation/test performance metrics (e.g., accuracy, loss).  
**Example**: A model trained on diverse datasets generalizes well to new inputs without memorizing training examples.  

---

## **Optimization**  
**Definition**: Process of minimizing training error by adjusting model parameters (weights/bias) using gradient-based methods.  
**Formula**: Minimize loss function \( \mathcal{L}(W, b) \), where \( W \) = weights, \( b \) = bias.  
**Example**: Using stochastic gradient descent (SGD) to iteratively reduce training loss.  

---

## **Underfitting**  
**Definition**: Occurs when a model is too simple to capture data patterns, leading to high training and validation errors.  
**Formula**: High **bias** error dominates total error: \( \text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error} \).  
**Example**: A linear regression model failing to fit nonlinear data.  

---

## **Overfitting**  
**Definition**: Model learns training data noise/spurious patterns, performing well on training data but poorly on validation/test data.  
**Formula**: High **variance** error dominates total error (see underfitting formula).  
**Example**: A deep neural network with excessive layers memorizing training examples but failing on new data.  

---

## **Bias-Variance Trade-off**  
**Definition**: Balancing model complexity to minimize total error, avoiding high bias (underfitting) and high variance (overfitting).  
**Formula**: \( \text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Error} \).  
**Example**: Reducing model layers to decrease variance but risking increased bias.  

---

## **L1 Regularization (Lasso)**  
**Definition**: Adds penalty proportional to absolute weights to the loss function, encouraging sparsity.  
**Formula**: \( \mathcal{L}_{\text{L1}} = \mathcal{L}_{\text{original}} + \lambda \sum |W| \), where \( \lambda \) = regularization strength.  
**Example**: Setting unimportant weights to zero in a dense layer.  

---

## **L2 Regularization (Ridge)**  
**Definition**: Adds penalty proportional to squared weights to the loss function, encouraging small weights.  
**Formula**: \( \mathcal{L}_{\text{L2}} = \mathcal{L}_{\text{original}} + \lambda \sum W^2 \).  
**Example**: Penalizing large weights in a convolutional layer to prevent overfitting.  

---

## **Dropout**  
**Definition**: Randomly deactivates a fraction of neurons during training to prevent co-adaptation.  
**Formula**: No direct formula; dropout rate \( p \) (e.g., 0.5) determines the proportion of neurons dropped.  
**Example**: Applying `Dropout(0.2)` in Keras to reduce overfitting in a classification task.  

---

## **Remedies for Overfitting**  
1. **More Data**: Collect additional data or use **data augmentation** (e.g., image rotations/flips).  
2. **Reduce Model Capacity**: Decrease layers/units (e.g., from 10 to 5 neurons per layer).  
3. **Regularization**: Apply L1/L2 penalties or dropout.  

---

## **Remedies for Underfitting**  
1. **Increase Model Capacity**: Add layers or units (e.g., adding a hidden layer).  
2. **Train Longer**: Increase epochs to allow better convergence.  
3. **Reduce Regularization**: Decrease \( \lambda \) or remove dropout.  

---

### **Key Links**  
- [[Overfitting]] and [[Underfitting]] are addressed via [[Bias-Variance Trade-off]].  
- [[L1 Regularization]] and [[L2 Regularization]] are types of [[Regularization]].  
- [[Dropout]] is a technique to reduce [[Overfitting]].  

This summary balances conciseness with technical depth, aligning with polytechnic-level expectations. Let me know if further refinements are needed!