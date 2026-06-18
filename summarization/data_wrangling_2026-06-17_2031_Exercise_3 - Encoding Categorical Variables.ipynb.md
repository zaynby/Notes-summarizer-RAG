# Exercise_3 - Encoding Categorical Variables.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Encoding Categorical Variables  

## [[Categorical Variable]]  
**Definition**: A variable whose values represent categories or labels. These can be **nominal** (no intrinsic order, e.g., City) or **ordinal** (ordered categories, e.g., Grade A > B > C).  
**Formula**: N/A  
**Example**: In `airbnb_sg.csv`, columns like `neighbourhood` (nominal) and `amenities` (ordinal if ranked) are categorical.  

---

## [[Categorical Encoding]]  
**Definition**: The process of converting categorical variables into numerical values for use in machine learning models.  
**Formula**: N/A  
**Example**: Scikit-learn requires numerical input, so encoding transforms strings (e.g., "Male", "Female") into integers or binary vectors.  

---

## [[One-Hot Encoding]]  
**Definition**: A technique where each category is represented as a binary vector (0 or 1) across multiple columns.  
**Formula**: For \( n \) categories, create \( n \) columns where only one column is 1 (indicating the category) and others are 0.  
**Example**:  
```python  
from sklearn.preprocessing import OneHotEncoder  
encoder = OneHotEncoder(drop='first')  
X_train_ohe = encoder.fit_transform(X_train[cat_cols])  
```  
**Output**: A matrix where each original category becomes a separate binary column.  

---

## [[Ordinal Encoding]]  
**Definition**: Assigns integer values to categories based on their inherent order.  
**Formula**: \( \text{Encoded value} = \text{Rank of category} \) (e.g., "Low" → 0, "Medium" → 1, "High" → 2).  
**Example**:  
```python  
from sklearn.preprocessing import OrdinalEncoder  
le = OrdinalEncoder()  
X_train_ord = le.transform(X_train[cat_cols])  
```  
**Output**: A numerical array where each category is replaced by its ordinal value.  

---

## [[Target Mean Encoding]]  
**Definition**: Replaces categories with the mean of the target variable for that category.  
**Formula**: \( \text{Encoded value} = \frac{\sum y}{\text{count of category}} \) for each category.  
**Example**:  
```python  
from feature_engine.encoding import MeanEncoder  
mean_enc = MeanEncoder(variables=cat_cols)  
X_train_enc = mean_enc.fit_transform(X_train, y_train)  
```  
**Output**: Numerical values representing the average target (e.g., price) per category.  

---

## [[Mean Absolute Error (MAE)]]  
**Definition**: A metric to evaluate model performance by averaging the absolute differences between predicted and actual values.  
**Formula**: \( \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{true}} - y_{\text{pred}}| \)  
**Example**:  
```python  
from sklearn.metrics import mean_absolute_error  
print('test_mae:', mean_absolute_error(y_test, lm_reg.predict(X_test)))  
```  
**Result**: Lower MAE indicates better model performance.  

---

## [[Linear Regression Model]]  
**Definition**: A statistical model that predicts a continuous target variable using linear relationships with input features.  
**Formula**: \( y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon \)  
**Example**:  
```python  
from sklearn.linear_model import LinearRegression  
lm_reg = LinearRegression()  
lm_reg.fit(X_train, y_train)  
```  
**Application**: Used here to predict `price` after encoding categorical variables.  

---

## [[Missing Data Imputation]]  
**Definition**: The process of replacing missing values in a dataset with plausible estimates.  
**Formula**: N/A  
**Example**:  
```python  
from sklearn.impute import SimpleImputer  
imputer = SimpleImputer(strategy='constant', fill_value=0.0)  
X_train[['reviews_per_month']] = imputer.fit_transform(X_train[['reviews_per_month']])  
```  
**Purpose**: Ensures the dataset is complete before encoding and modeling.  

---

## Key Comparison of Encoding Methods  
| Method               | MAE (Test Set) | Notes                                      |  
|----------------------|-----------------|--------------------------------------------|  
| One-Hot Encoding    | Higher          | Avoids assumptions about category order. |  
| Ordinal Encoding    | **Lower**       | Assumes order; worked best in this case.  |  
| Target Mean Encoding| Moderate        | Risk of overfitting if categories are rare. |  

**Conclusion**: Ordinal encoding yielded the best performance (lowest MAE) for the Airbnb dataset, likely due to implicit ordering in categories like `amenities` or `neighbourhood`.