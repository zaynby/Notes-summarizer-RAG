# Exercise_1 - Foreseeing Variable Problems When building ML Models.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the provided **Data Wrangling** notebook:

---

### **Term: Variable**  
**Definition**: A characteristic, number, or quantity measurable or countable in a dataset.  
**Formula**: N/A  
**Example**: In the Airbnb Singapore dataset (`airbnb_sg.csv`), variables include `price`, `neighbourhood`, and `reviews_per_month`.  

---

### **Term: Numerical Variable**  
**Definition**: A variable taking numeric values, either discrete (countable, e.g., number of bedrooms) or continuous (measurable, e.g., price).  
**Formula**: N/A  
**Example**: `price` (continuous) and `number_of_reviews` (discrete) in the dataset.  

---

### **Term: Categorical Variable**  
**Definition**: A variable with values selected from predefined categories (labels), e.g., text or ordinal labels.  
**Formula**: N/A  
**Example**: `neighbourhood` (e.g., "Downtown", "Orchard") in the Airbnb dataset.  

---

### **Term: Missing Data**  
**Definition**: Absent or null values in a dataset, often represented as `NaN` or empty cells.  
**Formula**: N/A  
**Example**: Identified using `data.isnull().mean()`; handled by dropping rows with `clean = data.dropna()`.  

---

### **Term: Cardinality**  
**Definition**: The number of unique categories in a categorical variable.  
**Formula**: N/A  
**Example**: Visualized using `clean.nunique().plot.bar()` to compare uniqueness across variables.  

---

### **Term: Rare Categories**  
**Definition**: Categories with very low frequency in a dataset, often requiring merging or removal.  
**Formula**: N/A  
**Example**: Neighbourhoods with <1% of Airbnb listings were highlighted using `label_freq.sort_values().plot.bar()` with a threshold line at `y=0.01`.  

---

### **Term: Linear Relationship**  
**Definition**: A straight-line relationship between two variables, indicating constant rate of change.  
**Formula**: \( y = mx + b \) (where \( m \) = slope, \( b \) = intercept)  
**Example**: Checked between `reviews_per_month` and `price` using `sns.lmplot()`, revealing a non-linear relationship.  

---

### **Term: Normal Distribution**  
**Definition**: A symmetric, bell-shaped probability distribution where most values cluster around the mean.  
**Formula**: \( f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}} \) (Gaussian function)  
**Example**: `price` was tested via `sns.histplot()` with `kde=True`, showing a non-normal skewed distribution.  

---

### **Term: Outlier Detection (IQR Method)**  
**Definition**: Identifying data points far from the median, often using the Interquartile Range (IQR).  
**Formula**:  
- \( IQR = Q3 - Q1 \)  
- Lower Bound: \( Q1 - 1.5 \times IQR \)  
- Upper Bound: \( Q3 + 1.5 \times IQR \)  
**Example**: Outliers in `price` were found using `find_boundaries()` and `np.where()`.  

---

### **Term: Feature Engineering**  
**Definition**: Transforming raw variables into formats suitable for machine learning models.  
**Formula**: N/A  
**Example**: Handling missing data via `dropna()`, encoding categorical variables, or scaling numerical features.  

---

### **Key Wikilinks**  
- [[Missing Data]] → [[Handling Missing Data]]  
- [[Categorical Variable]] → [[One-Hot Encoding]]  
- [[Outlier Detection]] → [[Interquartile Range (IQR)]]  
- [[Normal Distribution]] → [[Feature Scaling]]  

--- 

This summary aligns with the notebook’s focus on identifying variable characteristics (missingness, cardinality, distributions, outliers) to guide feature engineering for ML models.