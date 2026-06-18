# Practical 1.5 - Identifying-a-Linear-Relationship.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured summary of the content using the requested format:

---

### **Linear Relationship**  
**Definition**: A straight-line connection between an independent variable **X** and a dependent variable **Y**, assumed by linear models for accurate predictions.  
**Formula**:  
$$
Y = \beta_0 + \beta_1X + \epsilon
$$  
Where:  
- $ \beta_0 $ = intercept  
- $ \beta_1 $ = slope coefficient  
- $ \epsilon $ = error term  

**Example**:  
In Code Cell 3, a synthetic dataset is created where `y = x * 10 + np.random.randn(n) * 2`, demonstrating a linear relationship. The scatter plot (Code Cell 5) shows data points closely aligning with the regression line, confirming linearity.  

---

### **Scatter Plot**  
**Definition**: A graphical tool to visualize the relationship between two variables, often used to assess linearity.  
**Formula**: Not applicable (visual tool). Axes represent:  
- **X-axis**: Independent variable  
- **Y-axis**: Dependent variable  

**Example**:  
In Code Cell 5, `sns.lmplot` generates a scatter plot for `x` vs `y` with a regression line (`order=1`), illustrating how linear relationships appear in data.  

---

### **Linear Regression**  
**Definition**: A statistical method to model the linear relationship between variables by fitting a straight line to observed data.  
**Formula**: Same as **Linear Relationship** (see above).  

**Example**:  
In Code Cell 2, `LinearRegression` from `sklearn` is imported for modeling. The simulated data (Code Cell 3) and Boston Housing plots (Code Cells 7-9) use regression lines to quantify relationships like `LSTAT` vs `MEDV`.  

---

### **Boston House Price Dataset**  
**Definition**: A classic dataset containing housing prices and features (e.g., crime rate, population stats) used to demonstrate regression analysis.  
**Formula**: Not applicable (dataset). Key variables include:  
- `MEDV`: Target (median house value)  
- `LSTAT`: % lower status population  
- `CRIM`: Crime rate  

**Example**:  
In Code Cell 6, the dataset is loaded (`boston = pd.read_csv("./data/boston_local.csv")`). Code Cell 7 plots `LSTAT` vs `MEDV`, showing a roughly linear inverse relationship.  

---

### **Wikilinks**  
- [[Linear Relationship]]  
- [[Scatter Plot]]  
- [[Linear Regression]]  
- [[Boston House Price Dataset]]  

This summary links concepts to enable cross-referencing in academic notes.