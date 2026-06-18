# Practical 5.4 - Arbitrary-interval-discretization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Arbitrary Interval Discretization  

## Term: **Arbitrary Interval Discretization**  
### Definition  
A method of discretizing continuous variables where the interval boundaries are manually defined by the user, rather than determined algorithmically (e.g., equal-width or equal-frequency). This approach allows for domain-specific or strategic grouping of values.  

### Formula  
No explicit mathematical formula is required. Instead, the process involves:  
- Defining interval boundaries (`bins`) and optional labels.  
- Using `pandas.cut()` with parameters:  
  ```python  
  pd.cut(x, bins, labels=None, include_lowest=True)  
  ```  
  Where:  
  - `x`: Input continuous variable.  
  - `bins`: List of interval edges (e.g., `[0, 10, 20, np.Inf]`).  
  - `labels`: Optional descriptive names for intervals.  

### Example  
**Code Implementation**:  
```python  
# Define custom intervals and labels  
intervals = [0, 10, 20, 30, np.Inf]  
labels = ['0-10', '10-20', '20-30', '>30']  

# Apply arbitrary interval discretization  
data['lstat_labels'] = pd.cut(data['LSTAT'], bins=intervals, labels=labels, include_lowest=True)  

# View discretized results  
data[['LSTAT', 'lstat_labels']].head()  
```  

**Output**:  
| LSTAT   | lstat_labels |  
|---------|---------------|  
| 5.0     | 0-10          |  
| 4.5     | 0-10          |  
| 11.3    | 10-20         |  

**Distribution Check**:  
```python  
data['lstat_labels'].value_counts()  
```  
Output:  
```  
0-10    100  
10-20   80  
20-30   50  
>30     20  
```  

---

## Related Concepts  
- [[Equal-width Discretization]]: Intervals of fixed width.  
- [[Equal-frequency Discretization]]: Intervals with equal observation counts.  
- [[pandas cut()]]: Function for discretization.  
- [[value_counts()]]: Method to analyze distribution of discretized bins.  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).