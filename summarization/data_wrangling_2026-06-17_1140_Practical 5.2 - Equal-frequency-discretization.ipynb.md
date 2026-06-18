# Practical 5.2 - Equal-frequency-discretization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Structured Academic Summary: Equal-Frequency Discretization  

## [[Equal-Frequency Discretization]]  
**Definition**: A technique to divide continuous variables into intervals (bins) that contain an equal number of observations. This method uses quantiles to determine bin edges, making it robust to skewed distributions.  
**Formula**: For \( N \) bins, the \( i \)-th bin edge is the \( \frac{i}{N} \)-th quantile of the data.  
**Example**: Using `pd.qcut(X_train['LSTAT'], 10)` to split `LSTAT` into 10 equal-frequency bins.  

---

## [[Quantiles]]  
**Definition**: Values that divide the dataset into equal-sized groups. The \( k \)-th quantile represents the value below which \( \frac{k}{N} \times 100\% \) of observations fall.  
**Formula**: For \( N \) bins, quantiles are calculated as \( Q_i = \text{value at } \frac{i}{N} \)-th position in sorted data.  
**Example**: `pd.qcut` uses quantiles to define bin edges (e.g., 10 quantiles for deciles).  

---

## [[Bin Edges]]  
**Definition**: The boundary values that separate bins in discretization. In equal-frequency discretization, these are determined by quantiles.  
**Formula**: \( \text{Bin Edges} = [Q_0, Q_1, \dots, Q_N] \), where \( Q_0 = -\infty \) and \( Q_N = +\infty \).  
**Example**: `intervals` variable in Code Cell 8 stores the 10 quantile-based edges for `LSTAT`.  

---

## [[pandas.qcut]]  
**Definition**: A pandas function for quantile-based binning to ensure equal observation counts per bin.  
**Parameters**:  
- `q`: Number of bins (e.g., `q=10` for deciles).  
- `retbins`: Option to return bin edges.  
**Example**:  
```python  
X_train['lstat_disc'], intervals = pd.qcut(X_train['LSTAT'], 10, retbins=True)  
```  

---

## [[pd.cut]]  
**Definition**: A pandas function to discretize data into bins defined by user-specified edges.  
**Example**: Applying training-derived `intervals` to the test set:  
```python  
X_test['lstat_disc'] = pd.cut(X_test['LSTAT'], bins=intervals)  
```  

---

## [[EqualFrequencyDiscretiser (Feature-engine)]]  
**Definition**: A `Feature-engine` transformer that automates equal-frequency discretization for multiple variables.  
**Key Parameters**:  
- `q`: Number of bins (e.g., `q=10`).  
- `variables`: List of columns to discretize.  
**Example**:  
```python  
disc = EqualFrequencyDiscretiser(q=10, variables=['LSTAT', 'DIS', 'RM'])  
disc.fit(X_train)  
```  

---

## [[KBinsDiscretizer (scikit-learn)]]  
**Definition**: A scikit-learn method for binning using quantiles with `strategy='quantile'`.  
**Parameters**:  
- `n_bins`: Number of bins (e.g., `n_bins=10`).  
- `encode='ordinal'`: Encodes bins as integers (0, 1, ...).  
**Example**:  
```python  
disc = KBinsDiscretizer(n_bins=10, strategy='quantile', encode='ordinal')  
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])  
```  

---

## [[Observation Proportion per Bin]]  
**Definition**: The percentage of data points assigned to each bin, which should be roughly equal in equal-frequency discretization.  
**Formula**: \( \text{Proportion}_i = \frac{\text{Count in Bin } i}{\text{Total Observations}} \)  
**Example**:  
```python  
X_train['lstat_disc'].value_counts(normalize=True)  # Should show ~10% per bin  
```  

---

## **Answer to Q2: Leftmost Columns Difference**  
The leftmost bins (e.g., first two columns in the bar plot) may show discrepancies due to:  
1. **Skewed Data**: Variables like `LSTAT` (lower status of the population) often have right-skewed distributions, causing the lowest bin to capture fewer extreme values.  
2. **Quantile Calculation**: Edge cases (e.g., duplicates or sparse data at extremes) can lead to uneven splits.  
3. **Test Set Variability**: The test set may naturally differ slightly from the training set distribution.  

---

## **Related Concepts**  
- [[Quantile-Based Binning]]  
- [[Data Preprocessing]]  
- [[Feature Engineering]]  
- [[Scikit-learn Transformers]]  
- [[Pandas Data Manipulation]]  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)