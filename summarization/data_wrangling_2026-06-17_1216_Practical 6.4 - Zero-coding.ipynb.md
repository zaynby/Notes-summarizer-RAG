# Practical 6.4 - Zero-coding.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured summary of the content using the requested format:

---

### **Zero-coding**  
**Definition**: A variant of bottom-coding where the lower tail of a variable is capped at **zero**, typically used for variables that cannot logically take negative values (e.g., income, age).  
**Formula**:  
For all values \( x < 0 \), replace with \( 0 \):  
\[ x_{\text{capped}} = \max(x, 0) \]  
**Example**:  
```python  
# Cap negative values at 0 for all columns  
data.loc[data['x'] < 0, 'x'] = 0  
data.loc[data['y'] < 0, 'y'] = 0  
data.loc[data['z'] < 0, 'z'] = 0  
```  

---

### **ArbitraryOutlierCapper**  
**Definition**: A class from the `Feature-engine` library used to cap outliers at specified thresholds for either or both tails of a distribution.  
**Formula**:  
- **Parameters**:  
  - `min_capping_dict`: Dictionary specifying minimum caps (e.g., `{'x': 0}`).  
  - `max_capping_dict`: Dictionary specifying maximum caps (e.g., `{'x': 7}`).  
**Example**:  
```python  
# Cap minimum at 0 and maximum at 7 for all columns  
capper = ArbitraryOutlierCapper(  
    min_capping_dict={'x': 0, 'y': 0, 'z': 0},  
    max_capping_dict={'x': 7, 'y': 7, 'z': 7}  
)  
data_t = capper.fit_transform(data)  
```  

---

### **Top-coding & Bottom-coding**  
**Definition**:  
- **Top-coding**: Capping values above a specified threshold (right tail).  
- **Bottom-coding**: Capping values below a specified threshold (left tail).  
**Relationship**:  
- Zero-coding is a special case of **bottom-coding** where the threshold is 0.  
- Both are forms of [[Capping]] (also called censoring or capping).  
**Example**:  
```python  
# Bottom-coding at 0 (equivalent to zero-coding)  
data.loc[data['x'] < 0, 'x'] = 0  

# Top-coding at 7  
data.loc[data['x'] > 7, 'x'] = 7  
```  

---

### **Key Workflow Steps**  
1. **Visualize Data**: Use histograms to identify negative values (`data.hist()`).  
2. **Apply Capping**:  
   - Manual capping with `DataFrame.loc`.  
   - Automated capping with `ArbitraryOutlierCapper`.  
3. **Validate Results**:  
   - Check minimum/maximum values post-capping (`data.min()`, `data.max()`).  
   - Inspect caps via `capper.left_tail_caps_` and `capper.right_tail_caps_`.  

---

### **Solution to Q4**  
To cap both tails (min at 0, max at 7):  
```python  
# Modified capper for min and max thresholds  
capper = ArbitraryOutlierCapper(  
    min_capping_dict={'x': 0, 'y': 0, 'z': 0},  
    max_capping_dict={'x': 7, 'y': 7, 'z': 7}  
)  
data_t = capper.fit_transform(data)  
```  

---

### **Related Concepts**  
- [[Winsorization]]: Caps values at specified percentiles (e.g., 5th and 95th).  
- [[Outliers]]: Values that deviate significantly from the majority.  
- [[Capping]]: General term for threshold-based value replacement.  

This summary integrates methods from the notebook with foundational concepts for handling outliers in datasets.