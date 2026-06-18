# Practical 8.3 - PolynomialExpansion.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured summary of the provided content on **Polynomial Expansion** in feature engineering:

---

### [[Polynomial Expansion]]
**Definition**: A technique in feature engineering where new features are created by raising existing features to non-linear powers (e.g., squared, cubed) or combining them through multiplication to capture non-linear relationships and interactions.  
**Formula**: For a feature \( x \), polynomial expansion up to degree \( d \) generates terms like \( x^2, x^3, \dots, x^d \). Interaction terms between features \( x_1 \) and \( x_2 \) are \( x_1 \times x_2 \).  
**Example**:  
- In the Boston Housing dataset, the feature `LSTAT` (lower status of the population) is expanded to \( \text{LSTAT}^2 \), \( \text{LSTAT}^3 \), and interaction terms like \( \text{LSTAT} \times \text{RM} \) (rooms per dwelling) using `PolynomialFeatures(degree=3)`.  
- Visualized plots show improved linearity between transformed features (e.g., \( \text{LSTAT}^2 \)) and the target `MEDV` (median value).

---

### [[PolynomialFeatures]]
**Definition**: A scikit-learn class (`sklearn.preprocessing.PolynomialFeatures`) used to automatically generate polynomial and interaction features from numerical data.  
**Formula**: N/A (implementation-based).  
**Example**:  
```python
poly = PolynomialFeatures(degree=3, interaction_only=False, include_bias=False)
train_t = poly.fit_transform(X_train[['LSTAT', 'RM', 'NOX']])
```  
This transforms the input features into a matrix containing all polynomial terms up to degree 3 (e.g., \( \text{LSTAT}^3 \), \( \text{RM} \times \text{NOX} \)).

---

### [[Interaction Terms]]
**Definition**: Features created by multiplying two or more original features, capturing synergistic effects between variables.  
**Formula**: \( x_1 \times x_2 \) for two features \( x_1 \) and \( x_2 \).  
**Example**:  
In the expanded dataset, interaction terms like \( \text{LSTAT} \times \text{RM} \) or \( \text{RM} \times \text{NOX} \) are generated to model combined effects on housing prices.

---

### [[Degree of Polynomial]]
**Definition**: The highest power to which features are raised during polynomial expansion.  
**Formula**: For degree \( d \), terms include \( x^1, x^2, \dots, x^d \).  
**Example**:  
Using `PolynomialFeatures(degree=3)` generates terms up to the third degree (e.g., \( \text{NOX}^3 \), \( \text{LSTAT}^2 \times \text{RM} \)).

---

### [[Feature Engineering]]
**Definition**: The process of transforming raw data into relevant features to improve machine learning model performance.  
**Formula**: N/A (process-based).  
**Example**:  
- Polynomial expansion of `LSTAT`, `RM`, and `NOX` in the Boston dataset creates new features like \( \text{LSTAT}^2 \) and \( \text{RM} \times \text{NOX} \), which better capture non-linear relationships with `MEDV`.

---

### Key Workflow Steps (from the notebook):
1. **Data Loading**: Boston Housing dataset loaded via `pd.read_csv`.  
2. **Correlation Analysis**: Heatmap visualizes feature correlations using `sns.heatmap`.  
3. **Train-Test Split**: Data split into training and testing sets with `train_test_split`.  
4. **Polynomial Transformation**:  
   - `PolynomialFeatures` initialized with `degree=3` and `interaction_only=False`.  
   - Features transformed using `fit_transform` and `transform`.  
5. **Visualization**: Scatter plots compare original and polynomial features against the target `MEDV`.

---

### [[Wikilinks]] to Related Concepts:
- [[Feature Engineering]]  
- [[Polynomial Regression]]  
- [[Interaction Effects]]  
- [[Scikit-learn]] (for `PolynomialFeatures`)  

This summary aligns with the notebook’s focus on generating non-linear features to enhance model interpretability and performance.