# Practical 4.5 - Box-Cox-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Summary: Box-Cox Transformation and Related Concepts

---

#### [[Box-Cox Transformation]]
**Definition**: A power transformation method that normalizes data by applying a family of functions parameterized by λ (lambda). It generalizes the logarithm for λ=0 and handles positive values. The optimal λ is selected to achieve the best normalization.  
**Formula**:  
\[
X_t = 
\begin{cases} 
\frac{X^{\lambda} - 1}{\lambda} & \text{if } \lambda \neq 0 \\
\log(X) & \text{if } \lambda = 0 
\end{cases}
\]  
**Example**:  
- **SciPy**:  
  ```python
  data_tf['LSTAT'], param = stats.boxcox(data['LSTAT'])
  ```  
- **Scikit-learn**:  
  ```python
  transformer = PowerTransformer(method='box-cox', standardize=False)
  data_tf = transformer.transform(data[cols])
  ```  
- **Feature-engine**:  
  ```python
  bct = BoxCoxTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])
  data_tf = bct.transform(data)
  ```  

---

#### [[Power Transformation]]
**Definition**: A family of transformations using exponent functions (\(X_t = X^{\lambda}\)) to modify variable distributions. Special cases include square root (\(\lambda = 1/2\)) and cube root (\(\lambda = 1/3\)).  
**Formula**:  
\[
X_t = X^{\lambda}
\]  
**Example**:  
- **Square Root**: \(X_t = \sqrt{X}\)  
- **Cube Root**: \(X_t = \sqrt[3]{X}\)  
- **Box-Cox**: A generalized power transformation (see above).  

---

#### [[Optimal Lambda]]
**Definition**: The value of λ that maximizes normality in the transformed data, determined via maximum likelihood estimation.  
**Formula**: Derived from the likelihood function of the data.  
**Example**:  
- **SciPy**: Printed via `param` in `stats.boxcox()`.  
- **Scikit-learn**: Accessed through `transformer.lambdas_`.  
- **Feature-engine**: Stored in `bct.lambda_dict_`.  

---

#### [[Diagnostic Plots]]
**Definition**: Visual tools (e.g., histograms, Q-Q plots) to assess the distribution of variables before and after transformation.  
**Formula**: N/A (visual diagnostic tool).  
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

### Key Links  
- [[Logarithmic Transformation]] (special case of power/Box-Cox for λ=0).  
- [[Power Transformation]] (general family of transformations).  
- [[Scikit-learn]], [[SciPy]], [[Feature-engine]] (libraries for implementation).