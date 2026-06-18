# Practical 4.3 - square-cube-root.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### **Square Root Transformation**  
**Definition**: A power transformation with an exponent of \( \frac{1}{2} \), used to reduce right skewness in variables. Requires non-negative values to avoid NaN/errors.  
**Formula**:  
\[ X_t = X^{1/2} \]  
**Example**:  
- **NumPy**: `np.sqrt(data[['LSTAT', 'NOX']])`  
- **scikit-learn**: `FunctionTransformer(np.sqrt)`  
- **Feature-engine**: `PowerTransformer(exp=0.5)`  

---

### **Cube Root Transformation**  
**Definition**: A power transformation with an exponent of \( \frac{1}{3} \), less aggressive than square root for reducing skewness. Also requires non-negative values.  
**Formula**:  
\[ X_t = X^{1/3} \]  
**Example**:  
- **NumPy**: `np.cbrt(data[['DIS', 'RM']])`  
- **Feature-engine**: `PowerTransformer(exp=1/3)`  

---

### **Diagnostic Plots**  
**Definition**: Visual tools to evaluate the effect of transformations on variable distributions. Includes histograms and Q-Q plots.  
**Formula**: N/A  
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

### **Key Libraries & Tools**  
1. **[[NumPy]]**: Direct implementation of transformations (e.g., `np.sqrt`, `np.cbrt`).  
2. **[[scikit-learn]]**: `FunctionTransformer` for custom transformations.  
3. **[[Feature-engine]]**: `PowerTransformer` for flexible power/exponent adjustments.  

---

### **Workflow Steps**  
1. **Check original distribution**: Use `diagnostic_plots` on raw data.  
2. **Apply transformation**: Select method (NumPy, scikit-learn, or Feature-engine).  
3. **Visualize transformed data**: Re-run `diagnostic_plots` to assess normality.  

---

This summary links transformations to their mathematical foundations, implementation tools, and diagnostic techniques. Use [[Wikilinks]] to explore related concepts like [[Power Transformation]], [[Q-Q Plot]], or [[Data Preprocessing]] in other notes.