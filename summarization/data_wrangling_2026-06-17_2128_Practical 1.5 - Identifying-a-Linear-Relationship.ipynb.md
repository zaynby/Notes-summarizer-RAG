# Practical 1.5 - Identifying-a-Linear-Relationship.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

```markdown
# Summary: Linear Relationships and Visualization

## [[Linear Model]]
**Definition**: A statistical model that assumes a linear relationship between independent variables (X) and a dependent variable (Y).  
**Formula**:  
$$
Y = \beta_0 + \beta_1X + \epsilon
$$  
Where:  
- \( \beta_0 \) = intercept  
- \( \beta_1 \) = slope coefficient  
- \( \epsilon \) = error term  

**Example**:  
In Code Cell 3, a synthetic dataset is generated where \( y = 10x + \text{noise} \), demonstrating a clear linear relationship. The Boston Housing Dataset (Code Cell 6) is also used to test linearity between features (e.g., LSTAT, CRIM) and the target (MEDV).

---

## [[Scatter Plot]]
**Definition**: A graphical representation showing the relationship between two variables, typically with X on the horizontal axis and Y on the vertical axis.  
**Formula**: Not applicable (visual tool).  

**Example**:  
Code Cell 5 uses `sns.lmplot` to create a scatter plot of `x` vs `y` with a regression line (order=1), illustrating how points align with the linear trend. Similarly, Code Cells 7 and 9 visualize relationships in the Boston dataset.

---

## [[Linear Relationship]]
**Definition**: A relationship where changes in Y correspond to a consistent, straight-line pattern relative to changes in X.  
**Formula**:  
$$
Y = \beta_0 + \beta_1X
$$  

**Example**:  
The simulated data in Code Cell 3 shows a near-perfect linear relationship. In the Boston dataset, LSTAT vs MEDV (Code Cell 7) exhibits an approximate linear trend, though with some noise.

---

## [[Boston Housing Dataset]]
**Definition**: A classic dataset used for regression analysis, containing features like crime rate (CRIM), lower status population (LSTAT), and median house value (MEDV).  
**Formula**: Not applicable (dataset description).  

**Example**:  
Code Cell 6 loads the dataset, and Code Cells 7–9 explore linear relationships between variables (e.g., LSTAT vs MEDV, CRIM vs MEDV) using scatter plots with regression lines.
```