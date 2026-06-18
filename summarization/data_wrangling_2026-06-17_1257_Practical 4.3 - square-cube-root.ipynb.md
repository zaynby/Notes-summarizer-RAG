# Practical 4.3 - square-cube-root.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Summary: Square and Cube Root Transformations

#### **Square Root Transformation**  
**Definition**: A power transformation with an exponent of \( \frac{1}{2} \), used to reduce positive skewness in a dataset. It is only applicable to non-negative variables, as negative values would result in undefined or complex numbers.  
**Formula**:  
\[ X_t = X^{1/2} \]  
**Example**:  
- **NumPy**: Apply `np.sqrt()` to variables (e.g., `data[['LSTAT', 'NOX']] = np.sqrt(data[['LSTAT', 'NOX']])`).  
- **Scikit-learn**: Use `FunctionTransformer` with `np.sqrt` to transform selected columns.  
- **Feature-engine**: Utilize `PowerTransformer` with `exp=1/2` for cube root.  

#### **Cube Root Transformation**  
**Definition**: A power transformation with an exponent of \( \frac{1}{3} \), effective for variables with moderate skewness. Like the square root, it requires non-negative input values.  
**Formula**:  
\[ X_t = X^{1/3} \]  
**Example**:  
- **NumPy**: Apply `np.cbrt()` to variables (e.g., `data[['LSTAT', 'NOX']] = np.cbrt(data[['LSTAT', 'NOX']])`).  
- **Scikit-learn**: Implement `FunctionTransformer` with `np.cbrt` for transformation.  
- **Feature-engine**: Configure `PowerTransformer` with `exp=1/3` to achieve cube root.  

---

### Key Implementation Notes  
1. **Diagnostic Plots**: Use histograms and Q-Q plots (via `diagnostic_plots` function) to evaluate the effect of transformations on variable distributions.  
2. **Library Integration**:  
   - **NumPy**: Directly apply `np.sqrt()` or `np.cbrt()` for element-wise transformations.  
   - **Scikit-learn**: Leverage `FunctionTransformer` for flexible pipeline integration.  
   - **Feature-engine**: Use `PowerTransformer` for robust, exponent-specific transformations.  

3. **Constraints**: Both transformations are undefined for negative values, necessitating prior handling of negative data points (e.g., addition of a constant).  

[[Power Transformation]]  
[[NumPy]]  
[[Scikit-learn]]  
[[Feature-engine]]  
[[Q-Q Plot]]  

*Source: Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*