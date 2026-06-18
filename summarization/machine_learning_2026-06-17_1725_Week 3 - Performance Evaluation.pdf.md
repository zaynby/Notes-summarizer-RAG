# Week 3 - Performance Evaluation.pdf
**Module:** machine_learning
**Style:** structured_academic (experimenting)

### Model Evaluation and Metrics

#### Regression Model Evaluation

**Term -> Definition -> Formula -> Example**

1. **Mean Absolute Error (MAE)**
   - **Definition:** Measures the average absolute difference between actual and predicted values.
   - **Formula:** \( \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| \)
   - **Example:** If a model predicts house prices as [200k, 300k, 400k] and the actual prices are [195k, 305k, 410k], then \( \text{MAE} = \frac{|195-200| + |305-300| + |410-400|}{3} = \frac{5 + 5 + 10}{3} = 6.67 \).

2. **Mean Squared Error (MSE)**
   - **Definition:** Measures the average squared error between actual and predicted values.
   - **Formula:** \( \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \)
   - **Example:** Using the same data, \( \text{MSE} = \frac{(195-200)^2 + (305-300)^2 + (410-400)^2}{3} = \frac{25 + 25 + 100}{3} = 41.67 \).

3. **Root Mean Squared Error (RMSE)**
   - **Definition:** Measures the square root of average squared errors.
   - **Formula:** \( \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} \)
   - **Example:** Using the same data, \( \text{RMSE} = \sqrt{41.67} \approx 6.45 \).

4. **R-Squared Error (R²)**
   - **Definition:** Measures how well the model explains the variation in the data — also known as the coefficient of determination.
   - **Formula:** \( R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \)
   - **Example:** If the total sum of squares is 500 and the residual sum of squares is 167, then \( R^2 = 1 - \frac{167}{500} = 0.654 \).

#### Classification Model Evaluation

**Term -> Definition -> Formula -> Example**

1. **Accuracy**
   - **Definition:** Proportion of total correct predictions.
   - **Formula:** \( \text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{FP} + \text{FN} + \text{TN}} \)
   - **Example:** If a model predicts 75 out of 125 images correctly, then \( \text{Accuracy} = \frac{75}{125} = 0.6 \).

2. **Precision**
   - **Definition:** Proportion of predicted positives that are positive.
   - **Formula:** \( \text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} \)
   - **Example:** If out of 10 spam emails, the model correctly identifies 9 and incorrectly flags 5 non-spam emails as spam, then \( \text{Precision} = \frac{9}{9+5} = 0.643 \).

3. **Recall (True Positive Rate)**
   - **Definition:** Proportion of actual positives that were correctly predicted.
   - **Formula:** \( \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} \)
   - **Example:** If out of 10 spam emails, the model correctly identifies 9 and misses 1 as non-spam, then \( \text{Recall} = \frac{9}{9+1} = 0.9 \).

4. **Specificity (True Negative Rate)**
   - **Definition:** Proportion of actual negatives that were correctly predicted.
   - **Formula:** \( \text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}} \)
   - **Example:** If out of 90 non-spam emails, the model correctly identifies 89 and incorrectly flags 1 as spam, then \( \text{Specificity} = \frac{89}{89+1} = 0.99 \).

5. **F1 Score**
   - **Definition:** Harmonic mean of precision and recall.
   - **Formula:** \( \text{F1 Score} = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \)
   - **Example:** Using the same data, \( \text{F1 Score} = \frac{2 \times 0.643 \times 0.9}{0.643 + 0.9} = \frac{1.1574}{1.543} \approx 0.75 \).

6. **False Positive Rate (FPR)**
   - **Definition:** Proportion of actual negatives that were incorrectly predicted as positive.
   - **Formula:** \( \text{FPR} = 1 - \text{Specificity} \)
   - **Example:** If out of 90 non-spam emails, the model incorrectly flags 1 as spam, then \( \text{FPR} = 1 - 0.99 = 0.01 \).

7. **False Negative Rate (FNR)**
   - **Definition:** Proportion of actual positives that were incorrectly predicted as negative.
   - **Formula:** \( \text{FNR} = 1 - \text{Recall} \)
   - **Example:** If out of 10 spam emails, the model misses 1 as non-spam, then \( \text{FNR} = 1 - 0.9 = 0.1 \).

8. **ROC Curve and AUC**
   - **Definition:** Graphically show how classification models perform by plotting True Positive Rate versus False Positive Rate across thresholds.
   - **Formula for AUC:** Trapezoidal area calculation.
   - **Example:** Given a set of true labels and model scores, the AUC can be computed to compare model performance.

#### Summary

**Term -> Definition -> Use When...**

- **MAE (Mean Absolute Error)**
  - Measures average error magnitude in same units as target.
  - Quick, interpretable baseline metric for regression.

- **MSE (Mean Squared Error)**
  - Measures average squared error and heavily penalizes outliers.
  - Useful when large errors must be flagged.

- **RMSE (Root Mean Squared Error)**
  - Root of MSE with same units as target.
  - Most popular regression metric.

- **R² (Coefficient of Determination)**
  - Proportion of variation explained, ranges from 0 to 1.
  - Useful for comparing models on different datasets.

- **Accuracy**
  - Percentage of all predictions correct.
  - Suitable when classes are balanced.

- **Precision**
  - Proportion of positive predictions that are correct.
  - Important when false positives are costly.

- **Recall (True Positive Rate)**
  - Proportion of actual positives correctly caught.
  - Crucial when false negatives are dangerous.

- **F1 Score**
  - Harmonic mean of precision and recall, useful for imbalanced classes.
  - Balances precision and recall, providing a balanced tradeoff.

- **AUC (Area Under the ROC Curve)**
  - Model's ability to distinguish between classes across all thresholds.
  - Useful for comparing models in terms of threshold independence.