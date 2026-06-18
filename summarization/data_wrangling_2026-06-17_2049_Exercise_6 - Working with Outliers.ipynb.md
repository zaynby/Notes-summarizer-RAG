# Exercise_6 - Working with Outliers.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured summary of the content using the requested academic format:

---

### **Outlier**  
**Definition**: A data point significantly different from the rest of the dataset, often influencing statistical parameters (e.g., mean, variance) and machine learning model performance.  
**Formula**: N/A  
**Example**: In the `airbnb_sg` dataset, extreme values in the `price` column (e.g., $10,000/night) were identified as outliers using boxplots.  

---

### **Trimming**  
**Definition**: A technique to remove observations containing outliers from the dataset.  
**Formula**: N/A  
**Example**: Not directly applied in the code, but discussed as an alternative to capping.  

---

### **Capping (Winsorization)**  
**Definition**: Replacing outlier values with a specified threshold (e.g., percentile-based caps) to limit their influence.  
**Formula**:  
- Lower cap: \( \text{Quantile}(1 - \text{fold}) \)  
- Upper cap: \( \text{Quantile}(\text{fold}) \)  
**Example**:  
```python
windsorizer = Winsorizer(capping_method='quantiles', tail='both', fold=0.05, variables=['price'])
data_t = windsorizer.transform(data)
```  
Here, `price` values beyond the 5th and 95th percentiles were capped.  

---

### **Interquartile Range (IQR)**  
**Definition**: A measure of statistical dispersion, calculated as the difference between the 75th percentile (Q3) and 25th percentile (Q1) of a dataset. Used to detect outliers.  
**Formula**:  
\[ \text{IQR} = Q3 - Q1 \]  
**Example**: In Exercise 1, IQR was used to define outlier boundaries:  
```python
lower_boundary = Q1 - (IQR * distance)  
upper_boundary = Q3 + (IQR * distance)
```  

---

### **Boxplot**  
**Definition**: A graphical representation showing the distribution of data through quartiles, medians, and outliers.  
**Formula**: N/A  
**Example**:  
```python
sns.boxplot(y=data['price'])  # Visualized outliers in the original data
```  

---

### **Winsorization**  
**Definition**: A specific form of capping where outliers are replaced with the nearest non-outlier values (e.g., 5th or 95th percentile).  
**Formula**:  
- Capped value = \( \max(\min(x, \text{Upper Cap}), \text{Lower Cap}) \)  
**Example**: Applied in Code Cell 11 to limit `price` outliers using 5% folds.  

---

### **Diagnostic Plots**  
**Definition**: Visual tools (histogram, Q-Q plot, boxplot) to compare data distributions before and after outlier handling.  
**Formula**: N/A  
**Example**:  
```python
diagnostic_plots(data_t, 'price')  # Compared distributions pre/post Winsorization
```  

---

### Key Connections  
- Outliers are often detected using [[Interquartile Range (IQR)]] or boxplots.  
- Handling techniques include [[Trimming]], [[Capping]], or [[Winsorization]].  
- [[Winsorization]] is implemented via libraries like `feature_engine` in Python.  

Let me know if you need further refinements!