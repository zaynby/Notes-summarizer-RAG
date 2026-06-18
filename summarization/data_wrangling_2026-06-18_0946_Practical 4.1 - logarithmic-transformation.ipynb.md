# Practical 4.1 - logarithmic-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured summary of the content using the requested academic format:

---

### [[Logarithmic Transformation]]
**Definition**: A mathematical method used to reduce right-skewness in data by applying the logarithm function. It is applicable only to positive values and helps approximate a normal distribution.  
**Formula**:  
$$ X_t = \log(X) $$  
**Example**:  
```python
# Using NumPy
data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.log(data[['LSTAT', 'NOX', 'DIS', 'RM']])
```

---

### [[Q-Q Plot]]
**Definition**: A graphical tool to compare the distribution of a dataset against a theoretical normal distribution. Quantiles of the data are plotted against quantiles of a normal distribution.  
**Formula**: Not applicable (visual diagnostic tool)  
**Example**:  
```python
# Integrated into diagnostic_plots function
stats.probplot(df[variable], dist="norm", plot=plt)
```

---

### [[Diagnostic Plots]]
**Definition**: A combined visualization (histogram + Q-Q plot) to assess the distribution of a variable before and after transformation.  
**Formula**: Not applicable (visual diagnostic tool)  
**Example**:  
```python
def diagnostic_plots(df, variable):
    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    df[variable].hist(bins=30)
    plt.subplot(1, 2, 2)
    stats.probplot(df[variable], dist="norm", plot=plt)
    plt.show()
```

---

### [[FunctionTransformer (scikit-learn)]]
**Definition**: A scikit-learn class that allows application of arbitrary functions (e.g., logarithm) to transform data.  
**Formula**: Not applicable (implementation tool)  
**Example**:  
```python
from sklearn.preprocessing import FunctionTransformer
transformer = FunctionTransformer(np.log, validate=True)
data_tf = transformer.transform(data[cols])
```

---

### [[LogTransformer (Feature-engine)]]
**Definition**: A specialized transformer from the Feature-engine library for applying logarithmic transformations while handling errors for non-positive values.  
**Formula**: Not applicable (implementation tool)  
**Example**:  
```python
from feature_engine.transformation import LogTransformer
lt = LogTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])
data_tf = lt.transform(data)
```

---

### [[Normal Distribution]]
**Definition**: A probability distribution characterized by a symmetric bell-shaped curve, assumed by many statistical models (e.g., linear regression).  
**Formula**:  
$$ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} $$  
**Example**:  
Referenced in Q-Q plots (`dist="norm"`) to compare data against a theoretical normal distribution.

---

### Key Concept Links
- [[Logarithmic Transformation]] is used to approach [[Normal Distribution]].
- [[Q-Q Plot]] and [[Diagnostic Plots]] are used to evaluate the need for transformations.
- [[FunctionTransformer]] and [[LogTransformer]] are implementation tools for applying transformations.