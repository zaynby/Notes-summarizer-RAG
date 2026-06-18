# Practical 4.4 - power-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### [[Power Transformation]]
**Definition**: A mathematical transformation where a variable is raised to an exponent λ (lambda), used to make data more normally distributed or improve model performance.  
**Formula**:  
\[ X_t = X^{\lambda} \]  
**Examples**:  
- Square root: \( \lambda = 1/2 \)  
- Cube root: \( \lambda = 1/3 \)  
- Arbitrary exponent (e.g., \( \lambda = 0.3 \))  

---

### [[Square Root Transformation]]  
**Definition**: A specific power transformation with \( \lambda = 1/2 \), used for right-skewed data. Not defined for negative values.  
**Formula**:  
\[ X_t = X^{1/2} \]  
**Example**:  
```python
data_tf[['LSTAT', 'NOX']] = np.sqrt(data[['LSTAT', 'NOX']])
```  

---

### [[Cube Root Transformation]]  
**Definition**: A specific power transformation with \( \lambda = 1/3 \), suitable for moderately skewed data.  
**Formula**:  
\[ X_t = X^{1/3} \]  
**Example**:  
```python
data_tf[['DIS', 'RM']] = np.cbrt(data[['DIS', 'RM']])
```  

---

### [[Exponential Transformation with NumPy]]  
**Definition**: Applying power transformations using NumPy's `np.power()` function.  
**Formula**:  
\[ X_t = X^{\lambda} \]  
**Example**:  
```python
data_tf[['LSTAT', 'NOX']] = np.power(data[['LSTAT', 'NOX']], 0.3)
```  

---

### [[Exponential Transformation with Scikit-learn]]  
**Definition**: Using `FunctionTransformer` to apply custom power transformations.  
**Formula**:  
\[ X_t = X^{\lambda} \]  
**Example**:  
```python
transformer = FunctionTransformer(lambda x: np.power(x, 0.3), validate=True)
data_tf = pd.DataFrame(transformer.transform(data[cols]), columns=cols)
```  

---

### [[Exponential Transformation with Feature-engine]]  
**Definition**: Applying power transformations via `PowerTransformer` from the Feature-engine library.  
**Formula**:  
\[ X_t = X^{\lambda} \]  
**Example**:  
```python
et = PowerTransformer(variables=['LSTAT', 'NOX'], exp=0.3)
data_tf = et.transform(data)
```  

---

### [[Applying Different Power Transformations]]  
**Definition**: Using a pipeline to apply varying exponents to different features.  
**Formula**:  
\[ X_t = X^{\lambda_i} \quad \text{for feature } i \]  
**Example**:  
```python
pipe = Pipeline([
    ('power1', PowerTransformer(variables=['LSTAT'], exp=0.3)),
    ('power2', PowerTransformer(variables=['RM'], exp=0.5))
])
data_tf = pipe.transform(data)
```  

---

### Key Notes:
1. **Diagnostic Plots**: Use histograms and Q-Q plots (via `diagnostic_plots()`) to assess distributional changes post-transformation.  
2. **Constraints**: Square root requires non-negative values; cube root can handle negatives but may not fully normalize data.  
3. **Libraries**: NumPy (direct computation), Scikit-learn (flexible transformers), Feature-engine (dedicated power tools).  

All transformations aim to improve normality or linearity for regression models like linear/logistic regression.