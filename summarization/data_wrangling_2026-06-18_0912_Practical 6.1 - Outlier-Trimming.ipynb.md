# Practical 6.1 - Outlier-Trimming.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

## [[Outlier]]
**Definition**: A data point significantly different from the majority of observations, potentially arising from a different mechanism. Outliers can distort statistical measures (e.g., mean, variance) and affect machine learning model performance.

---

## [[Trimming (Outlier Trimming)]]
**Definition**: The process of removing observations containing outliers in one or more variables. Three common boundary-setting methods are used:
1. **Standard Deviation Method** (normal distributions)
2. **Inter-Quartile Range (IQR) Proximity Rule** (any distribution)
3. **Arbitrary Percentile Method** (direct quantile limits)

---

## [[Inter-Quartile Range (IQR) Proximity Rule]]
**Definition**: A method to identify outliers using quartiles, robust to non-normal distributions.  
**Formula**:  
- IQR = Q₃ (75th percentile) - Q₁ (25th percentile)  
- Lower boundary = Q₁ - (IQR × distance)  
- Upper boundary = Q₃ + (IQR × distance)  
*Typical distance = 1.5 (or 3 for extreme outliers)*  

**Example**:  
```python
def find_boundaries_IQR(df, variable, distance=1.5):
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)
    lower = df[variable].quantile(0.25) - (IQR * distance)
    upper = df[variable].quantile(0.75) + (IQR * distance)
    return upper, lower
```

---

## [[Standard Deviation Method]]
**Definition**: A parametric method assuming normal distribution, flagging data beyond ±3 standard deviations from the mean.  
**Formula**:  
- Lower boundary = mean - (3 × std)  
- Upper boundary = mean + (3 × std)  

**Example**:  
```python
def find_boundaries_SD(df, variable, distance=3):
    lower = df[variable].mean() - (df[variable].std() * distance)
    upper = df[variable].mean() + (df[variable].std() * distance)
    return upper, lower
```

---

## [[Arbitrary Percentile Method]]
**Definition**: A non-parametric approach using fixed percentiles (e.g., 5th and 95th) as boundaries.  
**Formula**:  
- Lower boundary = 5th percentile  
- Upper boundary = 95th percentile  

**Example**:  
```python
def find_boundaries_percentiles(df, variable):
    lower = df[variable].quantile(0.05)
    upper = df[variable].quantile(0.95)
    return upper, lower
```

---

## [[Outlier Flagging & Trimming Implementation]]
**Definition**: Process of identifying and removing outliers using boolean masking.  
**Example**:  
```python
# Flag outliers in 'RM' column using IQR boundaries
outliers_RM = np.where(boston['RM'] > RM_upper_limit, True,
                       np.where(boston['RM'] < RM_lower_limit, True, False))

# Trim dataset (remove rows with outliers in any variable)
boston_trimmed = boston.loc[~(outliers_RM + outliers_LSTAT + outliers_CRIM), :]
```

---

## Key Observations
- **Boxplots** visualize outliers as points beyond the whiskers (1.5×IQR).
- **Trimming** may not remove all extreme values if variables are skewed or multivariate relationships exist.
- Method choice depends on data distribution and context (e.g., IQR for skewed data, SD for normal distributions).

--- 

All terms are interconnected via [[Wikilinks]] for cross-referencing. Formulas and code examples are derived directly from the provided notebooks.