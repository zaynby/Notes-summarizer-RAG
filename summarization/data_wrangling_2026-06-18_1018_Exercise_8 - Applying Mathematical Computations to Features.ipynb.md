# Exercise_8 - Applying Mathematical Computations to Features.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here’s a structured summary of the key concepts from the provided notebook, formatted according to your specifications:

---

### **Feature Engineering**  
**Definition**: The process of creating new features (variables) from existing data to improve model performance or interpretability.  
**Formula**: N/A  
**Example**:  
- Created `family` column in Titanic dataset: `family = sibsp + parch`  
- Derived `is_alone` boolean feature: `is_alone = (family == 0)`  

[[Derived Features]]  

---

### **Derived Features**  
**Definition**: New variables generated through mathematical or logical operations on existing features.  
**Formula**:  
- `family = sibsp + parch` (addition of siblings/spouse and parents/children)  
- `is_alone = 1 if family == 0 else 0` (logical condition)  
**Example**:  
- `family` and `is_alone` columns in Titanic dataset.  

[[Feature Engineering]]  

---

### **Mathematical Operations for Feature Creation**  
**Definition**: Use of arithmetic operations (addition, subtraction, multiplication, division) to combine features.  
**Formula**:  
- `disposable_income = income - total_debt`  
- `debt_to_income_ratio = total_debt / total_income`  
**Example**:  
- `family = sibsp + parch` (Titanic dataset).  

[[Feature Engineering]]  

---

### **Exploratory Data Analysis (EDA)**  
**Definition**: Initial phase of data analysis to identify patterns, relationships, and anomalies.  
**Formula**: N/A  
**Example**:  
- Correlation matrix and heatmap of numerical variables in Titanic dataset.  

[[Correlation Matrix]]  

---

### **Correlation Matrix**  
**Definition**: A table displaying pairwise correlation coefficients between numerical variables.  
**Formula**: Pearson’s correlation coefficient:  
\[ r_{xy} = \frac{\text{cov}(x, y)}{\sigma_x \sigma_y} \]  
**Example**:  
- `data[num_cols].corr()` in Titanic dataset.  

[[Heatmap Visualization]]  

---

### **Heatmap Visualization**  
**Definition**: Visual representation of a correlation matrix using color gradients.  
**Formula**: N/A  
**Example**:  
- Seaborn heatmap of Titanic dataset correlations:  
  ```python  
  sns.heatmap(data[num_cols].corr(), annot=True)  
  ```  

[[Correlation Matrix]]  

---

### **Principal Component Analysis (PCA)**  
**Definition**: A dimensionality reduction technique that transforms variables into linearly uncorrelated principal components.  
**Formula**: Principal components are derived from eigenvectors of the covariance matrix.  
**Example**:  
- Applied to Airbnb dataset:  
  ```python  
  pca = PCA()  
  train_t = pca.transform(X_train)  
  ```  

[[Explained Variance Ratio]]  

---

### **Explained Variance Ratio**  
**Definition**: The proportion of total variance explained by each principal component.  
**Formula**:  
\[ \text{Variance Ratio}_i = \frac{\lambda_i}{\sum_{j=1}^n \lambda_j} \]  
**Example**:  
- Plotting PCA variance ratios:  
  ```python  
  plt.plot(pca.explained_variance_ratio_, linewidth=2)  
  ```  

[[PCA]]  

---

### **Data Preprocessing**  
**Definition**: Steps to clean, transform, and prepare data for analysis.  
**Formula**: N/A  
**Example**:  
- Dropped missing values in Airbnb dataset: `data = data.dropna()`  
- Train-test split:  
  ```python  
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)  
  ```  

[[Train-Test Split]]  

---

### **Train-Test Split**  
**Definition**: Dividing data into training and testing subsets to evaluate model performance.  
**Formula**:  
- `test_size=0.3` allocates 30% of data for testing.  
**Example**:  
- Split Airbnb dataset:  
  ```python  
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)  
  ```  

[[Data Preprocessing]]  

--- 

This summary connects key concepts like **Feature Engineering**, **PCA**, and **EDA** with practical examples from the notebook. Use [[Wikilinks]] to navigate between related terms.