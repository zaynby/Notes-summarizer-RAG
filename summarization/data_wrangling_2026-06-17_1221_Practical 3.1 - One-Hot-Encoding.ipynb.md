# Practical 3.1 - One-Hot-Encoding.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: One-Hot Encoding for Categorical Variables

## [[One-Hot Encoding]]  
**Definition**: A method to convert categorical variables into binary vectors where each binary variable represents a category. Only **k-1** binary variables are needed for **k** categories to avoid multicollinearity.  
**Formula**:  
\[ \text{Number of binary variables} = k - 1 \]  
**Example**:  
- For **Gender** (k=2: Male, Female), one binary variable (e.g., `Female=1` if female, `0` otherwise).  
- For **Color** (k=3: Red, Blue, Green), two binary variables (e.g., `Red` and `Blue`; Green is implied when both are `0`).  

---

## [[Categorical Variable]]  
**Definition**: A variable whose values represent categories or labels (e.g., "Male/Female", "Red/Blue/Green"). Can be **nominal** (no order) or **ordinal** (ordered).  
**Formula**: N/A  
**Example**:  
- **Nominal**: City (London, Manchester).  
- **Ordinal**: Student Grade (A, B, C, Fail).  

---

## [[Binary Variable]]  
**Definition**: A variable that takes only two values (0 or 1), used to represent the presence/absence of a category in one-hot encoding.  
**Formula**: N/A  
**Example**:  
- For **Gender**, `Female` binary variable: 1 = Female, 0 = Male.  

---

## [[k-1 Encoding]]  
**Definition**: A technique to encode **k** categories using **k-1** binary variables to prevent redundancy (e.g., dropping one category as the reference).  
**Formula**:  
\[ \text{Encoded variables} = k - 1 \]  
**Example**:  
- **Color** (Red, Blue, Green) → Encode with `Red` and `Blue`; Green is the absence of both.  

---

## [[pandas.get_dummies]]  
**Definition**: A pandas function to perform one-hot encoding by converting categorical variables into dummy variables.  
**Formula**: N/A  
**Example**:  
```python  
tmp = pd.get_dummies(X_train['A4'], drop_first=True, dtype=int)  
```  
- `drop_first=True` applies **k-1 encoding**.  

---

## [[Scikit-learn OneHotEncoder]]  
**Definition**: A scikit-learn class to encode categorical variables into a one-hot numeric array.  
**Formula**: N/A  
**Example**:  
```python  
from sklearn.preprocessing import OneHotEncoder  
encoder = OneHotEncoder(drop='first', sparse_output=False, dtype=int)  
X_train_enc = encoder.transform(X_train[vars_categorical])  
```  

---

## [[Feature-engine OneHotEncoder]]  
**Definition**: A Feature-engine class for one-hot encoding with additional flexibility (e.g., handling top categories).  
**Formula**: N/A  
**Example**:  
```python  
from feature_engine.encoding import OneHotEncoder  
ohe_enc = OneHotEncoder(drop_last=True)  
X_train_enc = ohe_enc.transform(X_train)  
```  

---

## Key Concepts  
- **Why k-1?**: To avoid perfect multicollinearity (redundant information) in regression models.  
- **Tools**:  
  - **pandas**: Quick encoding for individual columns.  
  - **Scikit-learn**: Integrated with ML pipelines.  
  - **Feature-engine**: Advanced feature engineering.  

**Example Dataset**: `creditApprovalUCI.csv` with categorical variables like `A4`, `A5`, etc.  

[[Scikit-learn]], [[Categorical Variable]], [[Data Preprocessing]]