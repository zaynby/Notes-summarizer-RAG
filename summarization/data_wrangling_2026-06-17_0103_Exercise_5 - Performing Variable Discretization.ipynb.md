# Exercise_5 - Performing Variable Discretization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Variable Discretization in Data Wrangling

## [[Discretization (Binning)]]
**Definition**: The process of transforming continuous variables into discrete intervals (bins) to reduce the impact of outliers and handle skewed distributions.  
**Formula**: N/A  
**Example**:  
```python
disc = EqualFrequencyDiscretiser(q=10, variables=['availability_365', 'calculated_host_listings_count'])
disc.fit(X_train)
train_t = disc.transform(X_train)
```
Used to bin numerical variables like `availability_365` and `calculated_host_listings_count` into 10 equal-frequency intervals.

---

## [[Equal Frequency Discretiser]]
**Definition**: A method that divides data into bins where each bin contains an equal number of observations.  
**Formula**:  
Number of observations per bin = \( \frac{\text{Total Observations}}{q} \)  
**Example**:  
```python
disc = EqualFrequencyDiscretiser(q=10, variables=[...])
```
Creates 10 bins (`q=10`) with equal instance counts for `availability_365` and `calculated_host_listings_count`.

---

## [[Equal Width Discretiser]]
**Definition**: A method that creates bins of equal range (width) based on the variable’s minimum and maximum values.  
**Formula**:  
Bin width = \( \frac{\text{Max} - \text{Min}}{q} \)  
**Example**: Not explicitly used in the code, but imported for potential use:  
```python
from feature_engine.discretisation import EqualWidthDiscretiser
```

---

## [[Monotonic Relationship]]
**Definition**: A relationship where the target variable changes consistently (increases or decreases) as the discrete bins increase.  
**Formula**: N/A  
**Example**:  
After binning, if the mean `price` per bin does not show a linear trend, bins are reordered:  
```python
enc = OrdinalEncoder(encoding_method='ordered')
enc.fit(train_t, y_train)
train_t = enc.transform(train_t)
```

---

## [[OrdinalEncoder]]
**Definition**: Encodes categorical variables with an ordered relationship to maintain monotonicity between bins and the target.  
**Formula**: N/A  
**Example**:  
```python
pd.concat([train_t, y_train], axis=1).groupby('availability_365')['price'].mean().plot()
```
Used to ensure `availability_365` bins correlate monotonically with `price`.

---

## [[Supervised Discretization]]
**Definition**: Binning methods that use target variable information to optimize bin boundaries.  
**Formula**: N/A  
**Example**: Not implemented in the code, but mentioned in objectives as a concept.

---

## [[Unsupervised Discretization]]
**Definition**: Binning methods that rely solely on the variable’s distribution (e.g., equal frequency/width) without target information.  
**Formula**: N/A  
**Example**:  
```python
disc = EqualFrequencyDiscretiser(...)  # Uses data distribution only
```

---

## Key Workflow Steps
1. **Variable Selection**: Choose numerical variables (e.g., `availability_365`, `calculated_host_listings_count`).  
2. **Binning**: Apply `EqualFrequencyDiscretiser` or `EqualWidthDiscretiser`.  
3. **Relationship Check**: Plot bin means against the target (e.g., `price`).  
4. **Monotonicity Adjustment**: Use `OrdinalEncoder` if the relationship is non-linear.  

This approach ensures discrete variables are robust to outliers and improve model performance.