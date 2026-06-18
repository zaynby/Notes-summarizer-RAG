# Practical 1.9 - Comparing-Feature-Magnitude.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

```markdown
# Summary: Feature Scaling and Statistical Analysis in Machine Learning

## [[Feature Scaling]]  
**Definition**: The process of normalizing the range of independent variables (features) in a dataset to ensure machine learning algorithms perform effectively. Algorithms like SVM, KNN, and gradient descent are sensitive to feature scales.  
**Formula**: Standardization (Z-score normalization):  
$$
X_{\text{scaled}} = \frac{X - \mu}{\sigma}
$$  
where \( \mu \) is the mean and \( \sigma \) is the standard deviation.  
**Example**: In the Boston Housing dataset, features like `CRIM` (0–89), `CHAS` (0–1), and `RM` (3.5–8.8) exhibit vastly different scales, necessitating scaling for consistent model performance.

---

## [[Statistical Metrics]]  
**Definition**: Quantitative measures used to summarize the distribution and characteristics of a dataset’s features. Key metrics include mean, standard deviation, quartiles, minimum, and maximum values.  
**Formula**:  
- Mean: \( \mu = \frac{1}{n} \sum_{i=1}^{n} x_i \)  
- Standard Deviation: \( \sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2} \)  
- Interquartile Range (IQR): \( Q3 - Q1 \)  
**Example**: The `boston.describe()` output provides summary statistics (e.g., `CRIM` has a mean of 3.6, std of 8.6, and range 0–89).

---

## [[Feature Magnitude]]  
**Definition**: The scale or range of values a feature takes, which impacts model training. Features with larger magnitudes can dominate others if not scaled.  
**Formula**: N/A (observed via statistical metrics).  
**Example**: In the Boston dataset, `CRIM` (crime rate) has a much larger magnitude (0–89) compared to `CHAS` (Charles River proximity, 0–1), indicating a need for scaling.

---

## [[Range of Variables]]  
**Definition**: The difference between the maximum and minimum values of a feature, indicating its spread.  
**Formula**:  
$$
\text{Range} = \max(X) - \min(X)
$$  
**Example**: The code `boston.max() - boston.min()` calculates the range for each feature (e.g., `CRIM` range = 89 - 0 = 89).

---

## Key Takeaways  
- Machine learning algorithms often require **feature scaling** to handle varying feature magnitudes.  
- **Statistical metrics** (mean, std, quartiles) and **range** provide insights into feature distributions.  
- The Boston Housing dataset illustrates how unscaled features (e.g., `CRIM`, `RM`) can distort model training.
```