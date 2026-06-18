# Practical 1.9 - Comparing-Feature-Magnitude.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

## Summary: Feature Magnitude and Statistical Metrics in Machine Learning  

### [[Feature Magnitude]]  
**Definition**: The scale or range of values that a feature (independent variable) takes in a dataset. Machine learning algorithms often perform poorly when features are on vastly different scales.  
**Formula**: Not applicable directly, but measured via metrics like range (max - min), standard deviation, or quantiles.  
**Example**: In the Boston Housing Dataset, `CRIM` (crime rate) ranges from 0 to 89, while `CHAS` (Charles River proximity) is binary (0 or 1), indicating differing magnitudes.  

---

### [[Statistical Metrics]]  
**Definition**: Quantitative measures used to summarize the distribution and central tendency of a feature. Key metrics include mean, standard deviation, min/max, and quantiles (25th, 50th, 75th percentiles).  
**Formula**:  
- Mean: \(\bar{x} = \frac{\sum x_i}{n}\)  
- Standard Deviation: \(\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}\)  
**Example**: The `boston.describe()` output provides statistical metrics for all features, showing skewed scales (e.g., `RM` ranges from 3.5 to 8.8, while `NOX` ranges from 0.385 to 0.871).  

---

### [[Feature Scaling]]  
**Definition**: The process of standardizing the range of features to improve model performance. Common techniques include Min-Max Scaling and Z-score normalization.  
**Formula**:  
- Min-Max Scaling: \(x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}\)  
- Z-score Normalization: \(x_{\text{scaled}} = \frac{x - \mu}{\sigma}\) (where \(\mu\) = mean, \(\sigma\) = standard deviation)  
**Example**: Normalizing `CRIM` (0–89) and `CHAS` (0–1) to a common scale (e.g., 0–1) would ensure equal contribution in distance-based algorithms like KNN.  

---

### [[Range of Variables]]  
**Definition**: The difference between the maximum and minimum values of a feature, indicating its spread.  
**Formula**: \(\text{Range} = x_{\text{max}} - x_{\text{min}}\)  
**Example**: The `boston.max() - boston.min()` calculation reveals ranges like `CRIM` (89 - 0 = 89) vs. `CHAS` (1 - 0 = 1), highlighting scale disparities.  

---

### [[Boston Housing Dataset]]  
**Definition**: A classic dataset used for regression tasks, containing 13 features influencing house prices in Boston suburbs (e.g., crime rate, room size, pollution).  
**Formula**: Not applicable.  
**Example**: Loaded via `pd.read_csv("./data/boston_local.csv")`, it serves as a practical example to analyze feature magnitudes and apply scaling.  

---

**Key Insight**: Features with differing magnitudes (e.g., `CRIM` vs. `CHAS`) require scaling to ensure algorithms like SVM or KNN perform optimally. Statistical metrics and range calculations guide this preprocessing step.