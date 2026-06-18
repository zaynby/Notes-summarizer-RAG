# Practical_3-Overfitting-and-Underfitting_Solution_Apr2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Deep Learning Practical: Overfitting and Underfitting  

**Module:** deep_learning  
**Style:** structured_academic (experimenting)  

---

## **Overfitting**  
**Definition**: Phenomenon where a model learns training data too well, including noise, leading to poor performance on unseen data.  
**Formula**: N/A  
**Example**: Original model achieved near-zero training loss but validation loss increased to ~0.98 by epoch 20 (Code Cell 23).  
**[[Wikilink]]**: [[Underfitting]], [[Weight Regularization]], [[Dropout]]  

---

## **Underfitting**  
**Definition**: Model is too simple to capture underlying patterns in the data, leading to poor performance on both training and validation data.  
**Formula**: N/A  
**Example**: A model with excessively few layers/neurons might show high training and validation loss.  
**[[Wikilink]]**: [[Overfitting]], [[Model Capacity]]  

---

## **Model Capacity**  
**Definition**: Ability of a model to learn complex patterns, determined by its architecture (e.g., number of layers, neurons).  
**Formula**: N/A  
**Example**:  
- **High Capacity**: `Dense(512)` layers in `bigger_model` overfit severely (Code Cell 18).  
- **Low Capacity**: `Dense(4)` layers in `smaller_model` overfit later and less severely (Code Cell 11).  
**[[Wikilink]]**: [[Overfitting]], [[Underfitting]]  

---

## **Weight Regularization (L1/L2)**  
**Definition**: Technique to penalize large weights in the model, reducing overfitting.  
**Formula**:  
- **L2 Regularization**: Loss = Original Loss + λ * Σ(weights²)  
- **L1 Regularization**: Loss = Original Loss + λ * Σ|weights|  
**Example**: `kernel_regularizer=l2(0.002)` in `l2_model` reduced validation loss compared to the original model (Code Cell 26).  
**[[Wikilink]]**: [[Dropout]], [[Overfitting]]  

---

## **Dropout**  
**Definition**: Regularization technique that randomly deactivates neurons during training to prevent overfitting.  
**Formula**: N/A (outputs are scaled by `(1 - dropout_rate)` at test time).  
**Example**: `layers.Dropout(0.5)` in `dpt_model` improved validation loss stability (Code Cell 34).  
**[[Wikilink]]**: [[Weight Regularization]], [[Overfitting]]  

---

## **Validation Loss vs. Training Loss**  
**Definition**:  
- **Training Loss**: Error on the data used to train the model.  
- **Validation Loss**: Error on unseen data during training.  
**Formula**: N/A  
**Example**:  
- Original model: Training loss ≈ 0, Validation loss ≈ 0.98 (Code Cell 23).  
- Regularized model (`s_model`): Training loss ≈ 0.1, Validation loss ≈ 0.52 (Code Cell 42).  
**[[Wikilink]]**: [[Overfitting]]  

---

## **Universal Workflow of Machine Learning**  
**Definition**: Systematic approach to building ML models: data preparation, model building, training, evaluation, and tuning.  
**Formula**: N/A  
**Example**: Student exercise (Code Cells 40–43) involved building a model with dropout, L2 regularization, and hyperparameter tuning.  
**[[Wikilink]]**: [[Model Capacity]], [[Weight Regularization]]  

---

## **Key Observations**  
1. **Model Size vs. Overfitting**:  
   - Smaller networks (e.g., `smaller_model`) overfit later and less severely.  
   - Larger networks (e.g., `bigger_model`) overfit quickly and severely.  
2. **Regularization Techniques**:  
   - **L2 Regularization**: Penalizes large weights, improving generalization.  
   - **Dropout**: Reduces reliance on specific neurons, lowering validation loss.  
3. **Combined Techniques**: The student model (`s_model`) using dropout (0.5) and L2 regularization (0.001) achieved better validation loss (0.52 vs. 0.98) compared to the original model.  

---

## **[[Wikilinks]]**  
- [[Overfitting]] → [[Underfitting]], [[Model Capacity]], [[Weight Regularization]], [[Dropout]]  
- [[Weight Regularization]] → [[Dropout]], [[Overfitting]]  
- [[Dropout]] → [[Weight Regularization]], [[Overfitting]]  
- [[Model Capacity]] → [[Overfitting]], [[Underfitting]]  
- [[Validation Loss]] → [[Training Loss]], [[Overfitting]]  
- [[Universal Workflow of Machine Learning]] → [[Model Capacity]], [[Weight Regularization]]  

This summary connects strategies to mitigate overfitting (e.g., regularization, dropout, capacity adjustment) with empirical results from the practical exercise.