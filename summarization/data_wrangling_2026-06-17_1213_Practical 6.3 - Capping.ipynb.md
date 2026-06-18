# Practical 6.3 - Capping.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Academic Summary: Outlier Capping Techniques

## **Capping (Data Capping)**  
**Definition**: The process of replacing extreme outlier values with predefined maximum or minimum thresholds (caps) to mitigate their impact on statistical models.  
**Formula**: N/A (implemented via specific methods)  
**Example**:  
```python
boston['RM'] = np.where(boston['RM'] > RM_upper_limit, RM_upper_limit, 
                         np.where(boston['RM'] < RM_lower_limit, RM_lower_limit, boston['RM']))
```
This code caps 'RM' values beyond the calculated limits using `np.where`.

---

## **Interquartile Range (IQR) Method**  
**Definition**: A technique to identify outliers using the interquartile range (IQR), defined as the difference between the 75th (Q3) and 25th (Q1) percentiles.  
**Formula**:  
$$
\text{IQR} = Q3 - Q1 \\
\text{Lower Boundary} = Q1 - (\text{IQR} \times \text{distance}) \\
\text{Upper Boundary} = Q3 + (\text{IQR} \times \text{distance})
$$  
**Example**:  
```python
def find_skewed_boundaries(df, variable, distance):
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)
    lower_boundary = df[variable].quantile(0.25) - (IQR * distance)
    upper_boundary = df[variable].quantile(0.75) + (IQR * distance)
    return upper_boundary, lower_boundary
```

---

## **Gaussian (Standard Deviation) Method**  
**Definition**: A method assuming normal distribution, using mean (μ) and standard deviation (σ) to calculate outlier boundaries.  
**Formula**:  
$$
\text{Upper Boundary} = \mu + (\text{distance} \times \sigma) \\
\text{Lower Boundary} = \mu - (\text{distance} \times \sigma)
$$  
**Example**:  
```python
def find_normal_boundaries(df, variable, distance):
    upper_boundary = df[variable].mean() + df[variable].std() * distance
    lower_boundary = df[variable].mean() - df[variable].std() * distance
    return upper_boundary, lower_boundary
```

---

## **Winsorizer**  
**Definition**: A transformer from the `feature-engine` library that implements capping using methods like Gaussian or IQR.  
**Formula**: N/A (implementation tool)  
**Example**:  
```python
windsorizer = Winsorizer(capping_method='gaussian', tail='both', fold=3, variables=['RM', 'LSTAT', 'CRIM'])
windsorizer.fit(boston)
boston_t = windsorizer.transform(boston)
```

---

## **Censoring (Top and Bottom Coding)**  
**Definition**: Synonymous with capping; involves replacing extreme values with cutoffs (e.g., mean ± 3σ or IQR-based limits).  
**Formula**: Same as [[Capping (Data Capping)]] and its methods.  
**Example**:  
The notebook uses "censoring" interchangeably with capping, as seen in the description of the Winsorizer’s functionality.

---

## **Key Links**  
- [[Interquartile Range (IQR) Method]]  
- [[Gaussian (Standard Deviation) Method]]  
- [[Winsorizer]]  
- [[Capping (Data Capping)]]  
- [[Censoring (Top and Bottom Coding)]]