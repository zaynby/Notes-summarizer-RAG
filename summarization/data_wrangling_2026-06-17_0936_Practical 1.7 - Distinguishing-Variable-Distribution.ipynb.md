# Practical 1.7 - Distinguishing-Variable-Distribution.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

```markdown
# Summary: Visualizing Variable Distributions

## [[Data Visualization]]
### Definition  
Techniques used to graphically represent data to understand distributions and patterns, as demonstrated in this practical following Soledad Galli's *Python Feature Engineering Cookbook* (Jan 2020).

### Formula  
N/A  

### Example  
```python
import matplotlib.pyplot as plt
import pandas as pd
boston.hist(bins=30, figsize=(12,12), density=True)
plt.show()
```

---

## [[Histogram]]
### Definition  
A graphical representation of the distribution of numerical data, showing the frequency or density of different value ranges.

### Formula  
N/A  

### Example  
```python
boston.hist(bins=30, figsize=(12,12), density=True)
```

---

## [[Data Loading]]
### Definition  
The process of importing data from external sources into a program for analysis.

### Formula  
N/A  

### Example  
```python
boston = pd.read_csv("./data/boston_local.csv")
```

---

## [[Boston Housing Dataset]]
### Definition  
A widely used dataset containing features of Boston houses (e.g., crime rates, room counts) for regression analysis.

### Formula  
N/A  

### Example  
```python
boston = pd.read_csv("./data/boston_local.csv")
boston.head()
```

---

## [[Density Parameter in Histograms]]
### Definition  
A parameter that normalizes the histogram area to 1, displaying probability density instead of raw frequency counts.

### Formula  
N/A  

### Example  
```python
density=True  # within the hist() function
```
```