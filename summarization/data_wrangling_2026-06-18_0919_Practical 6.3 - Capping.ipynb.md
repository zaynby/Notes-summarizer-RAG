# Practical 6.3 - Capping.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### **Capping (Censoring/Top and Bottom Coding)**  
**Definition**: A method to replace extreme outlier values with predefined maximum or minimum thresholds, using statistical rules like Interquartile Range (IQR) or standard deviation (SD).  
**Formula**:  
- **IQR-based**:  
  Lower boundary = Q1 − (IQR × distance)  
  Upper boundary = Q3 + (IQR × distance)  
  Where IQR = Q3 − Q1 (Q1 = 25th percentile, Q3 = 75th percentile)  
- **Gaussian-based**:  
  Lower boundary = Mean − (SD × distance)  
  Upper boundary = Mean + (SD × distance)  
**Example**:  
```python
# Capping 'RM' using Gaussian boundaries (distance=3)
boston['RM'] = np.where(boston['RM'] > RM_upper_limit, RM_upper_limit, 
                         np.where(boston['RM'] < RM_lower_limit, RM_lower_limit, boston['RM']))
```

---

### **Interquartile Range (IQR)**  
**Definition**: A measure of statistical dispersion, representing the range between the first quartile (Q1) and third quartile (Q3) of a dataset.  
**Formula**:  
IQR = Q3 − Q1  
**Example**:  
```python
# Calculating IQR boundaries for skewed distributions
def find_skewed_boundaries(df, variable, distance):
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)
    lower_boundary = df[variable].quantile(0.25) - (IQR * distance)
    upper_boundary = df[variable].quantile(0.75) + (IQR * distance)
    return upper_boundary, lower_boundary
```

---

### **Gaussian (Normal Distribution) Boundaries**  
**Definition**: Outlier detection method assuming data follows a Gaussian distribution, using mean and standard deviation to define thresholds.  
**Formula**:  
Upper boundary = Mean + (SD × distance)  
Lower boundary = Mean − (SD × distance)  
**Example**:  
```python
# Calculating Gaussian boundaries (distance=3)
def find_normal_boundaries(df, variable, distance):
    upper_boundary = df[variable].mean() + df[variable].std() * distance
    lower_boundary = df[variable].mean() - df[variable].std() * distance
    return upper_boundary, lower_boundary
```

---

### **Winsorizer (Feature-engine)**  
**Definition**: A tool from the `feature_engine` library to cap outliers using either IQR or Gaussian methods.  
**Parameters**:  
- `capping_method`: 'iqr' or 'gaussian'  
- `tail`: 'left', 'right', or 'both'  
- `fold`: Multiplier for IQR or SD (e.g., 1.5, 3)  
**Example**:  
```python
# Applying Winsorizer to cap outliers in Boston dataset
windsorizer = Winsorizer(capping_method='gaussian', tail='both', fold=3, variables=['RM', 'LSTAT', 'CRIM'])
boston_t = windsorizer.transform(boston)
```

---

### **Boston Housing Dataset**  
**Definition**: A classical dataset containing housing prices and attributes in Boston, often used for regression and outlier analysis.  
**Example**:  
```python
# Loading Boston dataset with selected variables
boston = pd.read_csv("./data/boston_local.csv")
boston = boston[['RM', 'LSTAT', 'CRIM', 'MEDV']]
```

---

### Key Links  
- [[Capping]] is related to [[Winsorizer]] and [[Interquartile Range (IQR)]]  
- [[Gaussian Boundaries]] use [[Standard Deviation]] for outlier detection  
- [[Boston Housing Dataset]] is commonly used with outlier handling techniques like [[Capping]] and [[Winsorizer]]  

--- 

This summary integrates statistical concepts, code implementations, and domain-specific tools for outlier capping.