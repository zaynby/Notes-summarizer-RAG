# Practical 3.2 - One-Hot-Encoding-Top-Categories.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Academic Summary: One-Hot Encoding of Top Categories

## [[One-Hot Encoding]]  
**Definition**: A method to convert categorical variables into binary vectors where each category is represented as a separate binary column (0 or 1).  
**Formula**: For a category \( c \) in variable \( X \), create a binary feature \( X_c \) such that:  
\[ X_c = \begin{cases} 1 & \text{if } X = c \\ 0 & \text{otherwise} \end{cases} \]  
**Example**:  
- **Pandas Implementation**: Manual creation of binary columns for the top 5 categories of 'A6' (Code Cell 10):  
  ```python  
  for label in top_5:  
      X_train[f'A6_{label}'] = np.where(X_train['A6'] == label, 1, 0)  
  ```  

---

## [[Top Categories]]  
**Definition**: The most frequent categories in a categorical variable, selected based on their occurrence count (e.g., top 5 categories).  
**Formula**:  
\[ \text{Top } k \text{ categories} = \text{argtop}_k(\text{value counts of } X) \]  
**Example**:  
- Identifying top 5 categories in 'A6' using `value_counts().head(5)` (Code Cell 8):  
  ```python  
  X_train['A6'].value_counts().sort_values(ascending=False).head(5)  
  ```  

---

## [[Feature-engine]]  
**Definition**: A Python library for advanced feature engineering, including encoding categorical variables with customizable options (e.g., encoding only top categories).  
**Formula**: N/A (library-based implementation)  
**Example**:  
- Using `OneHotEncoder` to encode top 5 categories of 'A6' and 'A7' (Code Cell 14):  
  ```python  
  ohe_enc = OneHotEncoder(top_categories=5, variables=['A6', 'A7'], drop_last=False)  
  ohe_enc.fit(X_train)  
  ```  

---

## [[Rare Categories]]  
**Definition**: Categories present in a minority of observations (e.g., <5% frequency), often grouped into a single category to reduce dimensionality.  
**Formula**:  
\[ \text{Rare if frequency} < \theta \quad (\theta = 0.05 \text{ or } 0.01) \]  
**Example**:  
- Mentioned in the context of grouping remaining categories after encoding top categories (Markdown Cell 1).  

---

## Key Concepts Linkage  
- [[One-Hot Encoding]] of [[Top Categories]] reduces feature space expansion.  
- [[Feature-engine]] provides scalable implementation compared to manual [[One-Hot Encoding]] with pandas.  
- [[Rare Categories]] are addressed indirectly by grouping them after encoding top categories.  

*Source: Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*