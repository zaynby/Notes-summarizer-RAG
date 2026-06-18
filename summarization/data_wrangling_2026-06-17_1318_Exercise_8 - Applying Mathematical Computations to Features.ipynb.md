# Exercise_8 - Applying Mathematical Computations to Features.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content:

---

### [[Feature Engineering]]  
**Definition**: The process of creating new features (variables) from existing data to enhance model performance or insights.  
**Formula**: N/A  
**Example**:  
- Created `family` column in Titanic dataset: `family = sibsp + parch`  
- Derived `is_alone` binary feature: `is_alone = 1 if family == 0 else 0`

---

### [[Mathematical Feature Combination]]  
**Definition**: Combining variables using arithmetic operations (addition, subtraction) to generate meaningful new features.  
**Formula**:  
- Total Debt = Car Loan + Credit Card Debt + Mortgage Debt  
- Disposable Income = Income − Total Debt  
**Example**:  
- `family` column: Sum of `sibsp` (siblings/spouse) and `parch` (parents/children) in Titanic data.  

---

### [[Binary Indicator Features]]  
**Definition**: Categorical variables (0/1) created based on a logical condition.  
**Formula**:  
- `is_alone = 1` if `family == 0`, else `0`  
**Example**:  
- `is_alone` feature in Titanic dataset indicating solo travelers.

---

### [[Correlation Matrix]]  
**Definition**: A matrix showing pairwise correlation coefficients (e.g., Pearson’s *r*) between numerical variables.  
**Formula**:  
$$
r = \frac{\sum{(x_i - \bar{x})(y_i - \bar{y})}}{\sqrt{\sum{(x_i - \bar{x})^2} \sum{(y_i - \bar{y})^2}}}
$$
**Example**:  
- Generated using `data[num_cols].corr()` and visualized via heatmap in Titanic dataset.

---

### [[Principal Component Analysis (PCA)]]  
**Definition**: A dimensionality reduction technique that transforms correlated variables into uncorrelated principal components.  
**Formula**:  
- Explained variance ratio of component *i*:  
$$
\frac{\text{Variance of component } i}{\text{Total variance}}
$$
**Example**:  
- Applied to Airbnb dataset: Reduced dimensions using `PCA().fit_transform()`, plotted explained variance ratios.

---

### [[Explained Variance Ratio]]  
**Definition**: The proportion of total variance in the data explained by each principal component.  
**Formula**:  
$$
\text{Explained Variance Ratio} = \frac{\lambda_i}{\sum_{j=1}^n \lambda_j}
$$
**Example**:  
- Visualized using `plt.plot(pca.explained_variance_ratio_)` to assess component contributions.

---

### [[Dimensionality Reduction]]  
**Definition**: The process of reducing the number of features in a dataset while preserving essential information.  
**Formula**: N/A  
**Example**:  
- Used PCA on Airbnb dataset to compress numerical features into lower-dimensional space.

---

### Key Links  
- [[Feature Engineering]] → [[Mathematical Feature Combination]] → [[Binary Indicator Features]]  
- [[Correlation Matrix]] → [[Principal Component Analysis]] → [[Dimensionality Reduction]]  

This summary integrates concepts from mathematical feature creation to advanced techniques like PCA, aligning with the practical exercises provided.