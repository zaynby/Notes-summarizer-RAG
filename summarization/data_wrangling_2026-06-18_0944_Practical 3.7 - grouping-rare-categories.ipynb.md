# Practical 3.7 - grouping-rare-categories.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Grouping Rare or Infrequent Categories

## [[Rare Categories]]
- **Definition**: Categories present in a dataset where the percentage of observations falls below a predefined threshold (typically <5%). These categories are infrequent and may cause overfitting or poor generalization in machine learning models.
- **Formula**:  
  \[
  \text{Percentage} = \left( \frac{\text{Count of Category}}{\text{Total Observations}} \right) \times 100 < 5\%
  \]
- **Example**:  
  In the notebook, `X_train['A7'].value_counts() / len(X_train)` calculates the frequency of each category in the `A7` variable. Categories with a percentage below 5% are classified as rare.

---

## [[Grouping Rare Categories]]
- **Definition**: The process of merging infrequent categories into a single category (e.g., "Rare" or "Other") to reduce noise and improve model robustness. This prevents algorithms from overfitting to rare labels.
- **Formula**:  
  Categories with frequency \( < \tau \) (threshold, e.g., 0.05) are grouped into "Rare," where \( \tau \) is the tolerance level.
- **Example**:  
  Using `np.where` to replace rare categories in `A7` with "Rare":  
  ```python
  X_train['A7'] = np.where(X_train['A7'].isin(frequent_cat), X_train['A7'], 'Rare')
  ```

---

## [[RareLabelEncoder]]
- **Definition**: A transformer from the `Feature-engine` library that automatically identifies and groups rare categories into a single category based on a specified threshold. It ensures consistency between training and test sets.
- **Formula**:  
  Uses a tolerance parameter \( \tau \) (e.g., 0.05) to define rare categories. The `n_categories` parameter specifies the minimum number of observations required for a category to be considered frequent.
- **Example**:  
  Implementing `RareLabelEncoder` with a 5% threshold:  
  ```python
  rare_encoder = RareLabelEncoder(tol=0.05, n_categories=4)
  rare_encoder.fit(X_train)
  X_train_enc = rare_encoder.transform(X_train)
  ```

---

## [[Count Encoding]] (Contextual Reference)
- **Definition**: A technique where categories are replaced by the count (frequency) of their occurrences in the dataset. This captures the representation of each label and is often used in data science competitions.
- **Formula**:  
  For count encoding: \( \text{Encoded Value} = \text{Count of Category} \)  
  For frequency encoding: \( \text{Encoded Value} = \frac{\text{Count of Category}}{\text{Total Observations}} \)
- **Example**:  
  The `find_frequent_labels` function calculates category frequencies to identify rare categories:  
  ```python
  def find_frequent_labels(df, variable, tolerance):
      temp = df[variable].value_counts() / len(df)
      non_rare = [x for x in temp.loc[temp > tolerance].index.values]
      return non_rare
  ```

---

## [[One-Hot Encoding with Feature-engine]]
- **Definition**: A method to convert categorical variables into binary (0/1) features. When applied to frequent categories, it reduces dimensionality by treating rare categories as a single group.
- **Formula**:  
  Each category is represented as a binary vector (e.g., category "A" becomes [1, 0, 0], "B" becomes [0, 1, 0], etc.).
- **Example**:  
  After grouping rare categories, `RareLabelEncoder` performs one-hot encoding on the remaining frequent categories:  
  ```python
  X_train_enc = rare_encoder.transform(X_train)
  ```

---

### Key Concepts Linkage
- [[Rare Categories]] are identified using frequency thresholds.  
- [[Grouping Rare Categories]] mitigates overfitting by merging rare labels.  
- [[RareLabelEncoder]] automates this process using `Feature-engine`.  
- [[Count Encoding]] and [[One-Hot Encoding]] are complementary techniques for handling categorical data.