# Practical 2.0 - Data Preparation_CreditApprovalUCI.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Credit Approval Dataset Preparation

## [[Missing Data]]  
**Definition**: Absence of values in a dataset for specific observations within variables.  
**Formula**: N/A  
**Example**:  
```python
data.replace('?', np.nan)  # Replaces placeholder '?' with NaN
```

## [[Data Preprocessing]]  
**Definition**: Process of cleaning and transforming raw data into an analysis-ready format.  
**Formula**: N/A  
**Example**:  
- Handling missing values  
- Converting variable types (e.g., `A2` to float)  
- Encoding target variable (`A16` to binary 1/0)  

## [[Data Encoding]]  
**Definition**: Conversion of categorical variable values into numerical representations.  
**Formula**:  
Binary encoding:  
\[ y = \begin{cases} 1 & \text{if } x = '+' \\ 0 & \text{if } x = '-' \end{cases} \]  
**Example**:  
```python
data['A16'].map({'+': 1, '-': 0})  # Encodes target variable
```

## [[Categorical Variables]]  
**Definition**: Variables representing discrete categories (nominal/ordinal).  
**Formula**: N/A  
**Example**:  
```python
cat_cols = [c for c in data.columns if data[c].dtypes == 'O']  # Identifies object-type columns
```

## [[Numerical Variables]]  
**Definition**: Variables containing quantitative values (integer/float).  
**Formula**: N/A  
**Example**:  
```python
num_cols = [n for n in data.columns if data[n].dtypes == 'int']  # Selects integer-type columns
```

## [[Data Augmentation]]  
**Definition**: Introduction of synthetic modifications (e.g., missing values) to enhance data utility.  
**Formula**: N/A  
**Example**:  
```python
random.seed(9001)
values = [random.randint(0, len(data)) for _ in range(100)]
data.loc[values, ['A3', 'A8', 'A9', 'A10']] = np.nan  # Adds missing values
```

## [[Variable Conversion]]  
**Definition**: Changing the data type of a variable (e.g., string to numeric).  
**Formula**: N/A  
**Example**:  
```python
data['A2'] = data['A2'].astype('float')  # Converts column to float
```

---

**Source**: Adapted from Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)