# Practical 2.0 - Data Preparation_CreditApprovalUCI.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Credit Approval Dataset Preparation

## [[Data Preprocessing]]
**Definition**: Steps taken to transform raw data into a suitable format for analysis, including handling missing values, converting data types, and encoding variables.  
**Example**:  
```python
data = pd.read_csv('./data/crx.data', header=None)  # Load raw data
data.replace('?', np.nan)  # Handle missing values
data['A2'] = data['A2'].astype('float')  # Convert data types
```

---

## [[Missing Data Handling]]
**Definition**: Process of addressing absent or undefined values in a dataset.  
**Formula**: Not applicable (procedural step).  
**Example**:  
```python
data = data.replace('?', np.nan)  # Replace placeholder '?' with NaN
random.seed(9001)
values = list(set([random.randint(0, len(data)) for p in range(0, 100)]))
for var in ['A3', 'A8', 'A9', 'A10']: 
    data.loc[values, var] = np.nan  # Introduce artificial missing values
```

---

## [[Variable Type Conversion]]
**Definition**: Transforming variables into appropriate numerical or categorical formats.  
**Example**:  
```python
data['A2'] = data['A2'].astype('float')  # Convert column A2 to float
data['A14'] = data['A14'].astype('float')  # Convert column A14 to float
```

---

## [[Target Variable Encoding]]
**Definition**: Converting categorical target variables into numerical binary values (0/1).  
**Example**:  
```python
data['A16'] = data['A16'].map({'+':1, '-':0})  # Map '+' to 1 and '-' to 0
```

---

## [[Categorical Variable Identification]]
**Definition**: Identifying variables with non-numeric (object) data types.  
**Example**:  
```python
cat_cols = [c for c in data.columns if data[c].dtypes=='O']  # List categorical columns
data[cat_cols].head()  # Display first 5 rows of categorical variables
```

---

## [[Numerical Variable Identification]]
**Definition**: Identifying variables with integer or numeric data types.  
**Example**:  
```python
num_cols = [n for n in data.columns if data[n].dtypes=='int']  # List numerical columns
data[num_cols].head()  # Display first 5 rows of numerical variables
```

---

## [[Artificial Missing Data Generation]]
**Definition**: Introducing random missing values to simulate real-world data challenges.  
**Example**:  
```python
random.seed(9001)
values = list(set([random.randint(0, len(data)) for p in range(0, 100)]))
for var in ['A3', 'A8', 'A9', 'A10']: 
    data.loc[values, var] = np.nan  # Assign NaN to random positions
```

---

## [[Data Saving]]
**Definition**: Exporting processed data to a file for future use.  
**Example**:  
```python
data.to_csv('./data/creditApprovalUCI.csv', index=False)  # Save as CSV
```

---

**Source**: Adapted from *Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*.  
**Dataset Source**: [UCI Credit Approval Dataset](http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/)