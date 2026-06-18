# Practical 4.5 - Box-Cox-transformation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured summary of the content using the requested format:

---

### **Box-Cox Transformation**  
**Definition**: A power transformation method used to normalize data by applying a family of functions parameterized by λ (lambda). It generalizes the logarithm and power transformations.  
**Formula**:  
\[
X_t = 
\begin{cases} 
\frac{X^{\lambda} - 1}{\lambda} & \text{if } \lambda \neq 0 \\
\log(X) & \text{if } \lambda = 0 
\end{cases}
\]  
**Example**:  
- Applied to the `LSTAT` variable in the Boston House Price dataset using SciPy:  
  ```python
  data_tf['LSTAT'], param = stats.boxcox(data['LSTAT'])
  ```  
- Optimal λ is printed and stored in `param` or `transformer.lambdas_` (scikit-learn).  

---

### **Power Transformation**  
**Definition**: A broader class of transformations where a variable \(X\) is raised to a power \(\lambda\) to improve normality.  
**Formula**:  
\[
X_t = X^{\lambda}
\]  
**Example**:  
- Special cases include square root (\(\lambda = 0.5\)) and cube root (\(\lambda = 1/3\)).  
- Implemented via `PowerTransformer` in scikit-learn:  
  ```python
  transformer = PowerTransformer(method='box-cox', standardize=False)
  ```  

---

### **Diagnostic Plots**  
**Definition**: Visual tools to assess the distribution of a variable before and after transformation.  
**Formula**: N/A  
**Example**:  
- A custom function generates histograms and Q-Q plots:  
  ```python
  def diagnostic_plots(df, variable):
      plt.figure(figsize=(15,6))
      plt.subplot(1, 2, 1)
      df[variable].hist(bins=30)
      plt.subplot(1, 2, 2)
      stats.probplot(df[variable], dist="norm", plot=plt)
      plt.show()
  ```  
- Used to compare `LSTAT` distributions pre- and post-transformation.  

---

### **Optimal Lambda (λ)**  
**Definition**: The value of λ that maximizes normality in the transformed data, selected via maximum likelihood estimation.  
**Formula**: Determined algorithmically (e.g., via `scipy.stats.boxcox`).  
**Example**:  
- SciPy returns λ in `param` after fitting:  
  ```python
  print('Optimal λ: ', param)
  ```  
- Scikit-learn stores λ values in `transformer.lambdas_`.  

---

### **Libraries & Tools**  
#### **1. SciPy**  
**Definition**: Library for scientific computing, including statistical transformations.  
**Example**:  
- `stats.boxcox()` applies the Box-Cox transformation:  
  ```python
  from scipy.stats import boxcox
  ```  

#### **2. Scikit-learn**  
**Definition**: Machine learning library with preprocessing utilities.  
**Example**:  
- `PowerTransformer` with `method='box-cox'`:  
  ```python
  from sklearn.preprocessing import PowerTransformer
  ```  

#### **3. Feature-engine**  
**Definition**: Open-source library for feature engineering tasks.  
**Example**:  
- `BoxCoxTransformer` for direct application:  
  ```python
  from feature_engine.transformation import BoxCoxTransformer
  ```  

---

### **Boston House Price Dataset**  
**Definition**: A classic dataset containing housing prices and attributes (e.g., `LSTAT`, `NOX`).  
**Example**:  
- Loaded and transformed in the notebook:  
  ```python
  data = pd.read_csv("./data/boston_local.csv")
  ```  

---

### **Key Connections**  
- [[Box-Cox Transformation]] is a special case of [[Power Transformation]].  
- [[Logarithmic Transformation]] is equivalent to Box-Cox when \(\lambda = 0\).  
- Libraries like [[SciPy]], [[Scikit-learn]], and [[Feature-engine]] provide implementations.  
- [[Diagnostic Plots]] evaluate transformation effectiveness.  

--- 

This summary links concepts hierarchically and emphasizes practical implementation details. Let me know if you need expansions!