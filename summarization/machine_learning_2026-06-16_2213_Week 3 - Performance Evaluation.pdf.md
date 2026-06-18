# Week 3 - Performance Evaluation.pdf
**Module:** machine_learning
**Style:** structured_academic (experimenting)

# Machine Learning Model Evaluation Metrics

## [[Mean Absolute Error (MAE)]]
**Definition**: Measures the average absolute difference between actual and predicted values in regression tasks.  
**Formula**:  
\[
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)}|
\]  
**Example**: If true values are \([3, 5, 7]\) and predicted values are \([4, 4, 8]\), MAE = \(\frac{|3-4| + |5-4| + |7-8|}{3} = \frac{1 + 1 + 1}{3} = 1\).

---

## [[Root Mean Squared Error (RMSE)]]
**Definition**: Square root of the average squared differences between actual and predicted values, penalizing larger errors more heavily.  
**Formula**:  
\[
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}}^{(i)} - y_{\text{pred}}^{(i)})^2}
\]  
**Example**: Using the same values as MAE example, RMSE = \(\sqrt{\frac{(1^2 + 1^2 + 1^2)}{3}} = \sqrt{1} = 1\).

---

## [[R-Squared (R²)]]
**Definition**: Measures how well the model explains the variation in the target variable, ranging from 0 (no fit) to 1 (perfect fit).  
**Formula**:  
\[
R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}
\]  
Where \(\text{SS}_{\text{res}}\) = sum of squared residuals, \(\text{SS}_{\text{tot}}\) = total sum of squares.  
**Example**: A model with \(R^2 = 0.8\) explains 80% of the variance in the target variable.

---

## [[Accuracy]]
**Definition**: Proportion of total correct predictions (both true positives and true negatives) in classification tasks.  
**Formula**:  
\[
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
\]  
**Example**: For 125 images, if 75 are correctly predicted, accuracy = \(75/125 = 0.6\).

---

## [[Precision]]
**Definition**: Proportion of predicted positives that are actually positive (reliability of positive predictions).  
**Formula**:  
\[
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
\]  
**Example**: In spam detection, if 90 spam emails are correctly identified (TP) and 5 legitimate emails are flagged as spam (FP), precision = \(90/(90+5) = 0.947\).

---

## [[Recall (Sensitivity)]]
**Definition**: Proportion of actual positives correctly identified (ability to detect positives).  
**Formula**:  
\[
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
\]  
**Example**: In the same spam example, if 10 spam emails are missed (FN), recall = \(90/(90+10) = 0.9\).

---

## [[F1-Score]]
**Definition**: Harmonic mean of precision and recall, balancing both metrics.  
**Formula**:  
\[
\text{F1} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
\]  
**Example**: With precision = 0.947 and recall = 0.9, F1 = \(2 \cdot (0.947 \cdot 0.9)/(0.947 + 0.9) \approx 0.923\).

---

## [[Confusion Matrix]]
**Definition**: A table used to evaluate classification models by comparing actual and predicted labels.  
**Structure**:  
|                  | Predicted Positive | Predicted Negative |
|------------------|--------------------|--------------------|
| **Actual Positive** | TP                 | FN                 |
| **Actual Negative** | FP                 | TN                 |  
**Example**: In spam detection (page 18): TP=90, FN=10, FP=5, TN=895.

---

## [[ROC Curve and AUC]]
**Definition**:  
- **ROC Curve**: Plots True Positive Rate (TPR) vs. False Positive Rate (FPR) at various thresholds.  
- **AUC**: Area Under the ROC Curve, measuring model’s ability to distinguish classes (higher = better).  
**Formula**: AUC calculated via trapezoidal rule (page 25).  
**Example**: A medical diagnostic model with AUC = 0.95 has excellent discrimination between diseased and healthy patients.

---

## [[Tradeoffs Between Metrics]]
**Key Considerations**:  
- **Precision vs. Recall**: Prioritize precision when false positives are costly (e.g., fraud detection), recall when false negatives are dangerous (e.g., medical diagnoses).  
- **Context Dependency**: RMSE vs. MAE depends on sensitivity to outliers; accuracy vs. F1 depends on class balance.  
**Example**: A self-driving car prioritizes recall to minimize missed pedestrians (page 22).