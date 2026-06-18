# Practical 2.1 - Removing-observations-with-missing-data.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Complete Case Analysis (CCA)

## Term: [[Complete Case Analysis (CCA)]]  
### Definition  
Complete Case Analysis (CCA), also known as **list-wise deletion**, is a method for handling missing data where observations (rows) containing missing values in **any** of the variables are discarded. It preserves the distribution of variables **if data is missing at random** and the proportion of missing data is small. However, it risks significant data loss if missingness is widespread across variables.  

### Formula  
CCA is implemented using the `dropna()` function in pandas:  
- **Full dataset**: `data.dropna()`  
- **Subset of variables**: `data.dropna(subset=[column1, column2, ...])`  

### Example  
```python
# Create complete case dataset for all variables
data_cca = data.dropna()

# Create complete case dataset for specific variables (e.g., A1, A2, A6, A7, A14)
data_cca_subset = data.dropna(subset=['A1', 'A2', 'A6', 'A7', 'A14'])

# Output: Compare original and cleaned dataset sizes
print('Total observations:', len(data))
print('Complete cases:', len(data_cca))
```  
**Output**:  
```
Number of total observations: X  
Number of observations with complete cases: Y  
```  
Where `Y < X` due to removed rows with missing values.  

---

## Related Concepts  
- **[[Missing Data]]**: Data points not present in the dataset.  
- **[[List-wise Deletion]]**: Synonym for CCA.  
- **[[Data Imputation]]**: Alternative to CCA for handling missing data (e.g., mean/median imputation).  

*Source: Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*