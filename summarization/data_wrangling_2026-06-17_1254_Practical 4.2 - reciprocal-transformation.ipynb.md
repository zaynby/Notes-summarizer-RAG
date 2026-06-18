# Practical 4.2 - reciprocal-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Summary: Reciprocal Transformation and Diagnostic Plots

#### [[Reciprocal Transformation]]
**Definition:**  
A mathematical transformation that applies the reciprocal function \( \frac{1}{X} \) to variables, drastically altering their distribution. It is undefined for \( X = 0 \) but can be applied to negative values.  

**Formula:**  
\[
X_t = \frac{1}{X}
\]

**Examples:**  
1. **NumPy Implementation:**  
   ```python
   data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.reciprocal(data[['LSTAT', 'NOX', 'DIS', 'RM']])
   ```
2. **scikit-learn (FunctionTransformer):**  
   ```python
   transformer = FunctionTransformer(np.reciprocal, validate=True)
   data_tf = pd.DataFrame(transformer.transform(data[cols]), columns=cols)
   ```
3. **Feature-engine (ReciprocalTransformer):**  
   ```python
   rt = ReciprocalTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])
   data_tf = rt.transform(data)
   ```

---

#### [[Diagnostic Plot]]
**Definition:**  
A visualization tool combining a histogram and a Q-Q plot to evaluate the distribution of a variable before and after transformation.  

**Formula:**  
N/A  

**Example:**  
```python
def diagnostic_plots(df, variable):
    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    df[variable].hist(bins=30)
    plt.subplot(1, 2, 2)
    stats.probplot(df[variable], dist="norm", plot=plt)
    plt.show()
```
**Usage:**  
```python
diagnostic_plots(data_tf, 'DIS')  # To assess the effect of reciprocal transformation on 'DIS'
```

---

### Key Concepts Linked  
- [[Logarithmic Transformation]] (for comparison with other transformations)  
- [[Box-Cox Transformation]] / [[Yeo-Johnson Transformation]] (alternative methods for normalizing data)  
- [[Q-Q Plot]] (statistical tool within diagnostic plots)