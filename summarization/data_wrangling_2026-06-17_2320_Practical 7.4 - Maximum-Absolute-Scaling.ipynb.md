# Practical 7.4 - Maximum-Absolute-Scaling.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content:

---

### **Maximum Absolute Scaling**  
**Definition**: A scaling technique that transforms data by dividing each feature value by the maximum absolute value of that feature, ensuring all values fall within the range [-1, 1]. Recommended for data centered at zero or sparse datasets.  
**Formula**:  
\[ x_{\text{scaled}} = \frac{x}{\max(|x|)} \]  
**Example**:  
```python  # Code Cell 5
scaler = MaxAbsScaler()
X_train_scaled = scaler.transform(X_train)
```  
Visualized via KDE plots (Code Cells 9-10, 14-15) to compare distributions before/after scaling.

---

### **Centering**  
**Definition**: Adjusting data by subtracting the mean (μ) of each feature, shifting the distribution to have a mean of zero.  
**Formula**:  
\[ x_{\text{centered}} = x - \mu \]  
**Example**:  
```python  # Code Cell 12
scaler_mean = StandardScaler(with_mean=True, with_std=False)
X_train_centered = scaler_mean.transform(X_train)
```  

---

### **Combined Scaling (Centering + MaxAbsScaling)**  
**Definition**: A two-step process that first centers the data (mean removal) and then applies Maximum Absolute Scaling. This ensures data is both zero-centered and scaled to [-1, 1].  
**Formula**:  
1. \( x_{\text{centered}} = x - \mu \)  
2. \( x_{\text{scaled}} = \frac{x_{\text{centered}}}{\max(|x_{\text{centered}}|)} \)  
**Example**:  
```python  # Code Cell 12
X_train_scaled = scaler_maxabs.transform(scaler_mean.transform(X_train))
```  
Resulting distributions are visualized in Code Cells 14-15.

---

### **Key Concepts & Links**  
- [[Maximum Absolute Scaling]] is distinct from [[Min-Max Scaling]] (which uses the range \( \max(x) - \min(x) \)) and [[Standardization]] (which uses z-scores).  
- [[Centering]] is often a precursor to scaling in pipelines.  
- Visualization via [[KDE Plots]] (Kernel Density Estimation) demonstrates the impact of scaling on feature distributions.  

---

This summary integrates the theoretical and practical aspects of the notebook, emphasizing the implementation of **Maximum Absolute Scaling** and its combination with centering for robust feature engineering.