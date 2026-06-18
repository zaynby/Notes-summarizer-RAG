# Practical 4.6 - Yeo-Johnson-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Summary: Yeo-Johnson Transformation

#### Term: [[Yeo-Johnson Transformation]]  
**Definition**:  
An extension of the [[Box-Cox Transformation]] that can handle variables with zero and negative values, in addition to positive values. It applies different power transformation formulas based on the sign of the input variable \( X \) and the transformation parameter \( \lambda \).  

**Formula**:  
\[
X_t = 
\begin{cases} 
\frac{(X+1)^{\lambda} - 1}{\lambda} & \text{if } \lambda \neq 0, X \geq 0 \\ 
\log(X+1) & \text{if } \lambda = 0, X \geq 0 \\ 
-\frac{(-X+1)^{2-\lambda} - 1}{2-\lambda} & \text{if } \lambda \neq 2, X < 0 \\ 
-\log(-X+1) & \text{if } \lambda = 2, X < 0 \\ 
\end{cases}
\]  
where \( X \) is the original variable and \( \lambda \) is the optimal transformation parameter.  

**Examples**:  

1. **Using SciPy**  
   ```python  
   from scipy import stats  
   data_tf['LSTAT'], param = stats.yeojohnson(data['LSTAT'])  
   print('Optimal λ:', param)  
   ```  
   - Applies the transformation directly and returns the optimal \( \lambda \).  

2. **Using Scikit-learn (`PowerTransformer`)**  
   ```python  
   from sklearn.preprocessing import PowerTransformer  
   transformer = PowerTransformer(method='yeo-johnson', standardize=False)  
   transformer.fit(data[cols])  # cols = ['LSTAT', 'NOX', 'DIS', 'RM']  
   data_tf = transformer.transform(data[cols])  
   ```  
   - Fits the transformer to select \( \lambda \) for each variable and transforms the data.  

3. **Using Feature-engine (`YeoJohnsonTransformer`)**  
   ```python  
   from feature_engine.transformation import YeoJohnsonTransformer  
   yjt = YeoJohnsonTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])  
   yjt.fit(data)  
   data_tf = yjt.transform(data)  
   ```  
   - Stores learned \( \lambda \) values in `yjt.lambda_dict_` for each variable.  

**Purpose**:  
Used to stabilize variance, normalize distributions, or prepare data for models requiring normality (e.g., linear regression). Unlike [[Box-Cox Transformation]], it accommodates non-positive values.  

**Visualization**:  
Diagnostic plots (histograms and Q-Q plots) are used to compare distributions before and after transformation (via `diagnostic_plots` function).  

**Key Libraries**:  
- `scipy.stats.yeojohnson`  
- `sklearn.preprocessing.PowerTransformer`  
- `feature_engine.transformation.YeoJohnsonTransformer`  

**Related Concepts**:  
- [[Power Transformation]]  
- [[Box-Cox Transformation]]  
- [[Data Preprocessing]]  
- [[Normality Assumption]]