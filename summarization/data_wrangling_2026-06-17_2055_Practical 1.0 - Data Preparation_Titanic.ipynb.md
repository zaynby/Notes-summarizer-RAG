# Practical 1.0 - Data Preparation_Titanic.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Structured Academic Summary  

## [[Data Preprocessing]]  
**Definition**: The process of cleaning, transforming, and preparing raw data for analysis or modeling.  
**Formula**: Not applicable.  
**Example**:  
```python  
# Cabin extraction function  
def get_first_cabin(row):  
    try:  
        return row.split()[0]  
    except:  
        return np.nan  

# Handling missing data  
data = data.replace('?', np.nan)  

# Applying custom function  
data['cabin'] = data['cabin'].apply(get_first_cabin)  
```  

---

## [[NumPy]]  
**Definition**: A library for numerical computing in Python, providing support for arrays, matrices, and mathematical operations.  
**Formula**: `np.array([1, 2, 3])` (creates a NumPy array).  
**Example**:  
```python  
import numpy as np  # Importing NumPy  
```  

---

## [[Pandas]]  
**Definition**: A library for data manipulation and analysis in Python, built on NumPy.  
**Formula**: `pd.DataFrame(data)` (creates a Pandas DataFrame).  
**Example**:  
```python  
import pandas as pd  # Importing Pandas  
```  

---

## [[Feature Engineering]]  
**Definition**: The process of transforming raw data into meaningful features for machine learning models.  
**Formula**: Not applicable.  
**Example**:  
```python  
# Installing Feature Engine (commented)  
# pip install feature_engine  
```  

---

## [[Cabin Extraction Function]]  
**Definition**: A custom function to extract the first character from a cabin string (e.g., "C123" → "C").  
**Formula**: `row.split()[0]` (splits the string and returns the first element).  
**Example**:  
```python  
def get_first_cabin(row):  
    try:  
        return row.split()[0]  
    except:  
        return np.nan  
```  

---

## [[Data Loading from URL]]  
**Definition**: The process of loading data directly from a web URL into a Pandas DataFrame.  
**Formula**: `pd.read_csv('URL')` (loads CSV data from a URL).  
**Example**:  
```python  
data = pd.read_csv('https://www.openml.org/data/get_csv/16826755/phpMYEkMl')  
```  

---

## [[Handling Missing Data]]  
**Definition**: The process of identifying and addressing missing or invalid values in a dataset.  
**Formula**: `data.replace('value', np.nan)` (replaces specified values with NaN).  
**Example**:  
```python  
data = data.replace('?', np.nan)  
```  

---

## [[Applying Custom Function to Column]]  
**Definition**: Using the `.apply()` method to transform values in a DataFrame column with a custom function.  
**Formula**: `data['column'].apply(function_name)`.  
**Example**:  
```python  
data['cabin'] = data['cabin'].apply(get_first_cabin)  
```  

---

## [[Saving DataFrame to CSV]]  
**Definition**: Exporting a Pandas DataFrame to a CSV file for storage or sharing.  
**Formula**: `data.to_csv('path/to/file.csv', index=False)`.  
**Example**:  
```python  
data.to_csv('data/titanic.csv', index=False)  # Save to "data" subfolder  
```  

--- 

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).