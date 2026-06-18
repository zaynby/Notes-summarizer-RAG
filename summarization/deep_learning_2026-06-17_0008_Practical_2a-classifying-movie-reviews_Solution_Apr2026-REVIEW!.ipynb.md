# Practical_2a-classifying-movie-reviews_Solution_Apr2026-REVIEW!.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Movie Review Classification (IMDB Dataset)  
**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

## **IMDB Dataset**  
**Definition**: A preprocessed dataset containing 50,000 highly polarized movie reviews (25,000 for training, 25,000 for testing) with binary labels (positive/negative).  
**Example**: Loaded via `imdb.load_data(num_words=10000)`, restricting vocabulary to the top 10,000 most frequent words.  
**[[Wikilink]]**: [[One-Hot Encoding]]  

---

## **One-Hot Encoding**  
**Definition**: A vectorization method where each word index in a review is converted into a binary vector of size `num_words`, with 1s at the corresponding index positions.  
**Formula**: N/A  
**Example**: `vectorize_sequences(sequences, dimension=10000)` transforms review indices (e.g., `[3, 5]`) into 10,000-dimensional binary vectors.  
**[[Wikilink]]**: [[IMDB Dataset]]  

---

## **Neural Network Architecture**  
**Definition**: A Sequential model with input, hidden, and output layers designed for binary classification.  
**Example**:  
```python  
model = keras.Sequential([  
    Input(shape=(10000,)),  
    layers.Dense(16, activation="relu"),  
    layers.Dense(16, activation="relu"),  
    layers.Dense(1, activation="sigmoid"),  
])  
```  
**[[Wikilink]]**: [[Activation Function]]  

---

## **Adam Optimizer**  
**Definition**: Adaptive learning rate optimizer combining momentum and RMSProp to adjust weights efficiently.  
**Formula**: N/A  
**Example**: Compiled via `model.compile(optimizer='adam', ...)`.  
**[[Wikilink]]**: [[Loss Function]]  

---

## **Binary Crossentropy Loss**  
**Definition**: Loss function for binary classification, measuring the difference between predicted probabilities and true labels.  
**Formula**:  
\[ \text{Loss} = -\frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)] \]  
**Example**: Used in model compilation for training the IMDB classifier.  
**[[Wikilink]]**: [[Accuracy Metric]]  

---

## **Validation Split**  
**Definition**: Technique to reserve a portion of training data (e.g., 40%) for monitoring overfitting during training.  
**Example**: Implemented via `validation_split=0.4` in `model.fit()`.  
**[[Wikilink]]**: [[Overfitting]]  

---

## **Overfitting**  
**Definition**: Phenomenon where a model performs well on training data but poorly on validation/test data due to memorizing noise.  
**Example**: Training accuracy reaches 95% while validation accuracy plateaus at 88% after 4 epochs.  
**[[Wikilink]]**: [[Validation Split]], [[Regularization]]  

---

## **Model Prediction**  
**Definition**: Generating probabilities of new data belonging to a class using a trained model.  
**Example**: `model.predict(x_test)` outputs probabilities between 0 (negative) and 1 (positive).  
**[[Wikilink]]**: [[Binary Crossentropy Loss]]  

---

## **Activation Function (ReLU vs Sigmoid)**  
**Definition**: Introduces non-linearity into the model.  
- **ReLU**: $ f(x) = \max(0, x) $  
- **Sigmoid**: $ f(x) = \frac{1}{1 + e^{-x}} $  
**Example**:  
- **Scenario A**: Replacing ReLU with sigmoid in hidden layers slows convergence but may reduce overfitting initially.  
- **Scenario B**: Using ReLU with reduced capacity (2 units) leads to underfitting.  
**[[Wikilink]]**: [[Neural Network Architecture]]  

---

## **Model Capacity**  
**Definition**: The ability of a model to learn complex patterns, determined by the number of layers and units.  
**Example**:  
- **Scenario B**: Removing one hidden layer and reducing units to 2 results in underfitting (validation accuracy stagnates at ~87%).  
**[[Wikilink]]**: [[Underfitting]]  

---

## **Underfitting**  
**Definition**: Model is too simple to capture underlying patterns in the data.  
**Example**: Scenario B’s model with 2 units shows a large gap between training and validation performance.  
**[[Wikilink]]**: [[Model Capacity]]  

---

## **Epochs & Batch Size**  
**Definitions**:  
- **Epoch**: One full pass over the training data.  
- **Batch Size**: Number of samples processed before weight updates.  
**Example**: Training for 20 epochs with batch size 512.  
**[[Wikilink]]**: [[Adam Optimizer]]  

---

## **Key Observations**  
1. **Scenario A (Sigmoid)**: Slower convergence but smoother loss curves compared to ReLU.  
2. **Scenario B (Reduced Capacity)**: Underfitting due to insufficient model complexity.  
3. **Regularization via Architecture**: Simplifying the model or changing activation functions can mitigate overfitting.  

## **[[Wikilinks]]**  
- [[IMDB Dataset]] → [[One-Hot Encoding]]  
- [[Neural Network Architecture]] → [[Activation Function]], [[Model Capacity]]  
- [[Overfitting]] → [[Validation Split]], [[Scenario A]]  
- [[Model Capacity]] → [[Underfitting]], [[Scenario B]]  
- [[Binary Crossentropy Loss]] → [[Model Prediction]]  
- [[Adam Optimizer]] → [[Epochs & Batch Size]]