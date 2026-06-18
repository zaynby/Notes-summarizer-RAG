# Exercise_3 - Encoding Categorical Variables.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

# **Categorical Encoding Techniques**

## **1. Categorical Variables**  
**Definition**: Variables representing discrete categories or labels (e.g., "Gender", "City").  
**Formula**: N/A  
**Example**: In `airbnb_sg.csv`, columns like "neighbourhood" or "amenities" are categorical.  

## **2. Nominal Variables**  
**Definition**: Categorical variables with **no intrinsic order** (e.g., "Country", "Color").  
**Formula**: N/A  
**Example**: "City" (e.g., London, Paris) has no inherent ranking.  

## **3. Ordinal Variables**  
**Definition**: Categorical variables with a **clear ordinal relationship** (e.g., "Grade", "Size").  
**Formula**: N/A  
**Example**: "Student's grade" (A > B > C > Fail).  

---

## **4. One-Hot Encoding (OHE)**  
**Definition**: Transforms nominal variables into binary columns (0/1) to avoid implying order.  
**Formula**: \( x_{\text{new}} = \begin{cases} 1 & \text{if category matches} \\ 0 & \text{otherwise} \end{cases} \)  
**Example**:  
```python
encoder = OneHotEncoder(drop='first')  
X_train_ohe = encoder.fit_transform(X_train[cat_cols])  
```  
Used in `airbnb_sg.csv` to encode "neighbourhood".  

## **5. Ordinal Encoding**  
**Definition**: Assigns integers to categories based on their ordinal relationship.  
**Formula**: \( \text{Encoded value} = \text{Rank of category} \)  
**Example**:  
```python
le = OrdinalEncoder()  
X_train_ord = le.transform(X_train[cat_cols])  
```  
Applied to ordinal variables like "bedroom count".  

## **6. Target Mean Encoding**  
**Definition**: Replaces categories with the **mean of the target variable** for that category.  
**Formula**: \( \text{Encoded value} = \frac{\sum y}{\text{count of category}} \)  
**Example**:  
```python
mean_enc = MeanEncoder(variables=cat_cols)  
X_train_enc = mean_enc.fit_transform(X_train, y_train)  
```  
Used in `airbnb_sg.csv` to encode categorical features using the "price" target.  

---

## **7. Model Evaluation Metrics**  
### **Mean Absolute Error (MAE)**  
**Definition**: Average absolute difference between predicted and actual values.  
**Formula**: \( \text{MAE} = \frac{\sum |y_{\text{actual}} - y_{\text{predicted}}|}{n} \)  
**Example**:  
```python
print('MAE:', mean_absolute_error(y_test, lm_reg.predict(X_test)))  
```  

### **Coefficient of Determination (R²)**  
**Definition**: Proportion of variance explained by the model.  
**Formula**: \( R^2 = 1 - \frac{\sum (y_{\text{actual}} - y_{\text{predicted}})^2}{\sum (y_{\text{actual}} - \bar{y})^2} \)  
**Example**: Used to evaluate linear regression models in the notebook.  

---

## **8. Key Workflow Steps**  
1. **Data Preparation**:  
   - Dropped non-numeric columns (`name`, `host_name`).  
   - Handled missing values with `SimpleImputer`.  

2. **Encoding Comparison**:  
   - **One-Hot Encoding**: Reduced model performance due to high dimensionality.  
   - **Ordinal Encoding**: Best performance for ordered categories.  
   - **Target Mean Encoding**: Balanced performance and interpretability.  

3. **Model Training**:  
   - Used `LinearRegression` to predict "price".  

---

## **[[Wikilinks]]**  
- [[Categorical Variables]] → [[One-Hot Encoding]], [[Ordinal Encoding]]  
- [[Target Mean Encoding]] → [[Feature Engineering]]  
- [[MAE]] → [[Model Evaluation]]  

--- 

This summary aligns with the notebook's focus on encoding techniques and their practical application in a regression task.