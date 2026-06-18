# Practical 4.6 - Yeo-Johnson-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Yeo-Johnson Transformation

## Term 
[[Yeo-Johnson Transformation]]

---

### Definition 
The Yeo-Johnson transformation is an extension of the [[Box-Cox Transformation]] that generalizes power transformations to accommodate **variables with zero and negative values**, in addition to positive values. It applies different power functions based on the sign of the input data and the transformation parameter λ, aiming to stabilize variance and normalize data distributions.

---

### Formula 
The transformation is defined as a piecewise function:  
\[
X_t = 
\begin{cases} 
\frac{(X+1)^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0, \, X \geq 0 \\
\log(X+1) & \text{if } \lambda = 0, \, X \geq 0 \\
-\frac{(-X+1)^{2-\lambda} - 1}{2-\lambda} & \text{if } \lambda \neq 2, \, X < 0 \\
-\log(-X+1) & \text{if } \lambda = 2, \, X < 0 \\
\end{cases}
\]  
where \(X\) is the original variable and \(\lambda\) is the transformation parameter optimized for normality.

---

### Example 

#### 1. **SciPy Implementation**  
```python
import scipy.stats as stats  

# Apply Yeo-Johnson to 'LSTAT' and retrieve optimal λ
data_tf['LSTAT'], param = stats.yeojohnson(data['LSTAT'])
print('Optimal λ:', param)  # Outputs the best λ for normalization
```

#### 2. **Scikit-learn (PowerTransformer)**  
```python
from sklearn.preprocessing import PowerTransformer  

# Initialize transformer with Yeo-Johnson method
transformer = PowerTransformer(method='yeo-johnson', standardize=False)

# Fit to selected columns (e.g., ['LSTAT', 'NOX', 'DIS', 'RM'])
transformer.fit(data[cols])

# Transform data and extract learned λ values
data_tf = pd.DataFrame(transformer.transform(data[cols]), columns=cols)
print('Lambdas:', transformer.lambdas_)  # Optimal λ for each variable
```

#### 3. **Feature-engine (YeoJohnsonTransformer)**  
```python
from feature_engine.transformation import YeoJohnsonTransformer  

# Initialize and fit transformer
yjt = YeoJohnsonTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])
yjt.fit(data)

# Transform data and inspect parameters
data_tf = yjt.transform(data)
print('Lambda dict:', yjt.lambda_dict_)  # Optimal λ per variable
```

---

### Key Notes 
- **Diagnostic Plots**: Use histograms and Q-Q plots (via `diagnostic_plots`) to compare distributions before/after transformation.  
- **Advantage**: Handles negative/zero values unlike [[Box-Cox Transformation]].  
- **Parameter Optimization**: Libraries like SciPy and Feature-engine automatically estimate the optimal λ for each variable.  

[[Power Transformation]] | [[Logarithmic Transformation]] | [[Box-Cox Transformation]]