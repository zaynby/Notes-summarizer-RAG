# Practical 7.1 - Standardization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary of Key Concepts in Feature Standardization and Model Diagnostics

## **Standardization (Z-score Standardization)**  
**Definition**: A method to transform data such that each feature has a mean of 0 and a standard deviation of 1, enabling comparability across features.  
**Formula**:  
\[ z = \frac{x - \text{mean}(x)}{\text{std}(x)} \]  
**Example**:  
```python  
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
X_train_scaled = scaler.fit_transform(X_train)  
```  
**Link**: [[Z-score]], [[Mean]], [[Standard Deviation]]

---

## **Z-score**  
**Definition**: The result of standardization, representing the number of standard deviations an observation is from the mean.  
**Formula**: Same as above.  
**Example**: Scaled features in `X_train_scaled` after applying `StandardScaler`.  
**Link**: [[Standardization]]

---

## **Mean (mean_)**  
**Definition**: The average value of a feature, calculated as the sum of all values divided by the number of values.  
**Formula**:  
\[ \text{mean}(x) = \frac{\sum_{i=1}^{n} x_i}{n} \]  
**Example**:  
```python  
scaler.mean_  # Returns the mean of each feature learned from the training data  
```  
**Link**: [[Standardization]]

---

## **Standard Deviation (scale_)**  
**Definition**: A measure of the spread of a dataset, indicating how much values deviate from the mean.  
**Formula**:  
\[ \text{std}(x) = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \text{mean}(x))^2} \]  
**Example**:  
```python  
scaler.scale_  # Returns the standard deviation of each feature  
```  
**Link**: [[Standardization]]

---

## **Feature-wise Normalization**  
**Definition**: Normalizing each feature individually (e.g., via standardization) to ensure equal contribution in models.  
**Formula**: Same as [[Standardization]].  
**Example**: Applying `StandardScaler` to the Boston housing dataset to homogenize feature scales.  
**Link**: [[Standardization]]

---

## **Coefficient (β)**  
**Definition**: In logistic regression, represents the influence of a predictor on the outcome. Sign indicates direction (positive/negative), magnitude indicates strength.  
**Formula**: Not explicitly provided, but part of the logistic regression equation:  
\[ \text{Logit}(p) = \beta_0 + \beta_1 x_1 + \dots + \beta_n x_n \]  
**Example**: A positive β for "RM" (average rooms) in house pricing models suggests larger rooms increase prices.  
**Link**: [[Confidence Interval]], [[Standard Error]]

---

## **Standard Error (SE)**  
**Definition**: Measures uncertainty in a coefficient estimate. Smaller SE implies higher confidence.  
**Formula**:  
\[ \text{SE} = \frac{\sigma}{\sqrt{n}} \]  
(where σ is sample standard deviation, n is sample size).  
**Example**: Reported in model summaries (e.g., `summary()` in statsmodels).  
**Link**: [[Confidence Interval]], [[Coefficient]]

---

## **Confidence Interval (CI)**  
**Definition**: Range of plausible values for a coefficient at a given confidence level (e.g., 95%).  
**Formula**:  
\[ \text{CI} = \beta \pm (1.96 \times \text{SE}) \]  
**Example**: A 95% CI of [0.2, 0.5] for β indicates the true value likely lies in this interval.  
**Link**: [[Coefficient]], [[Standard Error]]

---

## **Z statistic (Wald test)**  
**Definition**: Tests if a coefficient is significantly different from zero. Larger |Z| values indicate stronger evidence.  
**Formula**:  
\[ Z = \frac{\beta}{\text{SE}} \]  
**Example**: A Z statistic of 3.5 for "LSTAT" suggests it significantly affects house prices.  
**Link**: [[Coefficient]], [[Standard Error]]

---

This summary integrates concepts from both feature preprocessing (standardization) and model diagnostics (coefficient analysis), linking related terms for cohesive understanding.