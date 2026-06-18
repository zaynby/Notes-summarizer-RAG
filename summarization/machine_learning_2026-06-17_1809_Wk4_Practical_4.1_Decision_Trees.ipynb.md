# Wk4_Practical_4.1_Decision_Trees.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

# Week 4.2 Practical - Decision Trees  
**Module:** machine_learning  
**Style:** structured_academic  

---

### [[Decision Tree Classifier]]  
**Definition**: A supervised learning algorithm that constructs a tree model for classification tasks by splitting data into homogeneous subgroups based on feature conditions.  
**Formula**: N/A  
**Example**: Classified Titanic passenger survival using features like `Fare` and `Age`, achieving 85% testing accuracy after hyperparameter tuning.  

---

### [[Decision Tree Regressor]]  
**Definition**: A regression algorithm that predicts continuous values by averaging target values in terminal nodes of a decision tree.  
**Formula**: N/A  
**Example**: Predicted noisy quadratic data ($y = 4*(X - 0.5)^2 + \text{noise}$) with $R^2 = 0.85$ on test data.  

---

### [[GridSearchCV]]  
**Definition**: A systematic hyperparameter tuning method that evaluates all parameter combinations via cross-validation to identify optimal values.  
**Formula**: N/A  
**Example**: Optimized `DecisionTreeClassifier` by testing `criterion` (gini/entropy), `max_depth` (2-7), and `min_samples_leaf` (1/5/10), improving accuracy from 75% to 85%.  

---

### [[Hyperparameters]]  
**Definition**: Pre-set parameters controlling the structure of a decision tree model (e.g., `max_depth`, `min_samples_leaf`).  
**Formula**: N/A  
**Example**: GridSearch optimized hyperparameters for Titanic classification: `criterion='gini'`, `max_depth=3`, `min_samples_leaf=1`.  

---

### [[Mean Squared Error (MSE)]]  
**Definition**: Average squared difference between actual and predicted values, penalizing large errors.  
**Formula**:  
\[ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2 \]  
**Example**: Regression model achieved $\text{MSE} = 0.12$ on test data after tuning.  

---

### [[R-squared ($R^2$)]]  
**Definition**: Measures how well the model explains variance in the target variable (0 = no fit, 1 = perfect fit).  
**Formula**:  
\[ R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} \]  
**Example**: Decision Tree Regressor achieved $R^2 = 0.85$ on test data.  

---

### [[Cross-Validation]]  
**Definition**: Technique to assess model performance by partitioning data into folds, training on subsets, and validating on held-out folds.  
**Formula**: N/A  
**Example**: Used 10-fold cross-validation (`cv=10`) in `GridSearchCV` for hyperparameter tuning.  

---

### [[Training Accuracy]]  
**Definition**: Proportion of correct predictions on the training dataset.  
**Formula**:  
\[ \text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}} \]  
**Example**: Optimized model achieved 92% training accuracy after GridSearch.  

---

### [[Testing Accuracy]]  
**Definition**: Proportion of correct predictions on unseen test data, reflecting model generalization.  
**Formula**: Same as Training Accuracy  
**Example**: Final Decision Tree Classifier achieved 85% testing accuracy.  

---

### [[Overfitting]]  
**Definition**: Occurs when a model performs exceptionally well on training data but poorly on unseen data due to excessive complexity.  
**Formula**: N/A  
**Example**: Initial Decision Tree Classifier had 90% training accuracy but only 75% testing accuracy before pruning.  

---

### [[Feature Importance]]  
**Definition**: Relative contribution of each feature to the model's predictions.  
**Formula**: N/A  
**Example**: In the Titanic dataset, `Fare` and `Sex` were top features influencing survival predictions.  

---

### [[K-Fold Cross Validation]]  
**Definition**: Cross-validation method that splits data into *K* folds, training on *K-1* folds and validating on the remaining fold iteratively.  
**Formula**: N/A  
**Example**: Used 5-fold cross-validation (`cv=5`) to evaluate Decision Tree Classifier performance.  

---

### [[Decision Tree Visualization]]  
**Definition**: Graphical representation of a decision tree showing nodes, splits, and terminal leaves.  
**Formula**: N/A  
**Example**: Visualized Titanic survival model using `tree.plot_tree()` to show splits on features like `Fare` and `Age`.  

---

### Linked Concepts:  
- [[Supervised Learning]]  
- [[Classification]]  
- [[Regression]]  
- [[Hyperparameter Tuning]]  
- [[Model Evaluation]]  
- [[Overfitting]]  
- [[Cross-Validation]]  

This summary captures key concepts from the notebook, linking them via wikilinks for cross-referencing. Each term includes a concise definition, formula (where applicable), and practical examples from the exercises.