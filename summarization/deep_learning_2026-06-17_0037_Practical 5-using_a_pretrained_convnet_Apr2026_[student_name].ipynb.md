# Practical 5-using_a_pretrained_convnet_Apr2026_[student_name].ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Transfer Learning with Pre-Trained ConvNets  

**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

### **Transfer Learning**  
**Definition**: Technique where a model pre-trained on one task is reused as a starting point for a related task.  
**Formula**: N/A  
**Example**: Using VGG16 (pre-trained on ImageNet) for cat vs. dog classification.  
**[[Wikilink]]**: [[Pre-trained Model]], [[Feature Extraction]]  

---

### **Pre-trained Model**  
**Definition**: A model already trained on a large dataset (e.g., ImageNet), whose weights can be reused.  
**Formula**: N/A  
**Example**: VGG16 model from `keras.applications` with weights='imagenet'.  
**[[Wikilink]]**: [[Transfer Learning]], [[Feature Extraction]]  

---

### **Feature Extraction**  
**Definition**: Using a pre-trained model’s convolutional base to extract features, then training a new classifier on top.  
**Formula**: N/A  
**Example**: Extracting features from VGG16’s output (shape `(4, 4, 512)`) and flattening them for a dense classifier.  
**[[Wikilink]]**: [[Transfer Learning], [Data Augmentation]]  

---

### **Convolutional Base**  
**Definition**: The convolutional layers of a pre-trained model (excluding the final classifier layers).  
**Formula**: N/A  
**Example**: VGG16’s convolutional base with output shape `(4, 4, 512)`.  
**[[Wikilink]]**: [[Feature Extraction], [Fine-tuning]]  

---

### **Freezing Layers**  
**Definition**: Setting layers as non-trainable to preserve pre-trained weights.  
**Formula**: N/A  
**Example**: `conv_base.trainable = False` to freeze VGG16 layers.  
**[[Wikilink]]**: [[Fine-tuning], [Transfer Learning]]  

---

### **Fine-tuning**  
**Definition**: Unfreezing specific layers of a pre-trained model and training them alongside newly added layers.  
**Formula**: N/A  
**Example**: Unfreezing `block5_conv1`, `block5_conv2`, and `block5_conv3` in VGG16 for fine-tuning.  
**[[Wikilink]]**: [[Transfer Learning], [Feature Extraction]]  

---

### **Data Augmentation**  
**Definition**: Applying random transformations (e.g., flips, rotations) to training data to improve generalization.  
**Formula**: N/A  
**Example**: Using `RandomFlip`, `RandomRotation`, and `RandomZoom` in `data_augmentation_layers`.  
**[[Wikilink]]**: [[Overfitting], [Feature Extraction]]  

---

### **VGG16**  
**Definition**: A convolutional neural network architecture pre-trained on ImageNet.  
**Formula**: N/A  
**Example**: Instantiated via `VGG16(weights='imagenet', include_top=False, input_shape=(150, 150, 3))`.  
**[[Wikilink]]**: [[Convolutional Base], [Transfer Learning]]  

---

### **Dense Classifier**  
**Definition**: A fully connected neural network added on top of a convolutional base for classification.  
**Formula**: N/A  
**Example**: A `Dense(256, activation='relu')` layer followed by a `Dense(1, activation='sigmoid')` layer.  
**[[Wikilink]]**: [[Feature Extraction], [Binary Crossentropy Loss]]  

---

### **Binary Crossentropy Loss**  
**Definition**: Loss function for binary classification problems.  
**Formula**:  
$$
\text{Loss} = -\frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]
$$  
**Example**: Used in model compilation for cat vs. dog classification.  
**[[Wikilink]]**: [[Loss Functions]]  

---

### **Adam Optimizer**  
**Definition**: Adaptive learning rate optimizer combining momentum and RMSProp.  
**Formula**: N/A (uses adaptive learning rates with parameters `beta_1` and `beta_2`).  
**Example**: Compiled with `learning_rate=2e-5` for fine-tuning.  
**[[Wikilink]]**: [[Learning Rate]]  

---

### **Model Generalization**  
**Definition**: A model’s ability to perform well on unseen data.  
**Formula**: N/A  
**Example**: Achieving 99% validation accuracy after fine-tuning VGG16.  
**[[Wikilink]]**: [[Overfitting], [Transfer Learning]]  

---

### **Overfitting**  
**Definition**: Poor performance on validation/test data due to memorizing training data.  
**Formula**: N/A  
**Example**: Initial model without regularization achieved 99% training accuracy but ~73% validation accuracy.  
**[[Wikilink]]**: [[Data Augmentation], [Fine-tuning]]  

---

### **Dropout**  
**Definition**: Regularization technique that randomly deactivates neurons during training.  
**Formula**: N/A  
**Example**: `Dropout(0.5)` added to the dense classifier to reduce overfitting.  
**[[Wikilink]]**: [[Overfitting], [Regularization]]  

---

### **Key Outcomes**  
1. **Feature Extraction**: Achieved 97% validation accuracy by training a dense classifier on VGG16 features.  
2. **Fine-tuning**: Further improved validation accuracy to ~99% by unfreezing top VGG16 layers.  
3. **Data Augmentation**: Enabled end-to-end training with augmented data, improving generalization.  
4. **Efficiency**: Feature extraction without augmentation is faster but less flexible than fine-tuning.  

---

## **[[Wikilinks]]**  
- [[Transfer Learning]] → [[Pre-trained Model]], [[Feature Extraction]], [[Fine-tuning]]  
- [[Feature Extraction]] → [[Convolutional Base]], [[Data Augmentation]]  
- [[Fine-tuning]] → [[Freezing Layers], [VGG16]]  
- [[VGG16]] → [[Convolutional Base], [Transfer Learning]]  
- [[Data Augmentation]] → [[Overfitting], [Model Generalization]]  
- [[Overfitting]] → [[Dropout], [Data Augmentation]]  
- [[Model Generalization]] → [[Validation Accuracy]]  
- [[Binary Crossentropy Loss]] → [[Loss Functions]]  
- [[Adam Optimizer]] → [[Learning Rate]]