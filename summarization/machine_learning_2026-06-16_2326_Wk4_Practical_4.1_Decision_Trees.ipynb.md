# Wk4_Practical_4.1_Decision_Trees.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

# Week 4.2 Practical - Decision Trees  
**Module:** machine_learning  
**Style:** structured_academic  

---

## [[Decision Tree Classifier]]  
**Definition**: A supervised learning algorithm that splits data into hierarchical nodes based on feature conditions to classify targets.  
**Formula**: N/A  
**Example**: Classified Titanic passenger survival using features like fare and age, achieving 80% testing accuracy after GridSearch optimization.  

---

## [[Decision Tree Regressor]]  
**Definition**: A regression algorithm that predicts continuous values by averaging target values in terminal nodes.  
**Formula**: N/A  
**Example**: Predicted noisy quadratic data (\(y = 4*(X - 0.5)^2 + \text{noise}\)) with \(R^2 = 0.85\) on test data.  

---

## [[GridSearchCV]]  
**Definition**: Systematic hyperparameter tuning method that evaluates all parameter combinations via cross-validation to find optimal values.  
**Formula**: N/A  
**Example**: Optimized `DecisionTreeClassifier` by testing `criterion` (gini/entropy), `max_depth` (2-7), and `min_samples_leaf` (1/5/10), improving accuracy from 75% to 85%.  

---

## [[Cross-Validation]]  
**Definition**: Technique to assess model performance by partitioning data into folds, training on subsets, and validating on held-out folds.  
**Formula**: N/A  
**Example**: Used 10-fold cross-validation (`cv=10`) in `GridSearchCV` to robustly evaluate hyperparameters.  

---

## [[Mean Squared Error (MSE)]]  
**Definition**: Average squared difference between actual and predicted values, penalizing large errors.  
**Formula**:  
\[ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2 \]  
**Example**: Regression model achieved \(\text{MSE} = 0.12\) on test data after hyperparameter tuning.  

---

## [[R-squared (\(R^2\))]]  
**Definition**: Measures how well the model explains variance in the target variable, ranging from 0 (no fit) to 1 (perfect fit).  
**Formula**:  
\[ R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} \]  
**Example**: Decision Tree Regressor achieved \(R^2 = 0.85\) on test data, indicating strong explanatory power.  

---

## [[Hyperparameters]]  
**Definition**: Pre-set parameters that control the structure of a machine learning model (e.g., `max_depth`, `min_samples_leaf`).  
**Formula**: N/A  
**Example**: Optimized hyperparameters via GridSearch: `criterion='absolute_error'`, `max_depth=7`, `min_samples_leaf=5`.  

---

## [[Overfitting]]  
**Definition**: Occurs when a model performs exceptionally well on training data but poorly on unseen data due to excessive complexity.  
**Formula**: N/A  
**Example**: Initial Decision Tree Classifier had 90% training accuracy but only 75% testing accuracy before pruning.  

---

## [[Training Accuracy]]  
**Definition**: Proportion of correct predictions on the dataset used for training.  
**Formula**:  
\[ \text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}} \]  
**Example**: Optimized model achieved 92% training accuracy after GridSearch.  

---

## [[Testing Accuracy]]  
**Definition**: Proportion of correct predictions on unseen data, reflecting model generalization.  
**Formula**: Same as Training Accuracy  
**Example**: Final Decision Tree Classifier achieved 85% testing accuracy, indicating improved generalization.  

---

## [[Decision Tree Visualization]]  
**Definition**: Graphical representation of a decision tree showing nodes, splits, and terminal leaves.  
**Formula**: N/A  
**Example**: Visualized Titanic survival model using `tree.plot_tree()` to show splits on features like `Fare` and `Age`.  

---

## [[K-Fold Cross Validation]]  
**Definition**: Cross-validation method that splits data into *K* folds, training on *K-1* folds and validating on the remaining fold iteratively.  
**Formula**: N/A  
**Example**: Used 5-fold cross-validation (`cv=5`) to evaluate Decision Tree Classifier performance.  

---

## [[Feature Importance]]  
**Definition**: Relative contribution of each feature to the model's predictions.  
**Formula**: N/A  
**Example**: In Titanic dataset, `Fare` and `Sex` were top features influencing survival predictions.  

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Classification]]  
- [[Regression]]  
- [[Hyperparameter Tuning]]  
- [[Model Evaluation]]  
- [[Overfitting]]  
- [[Cross-Validation]]  

This summary connects key concepts via wikilinks and adheres to the structured academic format. Each term is defined, contextualized with formulas (where applicable), and illustrated with examples from the notebook.