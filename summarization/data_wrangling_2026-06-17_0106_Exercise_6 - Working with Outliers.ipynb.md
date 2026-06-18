# Exercise_6 - Working with Outliers.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

## **Outlier**  
**Definition**: A data point significantly different from the majority of observations in a dataset. Outliers skew statistical parameters (e.g., mean, variance) and can degrade machine learning model performance (e.g., linear regression, AdaBoost).  
**Formula**: N/A (detected via methods like IQR or Z-score)  
**Example**: In the `airbnb_sg` dataset, outliers in the `price` column were visualized using a boxplot (`Code Cell 10`), showing extreme values beyond the interquartile range.

---

## **Interquartile Range (IQR)**  
**Definition**: A measure of statistical dispersion representing the range between the first quartile (Q1, 25th percentile) and third quartile (Q3, 75th percentile). Used to identify outliers.  
**Formula**:  
\[
\text{IQR} = Q3 - Q1
\]  
Lower boundary: \( Q1 - 1.5 \times \text{IQR} \)  
Upper boundary: \( Q3 + 1.5 \times \text{IQR} \)  
**Example**: In `Exercise 1`, the `find_boundaries` function calculated IQR-based thresholds to detect outliers in the `price` column.

---

## **Winsorization**  
**Definition**: A technique to cap outliers at specified percentiles (e.g., 5th and 95th), reducing their influence while retaining data points.  
**Formula**:  
For a variable \( X \), values below \( P_{\text{lower}} \) or above \( P_{\text{upper}} \) are replaced with the respective percentiles.  
**Example**: In `Code Cell 11`, the `Winsorizer` capped `price` at 5% and 95% quantiles (`fold=0.05`) to handle outliers.

---

## **Trimming**  
**Definition**: The removal of observations containing outliers from the dataset.  
**Formula**: N/A (involves filtering data outside predefined bounds)  
**Example**: Discussed in objectives as a method to eliminate outliers, though not explicitly implemented in the provided code.

---

## **Capping**  
**Definition**: Setting maximum/minimum thresholds for variables to limit the impact of outliers. Winsorization is a form of capping.  
**Formula**: Similar to Winsorization, but thresholds may be defined using domain knowledge or statistical methods.  
**Example**: The `Winsorizer` in `Code Cell 11` capped `price` values at 5% and 95% quantiles.

---

## **Discretization**  
**Definition**: The process of converting continuous variables into discrete bins (intervals) to reduce outlier sensitivity and normalize skewed distributions.  
**Formula**: N/A (methods include equal-frequency, equal-width, or value-based binning)  
**Example**: In `Exercise 5`, discretization was applied to minimize the impact of outliers by grouping extreme values into lower/upper bins.

---

### **Key Links**  
- [[Outlier]] detection methods: [[Interquartile Range (IQR)]], [[Winsorization]]  
- Outlier handling techniques: [[Trimming]], [[Capping]], [[Discretization]]  
- Related concepts: [[Data Wrangling]], [[Machine Learning Model Performance]]  

This summary integrates content from the provided files and links to related concepts for cohesive note-taking.