# Practical 4.2 - reciprocal-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Summary: Reciprocal Transformation

#### **Term**: [[Reciprocal Transformation]]  
**Definition**: A mathematical transformation that applies the reciprocal function (\( X_t = 1/X \)) to variables. It drastically alters the distribution of variables and is undefined for \( X = 0 \), but applicable to negative values. It is often used to normalize skewed data or unmask linear relationships in regression models.  

**Formula**:  
\[
X_t = \frac{1}{X}
\]  

**Example**:  
1. **NumPy Implementation**:  
   ```python  
   data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.reciprocal(data[['LSTAT', 'NOX', 'DIS', 'RM']])  
   ```  
   Applies the reciprocal to specified columns in a DataFrame.  

2. **Scikit-learn (`FunctionTransformer`)**:  
   ```python  
   transformer = FunctionTransformer(np.reciprocal, validate=True)  
   data_tf = pd.DataFrame(transformer.transform(data[cols]), columns=cols)  
   ```  
   Transforms selected columns using scikit-learn’s `FunctionTransformer`.  

3. **Feature-engine (`ReciprocalTransformer`)**:  
   ```python  
   rt = ReciprocalTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])  
   data_tf = rt.transform(data)  
   ```  
   Uses Feature-engine’s dedicated `ReciprocalTransformer` for the transformation.  

**Evaluation**:  
The effect of the transformation is assessed using [[Diagnostic Plots]] (histogram and Q-Q plots) to compare the distribution before and after applying the reciprocal function.  

---

### Key Concepts:  
- **[[Diagnostic Plots]]**: Visual tools (histogram + Q-Q plot) to evaluate distributional changes.  
- **[[NumPy]]**: Library for numerical computations in Python.  
- **[[scikit-learn]]**: Machine learning library providing preprocessing tools like `FunctionTransformer`.  
- **[[Feature-engine]]**: Library specialized in feature engineering, including `ReciprocalTransformer`.  
- **[[Box-Cox Transformation]]**: Another common transformation for normalizing data (requires positive values).  

--- 

This summary aligns with the structured academic format and connects related concepts via wikilinks for cross-referencing.