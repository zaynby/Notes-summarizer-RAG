# Practical 5.3 - Discretization-plus-categorical-encoding.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured summary of the content using the requested format:

---

### [[Discretization (Binning)]]
**Definition**:  
The process of converting continuous variables into discrete intervals (bins) to reduce the impact of outliers, handle skewed distributions, and enable categorical encoding.  
**Formula**:  
Not applicable directly, but involves partitioning data range into intervals (e.g., $ \text{Range} = \frac{\text{Max} - \text{Min}}{\text{Number of Bins}} $ for equal-width binning).  
**Example**:  
```python
disc = EqualFrequencyDiscretiser(q=10, variables=['LSTAT', 'DIS', 'RM'], return_object=True)
disc.fit(X_train)
```

---

### [[Equal-Frequency Discretization]]
**Definition**:  
A discretization method where data is split into bins such that each bin contains an equal number of observations (using quantiles).  
**Formula**:  
Bin edges determined by $ q $ quantiles:  
$$
\text{Bin edges} = \left\{x_{(i \cdot 100/q)\%}\right\}_{i=0}^{q}
$$  
**Example**:  
```python
disc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='quantile')
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])
```

---

### [[Ordinal Encoding]]
**Definition**:  
A categorical encoding technique that maps discrete bins to ordered integers, preserving the monotonic relationship between bins and the target variable.  
**Formula**:  
Mapped values follow ordinal order:  
$$
\text{Encoded value} = \text{Rank of bin based on target association}
$$  
**Example**:  
```python
enc = OrdinalEncoder(encoding_method='ordered')
enc.fit(train_t, y_train)
train_t = enc.transform(train_t)
```

---

### [[Monotonic Relationship]]
**Definition**:  
A relationship where an increase in one variable consistently corresponds to an increase (or decrease) in another variable. In discretization, this ensures ordered bins correlate linearly with the target.  
**Formula**:  
Slope between bin means and target values should be consistent:  
$$
\text{Slope} = \frac{\text{Mean}(Y_{\text{bin } i+1}) - \text{Mean}(Y_{\text{bin } i})}{1} \geq 0
$$  
**Example**:  
After ordinal encoding, plotting mean target values per bin shows a linear trend:  
```python
pd.concat([train_t, y_train], axis=1).groupby('DIS')['MEDV'].mean().plot()
```

---

### Key Workflow Integration
1. **Discretization**: Apply `EqualFrequencyDiscretiser` to create bins.  
2. **Ordinal Encoding**: Use `OrdinalEncoder` to reorder bins based on target correlation.  
3. **Validation**: Verify monotonic relationships via grouped mean plots.  

**Linked Concepts**:  
- [[Discretization (Binning)]] → [[Equal-Frequency Discretization]] → [[Ordinal Encoding]] → [[Monotonic Relationship]]  
- Tools: `Feature-engine`, `KBinsDiscretizer`, `scikit-learn` datasets (e.g., Boston Housing).  

--- 

This summary integrates code examples, mathematical reasoning, and conceptual definitions for educational clarity.