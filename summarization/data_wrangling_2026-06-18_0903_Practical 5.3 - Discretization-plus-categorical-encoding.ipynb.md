# Practical 5.3 - Discretization-plus-categorical-encoding.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Summary: Discretization and Categorical Encoding

#### [[Discretization (Binning)]]
**Definition**: The process of converting continuous variables into discrete intervals (bins) to reduce the impact of outliers, handle skewed distributions, and improve model performance.  
**Formula**: No direct formula; depends on the method (e.g., equal-width or equal-frequency).  
**Example**:  
```python
# Using KBinsDiscretizer for equal-frequency discretization
disc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='quantile')
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])
```

---

#### [[Equal-Frequency Discretization]]
**Definition**: A discretization method where each bin contains an equal number of observations, achieved by splitting data at quantiles.  
**Formula**: Bin edges defined by quantiles:  
$$
\text{Quantile positions} = \left\{0, \frac{1}{n}, \frac{2}{n}, \ldots, 1\right\}
$$
**Example**:  
```python
# Using Feature-engine for equal-frequency discretization
disc = EqualFrequencyDiscretiser(q=10, variables=['LSTAT', 'DIS', 'RM'], return_object=True)
disc.fit(X_train)
```

---

#### [[Equal-Width Discretization]]
**Definition**: A discretization method where bins have equal range intervals, calculated as (max - min)/number of bins.  
**Formula**: Bin width =  
$$
\text{Width} = \frac{\text{max}(X) - \text{min}(X)}{n_{\text{bins}}}
$$
**Example**:  
```python
# Using KBinsDiscretizer for equal-width discretization
disc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])
```

---

#### [[Ordinal Encoding (Ordered)]]
**Definition**: Assigning integer codes to categorical bins in a way that reflects the monotonic relationship with the target variable.  
**Formula**: No direct formula; based on sorting bin means of the target.  
**Example**:  
```python
# Reordering bins to achieve monotonicity
enc = OrdinalEncoder(encoding_method='ordered')
enc.fit(train_t, y_train)
train_t = enc.transform(train_t)
```

---

#### [[Monotonic Relationship]]
**Definition**: A relationship where an increase in one variable consistently corresponds to an increase (or decrease) in another variable.  
**Example**:  
```python
# Plotting mean target values after ordinal encoding
pd.concat([train_t, y_train], axis=1).groupby('DIS')['MEDV'].mean().plot()
plt.ylabel('Mean House Price')
```
**Outcome**: The plot shows a steady increase/decrease in target values across bins, confirming monotonicity.

---

### Key Concepts Linkage  
- Discretization methods ([[Equal-Frequency Discretization]] and [[Equal-Width Discretization]]) are used to bin continuous variables.  
- [[Ordinal Encoding (Ordered)]] ensures bins are ordered to create a [[Monotonic Relationship]] with the target.  
- Outliers are minimized by grouping extreme values into bins with other observations.  
- Libraries like `Feature-engine` and `scikit-learn` implement these techniques.