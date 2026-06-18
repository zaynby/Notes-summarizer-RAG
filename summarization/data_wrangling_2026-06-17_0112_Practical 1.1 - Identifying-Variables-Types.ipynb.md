# Practical 1.1 - Identifying-Variables-Types.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Identifying Numerical and Categorical Variables

## [[Numerical Variable]]
**Definition**: Data that can be measured and expressed as integers or floats, representing quantities.  
**Formula**: Identified via `data.dtypes` (e.g., `int64`, `float64`).  
**Example**:  
```python
data['fare'].dtype  # float64
```

## [[Discrete Variable]]
**Definition**: A type of numerical variable that represents countable, distinct values (e.g., integers).  
**Formula**: N/A  
**Example**:  
```python
data['sibsp'].unique()  # [0, 1, 2, 3, 4, 5, 8]
```

## [[Continuous Variable]]
**Definition**: A type of numerical variable that can take any value within a range (e.g., real numbers).  
**Formula**: N/A  
**Example**:  
```python
data['fare'].unique()[0:20]  # [7.25, 71.2833, ...]
```

## [[Categorical Variable]]
**Definition**: Variables representing distinct categories or labels (non-numeric).  
**Formula**: Identified via `data.dtypes == 'O'` (object type in pandas).  
**Example**:  
```python
data['embarked'].unique()  # ['S', 'C', 'Q']
```

## [[Mixed Variable]]
**Definition**: A variable containing both numerical and categorical data (e.g., alphanumeric codes).  
**Formula**: N/A  
**Example**:  
```python
data['cabin'].unique()[0:20]  # [nan, 'C86', 'E38', ...]
```

## [[Data Types]]
**Definition**: The classification of data (e.g., integer, float, object) that determines valid operations.  
**Formula**: `data.dtypes`  
**Example**:  
```python
data.dtypes  # fare: float64, embarked: object
```

## [[Unique Values]]
**Definition**: Distinct values present in a variable, used to understand data granularity.  
**Formula**: `.unique()`  
**Example**:  
```python
data['sibsp'].unique()  # [0, 1, 2, 3, 4, 5, 8]
```

## [[Histogram]]
**Definition**: A plot showing the frequency distribution of numerical variables using bins.  
**Formula**: `.hist(bins=X)`  
**Example**:  
```python
data['sibsp'].hist(bins=20)
```

## [[Bar Plot]]
**Definition**: A visualization for categorical variables showing category frequencies.  
**Formula**: `.value_counts().plot.bar()`  
**Example**:  
```python
data['embarked'].value_counts().plot.bar()
```

## [[Value Counts Plot]]
**Definition**: A plot derived from `.value_counts()` to display categorical variable frequencies.  
**Formula**: `.value_counts()`  
**Example**:  
```python
data['embarked'].value_counts()
# S: 644, C: 215, Q: 112
```

---

This summary links key concepts for data wrangling, enabling efficient identification and visualization of variable types in datasets like the Titanic example. Use [[Wikilinks]] to navigate related terms.