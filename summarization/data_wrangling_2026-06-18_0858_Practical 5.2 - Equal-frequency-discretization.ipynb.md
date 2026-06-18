# Practical 5.2 - Equal-frequency-discretization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the notebook content on **Equal-Frequency Discretization**:

---

### **Equal-Frequency Discretization**  
**Definition**: A technique to divide continuous variables into intervals (bins) such that each bin contains an equal proportion of observations. Bin edges are determined using quantiles, leading to variable bin widths. This method is particularly effective for skewed distributions.  
**Formula**: For \( N \) bins, the \( i \)-th quantile is calculated as:  
\[ Q_i = \text{Value at } \frac{i}{N} \text{-th percentile} \]  
**Example**:  
```python  
# Using pandas qcut for 10 equal-frequency bins  
X_train['lstat_disc'], intervals = pd.qcut(  
    X_train['LSTAT'], 10,  
    retbins=True, precision=3, duplicates='raise'  
)  
```  

---

### **Quantiles**  
**Definition**: Points dividing the data into intervals with equal probabilities (e.g., deciles for 10 intervals). Used to determine bin edges in equal-frequency discretization.  
**Formula**: The \( k \)-th quantile is computed as:  
\[ Q_k = (1 - \alpha) \cdot \text{min}(X) + \alpha \cdot \text{max}(X) \]  
where \( \alpha = \frac{k}{N} \), \( N \) = number of observations.  
**Example**:  
```python  
# Extracting quantile-based intervals for test set  
X_test['lstat_disc'] = pd.cut(X_test['LSTAT'], bins=intervals)  
```  

---

### **pandas.qcut**  
**Definition**: A pandas function to perform equal-frequency discretization by dividing data into quantiles.  
**Formula**: N/A (implementation-based).  
**Example**:  
```python  
# Discretizing 'LSTAT' into 10 bins with pandas  
X_train['lstat_disc'] = pd.qcut(X_train['LSTAT'], 10)  
```  

---

### **Feature-engine.EqualFrequencyDiscretiser**  
**Definition**: A `Feature-engine` transformer that automates equal-frequency discretization for multiple variables.  
**Formula**: N/A (method-based).  
**Example**:  
```python  
# Applying to multiple features (LSTAT, DIS, RM)  
disc = EqualFrequencyDiscretiser(q=10, variables=['LSTAT', 'DIS', 'RM'])  
disc.fit(X_train)  
train_t = disc.transform(X_train)  
```  

---

### **scikit-learn KBinsDiscretizer**  
**Definition**: A scikit-learn method for binning continuous features using quantile strategy.  
**Formula**: N/A (implementation-based).  
**Example**:  
```python  
# Quantile-based discretization with KBinsDiscretizer  
disc = KBinsDiscretizer(n_bins=10, strategy='quantile')  
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])  
train_t = disc.transform(X_train[['LSTAT', 'DIS', 'RM']])  
```  

---

### **Bin Edges**  
**Definition**: The boundaries defining each interval in discretization. In equal-frequency methods, these are determined by quantiles.  
**Formula**: N/A (derived from quantile calculations).  
**Example**:  
```python  
# Accessing bin edges from pandas qcut  
print(intervals)  # Outputs the quantile-based edges  
```  

---

### **Train-Test Distribution Comparison**  
**Definition**: Ensuring that discretization applied to the test set uses bin edges derived from the training set to avoid data leakage.  
**Formula**: N/A (process-based).  
**Example**:  
```python  
# Comparing bin distributions between train and test  
t1 = X_train['lstat_disc'].value_counts() / len(X_train)  
t2 = X_test['lstat_disc'].value_counts() / len(X_test)  
tmp = pd.concat([t1, t2], axis=1).plot.bar()  
```  

---

### **Answer to Q2: Leftmost Columns Difference**  
**Explanation**: The leftmost bins (lowest values) often capture outliers or extreme values in skewed distributions. Differences between train and test sets may arise due to:  
1. **Sampling Variability**: The test set might have fewer observations in the tail due to random splitting.  
2. **Quantile Edge Cases**: Bin edges derived from training data may not perfectly align with test data distributions.  

---

### **Key Concepts**  
- **[[Equal-Frequency Discretization]]**: Focuses on equal observation counts per bin.  
- **[[Quantiles]]**: Basis for determining bin edges.  
- **[[Feature Engineering]]**: Process of transforming raw data into meaningful features.  
- **[[Data Leakage]]**: Avoided by fitting bin edges only on the training set.  

---

### **Visualization**  
- **Bar Plots**: Used to compare the proportion of observations per bin between train and test sets.  
- **Interval Inspection**: `intervals` or `bin_edges_` attributes show quantile-derived boundaries.  

This summary aligns with the notebook’s focus on implementing equal-frequency discretization using multiple libraries while ensuring consistency between train and test sets. Related concepts include [[Binning]], [[Skewness]], and [[Stratified Sampling]].