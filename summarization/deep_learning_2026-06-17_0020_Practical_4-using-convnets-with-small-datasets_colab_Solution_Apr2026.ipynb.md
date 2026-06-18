# Practical_4-using-convnets-with-small-datasets_colab_Solution_Apr2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Training a ConvNet for Image Classification (Cats vs. Dogs)  
**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

## **Convolutional Neural Network (ConvNet)**  
**Definition**: A deep learning architecture designed for grid-like data (e.g., images), using convolutional layers to extract spatial hierarchies of features.  
**Formula**: N/A  
**Example**: The model in Code Cell 9 with alternating `Conv2D` and `MaxPooling2D` layers for cats vs. dogs classification.  
**[[Wikilink]]**: [[Data Augmentation]], [[Overfitting]]  

---

## **Data Augmentation**  
**Definition**: Technique to artificially expand dataset diversity by applying random transformations (e.g., flipping, rotation) to training images.  
**Formula**: N/A  
**Example**: Layers like `RandomFlip`, `RandomRotation`, and `RandomZoom` in Code Cell 26 to augment the cats/dogs dataset.  
**[[Wikilink]]**: [[Overfitting]], [[Convolutional Neural Network (ConvNet)]]  

---

## **Overfitting**  
**Definition**: Phenomenon where a model performs well on training data but poorly on validation/test data due to memorizing noise.  
**Formula**: N/A  
**Example**: Initial model (Code Cell 9) achieved 99% training accuracy but only ~73% validation accuracy.  
**[[Wikilink]]**: [[Data Augmentation]], [[Dropout]]  

---

## **Dropout**  
**Definition**: Regularization technique that randomly deactivates a fraction of neurons during training to prevent overfitting.  
**Formula**: N/A  
**Example**: Adding `Dropout(0.5)` before the dense classifier in Code Cell 30 reduced validation loss from 0.98 to 0.52.  
**[[Wikilink]]**: [[Overfitting], [Weight Regularization]]  

---

## **Adam Optimizer**  
**Definition**: Adaptive learning rate optimizer combining momentum and RMSProp to adjust weights efficiently.  
**Formula**: N/A (uses adaptive learning rates with parameters `beta_1` and `beta_2`).  
**Example**: Compiled with `learning_rate=1e-4` in Code Cell 13.  
**[[Wikilink]]**: [[Learning Rate]]  

---

## **Binary Crossentropy Loss**  
**Definition**: Loss function for binary classification problems, measuring the difference between predicted probabilities and true labels.  
**Formula**:  
$$
\text{Loss} = -\frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]
$$  
**Example**: Used in model compilation (Code Cell 13) for cats vs. dogs classification.  
**[[Wikilink]]**: [[Loss Functions]]  

---

## **Batch Size**  
**Definition**: Number of samples processed before updating model weights during training.  
**Formula**: N/A  
**Example**: **Scenario A** reduces batch size from 20 to 10 (Code Cell 39), resulting in noisier but more frequent weight updates.  
**[[Wikilink]]**: [[Learning Rate]]  

---

## **Learning Rate**  
**Definition**: Hyperparameter controlling the step size of weight updates during optimization.  
**Formula**: N/A  
**Example**: **Scenario B** increases learning rate from `1e-4` to `2e-4` (Code Cell 41), accelerating convergence but risking instability.  
**[[Wikilink]]**: [[Adam Optimizer]]  

---

## **Key Observations**  
1. **Baseline Model (No Regularization)**: Achieved 99% training accuracy but only ~73% validation accuracy due to severe overfitting.  
2. **Data Augmentation + Dropout**: Improved validation accuracy to ~80% by reducing overfitting (Code Cell 30).  
3. **Scenario A (Batch Size=10)**: Smaller batches introduced more noise into gradient updates, slowing convergence but improving generalization.  
4. **Scenario B (Learning Rate=2e-4)**: Higher learning rate sped up training but required careful monitoring to avoid divergence.  

---

## **[[Wikilinks]]**  
- [[Convolutional Neural Network (ConvNet)]] → [[Data Augmentation]], [[Overfitting]]  
- [[Overfitting]] → [[Data Augmentation]], [[Dropout]]  
- [[Adam Optimizer]] → [[Learning Rate]]  
- [[Batch Size]] → [[Learning Rate]]  
- [[Binary Crossentropy Loss]] → [[Loss Functions]]  
- [[Data Augmentation]] → [[Convolutional Neural Network (ConvNet)]]  
- [[Dropout]] → [[Overfitting]]