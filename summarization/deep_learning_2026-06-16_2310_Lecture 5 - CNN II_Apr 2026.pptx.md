# Lecture 5 - CNN II_Apr 2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Here’s a structured summary of the provided content on **Deep Learning (Convolutional Neural Networks II)**:

---

### **Transfer Learning**  
**Definition**: Reusing a pre-trained neural network (trained on a large dataset) as a starting point for a new but related task.  
**Formula**: N/A  
**Example**: Using VGG16 (pre-trained on ImageNet) for classifying cats vs. dogs.  
**[[Wikilink]]**: [[Pre-trained ConvNet]]  

---

### **Pre-trained ConvNet**  
**Definition**: A convolutional neural network trained on a large labeled dataset (e.g., ImageNet with 14 million images and 21,000 classes).  
**Formula**: N/A  
**Example**: VGG16, VGG19, Inception V3, ResNet50.  
**[[Wikilink]]**: [[Transfer Learning]]  

---

### **Feature Extraction**  
**Definition**: Using the convolutional layers of a pre-trained ConvNet to extract features from new data, then training a custom classifier on those features.  
**Formula**: N/A  
**Steps**:  
1. Freeze pre-trained convolutional base (e.g., VGG16).  
2. Remove the original classifier.  
3. Train a new classifier on extracted features.  
**Example**: Extracting features from cat/dog images using VGG16’s `conv_base` and training a fully connected (FC) classifier.  
**[[Wikilink]]**: [[Fine-Tuning]]  

---

### **Fine-Tuning**  
**Definition**: Unfreezing select layers of a pre-trained ConvNet and training them on the new task to adapt high-level features.  
**Formula**: N/A  
**Example**: Unfreezing Conv Block 5 (4 layers) of VGG16 for cats vs. dogs classification.  
**[[Wikilink]]**: [[Feature Extraction]]  

---

### **Data Augmentation**  
**Definition**: Applying random transformations (e.g., rotation, flipping, zooming) to training images to increase dataset diversity and reduce overfitting.  
**Formula**: N/A  
**Example**: Augmenting cat/dog images during training to improve generalization.  
**[[Wikilink]]**: [[Overfitting]]  

---

### **VGG16 Architecture**  
**Definition**: A 16-layer convolutional neural network with 13 convolutional layers and 3 fully connected layers.  
**Formula**: N/A  
**Key Features**:  
- Uses 3x3 filters with stride 1.  
- Max pooling (2x2, stride 2).  
**Example**: Used as a feature extractor for image classification tasks.  
**[[Wikilink]]**: [[Pre-trained ConvNet]]  

---

### **Training Dynamics**  
**Term**: **Training Accuracy**  
**Definition**: Proportion of correct predictions on the training dataset.  
**Formula**: \( \text{Accuracy} = \frac{\text{True Positives + True Negatives}}{\text{Total Samples}} \)  
**Example**: Training accuracy rose to ~0.98 during fine-tuning.  

**Term**: **Validation Accuracy**  
**Definition**: Proportion of correct predictions on the validation dataset.  
**Formula**: Same as above.  
**Example**: Validation accuracy stabilized at ~0.98 during fine-tuning.  

**Term**: **Loss (Binary Cross-Entropy)**  
**Definition**: Measures the difference between predicted and actual labels (0 or 1).  
**Formula**: \( \text{Loss} = -\frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)] \)  
**Example**: Training loss dropped to near 0 during fine-tuning.  

---

### **Key Outcomes**  
1. **Pre-trained ConvNets** (e.g., VGG16) enable efficient feature extraction and reduce training time.  
2. **Data augmentation** improves generalization and reduces overfitting.  
3. **Fine-tuning** adapts high-level features to new tasks but requires careful control to avoid overfitting.  

**[[Wikilink]]**: [[Convolutional Neural Networks]]  

--- 

This summary integrates concepts from the lecture slides, emphasizing practical applications and results observed during training.