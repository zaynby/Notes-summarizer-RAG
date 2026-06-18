# Lecture 5 - CNN II_Apr 2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary: Convolutional Neural Networks (CNNs) & Transfer Learning  

## **Transfer Learning**  
**Definition**: A machine learning method where a pre-trained model (trained on a large dataset) is adapted to a new, related task.  
**Formula**: None (conceptual framework).  
**Example**: Using VGG16 (pre-trained on ImageNet) for a cats vs. dogs classification task by replacing the classifier layer.  
**Link**: [[Pre-trained ConvNet]]  

---

## **Pre-trained ConvNet**  
**Definition**: A convolutional neural network trained on a large dataset (e.g., ImageNet) that can be reused for new tasks.  
**Formula**: None (model architecture).  
**Example**: VGG16 (16-layer network), VGG19, ResNet50, Inception V3.  
**Key Features**:  
- Learns spatial hierarchies (edges → textures → object parts).  
- Reduces training time and data requirements.  
**Link**: [[Transfer Learning]]  

---

## **Feature Extraction**  
**Definition**: Using a pre-trained ConvNet to extract features from input data, then training a new classifier on those features.  
**Formula**:  
```  
Features = conv_base.predict(sample_images)  
```  
**Example**:  
1. Download VGG16 (`conv_base`) and remove its classifier layers.  
2. Use `conv_base.predict()` to extract features from cats/dogs images.  
3. Train a fully connected (FC) classifier on the extracted features.  
**Link**: [[Freezing Layers]]  

---

## **Freezing Layers**  
**Definition**: Disabling weight updates for specific layers during training (e.g., keeping VGG16 layers fixed).  
**Formula**:  
```python  
conv_base.trainable = False  # Freeze layers  
```  
**Example**: Freezing all VGG16 layers except the custom classifier during feature extraction.  
**Purpose**: Prevents overwriting pre-trained weights.  
**Link**: [[Fine-Tuning]]  

---

## **Data Augmentation**  
**Definition**: Applying random transformations (e.g., rotation, zoom) to training images to increase dataset diversity.  
**Formula**: None (applied via generators in frameworks like Keras).  
**Example**: Augmenting cats/dogs images with rotations, flips, and zooms during training.  
**Benefits**: Reduces overfitting, improves generalization.  
**Link**: [[Overfitting]]  

---

## **Fine-Tuning**  
**Definition**: Unfreezing some layers of a pre-trained model and training them alongside the classifier for better task adaptation.  
**Formula**:  
```python  
conv_base.trainable = True  # Unfreeze  
```  
**Example**: Unfreezing VGG16’s Conv Block 5 (4 layers) to adapt high-level features for cats/dogs.  
**Outcome**: Improved validation accuracy (e.g., 98% in practical examples).  
**Link**: [[Transfer Learning]]  

---

## **VGG16**  
**Definition**: A 16-layer convolutional neural network architecture pre-trained on ImageNet.  
**Formula**: None (specific architecture).  
**Key Details**:  
- Uses 3x3 convolutional filters.  
- Available in `keras.applications`.  
**Example**: Used as a feature extractor or fine-tuned model in cats/dogs classification.  
**Link**: [[Pre-trained ConvNet]]  

---

## **Training Results Comparison**  
| **Method**                | **Training Accuracy** | **Validation Accuracy** | **Notes**                                  |  
|---------------------------|-----------------------|-------------------------|--------------------------------------------|  
| Feature Extraction (No Aug) | ~95%                 | ~93%                    | Fast convergence, minimal overfitting     |  
| Feature Extraction (With Aug) | ~95% (slower)       | ~93% (stable)           | Added noise improves generalization        |  
| Fine-Tuning                | ~98%                 | ~98%                    | High accuracy, requires GPU support        |  

---

## **Key Takeaways**  
1. **Pre-trained ConvNets** (e.g., VGG16) enable efficient image classification with limited data.  
2. **Feature Extraction** is faster but less adaptive than **Fine-Tuning**.  
3. **Data Augmentation** reduces overfitting and enhances robustness.  
4. **Fine-Tuning** balances performance and computational cost for complex tasks.  

**Further Reading**:  
- Chollet, F. *Deep Learning with Python* (Chapter 8).  
- [VGG16 Implementation Guide](https://medium.com/@priyanshnagar015/step-by-step-vgg16-implementation-in-keras-for-beginners-100-understanding-89c6789eb4b4)  

**Links**:  
- [[CNN]], [[Image Classification]], [[Overfitting]]