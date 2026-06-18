# Practical 8.1 - Add-Multiply-Features.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Structured Academic Summary: Statistical Feature Engineering Operations

## [[Feature Engineering]]  
**Definition**: The process of creating new features from existing data to enhance machine learning model performance by applying mathematical or statistical operations.  
**Formula**: N/A (General concept)  
**Example**: Engineering new features like `added_features`, `prod_features`, etc., from existing columns in the breast cancer dataset.

---

## [[Summation]]  
**Definition**: The addition of values across selected features for each row in a dataset.  
**Formula**:  
\[ \text{Sum} = \sum_{i=1}^{n} x_i \]  
**Example**:  
```python
df['added_features'] = df[features].sum(axis=1)
```  
Creates a new column `added_features` by summing values across `features` for each row.

---

## [[Product]]  
**Definition**: The multiplication of values across selected features for each row.  
**Formula**:  
\[ \text{Product} = \prod_{i=1}^{n} x_i \]  
**Example**:  
```python
df['prod_features'] = df[features].prod(axis=1)
```  
Generates `prod_features` by multiplying values across `features` per row.

---

## [[Mean (Average)]]  
**Definition**: The average value of selected features for each row.  
**Formula**:  
\[ \text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n} \]  
**Example**:  
```python
df['mean_features'] = df[features].mean(axis=1)
```  
Computes `mean_features` as the average of `features` per row.

---

## [[Standard Deviation]]  
**Definition**: Measures the dispersion of values across features for each row.  
**Formula**:  
\[ \sigma = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}} \]  
(where \(\mu\) is the mean)  
**Example**:  
```python
df['std_features'] = df[features].std(axis=1)
```  
Calculates `std_features` using pandas' default sample standard deviation (divided by \(n-1\)).

---

## [[Maximum]]  
**Definition**: The highest value among selected features for each row.  
**Formula**:  
\[ \text{Max} = \max(x_1, x_2, \dots, x_n) \]  
**Example**:  
```python
df['max_features'] = df[features].max(axis=1)
```  
Extracts `max_features` as the maximum value across `features` per row.

---

## [[Minimum]]  
**Definition**: The lowest value among selected features for each row.  
**Formula**:  
\[ \text{Min} = \min(x_1, x_2, \dots, x_n) \]  
**Example**:  
```python
df['min_features'] = df[features].min(axis=1)
```  
Derives `min_features` as the minimum value across `features` per row.

---

## Aggregation of Multiple Operations  
**Definition**: Combining multiple statistical operations into a single step.  
**Formula**: N/A  
**Example**:  
```python
df_t = df[features].agg(['sum', 'prod', 'mean', 'std', 'max', 'min'], axis='columns')
```  
Applies all operations simultaneously using pandas' `agg()` function.

---

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)