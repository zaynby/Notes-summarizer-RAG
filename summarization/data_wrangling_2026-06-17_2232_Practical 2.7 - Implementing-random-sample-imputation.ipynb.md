# Practical 2.7 - Implementing-random-sample-imputation.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured summary of the content following the requested format:

---

### [[Random Sample Imputation]]
**Definition**:  
A missing data imputation technique that replaces missing values with random observations drawn from the existing values of the same variable. This method preserves the original data distribution and works for both numerical and categorical variables.

**Formula**:  
No explicit mathematical formula. The method involves:  
1. Counting missing values in a variable (e.g., `number_missing = X_train['A2'].isnull().sum()`)  
2. Sampling random observed values (with replacement or without) equal to the number of missing values  
3. Assigning these sampled values to missing data points while maintaining original distribution properties

**Example**:  
```python
# Using pandas (manual implementation)
number_missing = X_train['A2'].isnull().sum()
random_sample = X_train['A2'].dropna().sample(number_missing, random_state=0)
X_train.loc[X_train['A2'].isnull(), 'A2'] = random_sample.values

# Using Feature Engine (automated pipeline)
imputer = RandomSampleImputer()
imputer.fit(X_train)
X_train = imputer.transform(X_train)
```

---

### Related Concepts  
- [[Imputation Techniques]]: Parent category including methods like [[Mean/Median Imputation]] and [[Frequent Category Imputation]]  
- [[Data Distribution Preservation]]: Key advantage of random sample imputation vs. mean/median methods  
- [[Feature Engine]]: Library providing specialized imputation transformers  
- [[SimpleImputer]]: Scikit-learn's basic imputation tool (less flexible than Feature Engine)  

---

### Key Implementation Steps  
1. **Data Preparation**:  
   - Split data into train/test sets  
   - Identify variables with missing values (`X_train.isnull().mean()`)  

2. **Manual Implementation (Pandas)**:  
   - Calculate missing values per variable  
   - Sample random observed values  
   - Reindex and replace missing values  

3. **Automated Implementation (Feature Engine)**:  
   - Create `RandomSampleImputer` object  
   - Fit to training data  
   - Transform train/test sets  

4. **Validation**:  
   - Confirm missing values removed (`X_train.isnull().mean()`)  

---

This summary connects to previous imputation techniques discussed in the course materials while emphasizing the unique distribution-preserving properties of random sample imputation. The code examples demonstrate both low-level pandas operations and high-level library implementations.