# Practical 4.1 - logarithmic-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

```markdown
# Summary: Transforming Numerical Variables with Logarithmic Transformation

## [[Logarithmic Transformation]]
**Definition**: A mathematical transformation applied to positive variables to alter the shape of their distribution, often making it more Gaussian-like. It is particularly effective for right-skewed data and can help unmask linear relationships in regression models.

**Formula**: 
\[
X_t = \log(X)
\]
where \(X\) is the original variable and \(X_t\) is the transformed variable.

**Example**:  
- Applied to columns `LSTAT`, `NOX`, `DIS`, and `RM` in the Boston House Price dataset using:  
  - **NumPy**: `np.log(data[['LSTAT', 'NOX', 'DIS', 'RM']])`  
  - **Scikit-learn**: `FunctionTransformer(np.log)`  
  - **Feature-engine**: `LogTransformer(variables=[...])`  

---

## [[Q-Q Plot]]
**Definition**: A quantile-quantile plot used to compare the distribution of a variable against a theoretical normal distribution. It assesses whether the variable follows a Gaussian distribution by plotting its quantiles against the expected quantiles of a normal distribution.

**Formula**: No direct mathematical formula; based on comparing empirical quantiles (\(Q_{\text{observed}}\)) to theoretical normal quantiles (\(Q_{\text{expected}}\)).

**Example**:  
Generated using `scipy.stats.probplot` within the `diagnostic_plots` function to evaluate the normality of variables like `LSTAT` before and after transformation.

---

## [[Diagnostic Plots]]
**Definition**: A combination of visualizations (histogram and Q-Q plot) used to diagnose the distributional characteristics of a variable. These plots help evaluate the effectiveness of transformations in achieving normality.

**Formula**: Not applicable, as it is a visualization tool.

**Example**:  
The `diagnostic_plots` function generates:  
1. A histogram (left subplot) to visualize the variable's distribution.  
2. A Q-Q plot (right subplot) to compare quantiles against a normal distribution.  
```python
def diagnostic_plots(df, variable):
    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    df[variable].hist(bins=30)
    plt.subplot(1, 2, 2)
    stats.probplot(df[variable], dist="norm", plot=plt)
    plt.show()
```
**Usage**: `diagnostic_plots(data, 'LSTAT')` to compare distributions pre- and post-logarithmic transformation.

---

## Key Libraries and Tools
- **NumPy**: Directly applies logarithmic transformation via `np.log()`.  
- **Scikit-learn**: Uses `FunctionTransformer` to wrap `np.log` for pipeline compatibility.  
- **Feature-engine**: Provides `LogTransformer` for robust, column-specific transformations.
```