# Practical 8.2 - Substraction-Quotient-Features.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Structured Academic Summary  

## [[Feature Engineering]]  
**Definition**: The process of creating new features (variables) from existing data to enhance the predictive power of machine learning models.  
**Formula**: N/A (general concept)  
**Example**: Creating `difference` (subtraction of features) and `quotient` (division of features) in the breast cancer dataset.  

---

## [[Subtraction of Features]]  
**Definition**: A method to derive a new feature by subtracting the values of one column from another.  
**Formula**:  
\[ \text{New Feature} = \text{Feature}_1 - \text{Feature}_2 \]  
**Example**:  
```python  
df['difference'] = df['worst compactness'].sub(df['mean compactness'])  # Code Cell 6  
```  

---

## [[Division of Features]]  
**Definition**: A method to derive a new feature by dividing the values of one column by another.  
**Formula**:  
\[ \text{New Feature} = \frac{\text{Feature}_1}{\text{Feature}_2} \]  
**Example**:  
```python  
df['quotient'] = df['worst radius'].div(df['mean radius'])  # Code Cell 9  
```  

---

## [[Aggregation of Features]]  
**Definition**: Combining multiple features into a single feature using statistical operations (e.g., summation).  
**Formula**:  
\[ \text{Aggregated Feature} = \sum_{i=1}^{n} \text{Feature}_i \]  
**Example**:  
```python  
df['worst'] = df[['worst smoothness', 'worst compactness', ...]].sum(axis=1)  # Code Cell 13  
```  

---

## [[Derived Ratios]]  
**Definition**: Creating ratios by dividing original features by an aggregated or reference feature.  
**Formula**:  
\[ \text{Ratio Feature} = \frac{\text{Original Feature}}{\text{Aggregated Feature}} \]  
**Example**:  
```python  
df[features] = df[features].div(df['worst'], axis=0)  # Code Cell 15  
```  

---

## Connections to Prior Concepts  
- [[Feature Engineering]] is a subset of [[Data Wrangling]].  
- [[Aggregation of Features]] relates to [[Statistical Operations]] (e.g., sum, mean).  
- [[Derived Ratios]] extend [[Division of Features]] to multiple variables.  

*Source: Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*