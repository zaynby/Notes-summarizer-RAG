# Practical 2.2 - Performing-mean-or-median-imputation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Mean/Median Imputation Techniques

## [[Mean Imputation]]
- **Definition**: A method replacing missing values in numerical variables with the **mean** (average) of observed values in the training set. Preserves the general distribution but may reduce variance.
- **Formula**:  
  \[
  \text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n}
  \]
  where \( x_i \) are observed values and \( n \) is the count of observations.
- **Example**:  
  ```python
  # Using pandas to impute missing values with mean
  for var in ['A2', 'A3', 'A8', 'A11', 'A15']:
      value = X_train[var].mean()
      X_train[var].fillna(value, inplace=True)
      X_test[var].fillna(value, inplace=True)
  ```

---

## [[Median Imputation]]
- **Definition**: A technique replacing missing values in numerical variables with the **median** (middle value) of observed data. More robust to outliers than mean imputation.
- **Formula**:  
  \[
  \text{Median} = 
  \begin{cases} 
      x_{\frac{n}{2}} & \text{if } n \text{ is even} \\
      x_{\frac{n+1}{2}} & \text{if } n \text{ is odd}
  \end{cases}
  \]
- **Example**:  
  ```python
  # Using pandas to impute missing values with median
  for var in ['A2', 'A3', 'A8', 'A11', 'A15']:
      value = X_train[var].median()
      X_train[var].fillna(value, inplace=True)
      X_test[var].fillna(value, inplace=True)
  ```

---

## [[SimpleImputer (scikit-learn)]]
- **Definition**: A scikit-learn class for imputation that supports strategies like `mean`, `median`, or `most_frequent`. Learns imputation values from the training set.
- **Formula**:  
  Imputes missing values using the strategy parameter (e.g., \( \text{median}(\text{train data}) \)).
- **Example**:  
  ```python
  # Using scikit-learn's SimpleImputer for median imputation
  imputer = SimpleImputer(strategy='median')
  imputer.fit(X_train)
  X_train_imputed = imputer.transform(X_train)
  X_test_imputed = imputer.transform(X_test)
  ```

---

## [[MeanMedianImputer (Feature-engine)]]
- **Definition**: A Feature-engine transformer for mean or median imputation. Stores imputation values in `imputer_dict_` for consistency across datasets.
- **Formula**:  
  Uses \( \text{median}(\text{train data}) \) or \( \text{mean}(\text{train data}) \) for imputation.
- **Example**:  
  ```python
  # Using Feature-engine's MeanMedianImputer
  median_imputer = MeanMedianImputer(imputation_method='median', variables=['A2', 'A3', 'A8', 'A11', 'A15'])
  median_imputer.fit(X_train)
  X_train_imputed = median_imputer.transform(X_train)
  X_test_imputed = median_imputer.transform(X_test)
  ```

---

## Key Considerations
- **Training vs. Test Set**: Imputation parameters (mean/median) are calculated on the **training set** to avoid data leakage.
- **Data Types**: Mean/median imputation applies only to numerical variables.
- **Comparison**: 
  - **Mean** is sensitive to outliers.
  - **Median** is robust to outliers but discards distribution information.
  - Libraries like scikit-learn and Feature-engine automate parameter storage and application.