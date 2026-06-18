# Practical_3-Overfitting-and-Underfitting_Apr2026_[student_name].ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Overfitting and Underfitting  
**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

## **Overfitting**  
**Definition**: Phenomenon where a model learns training data too well, including noise, leading to poor performance on validation/test data.  
**Formula**: N/A  
**Example**: The "bigger model" (512 units) achieved near-zero training loss but validation loss remained high (Code Cell 21).  
**[[Wikilink]]**: [[Model Capacity]], [[Weight Regularization]], [[Dropout]]  

---

## **Underfitting**  
**Definition**: Model is too simple to capture underlying patterns in the data, leading to poor performance on both training and validation sets.  
**Formula**: N/A  
**Example**: A model with insufficient layers/units (e.g., 2 layers of 4 units) may fail to learn complex relationships in IMDB reviews.  
**[[Wikilink]]**: [[Model Capacity]], [[Bias-Variance Tradeoff]]  

---

## **Model Capacity**  
**Definition**: Ability of a model to learn patterns, determined by the number of layers, units, and connections.  
**Formula**: N/A  
**Example**:  
- **High Capacity**: `bigger_model` with 512-unit layers (Code Cell 18).  
- **Low Capacity**: `smaller_model` with 4-unit layers (Code Cell 11).  
**[[Wikilink]]**: [[Overfitting]], [[Underfitting]]  

---

## **Weight Regularization (L1/L2)**  
**Definition**: Technique to penalize large weights in the model to prevent overfitting.  
**Formula**:  
- **L1 Regularization**: Loss += λ∑|W|  
- **L2 Regularization**: Loss += λ∑W²  
**Example**: `l2(0.002)` applied to kernel weights in `l2_model` (Code Cell 26).  
**[[Wikilink]]**: [[Overfitting]], [[Dropout]]  

---

## **Dropout**  
**Definition**: Regularization technique that randomly deactivates neurons during training to improve generalization.  
**Formula**: N/A  
**Example**: `layers.Dropout(0.5)` in `dpt_model` (Code Cell 34).  
**[[Wikilink]]**: [[Overfitting], [Weight Regularization]]  

---

## **Validation Loss**  
**Definition**: Loss computed on the validation set during training, used to monitor overfitting.  
**Formula**: Typically same as training loss (e.g., binary crossentropy).  
**Example**: Comparison of validation losses for original vs. smaller models (Code Cell 16).  
**[[Wikilink]]**: [[Overfitting]], [[Generalization]]  

---

## **Generalization**  
**Definition**: Model’s ability to perform well on unseen data by learning robust patterns.  
**Formula**: N/A  
**Example**: The `dpt_model` with dropout achieved lower validation loss than the original model (Code Cell 37).  
**[[Wikilink]]**: [[Overfitting], [Validation Loss]]  

---

## **Key Observations**  
1. **Model Size vs. Overfitting**:  
   - Larger models (high capacity) overfit faster (e.g., `bigger_model`).  
   - Smaller models generalize better but may underfit if too simple.  
2. **Regularization Techniques**:  
   - **L2 Regularization**: Reduced overfitting compared to the original model (Code Cell 30).  
   - **Dropout**: Improved validation loss by 15–20% in experiments.  
3. **Training Dynamics**:  
   - High-capacity models achieve lower training loss faster but suffer from severe overfitting.  
   - Regularized models show slower training loss reduction but better validation performance.  

---

## **[[Wikilinks]]**  
- [[Overfitting]] → [[Model Capacity]], [[Weight Regularization]], [[Dropout]]  
- [[Underfitting]] → [[Model Capacity]]  
- [[Weight Regularization]] → [[L1 Regularization]], [[L2 Regularization]]  
- [[Dropout]] → [[Overfitting]]  
- [[Validation Loss]] → [[Generalization]]  
- [[Model Capacity]] → [[Overfitting]], [[Underfitting]]  

This summary integrates theoretical concepts with practical implementation details from the notebook, emphasizing techniques to balance model capacity and regularization for improved generalization.