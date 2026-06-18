# Practical 5.1 - Equal-width-discretization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Equal-Width Discretization  

## [[Equal-Width Discretization]]  
**Definition**: A method of binning continuous variables into discrete intervals of **equal width**, where the range of the variable is divided into a specified number of bins. Outliers can be accommodated by extending the first and last bin limits to infinity.  
**Formula**:  
\[ \text{Bin Width} = \frac{\text{Max}(X) - \text{Min}(X)}{\text{Number of Bins}} \]  
**Example**:  
For `LSTAT` (Min = 4.0, Max = 37.0) with 10 bins:  
```python  
width = (37.0 - 4.0) / 10 = 3.3  
intervals = [4.0, 7.3, 10.6, ..., 37.0]  
X_train['lstat_disc'] = pd.cut(X_train['LSTAT'], bins=intervals, include_lowest=True)  
```  

---

## [[Bin Width]]  
**Definition**: The uniform size of each interval in equal-width discretization, calculated as the total range of the variable divided by the number of bins.  
**Formula**:  
\[ \text{Bin Width} = \frac{\text{Max}(X) - \text{Min}(X)}{k} \]  
where \( k \) = number of bins.  
**Example**:  
For `LSTAT` with \( k = 10 \):  
```python  
lstat_range = X_train['LSTAT'].max() - X_train['LSTAT'].min()  
bin_width = lstat_range / 10  
```  

---

## [[Interval Edges]]  
**Definition**: The boundaries defining each bin in equal-width discretization. These are derived from the variable’s range and bin width.  
**Formula**: N/A (computed as \( \text{Min}(X) + i \times \text{Bin Width} \) for \( i = 0, 1, ..., k \)).  
**Example**:  
For `LSTAT` with 10 bins:  
```python  
min_value, max_value = 4.0, 37.0  
intervals = list(range(min_value, max_value + bin_width, int(bin_width)))  
# Output: [4, 7, 10, 14, 17, 20, 23, 27, 30, 33, 37]  
```  

---

## [[pd.cut()]]  
**Definition**: A pandas function to discretize continuous variables into bins defined by `include_lowest=True` ensures the first bin includes the lowest value.  
**Formula**: N/A (implementation-based).  
**Example**:  
```python  
X_train['lstat_disc'] = pd.cut(  
    X_train['LSTAT'],  
    bins=intervals,  
    include_lowest=True  # Captures values ≥ first interval edge  
)  
```  

---

## [[EqualWidthDiscretiser (Feature-engine)]]  
**Definition**: A `Feature-engine` transformer that automates equal-width discretization for multiple variables. Stores bin edges in `binner_dict_`.  
**Formula**: N/A (method-based).  
**Example**:  
```python  
disc = EqualWidthDiscretiser(bins=10, variables=['LSTAT', 'DIS', 'RM'])  
disc.fit(X_train)  
train_t = disc.transform(X_train)  # Transforms specified variables  
```  

---

## [[KBinsDiscretizer (scikit-learn)]]  
**Definition**: A scikit-learn method for equal-width discretization, returning NumPy arrays. Requires encoding strategy (e.g., `ordinal` for integer codes).  
**Formula**: N/A (method-based).  
**Example**:  
```python  
disc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')  
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])  
train_t = disc.transform(X_train[['LSTAT', 'DIS', 'RM']])  # Output: NumPy array  
```  

---

## [[Train-Test Split Consistency]]  
**Definition**: Ensuring discretization intervals are consistent between training and test sets to avoid data leakage. Intervals are determined on the training set and applied to the test set.  
**Formula**: N/A (process-based).  
**Example**:  
```python  
# Fit discretizer on training data  
disc.fit(X_train)  
# Transform both sets  
train_t = disc.transform(X_train)  
test_t = disc.transform(X_test)  
```  

---

## [[pandas Interval Object]]  
**Definition**: The data type used by pandas to represent discrete bins (e.g., `(34.0, 37.0]`). Includes methods to check membership (e.g., `34.0 in interval`).  
**Formula**: N/A (object-based).  
**Example**:  
```python  
test_interval = X_train["lstat_disc"].iloc[0]  
print(34.0 in test_interval)  # True  
print(37.1 in test_interval)  # False  
```  

---

### **Key Concepts**  
- **[[Feature Engineering]]**: Process of transforming raw data into meaningful features (e.g., discretization).  
- **[[Data Preprocessing]]**: Steps like train-test splitting and standardization before modeling.  
- **[[Outliers]]**: Values outside expected ranges, accommodated via expanded interval edges.  

### **Visualization**  
- **Bar Plots**: Used to compare observation counts per bin between train and test sets.  
- **Value Counts**: `value_counts()` checks distribution balance across bins.  

### **Workflow Integration**  
1. **Train-Test Split** → **Interval Calculation** → **Discretization** → **Distribution Validation**.  
2. Tools: `pandas`, `Feature-engine`, `scikit-learn`.  

### **Wikilinks**  
- [[Equal-Width Discretization]] → [[Feature Engineering]] → [[Data Preprocessing]]  
- [[pd.cut()]] → [[KBinsDiscretizer]] → [[EqualWidthDiscretiser]]  
- [[Interval Edges]] → [[Bin Width]] → [[Outliers]]  

This summary aligns with the notebook’s focus on implementing equal-width discretization using multiple libraries while ensuring consistency between datasets.