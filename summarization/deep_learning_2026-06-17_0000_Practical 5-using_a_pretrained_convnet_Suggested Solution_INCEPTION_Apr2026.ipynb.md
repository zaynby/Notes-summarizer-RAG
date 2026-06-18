# Practical 5-using_a_pretrained_convnet_Suggested Solution_INCEPTION_Apr2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Transfer Learning with Pre-trained Models (InceptionV3)

---

### **Pre-trained Model**  
**Definition**: A neural network trained on a large-scale dataset (e.g., ImageNet) with learned weights capturing general features.  
**Formula**: N/A  
**Example**: InceptionV3 used in Code Cell 4, pre-trained on ImageNet for image classification.  
**[[Wikilink]]**: [[Transfer Learning]]  

---

### **Feature Extraction**  
**Definition**: Using the convolutional layers of a pre-trained model to extract high-level features from new data, which are then used to train a task-specific classifier.  
**Formula**: N/A  
**Example**: Extracting features from InceptionV3’s output (shape `(3, 3, 2048)`) for cats vs. dogs classification (Code Cell 9).  
**[[Wikilink]]**: [[Convolutional Base]]  

---

### **Convolutional Base**  
**Definition**: The stack of convolutional and pooling layers in a pre-trained model that learns spatial hierarchies (edges → textures → objects).  
**Formula**: N/A  
**Example**: InceptionV3’s convolutional base outputs a feature map of shape `(3, 3, 2048)` (Code Cell 6).  
**[[Wikilink]]**: [[Feature Extraction]]  

---

### **Data Augmentation**  
**Definition**: Technique to artificially increase dataset diversity by applying random transformations (e.g., flipping, rotation) to training images.  
**Formula**: N/A  
**Example**: Layers like `RandomFlip`, `RandomRotation`, and `RandomZoom` in Code Cell 25.  
**[[Wikilink]]**: [[Overfitting]]  

---

### **Fine-Tuning**  
**Definition**: Unfreezing select layers of a pre-trained model and training them on the new task with a low learning rate to adapt high-level features.  
**Formula**: N/A  
**Example**: Unfreezing layers after `mixed6` in InceptionV3 and training with learning rate `2e-5` (Code Cell 33).  
**[[Wikilink]]**: [[Transfer Learning]]  

---

### **Dropout**  
**Definition**: Regularization technique that randomly deactivates a fraction of neurons during training to prevent overfitting.  
**Formula**: N/A  
**Example**: Adding `Dropout(0.5)` before the dense classifier in Code Cell 13.  
**[[Wikilink]]**: [[Overfitting]]  

---

### **Learning Rate**  
**Definition**: Hyperparameter controlling the step size during optimization; a low value (e.g., `2e-5`) is used in fine-tuning to avoid disrupting pre-trained weights.  
**Formula**: Specified in optimizer: `optimizers.Adam(learning_rate=2e-5)`  
**Example**: Fine-tuning InceptionV3 with learning rate `2e-5` (Code Cell 34).  
**[[Wikilink]]**: [[Fine-Tuning]]  

---

### **Overfitting**  
**Definition**: Phenomenon where a model performs well on training data but poorly on validation/test data due to memorizing noise.  
**Formula**: N/A  
**Example**: Initial model achieved 95% training accuracy vs. 62% validation accuracy (Markdown Cell 17).  
**[[Wikilink]]**: [[Data Augmentation]], [[Dropout]]  

---

### **Binary Crossentropy Loss**  
**Definition**: Loss function for binary classification problems, measuring the difference between predicted probabilities and true labels.  
**Formula**:  
\[ \text{Loss} = -\frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)] \]  
**Example**: Used in model compilation for cats vs. dogs classification (Code Cell 14).  
**[[Wikilink]]**: [[Model Compilation]]  

---

### **Dense Layer**  
**Definition**: Fully connected layer that combines features from previous layers for final classification.  
**Formula**: N/A  
**Example**: Adding `Dense(256, activation='relu')` and `Dense(1, activation='sigmoid')` layers (Code Cell 13).  
**[[Wikilink]]**: [[Neural Network]]  

---

### **Model Compilation**  
**Definition**: Configuring the model with a loss function, optimizer, and evaluation metrics.  
**Formula**: N/A  
**Example**: `model.compile(optimizer=Adam(learning_rate=2e-5), loss='binary_crossentropy', metrics=['acc'])` (Code Cell 14).  
**[[Wikilink]]**: [[Optimizer]]  

---

### **Transfer Learning**  
**Definition**: Technique where a pre-trained model (trained on a large dataset) is adapted to a new, related task.  
**Formula**: N/A  
**Example**: Using InceptionV3 (pre-trained on ImageNet) for cats vs. dogs classification (Code Cell 4).  
**[[Wikilink]]**: [[Pre-trained Model]]  

---

## **Key Observations**  
1. **Feature Extraction**: Achieved 95% training accuracy but only 62% validation accuracy, indicating overfitting.  
2. **Data Augmentation**: Reduced the training-validation accuracy gap, improving generalization.  
3. **Fine-Tuning**: Validation loss increased after epoch 17, suggesting overfitting despite low learning rates.  

## **[[Wikilinks]]**  
- [[Pre-trained Model]] → [[Feature Extraction]], [[Fine-Tuning]]  
- [[Convolutional Base]] → [[Feature Extraction]]  
- [[Data Augmentation]] → [[Overfitting]]  
- [[Fine-Tuning]] → [[Learning Rate]]  
- [[Transfer Learning]] → [[Pre-trained Model]]