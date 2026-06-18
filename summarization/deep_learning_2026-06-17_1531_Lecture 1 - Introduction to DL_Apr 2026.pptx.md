# Lecture 1 - Introduction to DL_Apr 2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

## Deep Learning (DL) - Summary

### Term -> Definition
- **Deep Learning (DL):** A subset of machine learning that involves training neural networks with multiple layers to learn complex representations from data.

### Formula -> Example
- **Loss Function:** Measures the discrepancy between predicted and actual outputs. Common loss functions include Mean Squared Error (MSE) for regression tasks, and Categorical Cross Entropy for classification tasks.
  - For example, in a binary classification problem with labels `y = [1, 0]`, and predictions `y_pred = [0.9, 0.1]`, the loss can be calculated as:
    \[
    \text{Loss} = -\sum y_i \log(y_{pred,i}) = -[1 \cdot \log(0.9) + 0 \cdot \log(0.1)] \approx 0.11
    \]

### Key Concepts

- **Artificial Intelligence (AI):** A field of creating systems that automate intellectual tasks traditionally performed by humans.
  
- **Machine Learning (ML):** A subset of AI where algorithms improve their performance on a task through experience without being explicitly programmed.

- **Deep Learning (DL):** A type of ML that uses neural networks with many layers to learn hierarchical representations from data. It is used for tasks like image and speech recognition, natural language processing, and more.

### Workflow Summary

1. **Data Representation:** Data are represented as tensors, which can be scalars, vectors, matrices, or higher-dimensional arrays.
2. **Tensor Operations:** Element-wise operations, broadcasting, tensor dot (matrix multiplication), reshaping, etc., are used to manipulate data.
3. **Model Building:**
   - **Inputs:** Input data points (e.g., images).
   - **Labels:** Expected output labels (e.g., cat or dog).
   - **Loss Function:** Measures the quality of network's output and is used as a feedback signal for learning.
4. **Training Phase:**
   - **Random Initialization:** Assign small random values to weights.
   - **Forward Pass:** Run the model on input data to get predictions.
   - **Backward Pass (Gradient Descent):** Compute loss, update weights using gradient descent.
5. **Model Evaluation:**
   - **Validation Set:** Use a hold-out validation set for evaluation and cross-validation techniques like K-fold or iterated K-fold.

### Example Applications

- **MNIST Dataset:** Classify grayscale images of handwritten digits (0 through 9) into categories using deep learning models.
  - **Steps:**
    1. Load the MNIST dataset.
    2. Build a neural network model with multiple layers.
    3. Compile and train the model on training data.
    4. Evaluate the model's performance on test data.

### Key Takeaways

- Deep learning is powerful but requires significant computational resources.
- Understanding hyperparameters, loss functions, and validation techniques is crucial for effective deep learning models.
- The universal workflow of machine learning involves inputs, labels, loss function, training, evaluation, and prediction phases.

### Further Reading
- **Chollet, F. (2018).** *Deep Learning with Python* (3rd Edition).
  - Chapters: 1, 2, 5, 6.
- **Hyperparameter Understanding:** https://medium.com/@ilyurek/understanding-hyperparameters-in-machine-learning-6ae699fcbdd1
- **Cross Validation:** https://medium.com/data-science/why-and-how-to-cross-validate-a-model-d6424b45261f

### Related Concepts
- [[Artificial Intelligence (AI)]]
- [[Machine Learning (ML)]]
- [[Tensor Operations]]

This summary provides a structured overview of deep learning, its components, and practical applications.