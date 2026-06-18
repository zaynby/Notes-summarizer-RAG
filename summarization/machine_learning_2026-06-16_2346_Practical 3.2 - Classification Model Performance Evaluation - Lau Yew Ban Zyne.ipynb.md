# Practical 3.2 - Classification Model Performance Evaluation - Lau Yew Ban Zyne.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

### Performance Evaluation in Machine Learning

#### Accuracy
**Definition:** Proportion of total correct predictions.
\[ \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} \]
**Interpretation:** Overall correctness, but can be misleading in imbalanced datasets.

#### Precision
**Definition:** Ratio of correctly predicted positive instances to the total predicted as positive.
\[ \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} \]
**Interpretation:** Indicates the proportion of true positives among all positive predictions.

#### Recall (Sensitivity)
**Definition:** Ratio of correctly predicted positive instances to the total actual positive cases.
\[ \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} \]
**Interpretation:** Indicates how many true positives are identified out of all actual positives.

#### F1-score
**Definition:** Harmonic mean of Precision and Recall.
\[ \text{F1-score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} \]
**Interpretation:** Balances the trade-off between Precision and Recall.

#### ROC Curve
- **True Positive Rate (TPR):** \( \text{TPR} = \frac{\text{TP}}{\text{TP} + \text{FN}} \)
- **False Positive Rate (FPR):** \( \text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}} \)

**Significance:** Illustrates the trade-off between TPR and FPR at various classification thresholds.

#### Area Under the Curve (AUC)
- **Definition:** Single scalar value summarizing model performance across all possible classification thresholds.
\[ \text{AUC} = \int_{0}^{1} \text{TPR}(fpr) \, dfpr \]
- **Interpretation:**
  - AUC of 1.0 represents a perfect classifier.
  - AUC of 0.5 indicates random guessing.
  - Lower than 0.5 suggests the model is worse than random guessing.

### Example Implementation

```python
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Load dataset and summarize class distribution
breast_cancer = load_breast_cancer()
X, y = breast_cancer.data, breast_cancer.target
counter = Counter(y)
print("Original Dataset Class Distribution:", counter)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Define and train Logistic Regression model
lg = LogisticRegression(solver='lbfgs', max_iter=10000)
lg.fit(X_train, y_train)

# Predictions on training set
y_fitted = lg.predict(X_train)  
accuracy_train  = accuracy_score(y_train, y_fitted)
precision_train = precision_score(y_train, y_fitted)
recall_train    = recall_score(y_train, y_fitted)
f1_train        = f1_score(y_train, y_fitted)

# Predictions on testing set
y_test_pred = lg.predict(X_test)  
accuracy_test  = accuracy_score(y_test, y_test_pred)
precision_test = precision_score(y_test, y_test_pred)
recall_test    = recall_score(y_test, y_test_pred)
f1_test        = f1_score(y_test, y_test_pred)

print(f"{'Metric':15} {'Training Set':15} {'Testing Set':15}")
print(f"{'Accuracy':15} {accuracy_train:<15.2f} {accuracy_test:<15.2f}")
print(f"{'Precision':15} {precision_train:<15.2f} {precision_test:<15.2f}")
print(f"{'Recall':15} {recall_train:<15.2f} {recall_test:<15.2f}")
print(f"{'F1-score':15} {f1_train:<15.2f} {f1_test:<15.2f}")

# Get predicted probabilities for positive class
y_fitted_prob = lg.predict_proba(X_train)[:, 1]

# Calculate ROC curve and AUC score
fpr, tpr, thresholds = roc_curve(y_train, y_fitted_prob)
auc_score = roc_auc_score(y_train, y_fitted_prob)

print(f"AUC Score: {auc_score:.2f}")

# Plot the ROC curve
plt.plot(fpr, tpr, label=f'ROC curve (AUC ={auc_score:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
```

### Explanation
- **Accuracy:** Overall correctness of the model.
- **Precision:** Proportion of true positives among all predicted positives.
- **Recall (Sensitivity):** Proportion of actual positives correctly identified.
- **F1-score:** Harmonic mean of Precision and Recall, providing a balanced measure.
- **ROC Curve & AUC:** Visual representation of the trade-off between TPR and FPR, with AUC summarizing overall model performance.

This implementation demonstrates how to evaluate a logistic regression model using various metrics and visualize its performance through ROC curves.