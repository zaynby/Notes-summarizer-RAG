# Practical 3.7 - grouping-rare-categories.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Grouping Rare or Infrequent Categories

## [[Rare Values]]
**Definition**: Categories present in a small percentage of observations, typically defined as those with less than 5% frequency in the dataset.  
**Formula**:  
\[
\text{Percentage} = \frac{\text{Count of category}}{\text{Total observations}} < 0.05
\]  
**Example**: In variable `A7`, categories with a frequency below 5% are labeled as "Rare" (e.g., `X_train['A7'].value_counts() / len(X_train)` identifies rare categories).

---

## [[Grouping Rare Categories]]
**Definition**: The process of combining infrequent categories into a single "Rare" or "Other" category to reduce overfitting and improve model robustness.  
**Formula**: Not applicable (process-based).  
**Example**: Using `np.where` to replace non-frequent categories in `A7` with "Rare":  
```python
X_train['A7'] = np.where(X_train['A7'].isin(frequent_cat), X_train['A7'], 'Rare')
```

---

## [[Count Encoding]]
**Definition**: Replacing categorical labels with their frequency (or count) of occurrence in the dataset.  
**Formula**:  
\[
\text{Frequency} = \frac{\text{Number of observations with category}}{\text{Total observations}}
\]  
**Example**: Calculating frequencies for `A7` categories using `X_train['A7'].value_counts() / len(X_train)`.

---

## [[One-Hot Encoding with Feature-engine]]
**Definition**: Applying one-hot encoding to the most frequent categories while grouping rare categories into a single "Rare" category using the `Feature-engine` library.  
**Formula**: Not directly applicable (threshold-based).  
**Example**: Using `RareLabelEncoder` to encode top categories:  
```python
rare_encoder = RareLabelEncoder(tol=0.05, n_categories=4)
```

---

## [[RareLabelEncoder]]
**Definition**: A `Feature-engine` transformer that groups rare categories into a single category based on a tolerance threshold (e.g., 5%).  
**Formula**: Parameters include `tol` (threshold for rare categories) and `n_categories` (number of top categories to retain).  
**Example**:  
```python
rare_encoder = RareLabelEncoder(tol=0.05, n_categories=4)
rare_encoder.fit(X_train)
X_train_enc = rare_encoder.transform(X_train)
```

---

## Key Takeaways
- **Rare Values**: Identified using a frequency threshold (e.g., 5%).  
- **Grouping**: Reduces dimensionality and prevents overfitting by merging rare categories.  
- **Count/Frequency Encoding**: Quantifies category representation for modeling.  
- **RareLabelEncoder**: Automates grouping of rare categories during preprocessing.  

[[Data Wrangling]] | [[Categorical Encoding]] | [[Feature Engineering]]