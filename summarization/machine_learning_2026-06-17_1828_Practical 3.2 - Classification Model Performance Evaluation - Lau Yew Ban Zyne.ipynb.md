# Practical 3.2 - Classification Model Performance Evaluation - Lau Yew Ban Zyne.ipynb
**Module:** machine_learning
**Style:** structured_academic (experimenting)

### Machine Learning - Practical 2.2: Classification Performance Metrics

#### Term -> Definition -> Formula -> Example

---

**Accuracy**

- **Definition:** Proportion of total correct predictions.
- **Formula:** 
  \[
  \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{FP} + \text{FN} + \text{TN}}
  \]
- **Example:**
  ```python
  accuracy_train = accuracy_score(y_train, y_fitted)
  print(f"Accuracy (Training Set): {accuracy_train:.2f}")
  ```

---

**Precision**

- **Definition:** Ratio of correctly predicted positive instances to the total predicted as positive.
- **Formula:** 
  \[
  \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
  \]
- **Example:**
  ```python
  precision_train = precision_score(y_train, y_fitted)
  print(f"Precision (Training Set): {precision_train:.2f}")
  ```

---

**Recall**

- **Definition:** Ratio of correctly predicted positive instances to the total actual positive.
- **Formula:** 
  \[
  \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
  \]
- **Example:**
  ```python
  recall_train = recall_score(y_train, y_fitted)
  print(f"Recall (Training Set): {recall_train:.2f}")
  ```

---

**F1-score**

- **Definition:** Harmonic mean of Precision and Recall.
- **Formula:** 
  \[
  \text{F1-score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
  \]
- **Example:**
  ```python
  f1_train = f1_score(y_train, y_fitted)
  print(f"F1-score (Training Set): {f1_train:.2f}")
  ```

---

**ROC Curve and Area Under the Curve (AUC)**

- **True Positive Rate (TPR) / Sensitivity:**
  \[
  \text{TPR} = \frac{\text{TP}}{\text{TP} + \text{FN}}
  \]
- **False Positive Rate (FPR):**
  \[
  \text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}
  \]
- **Significance:**
  - The ROC curve shows the trade-off between TPR and FPR at various threshold settings.
  - AUC summarizes the overall performance of a binary classifier across all possible classification thresholds.

---

**Example Code for ROC Curve and AUC Calculation**

```python
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_curve, roc_auc_score

# Load the dataset
breast_cancer = load_breast_cancer()
X, y = breast_cancer.data, breast_cancer.target

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Define and train a LogisticRegression model
lg = LogisticRegression(solver='lbfgs', max_iter=10000)
lg.fit(X_train, y_train)

# Predictions on training set
y_fitted = lg.predict(X_train)
y_test_pred = lg.predict(X_test)

# Calculate performance metrics for both sets
accuracy_train  = accuracy_score(y_train, y_fitted)
precision_train = precision_score(y_train, y_fitted)
recall_train    = recall_score(y_train, y_fitted)
f1_train        = f1_score(y_train, y_fitted)

accuracy_test  = accuracy_score(y_test, y_test_pred)
precision_test = precision_score(y_test, y_test_pred)
recall_test    = recall_score(y_test, y_test_pred)
f1_test        = f1_score(y_test, y_test_pred)

print(f"{'Metric':15} {'Training Set':15} {'Testing Set':15}")
print(f"{'Accuracy':15} {accuracy_train:<15.2f} {accuracy_test:<15.2f}")
print(f"{'Precision':15} {precision_train:<15.2f} {precision_test:<15.2f}")
print(f"{'Recall':15} {recall_train:<15.2f} {recall_test:<15.2f}")
print(f"{'F1-score':15} {f1_train:<15.2f} {f1_test:<15.2f}")

# Get the predicted probabilities for positive class
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

This code snippet demonstrates how to calculate and visualize the performance metrics (accuracy, precision, recall, F1-score) and the ROC curve for a logistic regression model trained on the Breast Cancer dataset.