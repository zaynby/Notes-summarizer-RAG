# Practical 5.1 - Equal-width-discretization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Structured Academic Summary: Equal-Width Discretization  

## [[Equal-Width Discretization]]  
**Definition**: A method of binning continuous variables into discrete intervals of equal size (width), determined by the variable’s range and the number of bins specified.  
**Formula**:  
\[ \text{Width} = \frac{\text{Max}(X) - \text{Min}(X)}{\text{Bins}} \]  
**Example**:  
For `LSTAT` in the Boston Housing dataset, with a range of 5–37 and 10 bins:  
```python  
width = (37 - 5) / 10 = 3.2  
```  
Bins: [5, 8.2), [8.2, 11.4), ..., [37, 40.2].  

---

## [[Interval Width]]  
**Definition**: The size of each bin in equal-width discretization, calculated as the range of the variable divided by the number of bins.  
**Formula**:  
\[ \text{Width} = \frac{\text{Max}(X) - \text{Min}(X)}{k} \]  
where \( k \) = number of bins.  
**Example**:  
For `LSTAT` (range = 32):  
```python  
lstat_range = X_train['LSTAT'].max() - X_train['LSTAT'].min()  
bin_width = lstat_range / 10  # 3.2  
```  

---

## [[pd.cut()]]  
**Definition**: A pandas function to discretize continuous variables into bins using specified edges.  
**Formula**: N/A  
**Example**:  
```python  
X_train['lstat_disc'] = pd.cut(  
    x=X_train['LSTAT'],  
    bins=intervals,  
    include_lowest=True  
)  
```  
Creates categorical bins for `LSTAT` (e.g., (5, 8.2], (8.2, 11.4]).  

---

## [[Train-Test Split]]  
**Definition**: Dividing data into training and testing subsets to evaluate model performance.  
**Formula**: N/A  
**Example**:  
```python  
X_train, X_test, y_train, y_test = train_test_split(  
    data.drop('MEDV', axis=1),  
    data['MEDV'],  
    test_size=0.3, random_state=0  
)  
```  

---

## [[EqualWidthDiscretiser (Feature-engine)]]  
**Definition**: A Feature-engine class to automate equal-width discretization for multiple variables.  
**Formula**: N/A  
**Example**:  
```python  
disc = EqualWidthDiscretiser(  
    bins=10,  
    variables=['LSTAT', 'DIS', 'RM']  
)  
disc.fit(X_train)  
X_train = disc.transform(X_train)  
```  

---

## [[KBinsDiscretizer (scikit-learn)]]  
**Definition**: A scikit-learn transformer for equal-width binning with ordinal encoding.  
**Formula**: N/A  
**Example**:  
```python  
disc = KBinsDiscretizer(  
    n_bins=10,  
    encode='ordinal',  
    strategy='uniform'  
)  
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])  
X_train_t = disc.transform(X_train[['LSTAT', 'DIS', 'RM']])  
```  

---

## [[Interval Object (pandas)]]  
**Definition**: The data type returned by `pd.cut()`, representing a half-open interval (e.g., (5, 8.2]).  
**Example**:  
```python  
print(X_train["lstat_disc"].iloc[0])  # Output: (34.0, 37.0]  
print(type(X_train["lstat_disc"].iloc[0]))  # Output: pandas._typeds.Interval  
```  
**Key Property**:  
```python  
34.0 in test_interval  # True  
37.0 in test_interval  # False (exclusive upper bound)  
```  

---

## [[Proportion of Observations per Bin]]  
**Definition**: The distribution of data points across discretized intervals, used to compare train/test set distributions.  
**Example**:  
```python  
t1 = X_train['lstat_disc'].value_counts() / len(X_train)  
t2 = X_test['lstat_disc'].value_counts() / len(X_test)  
tmp = pd.concat([t1, t2], axis=1).plot.bar()  
```  

---

### **Related Concepts**  
- [[Binning]]: General process of grouping continuous values into intervals.  
- [[Discretization]]: Conversion of continuous variables into discrete categories.  
- [[Feature Engineering]]: Process of transforming raw data into engineered features for modeling.  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)