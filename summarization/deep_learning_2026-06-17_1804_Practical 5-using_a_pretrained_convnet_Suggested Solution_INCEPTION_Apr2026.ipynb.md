# Practical 5-using_a_pretrained_convnet_Suggested Solution_INCEPTION_Apr2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Transfer Learning with Pretrained Models (InceptionV3)

**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

## **Transfer Learning**  
**Definition**: Technique where a pre-trained model (trained on a large dataset like ImageNet) is adapted to a new but related task.  
**Formula**: N/A  
**Example**: Utilizing InceptionV3 (pre-trained on ImageNet) for cats vs. dogs classification.  
**[[Wikilink]]**: [[Feature Extraction]], [[Fine-tuning]]  

---

## **Feature Extraction**  
**Definition**: Process of using a pre-trained model’s convolutional base to extract features from new data, then training a classifier on those features.  
**Formula**: N/A  
**Example**: Extracting features from InceptionV3’s output (shape `(3, 3, 2048)`) and flattening them for dense layers (Code Cell 11).  
**[[Wikilink]]**: [[Transfer Learning]], [[Convolutional Neural Network (ConvNet)]]  

---

## **Data Augmentation**  
**Definition**: Technique to artificially expand dataset diversity by applying random transformations (e.g., flipping, rotation) to training images.  
**Formula**: N/A  
**Example**: Applying `RandomFlip`, `RandomRotation`, and `RandomZoom` in Code Cell 25 to reduce overfitting.  
**[[Wikilink]]**: [[Overfitting]], [[Transfer Learning]]  

---

## **Fine-tuning**  
**Definition**: Process of unfreezing and retraining some layers of a pre-trained model to adapt to a new task.  
**Formula**: N/A  
**Example**: Unfreezing layers from `mixed6` in InceptionV3 (Code Cell 33) and training with a low learning rate (`2e-5`).  
**[[Wikilink]]**: [[Transfer Learning]], [[Feature Extraction]]  

---

## **Convolutional Neural Network (ConvNet)**  
**Definition**: Deep learning architecture designed for grid-like data (e.g., images), using convolutional layers to extract spatial hierarchies of features.  
**Formula**: Output width = $\frac{W - F + 2P}{S} + 1$ (W = input width, F = filter size, P = padding, S = stride)  
**Example**: InceptionV3’s convolutional base used for feature extraction (Code Cell 4).  
**[[Wikilink]]**: [[Transfer Learning], [Feature Extraction]]  

---

## **Adam Optimizer**  
**Definition**: Adaptive learning rate optimizer combining momentum and RMSProp to adjust weights efficiently.  
**Formula**: N/A (uses adaptive learning rates with parameters `beta_1` and `beta_2`).  
**Example**: Compiled with `learning_rate=2e-5` for fine-tuning (Code Cell 34).  
**[[Wikilink]]**: [[Learning Rate]]  

---

## **Overfitting**  
**Definition**: Phenomenon where a model performs well on training data but poorly on validation/test data due to memorizing noise.  
**Formula**: N/A  
**Example**: Initial feature extraction model showed a gap between training (95%) and validation (62%) accuracy (Markdown Cell 17).  
**[[Wikilink]]**: [[Data Augmentation], [Fine-tuning]]  

---

## **Dropout**  
**Definition**: Regularization technique that randomly deactivates a fraction of neurons during training to prevent overfitting.  
**Formula**: N/A  
**Example**: Added `Dropout(0.5)` in the classifier (Code Cell 13).  
**[[Wikilink]]**: [[Overfitting], [Feature Extraction]]  

---

## **Binary Crossentropy Loss**  
**Definition**: Loss function for binary classification problems, measuring the difference between predicted probabilities and true labels.  
**Formula**:  
$$
\text{Loss} = -\frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]
$$  
**Example**: Used in model compilation (Code Cell 14).  
**[[Wikilink]]**: [[Loss Functions]]  

---

## **Key Observations**  
1. **Feature Extraction**:  
   - Training accuracy reached ~95%, but validation accuracy plateaued at ~62% (Markdown Cell 17).  
   - Indicates the model learned useful features but had a generalization gap.  

2. **Data Augmentation**:  
   - Reduced overfitting by narrowing the training-validation accuracy gap (Markdown Cell 29).  

3. **Fine-tuning**:  
   - Validation loss began rising after epoch 17, suggesting overfitting (Markdown Cell 40).  
   - Required careful tuning of learning rate and trainable layers.  

---

## **[[Wikilinks]]**  
- [[Transfer Learning]] → [[Feature Extraction]], [[Fine-tuning]]  
- [[Convolutional Neural Network (ConvNet)]] → [[Feature Extraction]]  
- [[Overfitting]] → [[Data Augmentation]], [[Dropout]]  
- [[Adam Optimizer]] → [[Learning Rate]]  
- [[Binary Crossentropy Loss]] → [[Loss Functions]]  
- [[Data Augmentation]] → [[Transfer Learning]]  
- [[Fine-tuning]] → [[Transfer Learning]], [[Convolutional Neural Network (ConvNet)]]  

This summary integrates transfer learning techniques (feature extraction, data augmentation, fine-tuning) with practical observations from training InceptionV3 on a small dataset.