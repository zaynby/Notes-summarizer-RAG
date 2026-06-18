# Practical_2a-classifying-movie-reviews_Apr2026_[student_name].ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Classifying Movie Reviews (IMDB Dataset)  
**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

### **IMDB Dataset**  
**Definition**: A binary classification dataset containing 50,000 movie reviews (25,000 for training and 25,000 for testing) labeled as positive (1) or negative (0). Reviews are preprocessed into sequences of word indices.  
**Formula**: N/A  
**Example**:  
```python  
from keras.datasets import imdb  
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)  
```  
**[[Wikilink]]**: [[Data Preprocessing]]  

---

### **One-Hot Encoding**  
**Definition**: Conversion of integer sequences (word indices) into binary vectors where each dimension corresponds to a word in the vocabulary.  
**Formula**:  
For a sequence of integers \( S = [s_1, s_2, ..., s_n] \), create a binary matrix \( M \) of shape \( (1, 10000) \) where \( M[0, s_i] = 1 \).  
**Example**:  
```python  
def vectorize_sequences(sequences, dimension=10000):  
    results = np.zeros((len(sequences), dimension))  
    for i, sequence in enumerate(sequences):  
        results[i, sequence] = 1.  
    return results  
x_train = vectorize_sequences(train_data)  
```  
**[[Wikilink]]**: [[Neural Network Architecture]]  

---

### **Neural Network Architecture**  
**Definition**: A Sequential model with input, hidden, and output layers. Hidden layers use activation functions (e.g., ReLU, Sigmoid) to introduce non-linearity.  
**Formula**: N/A  
**Example**:  
```python  
model = keras.Sequential([  
    Input(shape=(10000,)),  
    layers.Dense(16, activation="relu"),  
    layers.Dense(16, activation="relu"),  
    layers.Dense(1, activation="sigmoid"),  
])  
```  
**[[Wikilink]]**: [[Adam Optimizer]], [[Binary Crossentropy Loss]]  

---

### **Adam Optimizer**  
**Definition**: Adaptive learning rate optimizer combining momentum and RMSProp to adjust weights efficiently during training.  
**Formula**: N/A (uses adaptive learning rates with parameters \( \beta_1 \) and \( \beta_2 \)).  
**Example**:  
```python  
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  
```  
**[[Wikilink]]**: [[Learning Rate]]  

---

### **Binary Crossentropy Loss**  
**Definition**: Loss function for binary classification tasks, measuring the difference between predicted probabilities and true labels.  
**Formula**:  
\[ \text{Loss} = -\frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)] \]  
**Example**:  
```python  
model.compile(loss='binary_crossentropy', metrics=['accuracy'])  
```  
**[[Wikilink]]**: [[Loss Functions]]  

---

### **Validation Split**  
**Definition**: Technique to reserve a portion of training data (e.g., 40%) for monitoring overfitting during training.  
**Formula**: N/A  
**Example**:  
```python  
history = model.fit(x_train, y_train, epochs=20, batch_size=512, validation_split=0.4)  
```  
**[[Wikilink]]**: [[Overfitting]]  

---

### **Overfitting**  
**Definition**: Phenomenon where a model performs well on training data but poorly on validation/test data due to memorizing noise.  
**Formula**: N/A  
**Example**: Training accuracy reaches 99%, but validation accuracy plateaus at ~88% after 4 epochs.  
**[[Wikilink]]**: [[Data Augmentation]], [[Dropout]]  

---

### **Scenario A: Sigmoid Activation**  
**Definition**: Replacing ReLU with Sigmoid activation in hidden layers to test its impact on training dynamics.  
**Formula**: \( \sigma(x) = \frac{1}{1 + e^{-x}} \)  
**Example**:  
```python  
model = keras.Sequential([  
    Input(shape=(10000,)),  
    layers.Dense(16, activation="sigmoid"),  
    layers.Dense(16, activation="sigmoid"),  
    layers.Dense(1, activation="sigmoid"),  
])  
```  
**Observation**: Slower convergence due to vanishing gradients; validation accuracy stabilizes at ~87%.  
**[[Wikilink]]**: [[Activation Function]]  

---

### **Scenario B: Reduced Model Capacity**  
**Definition**: Simplifying the network by removing a hidden layer and reducing units to test underfitting.  
**Formula**: N/A  
**Example**:  
```python  
model = keras.Sequential([  
    Input(shape=(10000,)),  
    layers.Dense(2, activation="relu"),  
    layers.Dense(1, activation="sigmoid"),  
])  
```  
**Observation**: Faster training but lower validation accuracy (~82%) due to underfitting.  
**[[Wikilink]]**: [[Model Capacity]]  

---

### **Key Observations**  
1. **Baseline Model**: Achieved 88.2% test accuracy with ReLU activations and two hidden layers.  
2. **Scenario A (Sigmoid)**: Slower training and similar validation performance compared to ReLU.  
3. **Scenario B (Reduced Capacity)**: Underfitting observed due to insufficient model complexity.  
4. **Overfitting Mitigation**: Early stopping after 4 epochs improved generalization.  

---

## **[[Wikilinks]]**  
- [[IMDB Dataset]] → [[One-Hot Encoding]], [[Neural Network Architecture]]  
- [[Neural Network Architecture]] → [[Adam Optimizer]], [[Binary Crossentropy Loss]]  
- [[Overfitting]] → [[Validation Split]], [[Scenario A: Sigmoid Activation]]  
- [[Scenario A: Sigmoid Activation]] → [[Activation Function]]  
- [[Scenario B: Reduced Capacity]] → [[Model Capacity]]  
- [[Binary Crossentropy Loss]] → [[Loss Functions]]