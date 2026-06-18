# Practical 5-using_a_pretrained_convnet_Suggested Solution_INCEPTION_Apr2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Transfer Learning with Pre-trained Models  

## **Transfer Learning**  
**Definition**: Technique where a pre-trained model (trained on a large dataset) is adapted to a new, related task.  
**Example**: Using InceptionV3 (pre-trained on ImageNet) for binary classification of cats vs. dogs.  
**[[Wikilink]]**: [[Pre-trained Model]]  

---

## **Pre-trained Model**  
**Definition**: A neural network trained on a large-scale dataset (e.g., ImageNet) with learned weights that capture general features.  
**Examples**:  
- **InceptionV3**: 299-layer architecture for image classification.  
- **VGG19**: 19-layer model with uniform 3x3 filters.  
**[[Wikilink]]**: [[Transfer Learning]]  

---

## **Feature Extraction**  
**Definition**: Using the convolutional layers of a pre-trained model to extract high-level features from new data.  
**Process**:  
1. Freeze the pre-trained convolutional base.  
2. Replace the top classifier.  
3. Train the new classifier on the extracted features.  
**Example**: Extracting features from InceptionV3’s output (shape `(3, 3, 2048)`) for cats/dogs classification.  
**[[Wikilink]]**: [[Convolutional Base]]  

---

## **Convolutional Base**  
**Definition**: The stack of convolutional and pooling layers in a pre-trained model that learns spatial hierarchies (edges → textures → objects).  
**Example**: InceptionV3’s convolutional base outputs a feature map of shape `(3, 3, 2048)`.  
**[[Wikilink]]**: [[Feature Extraction]]  

---

## **Dense Classifier**  
**Definition**: Fully connected layers added on top of the convolutional base for task-specific classification.  
**Formula**:  
- Input: Flattened feature vector (e.g., `3*3*2048 = 18432` dimensions).  
- Output: Sigmoid activation for binary classification.  
**Example**:  
```python  
model.add(layers.Dense(256, activation='relu'))  
model.add(layers.Dense(1, activation='sigmoid'))  
```  
**[[Wikilink]]**: [[Neural Network]]  

---

## **Data Augmentation**  
**Definition**: Applying random transformations (e.g., flips, rotations) to training data to reduce overfitting and improve generalization.  
**Techniques**:  
- `RandomFlip("horizontal")`  
- `RandomRotation([-0.1, 0.1])`  
- `RandomZoom(0.2)`  
**Example**: Augmenting cats/dogs dataset with 5 transformation layers.  
**[[Wikilink]]**: [[Overfitting]]  

---

## **Fine-Tuning**  
**Definition**: Unfreezing select layers of a pre-trained model and training them on the new task with a low learning rate.  
**Process**:  
1. Set `trainable=True` for specific layers (e.g., after `mixed6` in InceptionV3).  
2. Compile with a low learning rate (e.g., `2e-5`).  
**Example**: Fine-tuning InceptionV3 layers after `mixed6` for cats/dogs classification.  
**[[Wikilink]]**: [[Transfer Learning]]  

---

## **Learning Rate (Fine-Tuning)**  
**Definition**: Hyperparameter controlling the step size during optimization. A low value (e.g., `2e-5`) is used in fine-tuning to avoid disrupting pre-trained weights.  
**Formula**:  
```python  
optimizer = optimizers.Adam(learning_rate=2e-5)  
```  
**Example**: Preventing overfitting during fine-tuning by limiting weight updates.  
**[[Wikilink]]**: [[Optimizer]]  

---

## **Model Evaluation Metrics**  
**Definition**: Metrics like accuracy and loss curves used to assess model performance.  
**Observations**:  
- **Feature Extraction**: High training accuracy (~95%) but lower validation accuracy (~62%), indicating overfitting.  
- **With Data Augmentation**: Reduced gap between training and validation accuracy.  
- **Fine-Tuning**: Validation loss increased after epoch 17, suggesting overfitting.  
**Example**: Plotting accuracy/loss curves for cats/dogs classification.  
**[[Wikilink]]**: [[Loss Functions]]  

---

## **[[Wikilinks]]**  
- [[Transfer Learning]] → [[Pre-trained Model]], [[Feature Extraction]]  
- [[Convolutional Base]] → [[Fine-Tuning]], [[Convolutional Neural Network (ConvNet)]]  
- [[Data Augmentation]] → [[Overfitting]]  
- [[Fine-Tuning]] → [[Learning Rate]]  

This summary integrates practical implementation details and theoretical insights from the exercises, emphasizing the iterative process of transfer learning, feature extraction, and model optimization.