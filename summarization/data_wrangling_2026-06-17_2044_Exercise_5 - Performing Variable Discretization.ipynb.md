# Exercise_5 - Performing Variable Discretization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content on **Variable Discretization**:

---

### [[Discretization (Binning)]]
**Definition**:  
The process of converting continuous variables into discrete intervals (bins) to reduce the impact of outliers, handle skewed distributions, and improve model performance by creating homogeneous groups.

**Formula**:  
No direct formula, but involves dividing the range of a variable into intervals. For **equal-frequency bins**:  
\[ \text{Bin boundaries} = \text{Quantiles of the variable at intervals of } \frac{100\%}{\text{Number of bins}} \]  
For **equal-width bins**:  
\[ \text{Bin width} = \frac{\text{Max value} - \text{Min value}}{\text{Number of bins}} \]

**Example**:  
In the `airbnb_sg` dataset, `availability_365` and `calculated_host_listings_count` were binned using `EqualFrequencyDiscretiser` (10 bins):  
```python
disc = EqualFrequencyDiscretiser(q=10, variables=['availability_365', 'calculated_host_listings_count'])
```

---

### [[Equal Frequency Discretiser]]
**Definition**:  
An unsupervised discretization method that splits data into bins with **equal number of observations**, regardless of value ranges.

**Formula**:  
Bin boundaries are determined by quantiles:  
\[ Q_i = \text{Quantile}\left(\frac{i}{n}, 0 \leq i \leq n\right) \]  
where \( n \) = number of bins.

**Example**:  
```python
# Creates 10 bins with ~10% of data each
disc = EqualFrequencyDiscretiser(q=10, variables=['availability_365'])
```

---

### [[Equal Width Discretiser]]
**Definition**:  
An unsupervised discretization method that splits the variable’s range into bins of **equal size** (width).

**Formula**:  
\[ \text{Bin width} = \frac{\text{Max}(X) - \text{Min}(X)}{n} \]  
where \( n \) = number of bins.

**Example**:  
For a variable ranging from 0 to 100 with 10 bins:  
```python
# Bin widths = (100-0)/10 = 10
disc = EqualWidthDiscretiser(n_bins=10, variables=['price'])
```

---

### [[OrdinalEncoder (Ordered)]]
**Definition**:  
A supervised discretization method that orders categorical bins based on the **mean of the target variable**, ensuring a monotonic relationship.

**Formula**:  
Ranks bins by \( \mathbb{E}[Y | \text{Bin}_i] \), where \( Y \) is the target variable.

**Example**:  
```python
enc = OrdinalEncoder(encoding_method='ordered')
enc.fit(train_t, y_train)  # Orders bins by mean 'price'
```

---

### [[Monotonic Relationship]]
**Definition**:  
A relationship where an increase in one variable consistently corresponds to an increase (or decrease) in another variable. In discretization, this ensures ordered bins show a steady trend in the target.

**Formula**:  
For consecutive bins \( i \) and \( i+1 \):  
\[ \mathbb{E}[Y | \text{Bin}_i] \leq \mathbb{E}[Y | \text{Bin}_{i+1}] \]

**Example**:  
After applying `OrdinalEncoder`, the mean `price` by `availability_365` bins shows a steady increasing/decreasing trend:  
```python
pd.concat([train_t, y_train], axis=1).groupby('availability_365')['price'].mean().plot()
```

---

### Key Connections [[Wikilinks]]
- **Discretization** reduces the impact of [[Outliers]] and addresses [[Skewed Data]].  
- **Equal Frequency Discretiser** and **Equal Width Discretiser** are **unsupervised** methods, unlike supervised approaches like **OrdinalEncoder**.  
- **Monotonic Relationship** is critical for models requiring ordered categorical features (e.g., gradient-boosted trees).  

--- 

This summary aligns with the code and theory in the provided notebook, emphasizing practical implementation and theoretical foundations.