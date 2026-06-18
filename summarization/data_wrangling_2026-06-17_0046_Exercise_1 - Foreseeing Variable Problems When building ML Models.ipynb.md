# Exercise_1 - Foreseeing Variable Problems When building ML Models.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided **Data Wrangling** exercise using the requested format:

---

### **Variable Types**  
**Definition**: Characteristics measured or counted in a dataset, categorized into numerical (discrete/continuous) or categorical (labels).  
**Formula**: N/A  
**Example**: In the Airbnb Singapore dataset, `price` is a **numerical** variable (continuous), while `neighbourhood` is **categorical** (labels like "Downtown", "Orchard").  

---

### **Missing Data Handling**  
**Definition**: Values not present in the dataset that can affect machine learning model performance.  
**Formula**: N/A  
**Example**: Code Cell 8 uses `clean = data.dropna()` to remove rows with missing values, ensuring compatibility with scikit-learn algorithms.  

---

### **Cardinality**  
**Definition**: The number of unique categories in a categorical variable.  
**Formula**: N/A  
**Example**: Code Cell 9 visualizes cardinality using `clean.nunique().plot.bar()`, showing variables like `neighbourhood` with high cardinality.  

---

### **Rare Categories**  
**Definition**: Categories in a variable with very low frequency (e.g., <1% of observations).  
**Formula**: N/A  
**Example**: Code Cell 10 identifies rare neighbourhoods (e.g., <1% of listings) using `value_counts()` and highlights them with a red threshold line.  

---

### **Linear Relationship**  
**Definition**: A straight-line relationship between two variables, often assessed using regression plots.  
**Formula**: N/A  
**Example**: Code Cell 11 uses `sns.lmplot` to check if `reviews_per_month` and `price` have a linear relationship, concluding they do not.  

---

### **Normal Distribution**  
**Definition**: A symmetric, bell-shaped distribution where most values cluster around the mean.  
**Formula**: N/A  
**Example**: Code Cell 12 uses `sns.histplot` with KDE to show `price` does not follow a normal distribution (non-bell-shaped histogram).  

---

### **Outliers**  
**Definition**: Data points that significantly deviate from the majority of observations.  
**Formula**:  
Interquartile Range (IQR) = Q3 - Q1  
Lower Boundary = Q1 - 1.5 × IQR  
Upper Boundary = Q3 + 1.5 × IQR  
**Example**: Code Cell 13 calculates IQR-based boundaries for `price` and identifies outliers using `np.where()`.  

---

### **Key Concepts Linked**  
- [[Categorical Variable]] → [[Cardinality]] / [[Rare Categories]]  
- [[Numerical Variable]] → [[Linear Relationship]] / [[Normal Distribution]] / [[Outliers]]  
- [[Missing Data]] → Preprocessing for scikit-learn compatibility  

This summary aligns with the exercise’s focus on identifying variable characteristics to guide feature engineering for machine learning models.