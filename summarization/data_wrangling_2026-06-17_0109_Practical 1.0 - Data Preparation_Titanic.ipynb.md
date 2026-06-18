# Practical 1.0 - Data Preparation_Titanic.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary of Practical: Titanic Data Preprocessing  

## **NumPy**  
**Definition**: A library for numerical computing in Python, providing support for large, multi-dimensional arrays and matrices.  
**Formula**: N/A  
**Example**:  
```python  
import numpy as np  
```  
**Link**: [[Data Preprocessing]]  

---

## **Pandas**  
**Definition**: A library for data manipulation and analysis, offering data structures like DataFrame for structured data.  
**Formula**: N/A  
**Example**:  
```python  
import pandas as pd  
```  
**Link**: [[Data Loading]]  

---

## **Feature Engineering**  
**Definition**: The process of transforming raw data into features (variables) that better represent the underlying problem to learning algorithms.  
**Formula**: N/A  
**Example**:  
```python  
#pip install feature_engine  
```  
**Link**: [[Data Preprocessing]]  

---

## **Data Loading**  
**Definition**: The process of importing data from external sources (e.g., URLs, files) into a DataFrame.  
**Formula**: N/A  
**Example**:  
```python  
data = pd.read_csv('https://www.openml.org/data/get_csv/16826755/phpMYEkMl')  
```  
**Link**: [[Pandas]]  

---

## **Handling Missing Data**  
**Definition**: Replacing or removing invalid/missing data (e.g., placeholders like '?') to ensure data quality.  
**Formula**: N/A  
**Example**:  
```python  
data = data.replace('?', np.nan)  
```  
**Link**: [[Data Preprocessing]]  

---

## **Data Preprocessing Function**  
**Definition**: Custom functions to clean or transform data (e.g., extracting the first cabin letter).  
**Formula**: N/A  
**Example**:  
```python  
def get_first_cabin(row):  
    try:  
        return row.split()[0]  
    except:  
        return np.nan  
```  
**Link**: [[Column Transformation]]  

---

## **Column Transformation**  
**Definition**: Applying functions to modify specific columns in a DataFrame.  
**Formula**: N/A  
**Example**:  
```python  
data['cabin'] = data['cabin'].apply(get_first_cabin)  
```  
**Link**: [[Data Preprocessing Function]]  

---

## **Data Storage**  
**Definition**: Saving processed data to a file (e.g., CSV) for future use.  
**Formula**: N/A  
**Example**:  
```python  
data.to_csv('data/titanic.csv', index=False)  
```  
**Link**: [[Pandas]]  

---

**Key Concepts**: [[Data Preprocessing]], [[Pandas]], [[NumPy]], [[Feature Engineering]]  
**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)