# Practical 2.6 - Replacing-missing-values-by-a-value-at-the-end-of-the-distribution.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

## Summary: End Tail Imputation and Interquartile Range (IQR)

### [[End Tail Imputation]]
| **Term**               | **Definition**                                                                 | **Formula**                                                                 | **Example**                                                                 |
|-------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **End Tail Imputation** | A method to replace missing values with a value at the end of the variable distribution. For normally distributed data, values are derived from mean ± 3σ. For non-normal data, the inter-quartile range (IQR) proximity rule is used. | - Right tail: \( Q3 + 1.5 \times \text{IQR} \) <br> - Left tail: \( Q1 - 1.5 \times \text{IQR} \) | Using `EndTailImputer` from Feature-engine: <br> `imputer = EndTailImputer(imputation_method='iqr', tail='right', variables=['A2', 'A3', 'A8', 'A11', 'A15'])` |

---

### [[Interquartile Range (IQR)]]
| **Term**               | **Definition**                                                                 | **Formula**                                                                 | **Example**                                                                 |
|-------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Interquartile Range (IQR)** | A measure of statistical dispersion, representing the range between the first quartile (Q1) and third quartile (Q3) of a dataset. | \( \text{IQR} = Q3 - Q1 \) | Calculating IQR for variable 'A2': <br> `IQR = X_train['A2'].quantile(0.75) - X_train['A2'].quantile(0.25)` |

---

### Key Concepts and Workflow
1. **Data Splitting**:  
   - The dataset is split into training (70%) and testing (30%) sets using `train_test_split` with `random_state=0`.  
   - Example: `X_train, X_test, y_train, y_test = train_test_split(data.drop('A16', axis=1), data['A16'], test_size=0.3, random_state=0)`.

2. **Handling Missing Values**:  
   - **Pandas Approach**: Missing values in numerical variables (e.g., 'A2', 'A3') are replaced using the IQR proximity rule.  
     Example: `X_train[var].fillna(X_train[var].quantile(0.75) + 1.5 * IQR, inplace=True)`.  
   - **Feature-engine Approach**: The `EndTailImputer` transformer automates imputation, storing parameters from the training set for consistency.  

3. **Validation**:  
   - Missing values are verified post-imputation using `isnull().mean()` or `isnull().sum()`.  

This structured approach ensures robust handling of missing data while maintaining consistency across training, testing, and future datasets.