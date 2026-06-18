# Practical 6.1 - Outlier-Trimming.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the content:

---

## **Trimming Outliers**

### **Trimming**
**Definition**: The process of removing observations identified as outliers in one or more variables of a dataset.  
**Formula**: Not applicable (method-dependent).  
**Example**:  
```python
# Trimming dataset by removing rows with outliers in 'RM'
boston_trimmed = boston.loc[~outliers_RM]
```

---

### **Method 1: Standard Deviation Boundaries**
**Definition**: Outliers are defined as data points beyond **mean ± 3 × standard deviation (σ)**, assuming normal distribution (covers ~99% of data).  
**Formula**:  
\[
\text{Lower Boundary} = \mu - 3\sigma \quad \text{Upper Boundary} = \mu + 3\sigma
\]  
**Example**:  
```python
# Function to calculate boundaries using standard deviation
def find_boundaries(df, variable, distance):
    lower_boundary = df[variable].mean() - (df[variable].std() * distance)
    upper_boundary = df[variable].mean() + (df[variable].std() * distance)
    return upper_boundary, lower_boundary

# Applying for 'RM' with distance=3
RM_upper_limit, RM_lower_limit = find_boundaries(boston, 'RM', 3)
```

---

### **Method 2: Interquartile Range (IQR) Proximity Rule**
**Definition**: Outliers are data points outside **Q1 − 1.5×IQR** or **Q3 + 1.5×IQR**, where **IQR = Q3 − Q1** (works for normal and skewed distributions).  
**Formula**:  
\[
\text{IQR} = Q3 - Q1, \quad \text{Lower Boundary} = Q1 - 1.5 \times \text{IQR}, \quad \text{Upper Boundary} = Q3 + 1.5 \times \text{IQR}
\]  
**Example**:  
```python
# Function to calculate IQR-based boundaries
def find_boundaries(df, variable, distance):
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)
    lower_boundary = df[variable].quantile(0.25) - (IQR * distance)
    upper_boundary = df[variable].quantile(0.75) + (IQR * distance)
    return upper_boundary, lower_boundary

# Applying for 'LSTAT' with distance=1.5
LSTAT_upper_limit, LSTAT_lower_limit = find_boundaries(boston, 'LSTAT', 1.5)
```

---

### **Method 3: Arbitrary Percentile Boundaries**
**Definition**: Outliers are defined as data points below the **5th percentile** or above the **95th percentile**.  
**Formula**:  
\[
\text{Lower Boundary} = \text{Quantile}(0.05), \quad \text{Upper Boundary} = \text{Quantile}(0.95)
\]  
**Example**:  
```python
# Function to calculate percentile-based boundaries
def find_boundaries(df, variable):
    lower_boundary = df[variable].quantile(0.05)
    upper_boundary = df[variable].quantile(0.95)
    return upper_boundary, lower_boundary

# Applying for 'CRIM'
CRIM_upper_limit, CRIM_lower_limit = find_boundaries(boston, 'CRIM')
```

---

### **Key Notes**
1. **Trimming Across Multiple Variables**: Outliers can be removed based on multiple variables simultaneously:  
   ```python
   # Trim rows with outliers in any of the variables
   boston_trimmed = boston.loc[~(outliers_RM + outliers_LSTAT + outliers_CRIM), :]
   ```
2. **Persistent Outliers After Trimming**: Dots beyond whiskers in boxplots post-trimming may indicate outliers in other variables or method limitations (e.g., IQR sensitivity to quartile values).

---

### **Wikilinks**
- [[Trimming]]  
- [[Interquartile Range (IQR)]]  
- [[Standard Deviation]]  
- [[Percentile]]  
- [[Outlier Detection]]