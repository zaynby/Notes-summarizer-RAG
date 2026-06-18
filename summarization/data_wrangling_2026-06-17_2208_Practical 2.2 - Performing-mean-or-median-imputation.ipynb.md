# Practical 2.2 - Performing-mean-or-median-imputation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

## **Mean Imputation**  
**Definition**: A technique replacing missing values in numerical variables with the **mean** (average) of observed values in the training set.  
**Formula**:  
\[
\text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n}
\]  
**Example**:  
```python
# Using pandas
for var in ['A2', 'A3', 'A8', 'A11', 'A15']:
    value = X_train[var].mean()
    X_train[var] = X_train[var].fillna(value)
    X_test[var] = X_test[var].fillna(value)
```

---

## **Median Imputation**  
**Definition**: A technique replacing missing values in numerical variables with the **median** (middle value) of observed values in the training set.  
**Formula**:  
\[
\text{Median} = 
\begin{cases} 
x_{\frac{n}{2}} & \text{if } n \text{ is even} \\
\frac{x_{\frac{n}{2}-1} + x_{\frac{n}{2}}}{2} & \text{if } n \text{ is odd}
\end{cases}
\]  
**Example**:  
```python
# Using Feature-engine's MeanMedianImputer
median_imputer = MeanMedianImputer(imputation_method='median', variables=['A2', 'A3', 'A8', 'A11', 'A15'])
median_imputer.fit(X_train)
X_train = median_imputer.transform(X_train)
```

---

## **SimpleImputer (Scikit-learn)**  
**Definition**: A scikit-learn class for imputation that supports strategies like `mean`, `median`, or `constant`. Learns imputation values from the training set.  
**Formula**: N/A (Implementation-dependent)  
**Example**:  
```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
imputer.fit(X_train)  # Learns median values
X_train = imputer.transform(X_train)  # Imputes missing values
```

---

## **MeanMedianImputer (Feature-engine)**  
**Definition**: A Feature-engine transformer for mean or median imputation, providing additional functionality like storing imputation values in a dictionary.  
**Formula**: N/A (Implementation-dependent)  
**Example**:  
```python
from feature_engine.imputation import MeanMedianImputer
median_imputer = MeanMedianImputer(imputation_method='median', variables=['A2', 'A3', 'A8', 'A11', 'A15'])
median_imputer.fit(X_train)
print(median_imputer.imputer_dict_)  # Stores learned median values
```

---

## **Imputation Pipeline**  
**Definition**: A sequence of steps combining data preprocessing techniques (e.g., imputation, scaling) into a single workflow to ensure consistency across training and testing sets.  
**Formula**: N/A  
**Example**:  
```python
from sklearn.pipeline import Pipeline
pipe = Pipeline(steps=[
    ('imputer', MeanMedianImputer(imputation_method='median', variables=['A2', 'A3', 'A8', 'A11', 'A15']))
])
pipe.fit(X_train)
X_train = pipe.transform(X_train)
X_test = pipe.transform(X_test)
```

---

### Key Links  
- [[Imputation Techniques]]  
- [[Scikit-learn Pipeline]]  
- [[Feature-engine Library]]  
- [[Handling Missing Data]]  

This summary integrates concepts from the provided notebooks, emphasizing practical implementation and theoretical foundations for polytechnic students.