# Practical 5.4 - Arbitrary-interval-discretization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Arbitrary Interval Discretization  

## Term: [[Arbitrary Interval Discretization]]  
**Definition**: A method of discretizing continuous variables where the interval boundaries are manually defined by the user, rather than derived from statistical properties of the data (e.g., quantiles or equal width). This approach allows for domain-specific or context-driven binning.  

**Formula**: No fixed mathematical formula; intervals are explicitly specified by the user. The general process involves:  
1. Defining interval edges (e.g., `[0, 10, 20, 30, ∞]`).  
2. Applying these edges to categorize data using a function like `pd.cut()`.  

**Example**:  
- **Code**:  
  ```python  
  intervals = [0, 10, 20, 30, np.Inf]  
  labels = ['0-10', '10-20', '20-30', '>30']  
  data['lstat_labels'] = pd.cut(data['LSTAT'], bins=intervals, labels=labels, include_lowest=True)  
  ```  
- **Output**: The `LSTAT` variable (lower status of the population) is binned into user-defined ranges (e.g., `0-10`, `10-20`).  
- **Observation Counts**:  
  ```python  
  data['lstat_labels'].value_counts()  
  ```  
  This shows the number of observations in each arbitrary interval.  

---

## Related Concepts  
- **[[Equal-width Discretization]]**: Bins of equal size (e.g., width = (max - min)/bins).  
- **[[Equal-frequency Discretization]]**: Bins with equal number of observations (quantile-based).  
- **[[pandas cut()]]**: Function used to implement arbitrary interval discretization.  
- **[[Boston Housing Dataset]]**: Dataset used in examples, containing features like `LSTAT` (percentage of lower status of the population).  

---

## Key Parameters in `pd.cut()`  
- `bins`: User-defined interval edges (e.g., `[0, 10, 20, 30, ∞]`).  
- `labels`: Optional custom labels for bins (e.g., `['0-10', '10-20']`).  
- `include_lowest=True`: Ensures the first bin includes the minimum value.  

This method is useful for aligning discretization with business rules or domain knowledge rather than purely statistical criteria.