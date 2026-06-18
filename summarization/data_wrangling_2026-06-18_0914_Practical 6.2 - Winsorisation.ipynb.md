# Practical 6.2 - Winsorisation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content:

---

## **Winsorization**  
**Definition**: A technique to handle [[Outliers]] by capping extreme values at specified percentiles instead of removing them. Unlike trimming, Winsorization replaces outliers with a cutoff value (e.g., 5th or 95th percentile), preserving dataset size.  
**Formula**:  
For a variable \( X \):  
\[
X_{\text{winsorized}} = 
\begin{cases} 
\text{Lower Bound} & \text{if } X < \text{Lower Bound} \\
X & \text{if } \text{Lower Bound} \leq X \leq \text{Upper Bound} \\
\text{Upper Bound} & \text{if } X > \text{Upper Bound}
\end{cases}
\]  
**Example**:  
```python
# Using numpy to winsorize 'RM' column
boston['RM'] = np.where(
    boston['RM'] > boston['RM'].quantile(0.95),  # Upper bound: 95th percentile
    boston['RM'].quantile(0.95), 
    np.where(
        boston['RM'] < boston['RM'].quantile(0.05),  # Lower bound: 5th percentile
        boston['RM'].quantile(0.05), 
        boston['RM']
    )
)
```

---

## **Outliers**  
**Definition**: Data points that significantly deviate from the majority of observations in a dataset. Outliers can skew statistical measures (e.g., mean) and affect machine learning model performance.  
**Formula**: Outliers are often identified using:  
- **Interquartile Range (IQR)**: \( \text{Lower Bound} = Q1 - 1.5 \times \text{IQR} \), \( \text{Upper Bound} = Q3 + 1.5 \times \text{IQR} \)  
- **Z-score**: \( Z = \frac{X - \mu}{\sigma} \), where \( |Z| > 3 \) indicates an outlier  
**Example**:  
```python
# Flagging outliers in 'LSTAT' using percentiles
outliers_LSTAT = np.where(
    boston['LSTAT'] > LSTAT_upper_limit, True,
    np.where(boston['LSTAT'] < LSTAT_lower_limit, True, False)
)
```

---

## **Percentile Capping**  
**Definition**: A method to limit extreme values by setting them to a specified percentile (e.g., 5th or 95th percentile). This is a key step in Winsorization.  
**Formula**:  
\[
\text{Capped Value} = 
\begin{cases} 
P_{\alpha} & \text{if } X > P_{\alpha} \\
P_{\beta} & \text{if } X < P_{\beta} \\
X & \text{otherwise}
\end{cases}
\]  
where \( P_{\alpha} \) and \( P_{\beta} \) are the upper and lower percentile bounds.  
**Example**:  
```python
# Using Feature-engine's Winsorizer with 5% fold (95th and 5th percentiles)
windsorizer = Winsorizer(capping_method='quantiles', tail='both', fold=0.05, variables=['RM', 'LSTAT', 'CRIM'])
boston_t = windsorizer.transform(boston)
```

---

## **Feature-engine Winsorizer**  
**Definition**: A Python library tool (`Winsorizer` from `feature_engine.outliers`) that automates Winsorization using configurable parameters like `capping_method` (quantiles, Gaussian, skewed) and `fold` (percentile threshold).  
**Formula**: N/A (implementation-specific)  
**Example**:  
```python
# Inspecting caps after fitting Winsorizer
print(windsorizer.right_tail_caps_)  # Shows upper bounds for each variable
print(windsorizer.left_tail_caps_)   # Shows lower bounds for each variable
```

---

### **Key Connections**  
- [[Winsorization]] addresses [[Outliers]] via [[Percentile Capping]].  
- [[Feature-engine Winsorizer]] provides an automated implementation of [[Winsorization]].  
- Diagnostic plots (histograms, Q-Q plots, boxplots) are used to visualize [[Outliers]] before and after Winsorization.  

--- 

This summary aligns with the notebook's focus on handling outliers through Winsorization, using both manual implementations (NumPy/Pandas) and the Feature-engine library.