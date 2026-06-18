# Exercise_2 - Imputing Missing Data.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content on missing data imputation:

---

### **1. Missing Data**  
**Definition**: Absent values in a dataset where no observation was recorded.  
**Formula**: Not applicable (phenomenological concept)  
**Example**:  
```python
# Introducing missing values randomly
random.seed(10)
values = set([random.randint(0, len(data)) for p in range(0, 100)])
random_rows = list(values)
for var in ['neighbourhood', 'room_type', 'minimum_nights', 'availability_365']:
    data.loc[random_rows, var] = np.nan
```

---

### **2. Imputation**  
**Definition**: Process of replacing missing data with statistical estimates to create a complete dataset.  
**Formula**: Not applicable (methodological concept)  
**Example**:  
```python
# Using SimpleImputer for numerical columns
imputer_num_arb = Pipeline([('imputer', SimpleImputer(strategy='constant', fill_value=0))])
```

---

### **3. SimpleImputer (Scikit-learn)**  
**Definition**: A class for filling missing values with predefined strategies (mean, median, most_frequent, constant).  
**Formula**:  
For strategy \( s \):  
- \( \text{Imputed value} = \begin{cases} 
  \mu & \text{if } s = \text{mean} \\ 
  \tilde{x} & \text{if } s = \text{median} \\ 
  \text{mode} & \text{if } s = \text{most\_frequent} \\ 
  c & \text{if } s = \text{constant}
\end{cases} \)  
**Example**:  
```python
# Categorical imputation with most frequent strategy
imputer_cat_freq = Pipeline([('imputer', SimpleImputer(strategy='most_frequent')]))
```

---

### **4. ColumnTransformer**  
**Definition**: Scikit-learn class to apply different preprocessing pipelines to different columns.  
**Formula**: Not applicable (methodological tool)  
**Example**:  
```python
# Applying different imputers to numerical and categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num_arb', imputer_num_arb, num_arbitrary),
        ('num_med', imputer_num_med, num_median),
        ('cat_freq', imputer_cat_freq, cat_frequent),
        ('cat_miss', imputer_cat_miss, cat_missing)
    ],
    remainder='passthrough'
)
```

---

### **5. Pipeline**  
**Definition**: Sequential chain of data transformations and estimators.  
**Formula**: Not applicable (methodological tool)  
**Example**:  
```python
# Feature Engine pipeline for imputation
pipe = Pipeline(steps=[
    ('arb_num', mdi.ArbitraryNumberImputer(variables=num_arbitrary)),
    ('med_num', mdi.MeanMedianImputer(imputation_method='median', variables=num_median)),
    ('freq_cat', mdi.CategoricalImputer(variables=cat_frequent, imputation_method='frequent')),
    ('miss_cat', mdi.CategoricalImputer(variables=cat_missing, imputation_method='missing'))
])
```

---

### **6. Constant Imputation**  
**Definition**: Replacing missing values with a user-defined constant (e.g., 0, "Missing").  
**Formula**: \( x_{\text{missing}} = c \)  
**Example**:  
```python
# Imputing missing categorical values with "Missing"
imputer_cat_miss = Pipeline([('imputer', SimpleImputer(strategy='constant', fill_value='Missing'))])
```

---

### **7. Median Imputation**  
**Definition**: Replacing missing numerical values with the median of observed data.  
**Formula**: \( x_{\text{missing}} = \tilde{x} \) (median)  
**Example**:  
```python
# Median imputation for numerical columns
imputer_num_med = Pipeline([('imputer', SimpleImputer(strategy='median'))])
```

---

### **8. Most Frequent Imputation**  
**Definition**: Replacing missing categorical values with the most common observed value.  
**Formula**: \( x_{\text{missing}} = \text{mode} \)  
**Example**:  
```python
# Most frequent imputation for categorical variables
imputer_cat_freq = Pipeline([('imputer', SimpleImputer(strategy='most_frequent')]))
```

---

### **9. Feature Engine**  
**Definition**: Library for advanced feature engineering, including specialized imputers.  
**Formula**: Not applicable (library)  
**Example**:  
```python
# Using Feature Engine's ArbitraryNumberImputer
from feature_engine.imputation import ArbitraryNumberImputer
pipe = Pipeline(steps=[('arb_num', mdi.ArbitraryNumberImputer(variables=num_arbitrary))])
```

---

### **10. Data Splitting**  
**Definition**: Dividing data into training and testing sets to evaluate imputation pipelines.  
**Formula**: Not applicable (methodological step)  
**Example**:  
```python
# Splitting data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    data.drop('price', axis=1), 
    data['price'], 
    test_size=0.3, 
    random_state=0
)
```

---

### **11. Categorical Variables Handling**  
**Definition**: Special treatment for non-numeric columns requiring non-numeric imputation.  
**Formula**: Not applicable (data type concept)  
**Example**:  
```python
# Identifying categorical columns
cat_cols = [c for c in X_train.columns if data[c].dtypes == 'O']
```

---

### **12. Numerical Variables Analysis**  
**Definition**: Examining distributions of numerical features using histograms.  
**Formula**: Not applicable (exploratory step)  
**Example**:  
```python
# Plotting histograms for numerical columns
for col in num_cols:
    plt.hist(data[col].dropna(), bins=30, edgecolor='k', alpha=0.7)
```

---

### **Key Links**  
- [[SimpleImputer]] → [[ColumnTransformer]] → [[Pipeline]]  
- [[Median Imputation]] → [[Most Frequent Imputation]]  
- [[Feature Engine]] → [[Data Splitting]]  

This summary provides a concise yet thorough overview of missing data imputation techniques and tools demonstrated in the notebook.