# Practical 4.4 - power-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured summary of the content following the academic format:

---

### [[Power Transformation]]
**Definition**: A mathematical transformation where a variable \( X \) is raised to an exponent \( \lambda \) (lambda) to achieve normality or improve model performance.  
**Formula**:  
\[
X_t = X^{\lambda}
\]  
**Example**:  
```python
# Apply power transformation with λ=0.3 using NumPy
data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.power(data[['LSTAT', 'NOX', 'DIS', 'RM']], 0.3)
```

---

### [[Square Root Transformation]]
**Definition**: A specific power transformation where \( \lambda = \frac{1}{2} \), used for right-skewed data. Not defined for negative values.  
**Formula**:  
\[
X_t = X^{1/2}
\]  
**Example**:  
```python
# Apply square root transformation
data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.sqrt(data[['LSTAT', 'NOX', 'DIS', 'RM']])
```

---

### [[Cube Root Transformation]]
**Definition**: A specific power transformation where \( \lambda = \frac{1}{3} \), suitable for moderately skewed data.  
**Formula**:  
\[
X_t = X^{1/3}
\]  
**Example**:  
```python
# Apply cube root transformation
data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.cbrt(data[['LSTAT', 'NOX', 'DIS', 'RM']])
```

---

### [[FunctionTransformer (Scikit-learn)]]
**Definition**: A scikit-learn class for applying custom-defined functions (e.g., power transformations) to data.  
**Formula**: N/A (user-defined function)  
**Example**:  
```python
# Initialize FunctionTransformer for λ=0.3
transformer = FunctionTransformer(lambda x: np.power(x, 0.3), validate=True)
data_tf = transformer.transform(data[cols])
```

---

### [[PowerTransformer (Feature-engine)]]
**Definition**: A Feature-engine class for applying power transformations with specified exponents to selected variables.  
**Formula**: Follows \( X_t = X^{\lambda} \)  
**Example**:  
```python
# Initialize PowerTransformer with λ=0.3
et = PowerTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'], exp=0.3)
data_tf = et.transform(data)
```

---

### [[Pipeline (Scikit-learn)]]
**Definition**: A scikit-learn tool for chaining multiple transformations or models into a single workflow.  
**Formula**: N/A  
**Example**:  
```python
# Pipeline with different exponents for different features
pipe = Pipeline([
    ('power1', PowerTransformer(variables=['LSTAT', 'NOX'], exp=0.3)),
    ('power2', PowerTransformer(variables=['DIS'], exp=0.4)),
    ('power3', PowerTransformer(variables=['RM'], exp=0.5)),
])
data_tf = pipe.transform(data)
```

---

### Key Notes:
1. **Purpose**: Power transformations (including square/cube roots) are used to normalize data distributions or unmask linear relationships for linear/logistic regression models.
2. **Implementation**: 
   - **NumPy**: Direct array operations (e.g., `np.power`, `np.sqrt`).
   - **Scikit-learn**: `FunctionTransformer` for custom lambdas.
   - **Feature-engine**: `PowerTransformer` for scalable, pipeline-friendly transformations.
3. **Constraints**: Square root requires non-negative values; choose \( \lambda \) based on data skewness.  

Related concepts: [[Normality Assumption]], [[Linear Regression]], [[Data Preprocessing]].