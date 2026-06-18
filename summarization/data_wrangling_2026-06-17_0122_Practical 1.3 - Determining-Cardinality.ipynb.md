# Practical 1.3 - Determining-Cardinality.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Cardinality in Categorical Variables

## **Cardinality**  
### **Definition**  
Cardinality refers to the number of **unique categories** present in a categorical variable. It quantifies the diversity of distinct labels or values within a variable.  

### **Formula**  
Cardinality is calculated as:  
\[ \text{Cardinality}(X) = \text{Number of unique values in variable } X \]  
In Python, this is implemented using pandas' `nunique()` method:  
```python
data['column_name'].nunique()  # Excludes missing values by default
data['column_name'].nunique(dropna=False)  # Includes missing values as a category
```  

### **Example**  
- **Variable**: `GENDER` with values `['male', 'female', 'male', 'female']`  
  - Cardinality = 2 (unique categories: 'male', 'female').  
- **Code Example**:  
  ```python
  data['GENDER'].nunique()  # Output: 2
  ```  
- **Visualization**:  
  ```python
  data.nunique().plot.bar(figsize=(12,6))  # Bar plot showing cardinality per variable
  ```  

---

## **Related Concepts**  
- **[[Categorical Variable]]**: A variable whose values represent categories (e.g., "gender," "color").  
- **[[Missing Data]]**: Absent values in a dataset, which can optionally be counted as an additional category in cardinality calculations using `dropna=False`.  
- **[[Pandas (Python library)]]**: Provides methods like `nunique()` for efficient cardinality computation.  

---

## **Key Applications**  
1. **Data Exploration**: Identifying variables with high cardinality (e.g., ZIP codes) that may require special handling.  
2. **Feature Engineering**: Deciding between encoding techniques (e.g., one-hot encoding vs. target encoding) based on cardinality.  
3. **Outlier Detection**: High cardinality might indicate noisy or erroneous data entries.  

This summary integrates concepts from the provided notebooks, emphasizing practical implementation in Python.