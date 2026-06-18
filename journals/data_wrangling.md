# DATA_WRANGLING Journal

---

## 2026-06-17 00:46 — Exercise_1 - Foreseeing Variable Problems When building ML Models.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided **Data Wrangling** exercise using the requested format:

---

### **Variable Types**  
**Definition**: Characteristics measured or counted in a dataset, categorized into numerical (discrete/continuous) or categorical (labels).  
**Formula**: N/A  
**Example**: In the Airbnb Singapore dataset, `price` is a **numerical** variable (continuous), while `neighbourhood` is **categorical** (labels like "Downtown", "Orchard").  

---

### **Missing Data Handling**  
**Definition**: Values not present in the dataset that can affect machine learning model performance.  
**Formula**: N/A  
**Example**: Code Cell 8 uses `clean = data.dropna()` to remove rows with missing values, ensuring compatibility with scikit-learn algorithms.  

---

### **Cardinality**  
**Definition**: The number of unique categories in a categorical variable.  
**Formula**: N/A  
**Example**: Code Cell 9 visualizes cardinality using `clean.nunique().plot.bar()`, showing variables like `neighbourhood` with high cardinality.  

---

### **Rare Categories**  
**Definition**: Categories in a variable with very low frequency (e.g., <1% of observations).  
**Formula**: N/A  
**Example**: Code Cell 10 identifies rare neighbourhoods (e.g., <1% of listings) using `value_counts()` and highlights them with a red threshold line.  

---

### **Linear Relationship**  
**Definition**: A straight-line relationship between two variables, often assessed using regression plots.  
**Formula**: N/A  
**Example**: Code Cell 11 uses `sns.lmplot` to check if `reviews_per_month` and `price` have a linear relationship, concluding they do not.  

---

### **Normal Distribution**  
**Definition**: A symmetric, bell-shaped distribution where most values cluster around the mean.  
**Formula**: N/A  
**Example**: Code Cell 12 uses `sns.histplot` with KDE to show `price` does not follow a normal distribution (non-bell-shaped histogram).  

---

### **Outliers**  
**Definition**: Data points that significantly deviate from the majority of observations.  
**Formula**:  
Interquartile Range (IQR) = Q3 - Q1  
Lower Boundary = Q1 - 1.5 × IQR  
Upper Boundary = Q3 + 1.5 × IQR  
**Example**: Code Cell 13 calculates IQR-based boundaries for `price` and identifies outliers using `np.where()`.  

---

### **Key Concepts Linked**  
- [[Categorical Variable]] → [[Cardinality]] / [[Rare Categories]]  
- [[Numerical Variable]] → [[Linear Relationship]] / [[Normal Distribution]] / [[Outliers]]  
- [[Missing Data]] → Preprocessing for scikit-learn compatibility  

This summary aligns with the exercise’s focus on identifying variable characteristics to guide feature engineering for machine learning models.

---

---

## 2026-06-17 00:49 — Exercise_2 - Imputing Missing Data.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content on missing data imputation:

---

### **1. Missing Data**  
**Definition**: Absent values in a dataset where no observation was recorded.  
**Formula**: Not applicable (phenomenological concept)  
**Example**:  
```python
# Introducing missing values randomly
random.seed(10)
values = set([random.randint(0, len(data)) for p in range(0, 100)])
random_rows = list(values)
for var in ['neighbourhood', 'room_type', 'minimum_nights', 'availability_365']:
    data.loc[random_rows, var] = np.nan
```

---

### **2. Imputation**  
**Definition**: Process of replacing missing data with statistical estimates to create a complete dataset.  
**Formula**: Not applicable (methodological concept)  
**Example**:  
```python
# Using SimpleImputer for numerical columns
imputer_num_arb = Pipeline([('imputer', SimpleImputer(strategy='constant', fill_value=0))])
```

---

### **3. SimpleImputer (Scikit-learn)**  
**Definition**: A class for filling missing values with predefined strategies (mean, median, most_frequent, constant).  
**Formula**:  
For strategy \( s \):  
- \( \text{Imputed value} = \begin{cases} 
  \mu & \text{if } s = \text{mean} \\ 
  \tilde{x} & \text{if } s = \text{median} \\ 
  \text{mode} & \text{if } s = \text{most\_frequent} \\ 
  c & \text{if } s = \text{constant}
\end{cases} \)  
**Example**:  
```python
# Categorical imputation with most frequent strategy
imputer_cat_freq = Pipeline([('imputer', SimpleImputer(strategy='most_frequent')]))
```

---

### **4. ColumnTransformer**  
**Definition**: Scikit-learn class to apply different preprocessing pipelines to different columns.  
**Formula**: Not applicable (methodological tool)  
**Example**:  
```python
# Applying different imputers to numerical and categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num_arb', imputer_num_arb, num_arbitrary),
        ('num_med', imputer_num_med, num_median),
        ('cat_freq', imputer_cat_freq, cat_frequent),
        ('cat_miss', imputer_cat_miss, cat_missing)
    ],
    remainder='passthrough'
)
```

---

### **5. Pipeline**  
**Definition**: Sequential chain of data transformations and estimators.  
**Formula**: Not applicable (methodological tool)  
**Example**:  
```python
# Feature Engine pipeline for imputation
pipe = Pipeline(steps=[
    ('arb_num', mdi.ArbitraryNumberImputer(variables=num_arbitrary)),
    ('med_num', mdi.MeanMedianImputer(imputation_method='median', variables=num_median)),
    ('freq_cat', mdi.CategoricalImputer(variables=cat_frequent, imputation_method='frequent')),
    ('miss_cat', mdi.CategoricalImputer(variables=cat_missing, imputation_method='missing'))
])
```

---

### **6. Constant Imputation**  
**Definition**: Replacing missing values with a user-defined constant (e.g., 0, "Missing").  
**Formula**: \( x_{\text{missing}} = c \)  
**Example**:  
```python
# Imputing missing categorical values with "Missing"
imputer_cat_miss = Pipeline([('imputer', SimpleImputer(strategy='constant', fill_value='Missing'))])
```

---

### **7. Median Imputation**  
**Definition**: Replacing missing numerical values with the median of observed data.  
**Formula**: \( x_{\text{missing}} = \tilde{x} \) (median)  
**Example**:  
```python
# Median imputation for numerical columns
imputer_num_med = Pipeline([('imputer', SimpleImputer(strategy='median'))])
```

---

### **8. Most Frequent Imputation**  
**Definition**: Replacing missing categorical values with the most common observed value.  
**Formula**: \( x_{\text{missing}} = \text{mode} \)  
**Example**:  
```python
# Most frequent imputation for categorical variables
imputer_cat_freq = Pipeline([('imputer', SimpleImputer(strategy='most_frequent')]))
```

---

### **9. Feature Engine**  
**Definition**: Library for advanced feature engineering, including specialized imputers.  
**Formula**: Not applicable (library)  
**Example**:  
```python
# Using Feature Engine's ArbitraryNumberImputer
from feature_engine.imputation import ArbitraryNumberImputer
pipe = Pipeline(steps=[('arb_num', mdi.ArbitraryNumberImputer(variables=num_arbitrary))])
```

---

### **10. Data Splitting**  
**Definition**: Dividing data into training and testing sets to evaluate imputation pipelines.  
**Formula**: Not applicable (methodological step)  
**Example**:  
```python
# Splitting data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    data.drop('price', axis=1), 
    data['price'], 
    test_size=0.3, 
    random_state=0
)
```

---

### **11. Categorical Variables Handling**  
**Definition**: Special treatment for non-numeric columns requiring non-numeric imputation.  
**Formula**: Not applicable (data type concept)  
**Example**:  
```python
# Identifying categorical columns
cat_cols = [c for c in X_train.columns if data[c].dtypes == 'O']
```

---

### **12. Numerical Variables Analysis**  
**Definition**: Examining distributions of numerical features using histograms.  
**Formula**: Not applicable (exploratory step)  
**Example**:  
```python
# Plotting histograms for numerical columns
for col in num_cols:
    plt.hist(data[col].dropna(), bins=30, edgecolor='k', alpha=0.7)
```

---

### **Key Links**  
- [[SimpleImputer]] → [[ColumnTransformer]] → [[Pipeline]]  
- [[Median Imputation]] → [[Most Frequent Imputation]]  
- [[Feature Engine]] → [[Data Splitting]]  

This summary provides a concise yet thorough overview of missing data imputation techniques and tools demonstrated in the notebook.

---

---

## 2026-06-17 00:55 — Exercise_3 - Encoding Categorical Variables.ipynb
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

---

---

## 2026-06-17 00:58 — Exercise_4 - Transforming Numerical Variables.ipynb
**Style:** structured_academic (experimenting)

# Summary: Data Wrangling - Transforming Numerical Variables  

## **Normal Distribution**  
- **Definition**: A symmetric probability distribution where data points cluster around the mean, following a bell-shaped curve.  
- **Formula**:  
  \[ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2} \]  
  where \( \mu \) is the mean and \( \sigma \) is the standard deviation.  
- **Example**: In the `airbnb_sg` dataset, Q-Q plots were used to check if `minimum_nights` and `number_of_reviews` followed a normal distribution.  

---

## **Data Transformation**  
- **Definition**: Mathematical methods applied to variables to alter their distribution, often to achieve normality for improved model performance (e.g., linear regression).  
- **Formula**: Varies by method (e.g., logarithm: \( y = \log(x) \), Yeo-Johnson: see below).  
- **Example**: Yeo-Johnson transformation was applied to `minimum_nights` and `number_of_reviews` to normalize their distributions.  

---

## **Yeo-Johnson Transformation**  
- **Definition**: A power transformation generalizing the Box-Cox method, capable of handling both positive and negative values.  
- **Formula**:  
  For \( \lambda \neq 1 \):  
  - If \( x_i \geq 0 \):  
    \[ y_i(\lambda) = \frac{(x_i + 1)^{\lambda} - 1}{\lambda} \]  
  - If \( x_i < 0 \):  
    \[ y_i(\lambda) = \frac{\log(x_i + 1)}{\lambda} \]  
- **Example**: Implemented via `PowerTransformer(method='yeo-johnson')` in the notebook, which reduced outliers in the transformed variables.  

---

## **PowerTransformer (scikit-learn)**  
- **Definition**: A class in `scikit-learn` for applying power transformations (e.g., Box-Cox, Yeo-Johnson) to make data more normally distributed.  
- **Formula**: N/A (implementation-specific).  
- **Example**: Used to fit and transform `minimum_nights` and `number_of_reviews` in the code:  
  ```python  
  transformer = PowerTransformer(method='yeo-johnson', standardize=False)  
  ```  

---

## **Diagnostic Plots**  
### **Histogram**  
- **Definition**: A graphical representation showing the frequency distribution of data across bins.  
- **Formula**: N/A.  
- **Example**: Histograms of `minimum_nights` and `number_of_reviews` revealed skewed distributions before transformation.  

### **Q-Q Plot (Quantile-Quantile Plot)**  
- **Definition**: A plot comparing quantiles of a dataset to a theoretical normal distribution to assess normality.  
- **Formula**: N/A.  
- **Example**: Q-Q plots in the notebook showed deviations from normality (e.g., curved points) before transformation.  

---

## **Box-Cox Transformation**  
- **Definition**: A power transformation for positive data to stabilize variance and normalize distributions.  
- **Formula**:  
  For \( \lambda \neq 0 \):  
  \[ y_i(\lambda) = \frac{x_i^{\lambda} - 1}{\lambda} \]  
  For \( \lambda = 0 \):  
  \[ y_i(\lambda) = \log(x_i) \]  
- **Example**: Mentioned in objectives but not applied in the code (only Yeo-Johnson was used).  

---

## **Linear Regression Assumptions**  
- **Definition**: Key assumptions include linearity, normality of residuals, homoscedasticity, and independence of errors.  
- **Formula**: N/A.  
- **Example**: The notebook emphasized normalizing variables (e.g., `minimum_nights`) to meet linear regression assumptions.  

---

### **Key Results from Notebook**  
- **Before Transformation**: `minimum_nights` and `number_of_reviews` showed skewed distributions with outliers (evident from histograms and Q-Q plots).  
- **After Yeo-Johnson Transformation**:  
  - Data became more evenly distributed.  
  - Outliers were reduced, as noted in Task 12.  

[[Wikilink to related concepts: Normal Distribution, Data Transformation, PowerTransformer, Diagnostic Plots]]

---

---

## 2026-06-17 01:03 — Exercise_5 - Performing Variable Discretization.ipynb
**Style:** structured_academic (experimenting)

# Summary: Variable Discretization in Data Wrangling

## [[Discretization (Binning)]]
**Definition**: The process of transforming continuous variables into discrete intervals (bins) to reduce the impact of outliers and handle skewed distributions.  
**Formula**: N/A  
**Example**:  
```python
disc = EqualFrequencyDiscretiser(q=10, variables=['availability_365', 'calculated_host_listings_count'])
disc.fit(X_train)
train_t = disc.transform(X_train)
```
Used to bin numerical variables like `availability_365` and `calculated_host_listings_count` into 10 equal-frequency intervals.

---

## [[Equal Frequency Discretiser]]
**Definition**: A method that divides data into bins where each bin contains an equal number of observations.  
**Formula**:  
Number of observations per bin = \( \frac{\text{Total Observations}}{q} \)  
**Example**:  
```python
disc = EqualFrequencyDiscretiser(q=10, variables=[...])
```
Creates 10 bins (`q=10`) with equal instance counts for `availability_365` and `calculated_host_listings_count`.

---

## [[Equal Width Discretiser]]
**Definition**: A method that creates bins of equal range (width) based on the variable’s minimum and maximum values.  
**Formula**:  
Bin width = \( \frac{\text{Max} - \text{Min}}{q} \)  
**Example**: Not explicitly used in the code, but imported for potential use:  
```python
from feature_engine.discretisation import EqualWidthDiscretiser
```

---

## [[Monotonic Relationship]]
**Definition**: A relationship where the target variable changes consistently (increases or decreases) as the discrete bins increase.  
**Formula**: N/A  
**Example**:  
After binning, if the mean `price` per bin does not show a linear trend, bins are reordered:  
```python
enc = OrdinalEncoder(encoding_method='ordered')
enc.fit(train_t, y_train)
train_t = enc.transform(train_t)
```

---

## [[OrdinalEncoder]]
**Definition**: Encodes categorical variables with an ordered relationship to maintain monotonicity between bins and the target.  
**Formula**: N/A  
**Example**:  
```python
pd.concat([train_t, y_train], axis=1).groupby('availability_365')['price'].mean().plot()
```
Used to ensure `availability_365` bins correlate monotonically with `price`.

---

## [[Supervised Discretization]]
**Definition**: Binning methods that use target variable information to optimize bin boundaries.  
**Formula**: N/A  
**Example**: Not implemented in the code, but mentioned in objectives as a concept.

---

## [[Unsupervised Discretization]]
**Definition**: Binning methods that rely solely on the variable’s distribution (e.g., equal frequency/width) without target information.  
**Formula**: N/A  
**Example**:  
```python
disc = EqualFrequencyDiscretiser(...)  # Uses data distribution only
```

---

## Key Workflow Steps
1. **Variable Selection**: Choose numerical variables (e.g., `availability_365`, `calculated_host_listings_count`).  
2. **Binning**: Apply `EqualFrequencyDiscretiser` or `EqualWidthDiscretiser`.  
3. **Relationship Check**: Plot bin means against the target (e.g., `price`).  
4. **Monotonicity Adjustment**: Use `OrdinalEncoder` if the relationship is non-linear.  

This approach ensures discrete variables are robust to outliers and improve model performance.

---

---

## 2026-06-17 01:06 — Exercise_6 - Working with Outliers.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

## **Outlier**  
**Definition**: A data point significantly different from the majority of observations in a dataset. Outliers skew statistical parameters (e.g., mean, variance) and can degrade machine learning model performance (e.g., linear regression, AdaBoost).  
**Formula**: N/A (detected via methods like IQR or Z-score)  
**Example**: In the `airbnb_sg` dataset, outliers in the `price` column were visualized using a boxplot (`Code Cell 10`), showing extreme values beyond the interquartile range.

---

## **Interquartile Range (IQR)**  
**Definition**: A measure of statistical dispersion representing the range between the first quartile (Q1, 25th percentile) and third quartile (Q3, 75th percentile). Used to identify outliers.  
**Formula**:  
\[
\text{IQR} = Q3 - Q1
\]  
Lower boundary: \( Q1 - 1.5 \times \text{IQR} \)  
Upper boundary: \( Q3 + 1.5 \times \text{IQR} \)  
**Example**: In `Exercise 1`, the `find_boundaries` function calculated IQR-based thresholds to detect outliers in the `price` column.

---

## **Winsorization**  
**Definition**: A technique to cap outliers at specified percentiles (e.g., 5th and 95th), reducing their influence while retaining data points.  
**Formula**:  
For a variable \( X \), values below \( P_{\text{lower}} \) or above \( P_{\text{upper}} \) are replaced with the respective percentiles.  
**Example**: In `Code Cell 11`, the `Winsorizer` capped `price` at 5% and 95% quantiles (`fold=0.05`) to handle outliers.

---

## **Trimming**  
**Definition**: The removal of observations containing outliers from the dataset.  
**Formula**: N/A (involves filtering data outside predefined bounds)  
**Example**: Discussed in objectives as a method to eliminate outliers, though not explicitly implemented in the provided code.

---

## **Capping**  
**Definition**: Setting maximum/minimum thresholds for variables to limit the impact of outliers. Winsorization is a form of capping.  
**Formula**: Similar to Winsorization, but thresholds may be defined using domain knowledge or statistical methods.  
**Example**: The `Winsorizer` in `Code Cell 11` capped `price` values at 5% and 95% quantiles.

---

## **Discretization**  
**Definition**: The process of converting continuous variables into discrete bins (intervals) to reduce outlier sensitivity and normalize skewed distributions.  
**Formula**: N/A (methods include equal-frequency, equal-width, or value-based binning)  
**Example**: In `Exercise 5`, discretization was applied to minimize the impact of outliers by grouping extreme values into lower/upper bins.

---

### **Key Links**  
- [[Outlier]] detection methods: [[Interquartile Range (IQR)]], [[Winsorization]]  
- Outlier handling techniques: [[Trimming]], [[Capping]], [[Discretization]]  
- Related concepts: [[Data Wrangling]], [[Machine Learning Model Performance]]  

This summary integrates content from the provided files and links to related concepts for cohesive note-taking.

---

---

## 2026-06-17 01:09 — Practical 1.0 - Data Preparation_Titanic.ipynb
**Style:** structured_academic (experimenting)

# Summary of Practical: Titanic Data Preprocessing  

## **NumPy**  
**Definition**: A library for numerical computing in Python, providing support for large, multi-dimensional arrays and matrices.  
**Formula**: N/A  
**Example**:  
```python  
import numpy as np  
```  
**Link**: [[Data Preprocessing]]  

---

## **Pandas**  
**Definition**: A library for data manipulation and analysis, offering data structures like DataFrame for structured data.  
**Formula**: N/A  
**Example**:  
```python  
import pandas as pd  
```  
**Link**: [[Data Loading]]  

---

## **Feature Engineering**  
**Definition**: The process of transforming raw data into features (variables) that better represent the underlying problem to learning algorithms.  
**Formula**: N/A  
**Example**:  
```python  
#pip install feature_engine  
```  
**Link**: [[Data Preprocessing]]  

---

## **Data Loading**  
**Definition**: The process of importing data from external sources (e.g., URLs, files) into a DataFrame.  
**Formula**: N/A  
**Example**:  
```python  
data = pd.read_csv('https://www.openml.org/data/get_csv/16826755/phpMYEkMl')  
```  
**Link**: [[Pandas]]  

---

## **Handling Missing Data**  
**Definition**: Replacing or removing invalid/missing data (e.g., placeholders like '?') to ensure data quality.  
**Formula**: N/A  
**Example**:  
```python  
data = data.replace('?', np.nan)  
```  
**Link**: [[Data Preprocessing]]  

---

## **Data Preprocessing Function**  
**Definition**: Custom functions to clean or transform data (e.g., extracting the first cabin letter).  
**Formula**: N/A  
**Example**:  
```python  
def get_first_cabin(row):  
    try:  
        return row.split()[0]  
    except:  
        return np.nan  
```  
**Link**: [[Column Transformation]]  

---

## **Column Transformation**  
**Definition**: Applying functions to modify specific columns in a DataFrame.  
**Formula**: N/A  
**Example**:  
```python  
data['cabin'] = data['cabin'].apply(get_first_cabin)  
```  
**Link**: [[Data Preprocessing Function]]  

---

## **Data Storage**  
**Definition**: Saving processed data to a file (e.g., CSV) for future use.  
**Formula**: N/A  
**Example**:  
```python  
data.to_csv('data/titanic.csv', index=False)  
```  
**Link**: [[Pandas]]  

---

**Key Concepts**: [[Data Preprocessing]], [[Pandas]], [[NumPy]], [[Feature Engineering]]  
**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)

---

---

## 2026-06-17 01:12 — Practical 1.1 - Identifying-Variables-Types.ipynb
**Style:** structured_academic (experimenting)

# Summary: Identifying Numerical and Categorical Variables

## [[Numerical Variable]]
**Definition**: Data that can be measured and expressed as integers or floats, representing quantities.  
**Formula**: Identified via `data.dtypes` (e.g., `int64`, `float64`).  
**Example**:  
```python
data['fare'].dtype  # float64
```

## [[Discrete Variable]]
**Definition**: A type of numerical variable that represents countable, distinct values (e.g., integers).  
**Formula**: N/A  
**Example**:  
```python
data['sibsp'].unique()  # [0, 1, 2, 3, 4, 5, 8]
```

## [[Continuous Variable]]
**Definition**: A type of numerical variable that can take any value within a range (e.g., real numbers).  
**Formula**: N/A  
**Example**:  
```python
data['fare'].unique()[0:20]  # [7.25, 71.2833, ...]
```

## [[Categorical Variable]]
**Definition**: Variables representing distinct categories or labels (non-numeric).  
**Formula**: Identified via `data.dtypes == 'O'` (object type in pandas).  
**Example**:  
```python
data['embarked'].unique()  # ['S', 'C', 'Q']
```

## [[Mixed Variable]]
**Definition**: A variable containing both numerical and categorical data (e.g., alphanumeric codes).  
**Formula**: N/A  
**Example**:  
```python
data['cabin'].unique()[0:20]  # [nan, 'C86', 'E38', ...]
```

## [[Data Types]]
**Definition**: The classification of data (e.g., integer, float, object) that determines valid operations.  
**Formula**: `data.dtypes`  
**Example**:  
```python
data.dtypes  # fare: float64, embarked: object
```

## [[Unique Values]]
**Definition**: Distinct values present in a variable, used to understand data granularity.  
**Formula**: `.unique()`  
**Example**:  
```python
data['sibsp'].unique()  # [0, 1, 2, 3, 4, 5, 8]
```

## [[Histogram]]
**Definition**: A plot showing the frequency distribution of numerical variables using bins.  
**Formula**: `.hist(bins=X)`  
**Example**:  
```python
data['sibsp'].hist(bins=20)
```

## [[Bar Plot]]
**Definition**: A visualization for categorical variables showing category frequencies.  
**Formula**: `.value_counts().plot.bar()`  
**Example**:  
```python
data['embarked'].value_counts().plot.bar()
```

## [[Value Counts Plot]]
**Definition**: A plot derived from `.value_counts()` to display categorical variable frequencies.  
**Formula**: `.value_counts()`  
**Example**:  
```python
data['embarked'].value_counts()
# S: 644, C: 215, Q: 112
```

---

This summary links key concepts for data wrangling, enabling efficient identification and visualization of variable types in datasets like the Titanic example. Use [[Wikilinks]] to navigate related terms.

---

---

## 2026-06-17 01:17 — Practical 1.2 - Quantifying-Missing-Data.ipynb
**Style:** structured_academic (experimenting)

### [[Missing Data]]
**Definition**: The absence of values for certain observations within a variable in a dataset, a common issue in real-world data sources.  
**Formula**: N/A  
**Example**: In the KDD-CUP-98 dataset, variables like `AGE` or `INCOME` may contain missing entries, which can be detected using `data.isnull().sum()`.

---

### [[Quantifying Missing Values]]
**Definition**: The process of measuring the extent of missing data in a dataset, often expressed as counts or percentages.  
**Formula**:  
Percentage of missing values = (Number of missing values / Total number of observations) × 100  
**Example**: Using `data.isnull().mean()` to calculate the percentage of missing values per variable (e.g., `0.15` indicates 15% missing values in a variable).

---

### [[Visualizing Missing Data]]
**Definition**: Representing the proportion of missing values graphically to enable intuitive interpretation of data quality issues.  
**Formula**: N/A  
**Example**: Generating a bar chart with `data.isnull().mean().plot.bar()` to visualize missing data percentages across variables, as shown in the practical.

---

### [[KDD-CUP-98 Dataset]]
**Definition**: A dataset from the UCI Machine Learning Repository, used in this practical to demonstrate missing data quantification and visualization.  
**Formula**: N/A  
**Example**: The dataset includes variables such as `AGE`, `NUMCHLD`, and `INCOME`, which are loaded using `pd.read_csv('./data/cup98LRN.txt', usecols=cols)` for analysis.  

---

This summary connects key concepts for handling missing data, with links to related techniques like [[Imputation]] (not covered in this practical but relevant for subsequent steps).

---

---

## 2026-06-17 01:22 — Practical 1.3 - Determining-Cardinality.ipynb
**Style:** structured_academic (experimenting)

# Summary: Cardinality in Categorical Variables

## **Cardinality**  
### **Definition**  
Cardinality refers to the number of **unique categories** present in a categorical variable. It quantifies the diversity of distinct labels or values within a variable.  

### **Formula**  
Cardinality is calculated as:  
\[ \text{Cardinality}(X) = \text{Number of unique values in variable } X \]  
In Python, this is implemented using pandas' `nunique()` method:  
```python
data['column_name'].nunique()  # Excludes missing values by default
data['column_name'].nunique(dropna=False)  # Includes missing values as a category
```  

### **Example**  
- **Variable**: `GENDER` with values `['male', 'female', 'male', 'female']`  
  - Cardinality = 2 (unique categories: 'male', 'female').  
- **Code Example**:  
  ```python
  data['GENDER'].nunique()  # Output: 2
  ```  
- **Visualization**:  
  ```python
  data.nunique().plot.bar(figsize=(12,6))  # Bar plot showing cardinality per variable
  ```  

---

## **Related Concepts**  
- **[[Categorical Variable]]**: A variable whose values represent categories (e.g., "gender," "color").  
- **[[Missing Data]]**: Absent values in a dataset, which can optionally be counted as an additional category in cardinality calculations using `dropna=False`.  
- **[[Pandas (Python library)]]**: Provides methods like `nunique()` for efficient cardinality computation.  

---

## **Key Applications**  
1. **Data Exploration**: Identifying variables with high cardinality (e.g., ZIP codes) that may require special handling.  
2. **Feature Engineering**: Deciding between encoding techniques (e.g., one-hot encoding vs. target encoding) based on cardinality.  
3. **Outlier Detection**: High cardinality might indicate noisy or erroneous data entries.  

This summary integrates concepts from the provided notebooks, emphasizing practical implementation in Python.

---

---

## 2026-06-17 01:26 — Practical 1.4 - Pinpointing-Rare-Categories.ipynb
**Style:** structured_academic (experimenting)

# Summary: Identifying Rare Categories and Cardinality  

## **Rare Categories**  
**Definition**: Categories in a categorical variable that represent a tiny minority of observations in the dataset, typically defined as those with a frequency below a threshold (e.g., 5% or 1%).  
**Formula**:  
Frequency of a category = \(\frac{\text{Count of category}}{\text{Total number of observations}}\)  
**Example**:  
In the Car Evaluation dataset, categories in the `class` variable with frequencies below 5% are flagged as rare. The code calculates frequencies using:  
```python  
label_freq = data['class'].value_counts() / len(data)  
```  
A bar plot with a red line at \(y=0.05\) visualizes categories below this threshold.  

## **Cardinality**  
**Definition**: The number of unique categories present in a categorical variable (e.g., the variable `class` in the Car Evaluation dataset has a cardinality of 4 if it has 4 unique labels).  
**Formula**:  
Cardinality = \(\text{Number of unique categories}\)  
**Example**:  
For the `class` variable in the dataset:  
```python  
data['class'].nunique()  # Returns the count of unique categories  
```  

## **Frequency Calculation**  
**Definition**: The process of determining the proportion of observations each category represents in a dataset.  
**Formula**:  
Frequency = \(\frac{\text{Number of occurrences of a category}}{\text{Total number of observations}}\)  
**Example**:  
```python  
total_cars = len(data)  
label_freq = data['class'].value_counts() / total_cars  
```  

## **Visualization of Rare Categories**  
**Definition**: A graphical method to identify rare categories by plotting their frequencies and overlaying a threshold line (e.g., 5%).  
**Formula**: N/A (Method involves sorting frequencies and plotting).  
**Example**:  
```python  
fig = label_freq.sort_values(ascending=False).plot.bar()  
fig.axhline(y=0.05, color='red')  # Threshold line for 5%  
```  

---

### **Key Links**  
- [[Cardinality]] is critical for understanding the diversity of categories.  
- [[Frequency Calculation]] directly determines whether a category is classified as rare.  
- Rare categories often require special handling in machine learning pipelines, such as merging or removing them to improve model performance.

---

---

## 2026-06-17 01:32 — Practical 1.5 - Identifying-a-Linear-Relationship.ipynb
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

---

---

## 2026-06-17 09:32 — Practical 1.6 - Identifying-a-Normal-Distribution.ipynb
**Style:** structured_academic (experimenting)

### Normality Assessment in Linear Models

**Term:** Normal Distribution -> **Definition:** A probability distribution that is symmetric and bell-shaped. It is characterized by its mean (\(\mu\)) and standard deviation (\(\sigma\)). -> **Formula:** 
\[ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \]
-> **Example:**
```python
import pandas as pd
import numpy as np

# for plotting
import matplotlib.pyplot as plt
import seaborn as sns

# for the Q-Q plots
import scipy.stats as stats

# load the Boston House price data
boston = pd.read_csv("./data/boston_local.csv")

sns.histplot(boston['RM'], bins=30, kde=True, stat="density")
```

---

**Term:** Histogram -> **Definition:** A graphical representation that organizes a group of data points into user-specified ranges. -> **Formula:** 
\[ \text{Frequency} = \frac{\text{Number of Observations in the Range}}{\text{Total Number of Observations}} \times 100 \]
-> **Example:**
```python
sns.histplot(boston['RM'], bins=30, kde=True, stat="density")
```

---

**Term:** Q-Q Plot -> **Definition:** A graphical technique for checking the normality of a dataset. It compares the quantiles of the data against the quantiles of a normal distribution. -> **Formula:** 
\[ \text{Theoretical Quantile} = \Phi^{-1}(P) \]
where \( P \) is the empirical cumulative probability and \( \Phi^{-1} \) is the inverse cumulative density function of the standard normal distribution.
-> **Example:**
```python
sns.histplot(boston['LSTAT'], bins=30, kde=True, stat="density")
stats.probplot(boston['LSTAT'], dist="norm", plot=plt)
```

---

**Term:** Scatter Plot -> **Definition:** A type of plot or mathematical diagram using Cartesian coordinates to display values for typically two variables for a set of data. -> **Formula:** 
\[ \text{Scatter Plot} = (x, y) \]
-> **Example:**
```python
sns.lmplot(x="LSTAT", y="MEDV", data=boston, order=1)
```

---

**Term:** Simulated Independent Variable x -> **Definition:** A variable that is generated to follow a normal distribution for the purpose of demonstration. -> **Formula:** 
\[ x \sim N(\mu, \sigma^2) \]
where \( \mu \) is the mean and \( \sigma \) is the standard deviation.
-> **Example:**
```python
np.random.seed(29)
n = 200
x = np.random.randn(n)

data = pd.DataFrame([x]).T
data.columns = ['x']
sns.histplot(x, bins=30, kde=True, stat="density")
```

---

**Term:** Confidence Interval -> **Definition:** A range of values that is likely to contain the true value of a parameter. -> **Formula:** 
\[ \text{Confidence Interval} = \hat{\theta} \pm z_{\alpha/2} \times SE(\hat{\theta}) \]
where \( \hat{\theta} \) is the estimate, \( z_{\alpha/2} \) is the critical value from the standard normal distribution, and \( SE(\hat{\theta}) \) is the standard error.
-> **Example:**
```python
sns.lmplot(x="LSTAT", y="MEDV", data=boston, order=1)
```

### Example Code for Q5:
```python
# insert code here
sns.histplot(x,bins=30,kde=True,stat="density")
```

---

---

## 2026-06-17 09:36 — Practical 1.7 - Distinguishing-Variable-Distribution.ipynb
**Style:** structured_academic (experimenting)

```markdown
# Summary: Visualizing Variable Distributions

## [[Data Visualization]]
### Definition  
Techniques used to graphically represent data to understand distributions and patterns, as demonstrated in this practical following Soledad Galli's *Python Feature Engineering Cookbook* (Jan 2020).

### Formula  
N/A  

### Example  
```python
import matplotlib.pyplot as plt
import pandas as pd
boston.hist(bins=30, figsize=(12,12), density=True)
plt.show()
```

---

## [[Histogram]]
### Definition  
A graphical representation of the distribution of numerical data, showing the frequency or density of different value ranges.

### Formula  
N/A  

### Example  
```python
boston.hist(bins=30, figsize=(12,12), density=True)
```

---

## [[Data Loading]]
### Definition  
The process of importing data from external sources into a program for analysis.

### Formula  
N/A  

### Example  
```python
boston = pd.read_csv("./data/boston_local.csv")
```

---

## [[Boston Housing Dataset]]
### Definition  
A widely used dataset containing features of Boston houses (e.g., crime rates, room counts) for regression analysis.

### Formula  
N/A  

### Example  
```python
boston = pd.read_csv("./data/boston_local.csv")
boston.head()
```

---

## [[Density Parameter in Histograms]]
### Definition  
A parameter that normalizes the histogram area to 1, displaying probability density instead of raw frequency counts.

### Formula  
N/A  

### Example  
```python
density=True  # within the hist() function
```
```

---

---

## 2026-06-17 09:39 — Practical 1.8 - Highlighting-Outliers.ipynb
**Style:** structured_academic (experimenting)

# Summary: Outlier Detection and Handling  

## [[Outlier]]  
**Definition**: A data point significantly different from the remaining data, potentially generated by a different mechanism (Hawkins, 1980).  
**Formula**: Not applicable directly; detected using the **IQR Proximity Rule**.  
**Example**:  
```python  
# Flag outliers using IQR boundaries  
outliers = np.where(boston['RM'] > upper_boundary, True, np.where(boston['RM'] < lower_boundary, True, False))  
```  

---

## [[Interquartile Range (IQR)]]  
**Definition**: The range between the 25th (Q1) and 75th (Q3) percentiles of a dataset.  
**Formula**:  
\[ \text{IQR} = Q3 - Q1 \]  
**Example**:  
```python  
IQR = boston['RM'].quantile(0.75) - boston['RM'].quantile(0.25)  
```  

---

## [[IQR Proximity Rule]]  
**Definition**: A statistical method to identify outliers based on distances from the IQR. Data points outside the boundaries are considered outliers.  
**Formula**:  
- Upper boundary: \( Q3 + (1.5 \times \text{IQR}) \)  
- Lower boundary: \( Q1 - (1.5 \times \text{IQR}) \)  
**Example**:  
```python  
def find_boundaries(df, variable, distance):  
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)  
    lower_boundary = df[variable].quantile(0.25) - (IQR * distance)  
    upper_boundary = df[variable].quantile(0.75) + (IQR * distance)  
    return upper_boundary, lower_boundary  
```  

---

## [[Boxplot]]  
**Definition**: A graphical representation showing the distribution of data, including median, IQR, and outliers.  
**Components**:  
- Box: Span of IQR (Q1 to Q3).  
- Line inside box: Median (Q2).  
- Whiskers: Boundaries defined by the IQR Proximity Rule.  
**Example**:  
```python  
sns.boxplot(y=boston['RM'])  # Visualize outliers for 'RM' variable  
```  

---

## [[Discretization]]  
**Definition**: The process of converting continuous variables into discrete bins to reduce the impact of outliers.  
**Purpose**: Minimizes outlier influence by grouping extreme values into intervals.  
**Example**:  
```python  
# Outliers in 'RM' are grouped into lower/upper bins, reducing their skewing effect  
```  

---

## Key Concepts Linkage  
- **Outliers** are detected using the **IQR Proximity Rule** and visualized via **Boxplots**.  
- **Discretization** mitigates their impact by binning data.  
- Code examples demonstrate outlier identification (e.g., `find_boundaries`) and visualization (e.g., `sns.boxplot`).  

[[Discretization]] is further explored in Exercise 5, while outlier handling techniques (e.g., imputation) are detailed in Exercise 6.

---

---

## 2026-06-17 09:42 — Practical 1.9 - Comparing-Feature-Magnitude.ipynb
**Style:** structured_academic (experimenting)

## Summary: Feature Magnitude and Statistical Metrics in Machine Learning  

### [[Feature Magnitude]]  
**Definition**: The scale or range of values that a feature (independent variable) takes in a dataset. Machine learning algorithms often perform poorly when features are on vastly different scales.  
**Formula**: Not applicable directly, but measured via metrics like range (max - min), standard deviation, or quantiles.  
**Example**: In the Boston Housing Dataset, `CRIM` (crime rate) ranges from 0 to 89, while `CHAS` (Charles River proximity) is binary (0 or 1), indicating differing magnitudes.  

---

### [[Statistical Metrics]]  
**Definition**: Quantitative measures used to summarize the distribution and central tendency of a feature. Key metrics include mean, standard deviation, min/max, and quantiles (25th, 50th, 75th percentiles).  
**Formula**:  
- Mean: \(\bar{x} = \frac{\sum x_i}{n}\)  
- Standard Deviation: \(\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}\)  
**Example**: The `boston.describe()` output provides statistical metrics for all features, showing skewed scales (e.g., `RM` ranges from 3.5 to 8.8, while `NOX` ranges from 0.385 to 0.871).  

---

### [[Feature Scaling]]  
**Definition**: The process of standardizing the range of features to improve model performance. Common techniques include Min-Max Scaling and Z-score normalization.  
**Formula**:  
- Min-Max Scaling: \(x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}\)  
- Z-score Normalization: \(x_{\text{scaled}} = \frac{x - \mu}{\sigma}\) (where \(\mu\) = mean, \(\sigma\) = standard deviation)  
**Example**: Normalizing `CRIM` (0–89) and `CHAS` (0–1) to a common scale (e.g., 0–1) would ensure equal contribution in distance-based algorithms like KNN.  

---

### [[Range of Variables]]  
**Definition**: The difference between the maximum and minimum values of a feature, indicating its spread.  
**Formula**: \(\text{Range} = x_{\text{max}} - x_{\text{min}}\)  
**Example**: The `boston.max() - boston.min()` calculation reveals ranges like `CRIM` (89 - 0 = 89) vs. `CHAS` (1 - 0 = 1), highlighting scale disparities.  

---

### [[Boston Housing Dataset]]  
**Definition**: A classic dataset used for regression tasks, containing 13 features influencing house prices in Boston suburbs (e.g., crime rate, room size, pollution).  
**Formula**: Not applicable.  
**Example**: Loaded via `pd.read_csv("./data/boston_local.csv")`, it serves as a practical example to analyze feature magnitudes and apply scaling.  

---

**Key Insight**: Features with differing magnitudes (e.g., `CRIM` vs. `CHAS`) require scaling to ensure algorithms like SVM or KNN perform optimally. Statistical metrics and range calculations guide this preprocessing step.

---

---

## 2026-06-17 09:47 — Practical 2.0 - Data Preparation_CreditApprovalUCI.ipynb
**Style:** structured_academic (experimenting)

# Summary: Credit Approval Dataset Preparation

## [[Missing Data]]  
**Definition**: Absence of values in a dataset for specific observations within variables.  
**Formula**: N/A  
**Example**:  
```python
data.replace('?', np.nan)  # Replaces placeholder '?' with NaN
```

## [[Data Preprocessing]]  
**Definition**: Process of cleaning and transforming raw data into an analysis-ready format.  
**Formula**: N/A  
**Example**:  
- Handling missing values  
- Converting variable types (e.g., `A2` to float)  
- Encoding target variable (`A16` to binary 1/0)  

## [[Data Encoding]]  
**Definition**: Conversion of categorical variable values into numerical representations.  
**Formula**:  
Binary encoding:  
\[ y = \begin{cases} 1 & \text{if } x = '+' \\ 0 & \text{if } x = '-' \end{cases} \]  
**Example**:  
```python
data['A16'].map({'+': 1, '-': 0})  # Encodes target variable
```

## [[Categorical Variables]]  
**Definition**: Variables representing discrete categories (nominal/ordinal).  
**Formula**: N/A  
**Example**:  
```python
cat_cols = [c for c in data.columns if data[c].dtypes == 'O']  # Identifies object-type columns
```

## [[Numerical Variables]]  
**Definition**: Variables containing quantitative values (integer/float).  
**Formula**: N/A  
**Example**:  
```python
num_cols = [n for n in data.columns if data[n].dtypes == 'int']  # Selects integer-type columns
```

## [[Data Augmentation]]  
**Definition**: Introduction of synthetic modifications (e.g., missing values) to enhance data utility.  
**Formula**: N/A  
**Example**:  
```python
random.seed(9001)
values = [random.randint(0, len(data)) for _ in range(100)]
data.loc[values, ['A3', 'A8', 'A9', 'A10']] = np.nan  # Adds missing values
```

## [[Variable Conversion]]  
**Definition**: Changing the data type of a variable (e.g., string to numeric).  
**Formula**: N/A  
**Example**:  
```python
data['A2'] = data['A2'].astype('float')  # Converts column to float
```

---

**Source**: Adapted from Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)

---

---

## 2026-06-17 09:51 — Practical 2.1 - Removing-observations-with-missing-data.ipynb
**Style:** structured_academic (experimenting)

# Summary: Complete Case Analysis (CCA)

## Term: [[Complete Case Analysis (CCA)]]  
### Definition  
Complete Case Analysis (CCA), also known as **list-wise deletion**, is a method for handling missing data where observations (rows) containing missing values in **any** of the variables are discarded. It preserves the distribution of variables **if data is missing at random** and the proportion of missing data is small. However, it risks significant data loss if missingness is widespread across variables.  

### Formula  
CCA is implemented using the `dropna()` function in pandas:  
- **Full dataset**: `data.dropna()`  
- **Subset of variables**: `data.dropna(subset=[column1, column2, ...])`  

### Example  
```python
# Create complete case dataset for all variables
data_cca = data.dropna()

# Create complete case dataset for specific variables (e.g., A1, A2, A6, A7, A14)
data_cca_subset = data.dropna(subset=['A1', 'A2', 'A6', 'A7', 'A14'])

# Output: Compare original and cleaned dataset sizes
print('Total observations:', len(data))
print('Complete cases:', len(data_cca))
```  
**Output**:  
```
Number of total observations: X  
Number of observations with complete cases: Y  
```  
Where `Y < X` due to removed rows with missing values.  

---

## Related Concepts  
- **[[Missing Data]]**: Data points not present in the dataset.  
- **[[List-wise Deletion]]**: Synonym for CCA.  
- **[[Data Imputation]]**: Alternative to CCA for handling missing data (e.g., mean/median imputation).  

*Source: Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*

---

---

## 2026-06-17 09:56 — Practical 2.10 - Assembling-an-imputation-pipeline-with-Feature-Engine.ipynb
**Style:** structured_academic (experimenting)

# Summary: Imputing Missing Data with Feature-engine

## [[Missing Data Imputation]]
**Definition**: The process of replacing missing values in a dataset with statistically estimated values to enable machine learning model training.  
**Formula**: N/A  
**Example**:  
```python
pipe = Pipeline(steps=[  
    ('imp_num_arbitrary', mdi.ArbitraryNumberImputer(variables=features_num_arbitrary)),  
    ('imp_num_median', mdi.MeanMedianImputer(imputation_method='median', variables=features_num_median)),  
    ...  
])  
```

---

## [[Feature-engine]]
**Definition**: An open-source Python library for feature engineering, providing tools for imputation, encoding, and discretization.  
**Formula**: N/A  
**Example**:  
```python  
import feature_engine.imputation as mdi  # Importing imputation module  
```

---

## [[Arbitrary Number Imputer]]
**Definition**: Replaces missing values with a user-specified constant (e.g., 0).  
**Formula**:  
\[ \text{Imputed Value} = c \]  
where \( c \) is a constant.  
**Example**:  
```python  
SimpleImputer(strategy='constant', fill_value=0)  
# or  
mdi.ArbitraryNumberImputer(variables=features_num_arbitrary)  
```

---

## [[Mean/Median Imputer]]
**Definition**: Replaces missing values with the mean or median of the feature.  
**Formula**:  
- **Mean**:  
\[ \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i \]  
- **Median**: Middle value of ordered data.  
**Example**:  
```python  
SimpleImputer(strategy='median')  
# or  
mdi.MeanMedianImputer(imputation_method='median', variables=features_num_median)  
```

---

## [[Categorical Imputer]]
**Definition**: Replaces missing categorical values with the most frequent category or a 'missing' placeholder.  
**Formula**: N/A  
**Example**:  
```python  
mdi.CategoricalImputer(variables=features_cat_frequent, imputation_method='frequent')  
# or  
mdi.CategoricalImputer(variables=features_cat_missing, imputation_method='missing')  
```

---

## [[Pipeline]]
**Definition**: A sequence of data transformation steps combined into a single workflow.  
**Formula**: N/A  
**Example**:  
```python  
pipe = Pipeline(steps=[  
    ('imp_num_arbitrary', mdi.ArbitraryNumberImputer(...)),  
    ('imp_num_median', mdi.MeanMedianImputer(...)),  
])  
```

---

## [[ColumnTransformer]]
**Definition**: Applies different preprocessing steps to specific columns of a dataset.  
**Formula**: N/A  
**Example**:  
```python  
preprocessor = ColumnTransformer(transformers=[  
    ('num_arb', imputer_num_arb, num_arbitrary),  
    ('num_med', imputer_num_med, num_median),  
])  
```

---

## [[Train-Test Split]]
**Definition**: Dividing a dataset into training and testing subsets to evaluate model performance.  
**Formula**: N/A  
**Example**:  
```python  
X_train, X_test, y_train, y_test = train_test_split(  
    data.drop('A16', axis=1), data['A16'], test_size=0.3, random_state=0  
)  
```

---

## [[Handling Different Variable Types]]
**Definition**: Applying appropriate imputation techniques based on whether variables are numerical or categorical.  
**Formula**: N/A  
**Example**:  
```python  
cat_cols = [c for c in data.columns if data[c].dtypes == 'O']  # Categorical  
num_cols = [c for c in data.columns if data[c].dtypes != 'O']  # Numerical  
```

---

## [[Imputation Strategy]]
**Definition**: Selection of imputation methods based on data characteristics (e.g., missingness pattern, variable type) and model requirements.  
**Formula**: N/A  
**Example**:  
- Using **median imputation** for numerical variables with low missingness.  
- Using **'missing'** imputation for categorical variables with high missingness.  

---

**Wikilinks**:  
- [[Missing Data Imputation]] → [[Data Wrangling]]  
- [[Pipeline]] → [[Machine Learning Workflow]]  
- [[Feature-engine]] → [[Python Libraries for Data Science]]  
- [[ColumnTransformer]] → [[Scikit-learn]]

---

---

## 2026-06-17 10:04 — Practical 2.2 - Performing-mean-or-median-imputation.ipynb
**Style:** structured_academic (experimenting)

# Summary: Mean/Median Imputation Techniques

## [[Mean Imputation]]
- **Definition**: A method replacing missing values in numerical variables with the **mean** (average) of observed values in the training set. Preserves the general distribution but may reduce variance.
- **Formula**:  
  \[
  \text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n}
  \]
  where \( x_i \) are observed values and \( n \) is the count of observations.
- **Example**:  
  ```python
  # Using pandas to impute missing values with mean
  for var in ['A2', 'A3', 'A8', 'A11', 'A15']:
      value = X_train[var].mean()
      X_train[var].fillna(value, inplace=True)
      X_test[var].fillna(value, inplace=True)
  ```

---

## [[Median Imputation]]
- **Definition**: A technique replacing missing values in numerical variables with the **median** (middle value) of observed data. More robust to outliers than mean imputation.
- **Formula**:  
  \[
  \text{Median} = 
  \begin{cases} 
      x_{\frac{n}{2}} & \text{if } n \text{ is even} \\
      x_{\frac{n+1}{2}} & \text{if } n \text{ is odd}
  \end{cases}
  \]
- **Example**:  
  ```python
  # Using pandas to impute missing values with median
  for var in ['A2', 'A3', 'A8', 'A11', 'A15']:
      value = X_train[var].median()
      X_train[var].fillna(value, inplace=True)
      X_test[var].fillna(value, inplace=True)
  ```

---

## [[SimpleImputer (scikit-learn)]]
- **Definition**: A scikit-learn class for imputation that supports strategies like `mean`, `median`, or `most_frequent`. Learns imputation values from the training set.
- **Formula**:  
  Imputes missing values using the strategy parameter (e.g., \( \text{median}(\text{train data}) \)).
- **Example**:  
  ```python
  # Using scikit-learn's SimpleImputer for median imputation
  imputer = SimpleImputer(strategy='median')
  imputer.fit(X_train)
  X_train_imputed = imputer.transform(X_train)
  X_test_imputed = imputer.transform(X_test)
  ```

---

## [[MeanMedianImputer (Feature-engine)]]
- **Definition**: A Feature-engine transformer for mean or median imputation. Stores imputation values in `imputer_dict_` for consistency across datasets.
- **Formula**:  
  Uses \( \text{median}(\text{train data}) \) or \( \text{mean}(\text{train data}) \) for imputation.
- **Example**:  
  ```python
  # Using Feature-engine's MeanMedianImputer
  median_imputer = MeanMedianImputer(imputation_method='median', variables=['A2', 'A3', 'A8', 'A11', 'A15'])
  median_imputer.fit(X_train)
  X_train_imputed = median_imputer.transform(X_train)
  X_test_imputed = median_imputer.transform(X_test)
  ```

---

## Key Considerations
- **Training vs. Test Set**: Imputation parameters (mean/median) are calculated on the **training set** to avoid data leakage.
- **Data Types**: Mean/median imputation applies only to numerical variables.
- **Comparison**: 
  - **Mean** is sensitive to outliers.
  - **Median** is robust to outliers but discards distribution information.
  - Libraries like scikit-learn and Feature-engine automate parameter storage and application.

---

---

## 2026-06-17 10:06 — Practical 2.3 - Implementing-mode-or-frequent-category-imputation.ipynb
**Style:** structured_academic (experimenting)

### [[Frequent Category Imputation]]  
**Definition**: A technique to replace missing values in categorical variables with the **mode** (most frequently occurring category) estimated from the training dataset. The mode is stored and applied to training, test, and future datasets to ensure consistency.  

**Formula**:  
Mode = \( \text{argmax}_k(\text{count of category } k \text{ in training set}) \)  

**Example**:  
- **Pandas**:  
  ```python  
  value = X_train[var].mode()[0]  
  X_train[var].fillna(value, inplace=True)  
  X_test[var].fillna(value, inplace=True)  
  ```  
- **Feature-engine**:  
  ```python  
  mode_imputer = mdi.CategoricalImputer(variables=['A4', 'A5'], imputation_method='frequent')  
  mode_imputer.fit(X_train)  
  X_train = mode_imputer.transform(X_train)  
  ```  
- **Scikit-learn**:  
  ```python  
  imputer = SimpleImputer(strategy='most_frequent')  
  X_train = imputer.fit_transform(X_train)  
  X_test = imputer.transform(X_test)  
  ```  

---

### [[Pandas Frequent Imputation]]  
**Definition**: Using Pandas' `fillna` method to manually replace missing categorical values with the mode computed from the training set.  

**Formula**:  
Mode = \( \text{X_train[var].mode()[0]} \)  

**Example**:  
```python  
for var in ['A4', 'A5']:  
    value = X_train[var].mode()[0]  
    X_train[var].fillna(value, inplace=True)  
    X_test[var].fillna(value, inplace=True)  
```  

---

### [[Feature-engine CategoricalImputer]]  
**Definition**: A transformer from the **Feature-engine** library that automates frequent category imputation by learning the mode during `fit` and storing it in `imputer_dict_`.  

**Formula**:  
\( \text{imputer_dict_} = \{\text{variable: mode for each variable}\} \)  

**Example**:  
```python  
mode_imputer = mdi.CategoricalImputer(variables=['A6', 'A7'], imputation_method='frequent')  
mode_imputer.fit(X_train)  
X_train = mode_imputer.transform(X_train)  
```  

---

### [[Scikit-learn SimpleImputer (most_frequent)]]  
**Definition**: Scikit-learn’s `SimpleImputer` with the `most_frequent` strategy, which replaces missing values in categorical features with the mode learned from the training set.  

**Formula**:  
\( \text{statistics_} = \text{mode of each feature in the training set} \)  

**Example**:  
```python  
imputer = SimpleImputer(strategy='most_frequent')  
X_train = imputer.fit_transform(X_train)  
X_test = imputer.transform(X_test)  
```  

--- 

**Key Concepts**:  
- [[Mode]]: Most frequent category in a dataset.  
- [[Training Set]]: Data used to learn imputation parameters (e.g., mode).  
- [[Test Set]]: Data imputed using parameters learned from the training set.

---

---

## 2026-06-17 10:09 — Practical 2.4 - Replacing-missing-values-by-an-arbitrary-number.ipynb
**Style:** structured_academic (experimenting)

# Summary: Imputation Techniques for Missing Data

## [[Imputation]]
**Definition**: The process of replacing missing values in a dataset with statistically estimated or predefined values to create a complete dataset for analysis or modeling.  
**Formula**: N/A  
**Example**:  
```python
# Imputing missing values using pandas
X_train[var] = X_train[var].fillna(99)
```

---

## [[Missing Data]]
**Definition**: Absence of values for certain observations in a dataset, often due to collection errors, non-response, or other factors.  
**Formula**: N/A  
**Example**:  
```python
# Checking percentage of missing values per variable
X_train.isnull().mean()
```

---

## [[Arbitrary Number Imputation]]
**Definition**: A technique where missing values are replaced with a predefined arbitrary constant (e.g., 99, -1) not close to the distribution’s mean/median.  
**Formula**:  
\[ \text{Imputed Value} = c \]  
where \( c \) is the arbitrary constant (e.g., 99).  
**Example**:  
```python
# Using Feature-engine's ArbitraryNumberImputer
imputer = ArbitraryNumberImputer(arbitrary_number=99, variables=['A2','A3', 'A8', 'A11'])
imputer.fit(X_train)
X_train = imputer.transform(X_train)
```

---

## [[Pandas Imputation]]
**Definition**: Using Pandas' `fillna()` method to replace missing values in a DataFrame.  
**Formula**: N/A  
**Example**:  
```python
# Replacing missing values with 99 in specified columns
for var in ['A2','A3', 'A8', 'A11']:
    X_train[var] = X_train[var].fillna(99)
    X_test[var] = X_test[var].fillna(99)
```

---

## [[Feature-engine]]
**Definition**: An open-source Python library for feature engineering tasks, including advanced imputation methods.  
**Formula**: N/A  
**Example**:  
```python
# Transforming data with Feature-engine imputer
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)
```

---

## [[Scikit-learn SimpleImputer (Constant Strategy)]]
**Definition**: Scikit-learn’s `SimpleImputer` class with `strategy='constant'` to fill missing values with a user-defined constant.  
**Formula**: N/A  
**Example**:  
```python
# Using Scikit-learn's SimpleImputer
imputer = SimpleImputer(strategy='constant', fill_value=99)
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## Verification of Imputation
**Definition**: Checking for the absence of missing values post-imputation.  
**Formula**: N/A  
**Example**:  
```python
# Confirming no missing values remain
X_train[['A2','A3', 'A8', 'A11']].isnull().sum()
```

---

---

## 2026-06-17 10:12 — Practical 2.5 - Capturing-missing-values-in-a-bespoke-category.ipynb
**Style:** structured_academic (experimenting)

### Summary: Bespoke Category Imputation

#### Term: [[Bespoke Category Imputation]]  
**Definition**: A strategy for handling missing values in categorical variables by replacing them with a user-defined category (e.g., "Missing"). This treats missingness as a distinct group, preserving its potential informational value.  

**Formula**: N/A (categorical replacement strategy)  

**Examples**:  
1. **Pandas Implementation**:  
   ```python  
   for var in ['A4', 'A5', 'A6', 'A7']:  
       X_train[var] = X_train[var].fillna('Missing')  
       X_test[var] = X_test[var].fillna('Missing')  
   ```  
2. **Scikit-learn (`SimpleImputer`)**:  
   ```python  
   imputer = SimpleImputer(strategy='constant', fill_value='Missing')  
   X_train = imputer.fit_transform(X_train)  
   X_test = imputer.transform(X_test)  
   ```  
3. **Feature-engine (`CategoricalImputer`)**:  
   ```python  
   imputer = CategoricalImputer(variables=['A4', 'A5', 'A6', 'A7'])  
   X_train = imputer.fit_transform(X_train)  
   X_test = imputer.transform(X_test)  
   ```  

---

#### Term: [[SimpleImputer (Constant Strategy)]]  
**Definition**: Scikit-learn’s `SimpleImputer` with `strategy='constant'` allows users to fill missing values with a predefined constant (e.g., "Missing").  

**Formula**:  
$$ \text{Imputed Value} = \text{fill\_value} \quad \text{(user-specified constant)} $$  

**Example**:  
```python  
imputer = SimpleImputer(strategy='constant', fill_value='Missing')  
imputer.fit(X_train)  
X_train = imputer.transform(X_train)  
```  

---

#### Term: [[CategoricalImputer (Feature-engine)]]  
**Definition**: Feature-engine’s `CategoricalImputer` is designed to replace missing values in categorical variables with a specified category (e.g., "Missing"), learned from the training data.  

**Formula**: N/A (applies predefined category)  

**Example**:  
```python  
imputer = CategoricalImputer(variables=['A4', 'A5', 'A6', 'A7'])  
imputer.fit(X_train)  
X_train = imputer.transform(X_train)  
```  

---

#### Term: [[Pandas `fillna()` for Imputation]]  
**Definition**: Pandas’ `fillna()` method is used to replace missing values in DataFrame columns with a specified value (e.g., "Missing").  

**Formula**: N/A (direct value replacement)  

**Example**:  
```python  
X_train["A4"] = X_train["A4"].fillna('Missing')  
X_test["A4"] = X_test["A4"].fillna('Missing')  
```  

---

### Related Concepts  
- [[Missing Data Imputation]]  
- [[Categorical Variables]]  
- [[Scikit-learn]]  
- [[Feature-engine]]  
- [[Pandas]]  

This summary integrates methods for handling missing categorical data using bespoke categories, with implementations across pandas, scikit-learn, and Feature-engine.

---

---

## 2026-06-17 10:18 — Practical 2.6 - Replacing-missing-values-by-a-value-at-the-end-of-the-distribution.ipynb
**Style:** structured_academic (experimenting)

## Summary: End Tail Imputation and Interquartile Range (IQR)

### [[End Tail Imputation]]
| **Term**               | **Definition**                                                                 | **Formula**                                                                 | **Example**                                                                 |
|-------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **End Tail Imputation** | A method to replace missing values with a value at the end of the variable distribution. For normally distributed data, values are derived from mean ± 3σ. For non-normal data, the inter-quartile range (IQR) proximity rule is used. | - Right tail: \( Q3 + 1.5 \times \text{IQR} \) <br> - Left tail: \( Q1 - 1.5 \times \text{IQR} \) | Using `EndTailImputer` from Feature-engine: <br> `imputer = EndTailImputer(imputation_method='iqr', tail='right', variables=['A2', 'A3', 'A8', 'A11', 'A15'])` |

---

### [[Interquartile Range (IQR)]]
| **Term**               | **Definition**                                                                 | **Formula**                                                                 | **Example**                                                                 |
|-------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Interquartile Range (IQR)** | A measure of statistical dispersion, representing the range between the first quartile (Q1) and third quartile (Q3) of a dataset. | \( \text{IQR} = Q3 - Q1 \) | Calculating IQR for variable 'A2': <br> `IQR = X_train['A2'].quantile(0.75) - X_train['A2'].quantile(0.25)` |

---

### Key Concepts and Workflow
1. **Data Splitting**:  
   - The dataset is split into training (70%) and testing (30%) sets using `train_test_split` with `random_state=0`.  
   - Example: `X_train, X_test, y_train, y_test = train_test_split(data.drop('A16', axis=1), data['A16'], test_size=0.3, random_state=0)`.

2. **Handling Missing Values**:  
   - **Pandas Approach**: Missing values in numerical variables (e.g., 'A2', 'A3') are replaced using the IQR proximity rule.  
     Example: `X_train[var].fillna(X_train[var].quantile(0.75) + 1.5 * IQR, inplace=True)`.  
   - **Feature-engine Approach**: The `EndTailImputer` transformer automates imputation, storing parameters from the training set for consistency.  

3. **Validation**:  
   - Missing values are verified post-imputation using `isnull().mean()` or `isnull().sum()`.  

This structured approach ensures robust handling of missing data while maintaining consistency across training, testing, and future datasets.

---

---

## 2026-06-17 10:24 — Practical 2.7 - Implementing-random-sample-imputation.ipynb
**Style:** structured_academic (experimenting)

# Summary: Random Sample Imputation  

## [[Random Sample Imputation]]  
**Definition**: A technique that replaces missing values by randomly sampling from the observed values in the dataset, preserving the original data distribution. Suitable for both numerical and categorical variables.  

**Formula**:  
For a variable with *n* missing values:  
1. Extract a random sample of size *n* from the observed data.  
2. Assign this sample to the missing value positions.  

**Example**:  
```python  
# Using pandas  
number_missing = X_train['A2'].isnull().sum()  
random_sample = X_train['A2'].dropna().sample(number_missing, random_state=0)  
X_train.loc[X_train['A2'].isnull(), 'A2'] = random_sample.values  
```  

---

## [[Pandas Implementation]]  
**Definition**: Manual implementation of random sample imputation using pandas functions to handle missing data.  

**Formula**:  
1. Calculate missing values per variable.  
2. Sample observed data to match the number of missing values.  
3. Reindex the sample to align with missing positions.  
4. Replace missing values in both training and test sets.  

**Example**:  
```python  
for var in ['A1', 'A3', 'A4']:  
    # Train set  
    sample_train = X_train[var].dropna().sample(X_train[var].isnull().sum(), random_state=0)  
    sample_train.index = X_train[X_train[var].isnull()].index  
    X_train.loc[X_train[var].isnull(), var] = sample_train.values  
    # Repeat for test set  
```  

---

## [[Feature-engine Implementation]]  
**Definition**: Uses the `RandomSampleImputer` class from the `feature_engine` library to streamline the imputation process.  

**Formula**:  
1. Fit the imputer on the training data to learn the sampling distribution.  
2. Transform both training and test sets to replace missing values.  

**Example**:  
```python  
from feature_engine.imputation import RandomSampleImputer  
imputer = RandomSampleImputer()  
imputer.fit(X_train)  
X_train = imputer.transform(X_train)  
X_test = imputer.transform(X_test)  
```  

---

## Key Links  
- [[Missing Data]]: Absence of values in a dataset.  
- [[Imputation Techniques]]: Methods to replace missing data (e.g., mean, median, mode).  
- [[SimpleImputer]]: Scikit-learn’s basic imputation tool.  
- [[Data Preprocessing]]: General steps for preparing data for analysis.  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).

---

---

## 2026-06-17 10:28 — Practical 2.8 - Adding-a-missing-value-indicator-variable.ipynb
**Style:** structured_academic (experimenting)

# Summary: Adding Missing Value Indicator Variables

## [[Missing Value Indicator]]
### Definition
A binary variable that flags whether an observation originally had a missing value (1) for the respective feature or not (0). It preserves information about missingness, which can be informative for downstream models.

### Formula
Binary assignment:  
$$
\text{Indicator} = 
\begin{cases} 
1 & \text{if original value was missing} \\
0 & \text{otherwise}
\end{cases}
$$

### Example (Pandas Implementation)
```python
# Using NumPy to create indicators for specified columns
for var in ['A1', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']:
    X_train[var+'_NA'] = np.where(X_train[var].isnull(), 1, 0)
    X_test[var+'_NA'] = np.where(X_test[var].isnull(), 1, 0)
```

---

## [[Pandas Implementation]]
### Definition
Manual creation of missing indicators using Pandas and NumPy for specified columns.

### Formula
`np.where(condition, value_if_true, value_if_false)`  
- **Condition**: `X_train[var].isnull()`  
- **Value if true**: `1` (missing)  
- **Value if false**: `0` (not missing)

### Example
```python
# Check alignment between missing rate and indicator mean
X_train['A3'].isnull().mean(), X_train['A3_NA'].mean()
# Output: (0.05, 0.05)  # Example alignment
```

---

## [[Feature-engine Implementation]]
### Definition
Using the `AddMissingIndicator` class from the **Feature-engine** library to automate indicator creation.

### Formula
1. Initialize imputer: `imputer = AddMissingIndicator()`  
2. Fit to training data: `imputer.fit(X_train)`  
3. Transform data: `X_train = imputer.transform(X_train)`

### Example
```python
imputer = AddMissingIndicator()
imputer.fit(X_train)
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)
```

---

## [[Scikit-learn Implementation]]
### Definition
Using `MissingIndicator` from **Scikit-learn** to generate indicators, requiring manual concatenation with the original dataset.

### Formula
1. Initialize indicator: `indicator = MissingIndicator()`  
2. Fit to training data: `indicator.fit(X_train)`  
3. Transform data: `indicator.transform(X_train)`  
4. Concatenate indicators to original data.

### Example
```python
indicator = MissingIndicator()
indicator.fit(X_train)
indicator_cols = [c+'_NA' for c in X_train.columns[indicator.features_]]
X_train = pd.concat([
    X_train.reset_index(),
    pd.DataFrame(indicator.transform(X_train), columns=indicator_cols)
], axis=1)
```

---

## Key Considerations
- **Purpose**: Combines with imputation methods (e.g., [[Mean Imputation]], [[Median Imputation]]) to retain information about missingness.
- **Best Practice**: Always fit the imputer/indicator on the **training set** to avoid data leakage.
- **Libraries**: [[Feature-engine]] and [[Scikit-learn]] provide streamlined implementations compared to manual Pandas approaches.

---

---

## 2026-06-17 10:31 — Practical 2.9 - Assembling-an-imputation-pipeline-with-Scikit-learn.ipynb
**Style:** structured_academic (experimenting)

Here's a structured summary of the content using the requested format:

---

### [[Imputation Pipeline]]
**Definition**: A sequence of data preprocessing steps designed to handle missing values in a dataset using different strategies for various feature types.  
**Formula**: N/A (process-oriented concept)  
**Example**:  
```python
preprocessor = ColumnTransformer([...])
preprocessor.fit(X_train)
X_train = preprocessor.transform(X_train)
```

---

### [[ColumnTransformer]]
**Definition**: A scikit-learn class that applies different column-specific transformers to subsets of data features.  
**Formula**: N/A (structural component)  
**Example**:  
```python
preprocessor = ColumnTransformer(
    transformers=[
        ('imp_num_arbitrary', imputer_num_arbitrary, features_num_arbitrary),
        ('imp_num_median', imputer_num_median, features_num_median)
    ]
)
```

---

### [[SimpleImputer]]
**Definition**: A scikit-learn class for filling missing values using specified strategies.  
**Formula**:  
- For numerical: \( \text{Imputed value} = \begin{cases} 
  \text{median}(X) & \text{if strategy='median'} \\
  c & \text{if strategy='constant'} 
\end{cases} \)  
- For categorical: \( \text{Imputed value} = \text{mode}(X) \) (most frequent)  
**Example**:  
```python
imputer_num_median = Pipeline([('imputer', SimpleImputer(strategy='median'))])
```

---

### [[Constant Imputation]]
**Definition**: Replaces missing values with a user-defined constant.  
**Formula**: \( \text{Imputed value} = c \) (where \( c \) is the specified constant)  
**Example**:  
```python
SimpleImputer(strategy='constant', fill_value=99)
```

---

### [[Median Imputation]]
**Definition**: Replaces missing values with the median of the observed data.  
**Formula**: \( \text{Median} = \text{middle value of sorted observations} \)  
**Example**:  
```python
SimpleImputer(strategy='median')
```

---

### [[Most Frequent Imputation]]
**Definition**: Replaces missing values with the most frequent category or value.  
**Formula**: \( \text{Mode} = \text{most frequently occurring value} \)  
**Example**:  
```python
SimpleImputer(strategy='most_frequent')
```

---

### [[Feature Engineering]]
**Definition**: The process of transforming raw data into features suitable for modeling.  
**Formula**: N/A (broad concept)  
**Example**:  
```python
features_num_arbitrary = ['A3', 'A8']  # Custom feature grouping
```

---

### [[Pipeline (scikit-learn)]]
**Definition**: Chains multiple preprocessing steps or models into a single unit.  
**Formula**: N/A (methodological concept)  
**Example**:  
```python
imputer_num_arbitrary = Pipeline([('imputer', SimpleImputer(...))])
```

---

### Key Workflow Steps:
1. **Data Splitting**: `train_test_split` for training/testing sets.  
2. **Feature Categorization**: Separate numerical/categorical features.  
3. **Imputer Initialization**: Define strategies for specific feature groups.  
4. **ColumnTransformer Assembly**: Combine imputers for parallel execution.  
5. **Fit/Transform**: Apply pipeline to training/test data.  

All concepts are interconnected through [[Feature Engineering]] and [[Imputation Pipeline]] design.

---

---

## 2026-06-17 10:37 — Practical 7.1 - Standardization.ipynb
**Style:** structured_academic (experimenting)

### Standardization (Z-score normalization)  
**Definition**: A method to rescale features by subtracting the mean and dividing by the standard deviation, resulting in a distribution centered at 0 with unit variance. This ensures features contribute equally to model training and improves convergence in algorithms like neural networks.  

**Formula**:  
\[
z = \frac{x - \mu}{\sigma}
\]  
where \( z \) is the standardized value, \( x \) is the original value, \( \mu \) is the mean, and \( \sigma \) is the standard deviation.  

**Example**:  
```python
from sklearn.preprocessing import StandardScaler  

# Initialize scaler  
scaler = StandardScaler()  

# Fit to training data and transform  
X_train_scaled = scaler.fit_transform(X_train)  

# Apply same transformation to test data  
X_test_scaled = scaler.transform(X_test)  
```  
This code uses `StandardScaler` to standardize features. The scaler computes mean (`scaler.mean_`) and standard deviation (`scaler.scale_`) from the training set and applies the same transformation to the test set to prevent data leakage.  

**Visualization Insight**:  
After standardization, distributions are centered at 0 but retain their original shape (e.g., skewed or Gaussian). This is verified using kernel density plots (`sns.kdeplot`) comparing distributions before and after scaling.  

**Key Notes**:  
- **Why Standardize?** Prevents features with larger scales from dominating the model.  
- **Wikilinks**: [[Z-score]], [[Feature Scaling]], [[Data Preprocessing]]  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)

---

---

## 2026-06-17 10:45 — Practical 7.2 - Mean-normalization.ipynb
**Style:** structured_academic (experimenting)

# Summary: Mean Normalization in Data Preprocessing

## [[Mean Normalization]]
**Definition**: A technique to rescale features by centering data at zero and adjusting the range to [-1, 1] using the formula:  
**Formula**:  
\[ x_{\text{scaled}} = \frac{x - \text{mean}(x)}{\text{max}(x) - \text{min}(x)} \]  
**Example**:  
```python
X_train_scaled = (X_train - means) / ranges
X_test_scaled = (X_test - means) / ranges  # Code Cell 8
```

---

## [[Training Set]]
**Definition**: Subset of data used to compute scaling parameters (e.g., mean, range) for normalization.  
**Example**:  
```python
X_train, X_test, y_train, y_test = train_test_split(...)  # Code Cell 4
means = X_train.mean(axis=0)  # Code Cell 5
ranges = X_train.max(axis=0) - X_train.min(axis=0)  # Code Cell 6
```

---

## [[Test Set]]
**Definition**: Subset of data used for evaluation, scaled using parameters derived from the training set.  
**Example**:  
```python
X_test_scaled = (X_test - means) / ranges  # Code Cell 8
```

---

## [[Value Range]]
**Definition**: The difference between the maximum and minimum values of a feature.  
**Formula**:  
\[ \text{range}(x) = \text{max}(x) - \text{min}(x) \]  
**Example**:  
```python
ranges = X_train.max(axis=0) - X_train.min(axis=0)  # Code Cell 6
```

---

## [[Centering Data]]
**Definition**: Adjusting data by subtracting the mean to center the distribution at zero.  
**Formula**:  
\[ x_{\text{centered}} = x - \text{mean}(x) \]  
**Example**:  
```python
(X_train - means)  # Part of Code Cell 8
```

---

## [[Kernel Density Estimate (KDE) Plot]]
**Definition**: A statistical visualization tool to compare distributions before and after scaling.  
**Example**:  
```python
sns.kdeplot(X_train['RM'], ax=ax1, label='RM')  # Code Cells 13 & 14
```

---

## [[Feature Scaling]]
**Definition**: General process of standardizing the range of features to improve model performance.  
**Example**:  
Mean normalization implemented in Code Cell 8, visualized in Code Cells 13–14.

---

**Key Concepts**:  
- Mean normalization ensures features are on a comparable scale.  
- Parameters (mean, range) are learned from the **training set** to avoid data leakage.  
- **KDE plots** validate the effectiveness of scaling by showing distribution shifts.

---

---

## 2026-06-17 11:02 — Practical 7.3 - MinMaxScaling.ipynb
**Style:** structured_academic (experimenting)

# Summary: Min-Max Scaling and Data Transformation

## [[MinMax Scaling]]  
**Definition**: A feature scaling technique that rescales data to a fixed range, typically [0, 1], by subtracting the minimum value and dividing by the range (max - min).  
**Formula**:  
\[ x_{\text{scaled}} = \frac{x - \min(x)}{\max(x) - \min(x)} \]  
**Example**:  
Applied to the Boston Housing dataset to normalize features like `RM` (average number of rooms) and `LSTAT` (percentage of lower status population).  

---

## [[MinMaxScaler (Scikit-learn)]]  
**Definition**: A class in `sklearn.preprocessing` used to implement Min-Max scaling. It learns scaling parameters (min, max) from the training data and applies them to both training and test sets.  
**Attributes**:  
- `data_max_`: Maximum values of each feature (learned from training data).  
- `min_`: Minimum values of each feature.  
- `data_range_`: Range (max - min) of each feature.  
**Example**:  
```python  
from sklearn.preprocessing import MinMaxScaler  
scaler = MinMaxScaler()  
scaler.fit(X_train)  # Learns parameters  
X_train_scaled = scaler.transform(X_train)  # Scales training data  
X_test_scaled = scaler.transform(X_test)     # Scales test data  
```  

---

## [[Data Transformation (NumPy to DataFrame)]]  
**Definition**: Conversion of scaled NumPy arrays (output of `MinMaxScaler.transform`) into pandas DataFrames to preserve feature names and structure.  
**Example**:  
```python  
# Convert scaled arrays to DataFrames  
X_train_scaled = pd.DataFrame(scaler.transform(X_train), columns=X_train.columns)  
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)  
```  

---

## [[Distribution Visualization (KDE Plots)]]  
**Definition**: Use of Kernel Density Estimation (KDE) plots to compare feature distributions before and after scaling. This visualizes the impact of scaling on data spread and shape.  
**Example**:  
```python  
import matplotlib.pyplot as plt  
import seaborn as sns  

# Compare distributions of 'RM', 'LSTAT', and 'CRIM'  
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))  
sns.kdeplot(X_train['RM'], ax=ax1, label='RM (Before)')  
sns.kdeplot(X_train_scaled['RM'], ax=ax2, label='RM (After)')  
ax1.set_title('Before Scaling')  
ax2.set_title('After Scaling')  
plt.show()  
```  

---

## Key Concepts Linked  
- [[Feature Scaling]]: General term for techniques like Min-Max Scaling and Standardization.  
- [[Scikit-learn]]: Library providing implementations of scaling methods (e.g., `MinMaxScaler`).  
- [[Data Preprocessing]]: Broader category including scaling, transformation, and visualization.

---

---

## 2026-06-17 11:07 — Practical 7.4 - Maximum-Absolute-Scaling.ipynb
**Style:** structured_academic (experimenting)

Here's a structured summary of the content using the requested academic format:

---

### [[Maximum Absolute Scaling]]  
**Definition**: A data scaling technique that normalizes features by dividing each value by the maximum absolute value of that feature, resulting in values within the range [-1, 1]. Recommended for zero-centered or sparse data.  
**Formula**:  
\[ x_{\text{scaled}} = \frac{x}{\max(|x|)} \]  
**Example**:  
```python
from sklearn.preprocessing import MaxAbsScaler
scaler = MaxAbsScaler()
X_train_scaled = scaler.fit_transform(X_train)
```

---

### [[StandardScaler]] (Centering)  
**Definition**: A scaler that removes the mean (centers data at zero) but does not scale by standard deviation when configured appropriately. Used here as a preprocessing step before maximum absolute scaling.  
**Formula**:  
\[ x_{\text{centered}} = x - \mu \]  
where \( \mu \) is the mean of the feature.  
**Example**:  
```python
from sklearn.preprocessing import StandardScaler
scaler_mean = StandardScaler(with_mean=True, with_std=False)
X_centered = scaler_mean.fit_transform(X_train)
```

---

### [[Centering (Data Preprocessing)]]  
**Definition**: The process of subtracting the mean value from a dataset to ensure it is centered at zero, often used before applying scaling techniques like maximum absolute scaling.  
**Formula**: Same as [[StandardScaler]] (centering).  
**Example**: Combining centering with maximum absolute scaling:  
```python
X_train_scaled = scaler_maxabs.transform(scaler_mean.transform(X_train))
```

---

### [[Kernel Density Estimation (KDE)]]  
**Definition**: A non-parametric way to estimate the probability density function of a variable, used here to visualize the distribution of features before and after scaling.  
**Formula**:  
\[ \hat{f}(x) = \frac{1}{n h} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right) \]  
where \( K \) is the kernel function and \( h \) is the bandwidth.  
**Example**:  
```python
import seaborn as sns
sns.kdeplot(X_train['RM'], label='Before Scaling')
sns.kdeplot(X_train_scaled['RM'], label='After Scaling')
```

---

### Key Workflow Integration  
**Definition**: The process of combining centering and scaling for optimal data transformation.  
**Formula**: Sequential application of centering followed by maximum absolute scaling.  
**Example**:  
```python
# Center data
X_centered = StandardScaler(with_mean=True, with_std=False).fit_transform(X_train)
# Apply maximum absolute scaling
X_scaled = MaxAbsScaler().fit_transform(X_centered)
```

---

This summary connects data preprocessing techniques, their mathematical foundations, and practical implementations using Python. Use [[Wikilinks]] to explore related concepts like [[Feature Scaling]], [[Data Standardization]], or [[Probability Density Plots]].

---

---

## 2026-06-17 11:13 — Practical 7.5 - Robust-Scaling.ipynb
**Style:** structured_academic (experimenting)

# Summary: Robust Scaling and Related Concepts

## [[Robust Scaling]]  
**Definition**: A data preprocessing technique that transforms features by removing the median and scaling by the interquartile range (IQR). It is robust to outliers compared to mean-based scaling methods.  
**Formula**:  
\[
x_{\text{scaled}} = \frac{x - \text{median}(x)}{\text{IQR}} = \frac{x - \text{median}(x)}{Q3 - Q1}
\]  
**Example**:  
In the provided code, `RobustScaler` from scikit-learn is applied to the Boston Housing dataset. After fitting to the training data, features like `RM`, `LSTAT`, and `CRIM` are transformed to reduce the impact of outliers.  

---

## [[Median]]  
**Definition**: The middle value of a sorted dataset. If the dataset has an even number of observations, it is the average of the two middle values.  
**Formula**:  
For a sorted dataset \( x_1, x_2, \ldots, x_n \):  
- If \( n \) is odd: \( \text{median} = x_{(n+1)/2} \)  
- If \( n \) is even: \( \text{median} = \frac{x_{n/2} + x_{n/2 + 1}}{2} \)  
**Example**:  
The `RobustScaler` stores the median of each feature in the `center_` attribute (e.g., `scaler.center_` retrieves medians for `RM`, `LSTAT`, etc.).  

---

## [[Interquartile Range (IQR)]]  
**Definition**: The range between the first quartile (Q1, 25th percentile) and the third quartile (Q3, 75th percentile), representing the spread of the central 50% of the data.  
**Formula**:  
\[
\text{IQR} = Q3 - Q1
\]  
**Example**:  
In the code, the `scale_` attribute of `RobustScaler` stores the IQR for each feature (e.g., `scaler.scale_` returns IQR values for `AGE`, `DIS`, etc.).  

---

## [[RobustScaler]]  
**Definition**: A scikit-learn class that implements robust scaling using median and IQR. It is less sensitive to outliers than `StandardScaler`.  
**Key Parameters**:  
- No parameters required for default implementation.  
**Example**:  
```python
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
scaler.fit(X_train)  # Learns medians and IQRs
X_train_scaled = scaler.transform(X_train)  # Applies scaling
```  

---

## [[Boston Housing Dataset]]  
**Definition**: A classic dataset used for regression tasks, containing features like crime rate (`CRIM`), room size (`RM`), and pollution levels (`NOX`) to predict house prices (`MEDV`).  
**Example**:  
The dataset is loaded and split into training/testing sets in the code:  
```python
data = pd.read_csv("./data/boston_local.csv")
X_train, X_test, y_train, y_test = train_test_split(data.drop('MEDV', axis=1), data['MEDV'], test_size=0.3, random_state=0)
```  

---

## Visualization of Scaled Data  
**Example**:  
Kernel Density Estimation (KDE) plots compare feature distributions before and after scaling:  
```python
sns.kdeplot(X_train['RM'], label='Before Scaling')
sns.kdeplot(X_train_scaled['RM'], label='After Robust Scaling')
```  
This visualizes the effect of robust scaling on reducing outlier influence.  

--- 

**Related Concepts**:  
- [[Standardization]] (mean = 0, std = 1)  
- [[Min-Max Scaling]] (scales to a fixed range, e.g., [0, 1])  
- [[Data Preprocessing]] (general category for scaling techniques)

---

---

## 2026-06-17 11:16 — Practical 8.1 - Add-Multiply-Features.ipynb
**Style:** structured_academic (experimenting)

# Structured Academic Summary: Statistical Feature Engineering Operations

## [[Feature Engineering]]  
**Definition**: The process of creating new features from existing data to enhance machine learning model performance by applying mathematical or statistical operations.  
**Formula**: N/A (General concept)  
**Example**: Engineering new features like `added_features`, `prod_features`, etc., from existing columns in the breast cancer dataset.

---

## [[Summation]]  
**Definition**: The addition of values across selected features for each row in a dataset.  
**Formula**:  
\[ \text{Sum} = \sum_{i=1}^{n} x_i \]  
**Example**:  
```python
df['added_features'] = df[features].sum(axis=1)
```  
Creates a new column `added_features` by summing values across `features` for each row.

---

## [[Product]]  
**Definition**: The multiplication of values across selected features for each row.  
**Formula**:  
\[ \text{Product} = \prod_{i=1}^{n} x_i \]  
**Example**:  
```python
df['prod_features'] = df[features].prod(axis=1)
```  
Generates `prod_features` by multiplying values across `features` per row.

---

## [[Mean (Average)]]  
**Definition**: The average value of selected features for each row.  
**Formula**:  
\[ \text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n} \]  
**Example**:  
```python
df['mean_features'] = df[features].mean(axis=1)
```  
Computes `mean_features` as the average of `features` per row.

---

## [[Standard Deviation]]  
**Definition**: Measures the dispersion of values across features for each row.  
**Formula**:  
\[ \sigma = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}} \]  
(where \(\mu\) is the mean)  
**Example**:  
```python
df['std_features'] = df[features].std(axis=1)
```  
Calculates `std_features` using pandas' default sample standard deviation (divided by \(n-1\)).

---

## [[Maximum]]  
**Definition**: The highest value among selected features for each row.  
**Formula**:  
\[ \text{Max} = \max(x_1, x_2, \dots, x_n) \]  
**Example**:  
```python
df['max_features'] = df[features].max(axis=1)
```  
Extracts `max_features` as the maximum value across `features` per row.

---

## [[Minimum]]  
**Definition**: The lowest value among selected features for each row.  
**Formula**:  
\[ \text{Min} = \min(x_1, x_2, \dots, x_n) \]  
**Example**:  
```python
df['min_features'] = df[features].min(axis=1)
```  
Derives `min_features` as the minimum value across `features` per row.

---

## Aggregation of Multiple Operations  
**Definition**: Combining multiple statistical operations into a single step.  
**Formula**: N/A  
**Example**:  
```python
df_t = df[features].agg(['sum', 'prod', 'mean', 'std', 'max', 'min'], axis='columns')
```  
Applies all operations simultaneously using pandas' `agg()` function.

---

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)

---

---

## 2026-06-17 11:18 — Practical 8.2 - Substraction-Quotient-Features.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### **Feature Engineering with Mathematical Operations**

#### **1. Subtraction of Features**  
**Definition**: Creating a new feature by subtracting one numerical feature from another to derive meaningful differences (e.g., disposable income = income - debt).  
**Formula**:  
\[ \text{New Feature} = F_1 - F_2 \]  
**Example**:  
```python  
# Code Cell 6 & 7  
df['difference'] = df['worst compactness'].sub(df['mean compactness'])  
# or  
df['difference'] = df['worst compactness'] - df['mean compactness']  
```  
Visualized using a violin plot to compare differences across target classes.

---

#### **2. Division of Features**  
**Definition**: Generating a ratio-based feature by dividing one feature by another (e.g., debt-to-income ratio = total debt / total income).  
**Formula**:  
\[ \text{New Feature} = \frac{F_1}{F_2} \]  
**Example**:  
```python  
# Code Cell 9 & 10  
df['quotient'] = df['worst radius'].div(df['mean radius'])  
# or  
df['quotient'] = df['worst radius'] / df['mean radius']  
```  
Visualized using a violin plot to analyze quotient distributions.

---

#### **3. Aggregation of Features**  
**Definition**: Combining multiple features into a single value using statistical operations (e.g., summing "worst" features to create a composite metric).  
**Formula**:  
\[ \text{Aggregated Feature} = \sum_{i=1}^{n} F_i \]  
**Example**:  
```python  
# Code Cell 13  
df['worst'] = df[['worst smoothness', 'worst compactness', ...]].sum(axis=1)  
```  

---

#### **4. Ratio Calculation with Multiple Features**  
**Definition**: Deriving ratios by dividing multiple features against a reference feature (e.g., comparing mean features to an aggregated "worst" feature).  
**Formula**:  
\[ \text{Ratio Feature} = \frac{F_{\text{mean}}}{F_{\text{reference}}} \]  
**Example**:  
```python  
# Code Cell 15  
df[['mean smoothness', 'mean compactness', ...]].div(df['worst'], axis=0)  
```  

---

### **Key Concepts**  
- **[[Feature Engineering]]**: Process of creating new features from raw data to improve model performance.  
- **[[Mathematical Operations]]**: Includes subtraction, division, and aggregation for deriving insights.  
- **[[Reference Variable]]**: A base feature (e.g., "worst" aggregate) against which other features are compared.  

---

### **Visualization**  
- **Violin Plots**: Used to visualize distributions of new features (e.g., `difference`, `quotient`) across target classes.  

---

This summary aligns with the notebook's focus on using pandas for feature engineering via mathematical operations and aggregation. Related concepts like [[Outlier Detection]] (from prior examples) may also apply in preprocessing.

---

---

## 2026-06-17 11:25 — Practical 8.3 - PolynomialExpansion.ipynb
**Style:** structured_academic (experimenting)

```markdown
# Polynomial Feature Engineering Summary

## Polynomial Expansion
**Definition**: The process of generating new features by raising existing features to polynomial powers (e.g., squaring, cubing) or creating interaction terms between different features. This captures non-linear relationships and feature interactions.
**Formula**: For features \( x_1, x_2 \), examples include \( x_1^2 \), \( x_1^3 \), \( x_1x_2 \), \( x_1^2x_2 \), etc.
**Example**: Creating \( x^2 \) to model a quadratic relationship between \( x \) and the target variable \( y \), improving linear model performance.

## PolynomialFeatures
**Definition**: A scikit-learn transformer class used to automatically generate polynomial features from input data up to a specified degree.
**Formula**: N/A (method-based)
**Example**: 
```python
poly = PolynomialFeatures(degree=3, interaction_only=False, include_bias=False)
```
Generates all polynomial terms up to degree 3, including interactions and higher powers.

## Polynomial Degree
**Definition**: The highest exponent in the polynomial expansion. A degree \( d \) includes all terms where the sum of exponents across features is ≤ \( d \).
**Formula**: For \( d = 3 \), terms include \( x_1^3 \), \( x_1^2x_2 \), \( x_1x_2^2 \), etc.
**Example**: Setting `degree=3` in `PolynomialFeatures` to capture cubic relationships.

## Interaction-only Features
**Definition**: Features created by multiplying different base features (cross-product terms), excluding higher powers of individual features.
**Formula**: \( x_i x_j \) for \( i \neq j \).
**Example**: Using `interaction_only=True` to generate terms like \( \text{LSTAT} \times \text{RM} \).

## Bias Term
**Definition**: A constant feature (always 1) added to each sample to enable the model to learn an intercept term.
**Formula**: \( 1 \)
**Example**: Including a bias term via `include_bias=True` in `PolynomialFeatures`.

## Feature Transformation
**Definition**: The application of polynomial expansion to a dataset to derive new features.
**Formula**: N/A
**Example**: 
```python
train_t = poly.transform(X_train[['LSTAT', 'RM', 'NOX']])
```
Generates polynomial features for the training set.

## Feature Naming
**Definition**: The labeling of generated polynomial features with names reflecting their mathematical form (e.g., `LSTAT^2`, `LSTAT RM`).
**Formula**: N/A
**Example**: Using `poly.get_feature_names_out()` to retrieve descriptive names for transformed features.

## Correlation Analysis
**Definition**: Examining the linear relationships between features using statistical measures like Pearson correlation.
**Formula**: Pearson correlation coefficient \( r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}} \)
**Example**: Visualizing correlations with a heatmap via `sns.heatmap(data.corr())`.

## Train-Test Split
**Definition**: Dividing data into training and testing subsets to evaluate model performance.
**Formula**: N/A
**Example**: 
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
```
Splits data with 30% for testing.

## Feature-Target Visualization
**Definition**: Plotting individual features against the target variable to identify patterns or relationships.
**Formula**: N/A
**Example**: 
```python
plt.scatter(X_train['LSTAT'], y_train)
```
Visualizes the relationship between `LSTAT` and house prices (`MEDV`).
```

---

---

## 2026-06-17 11:31 — Practical 8.4 - PCA.ipynb
**Style:** structured_academic (experimenting)

# Summary: Principal Component Analysis (PCA)

## [[Principal Component Analysis (PCA)]]
**Definition**: A dimensionality reduction technique that transforms a high-dimensional dataset into a smaller set of orthogonal (uncorrelated) principal components (PCs), which capture the maximum variance in the data.  
**Formula**:  
PCA involves eigenvalue decomposition of the covariance (or correlation) matrix of the standardized data. The PCs are the eigenvectors, and the eigenvalues represent the variance explained by each PC:  
\[
\text{Cov}(X_{\text{scaled}}) = V \Lambda V^T
\]  
where \(V\) is the matrix of eigenvectors (PCs) and \(\Lambda\) is the diagonal matrix of eigenvalues.  
**Example**:  
In the provided code, PCA is implemented using `sklearn.decomposition.PCA` on the Boston Housing dataset after standardization:  
```python
pca = PCA()
pca.fit(X_train_scaled)  # Training PCA on scaled data
train_t = pca.transform(X_train_scaled)  # Projecting data onto PCs
```

---

## [[Principal Components (PCs)]]
**Definition**: Linear combinations of the original features that are orthogonal to each other and sequentially maximize the variance in the data.  
**Formula**:  
The \(i\)-th principal component is given by:  
\[
\text{PC}_i = w_{i1}X_1 + w_{i2}X_2 + \dots + w_{in}X_n
\]  
where \(w_{i1}, \dots, w_{in}\) are the eigenvectors (weights) from the covariance matrix.  
**Example**:  
After fitting PCA, the transformed data `train_t` and `test_t` represent the original data projected onto the principal components.

---

## [[Explained Variance Ratio]]
**Definition**: The proportion of variance in the data explained by each principal component, often used to determine the optimal number of PCs to retain.  
**Formula**:  
\[
\text{Explained Variance Ratio}_i = \frac{\lambda_i}{\sum_{j=1}^n \lambda_j}
\]  
where \(\lambda_i\) is the eigenvalue corresponding to the \(i\)-th PC.  
**Example**:  
The code extracts and visualizes the explained variance ratio:  
```python
print(pca.explained_variance_ratio_)  # Output: Array of variance ratios
plt.plot(pca.explained_variance_ratio_, linewidth=2)  # Plotting variance decay
```

---

## [[Standardization]]
**Definition**: A preprocessing step that centers the data (mean = 0) and scales it to unit variance (std = 1), ensuring PCA is not dominated by features with large scales.  
**Formula**:  
\[
z = \frac{x - \mu}{\sigma}
\]  
where \(\mu\) is the mean and \(\sigma\) is the standard deviation.  
**Example**:  
The code uses `StandardScaler` to standardize the training and test sets:  
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## [[Orthogonality in PCA]]
**Definition**: The property that all principal components are mutually orthogonal (perpendicular), meaning their covariance is zero.  
**Formula**:  
For two distinct PCs \( \text{PC}_i \) and \( \text{PC}_j \):  
\[
\text{Cov}(\text{PC}_i, \text{PC}_j) = 0 \quad \text{for} \quad i \neq j
\]  
**Example**:  
Orthogonality ensures that the transformed data `train_t` has uncorrelated columns, as seen in the PCA output.

---

## [[Variance Maximization]]
**Definition**: The principle that the first PC captures the maximum variance in the data, with subsequent PCs capturing the largest remaining variance under the constraint of orthogonality.  
**Formula**:  
The optimization problem for the first PC is:  
\[
\max_{\mathbf{w}} \mathbf{w}^T \Sigma \mathbf{w}
\]  
subject to \(\mathbf{w}^T \mathbf{w} = 1\), where \(\Sigma\) is the covariance matrix.  
**Example**:  
The plot of explained variance ratios (Code Cell 12) illustrates the decay in variance captured by each subsequent PC, guiding the selection of components.

---

---

## 2026-06-17 11:34 — Practical 5.1 - Equal-width-discretization.ipynb
**Style:** structured_academic (experimenting)

# Structured Academic Summary: Equal-Width Discretization  

## [[Equal-Width Discretization]]  
**Definition**: A method of binning continuous variables into discrete intervals of equal size (width), determined by the variable’s range and the number of bins specified.  
**Formula**:  
\[ \text{Width} = \frac{\text{Max}(X) - \text{Min}(X)}{\text{Bins}} \]  
**Example**:  
For `LSTAT` in the Boston Housing dataset, with a range of 5–37 and 10 bins:  
```python  
width = (37 - 5) / 10 = 3.2  
```  
Bins: [5, 8.2), [8.2, 11.4), ..., [37, 40.2].  

---

## [[Interval Width]]  
**Definition**: The size of each bin in equal-width discretization, calculated as the range of the variable divided by the number of bins.  
**Formula**:  
\[ \text{Width} = \frac{\text{Max}(X) - \text{Min}(X)}{k} \]  
where \( k \) = number of bins.  
**Example**:  
For `LSTAT` (range = 32):  
```python  
lstat_range = X_train['LSTAT'].max() - X_train['LSTAT'].min()  
bin_width = lstat_range / 10  # 3.2  
```  

---

## [[pd.cut()]]  
**Definition**: A pandas function to discretize continuous variables into bins using specified edges.  
**Formula**: N/A  
**Example**:  
```python  
X_train['lstat_disc'] = pd.cut(  
    x=X_train['LSTAT'],  
    bins=intervals,  
    include_lowest=True  
)  
```  
Creates categorical bins for `LSTAT` (e.g., (5, 8.2], (8.2, 11.4]).  

---

## [[Train-Test Split]]  
**Definition**: Dividing data into training and testing subsets to evaluate model performance.  
**Formula**: N/A  
**Example**:  
```python  
X_train, X_test, y_train, y_test = train_test_split(  
    data.drop('MEDV', axis=1),  
    data['MEDV'],  
    test_size=0.3, random_state=0  
)  
```  

---

## [[EqualWidthDiscretiser (Feature-engine)]]  
**Definition**: A Feature-engine class to automate equal-width discretization for multiple variables.  
**Formula**: N/A  
**Example**:  
```python  
disc = EqualWidthDiscretiser(  
    bins=10,  
    variables=['LSTAT', 'DIS', 'RM']  
)  
disc.fit(X_train)  
X_train = disc.transform(X_train)  
```  

---

## [[KBinsDiscretizer (scikit-learn)]]  
**Definition**: A scikit-learn transformer for equal-width binning with ordinal encoding.  
**Formula**: N/A  
**Example**:  
```python  
disc = KBinsDiscretizer(  
    n_bins=10,  
    encode='ordinal',  
    strategy='uniform'  
)  
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])  
X_train_t = disc.transform(X_train[['LSTAT', 'DIS', 'RM']])  
```  

---

## [[Interval Object (pandas)]]  
**Definition**: The data type returned by `pd.cut()`, representing a half-open interval (e.g., (5, 8.2]).  
**Example**:  
```python  
print(X_train["lstat_disc"].iloc[0])  # Output: (34.0, 37.0]  
print(type(X_train["lstat_disc"].iloc[0]))  # Output: pandas._typeds.Interval  
```  
**Key Property**:  
```python  
34.0 in test_interval  # True  
37.0 in test_interval  # False (exclusive upper bound)  
```  

---

## [[Proportion of Observations per Bin]]  
**Definition**: The distribution of data points across discretized intervals, used to compare train/test set distributions.  
**Example**:  
```python  
t1 = X_train['lstat_disc'].value_counts() / len(X_train)  
t2 = X_test['lstat_disc'].value_counts() / len(X_test)  
tmp = pd.concat([t1, t2], axis=1).plot.bar()  
```  

---

### **Related Concepts**  
- [[Binning]]: General process of grouping continuous values into intervals.  
- [[Discretization]]: Conversion of continuous variables into discrete categories.  
- [[Feature Engineering]]: Process of transforming raw data into engineered features for modeling.  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)

---

---

## 2026-06-17 11:40 — Practical 5.2 - Equal-frequency-discretization.ipynb
**Style:** structured_academic (experimenting)

# Structured Academic Summary: Equal-Frequency Discretization  

## [[Equal-Frequency Discretization]]  
**Definition**: A technique to divide continuous variables into intervals (bins) that contain an equal number of observations. This method uses quantiles to determine bin edges, making it robust to skewed distributions.  
**Formula**: For \( N \) bins, the \( i \)-th bin edge is the \( \frac{i}{N} \)-th quantile of the data.  
**Example**: Using `pd.qcut(X_train['LSTAT'], 10)` to split `LSTAT` into 10 equal-frequency bins.  

---

## [[Quantiles]]  
**Definition**: Values that divide the dataset into equal-sized groups. The \( k \)-th quantile represents the value below which \( \frac{k}{N} \times 100\% \) of observations fall.  
**Formula**: For \( N \) bins, quantiles are calculated as \( Q_i = \text{value at } \frac{i}{N} \)-th position in sorted data.  
**Example**: `pd.qcut` uses quantiles to define bin edges (e.g., 10 quantiles for deciles).  

---

## [[Bin Edges]]  
**Definition**: The boundary values that separate bins in discretization. In equal-frequency discretization, these are determined by quantiles.  
**Formula**: \( \text{Bin Edges} = [Q_0, Q_1, \dots, Q_N] \), where \( Q_0 = -\infty \) and \( Q_N = +\infty \).  
**Example**: `intervals` variable in Code Cell 8 stores the 10 quantile-based edges for `LSTAT`.  

---

## [[pandas.qcut]]  
**Definition**: A pandas function for quantile-based binning to ensure equal observation counts per bin.  
**Parameters**:  
- `q`: Number of bins (e.g., `q=10` for deciles).  
- `retbins`: Option to return bin edges.  
**Example**:  
```python  
X_train['lstat_disc'], intervals = pd.qcut(X_train['LSTAT'], 10, retbins=True)  
```  

---

## [[pd.cut]]  
**Definition**: A pandas function to discretize data into bins defined by user-specified edges.  
**Example**: Applying training-derived `intervals` to the test set:  
```python  
X_test['lstat_disc'] = pd.cut(X_test['LSTAT'], bins=intervals)  
```  

---

## [[EqualFrequencyDiscretiser (Feature-engine)]]  
**Definition**: A `Feature-engine` transformer that automates equal-frequency discretization for multiple variables.  
**Key Parameters**:  
- `q`: Number of bins (e.g., `q=10`).  
- `variables`: List of columns to discretize.  
**Example**:  
```python  
disc = EqualFrequencyDiscretiser(q=10, variables=['LSTAT', 'DIS', 'RM'])  
disc.fit(X_train)  
```  

---

## [[KBinsDiscretizer (scikit-learn)]]  
**Definition**: A scikit-learn method for binning using quantiles with `strategy='quantile'`.  
**Parameters**:  
- `n_bins`: Number of bins (e.g., `n_bins=10`).  
- `encode='ordinal'`: Encodes bins as integers (0, 1, ...).  
**Example**:  
```python  
disc = KBinsDiscretizer(n_bins=10, strategy='quantile', encode='ordinal')  
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])  
```  

---

## [[Observation Proportion per Bin]]  
**Definition**: The percentage of data points assigned to each bin, which should be roughly equal in equal-frequency discretization.  
**Formula**: \( \text{Proportion}_i = \frac{\text{Count in Bin } i}{\text{Total Observations}} \)  
**Example**:  
```python  
X_train['lstat_disc'].value_counts(normalize=True)  # Should show ~10% per bin  
```  

---

## **Answer to Q2: Leftmost Columns Difference**  
The leftmost bins (e.g., first two columns in the bar plot) may show discrepancies due to:  
1. **Skewed Data**: Variables like `LSTAT` (lower status of the population) often have right-skewed distributions, causing the lowest bin to capture fewer extreme values.  
2. **Quantile Calculation**: Edge cases (e.g., duplicates or sparse data at extremes) can lead to uneven splits.  
3. **Test Set Variability**: The test set may naturally differ slightly from the training set distribution.  

---

## **Related Concepts**  
- [[Quantile-Based Binning]]  
- [[Data Preprocessing]]  
- [[Feature Engineering]]  
- [[Scikit-learn Transformers]]  
- [[Pandas Data Manipulation]]  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)

---

---

## 2026-06-17 11:47 — Practical 5.3 - Discretization-plus-categorical-encoding.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured summary of the content using the requested format:

---

### [[Discretization (Binning)]]
**Definition**:  
The process of converting continuous variables into discrete intervals (bins) to reduce the impact of outliers, handle skewed distributions, and enable categorical encoding.  
**Formula**:  
Not applicable directly, but involves partitioning data range into intervals (e.g., $ \text{Range} = \frac{\text{Max} - \text{Min}}{\text{Number of Bins}} $ for equal-width binning).  
**Example**:  
```python
disc = EqualFrequencyDiscretiser(q=10, variables=['LSTAT', 'DIS', 'RM'], return_object=True)
disc.fit(X_train)
```

---

### [[Equal-Frequency Discretization]]
**Definition**:  
A discretization method where data is split into bins such that each bin contains an equal number of observations (using quantiles).  
**Formula**:  
Bin edges determined by $ q $ quantiles:  
$$
\text{Bin edges} = \left\{x_{(i \cdot 100/q)\%}\right\}_{i=0}^{q}
$$  
**Example**:  
```python
disc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='quantile')
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])
```

---

### [[Ordinal Encoding]]
**Definition**:  
A categorical encoding technique that maps discrete bins to ordered integers, preserving the monotonic relationship between bins and the target variable.  
**Formula**:  
Mapped values follow ordinal order:  
$$
\text{Encoded value} = \text{Rank of bin based on target association}
$$  
**Example**:  
```python
enc = OrdinalEncoder(encoding_method='ordered')
enc.fit(train_t, y_train)
train_t = enc.transform(train_t)
```

---

### [[Monotonic Relationship]]
**Definition**:  
A relationship where an increase in one variable consistently corresponds to an increase (or decrease) in another variable. In discretization, this ensures ordered bins correlate linearly with the target.  
**Formula**:  
Slope between bin means and target values should be consistent:  
$$
\text{Slope} = \frac{\text{Mean}(Y_{\text{bin } i+1}) - \text{Mean}(Y_{\text{bin } i})}{1} \geq 0
$$  
**Example**:  
After ordinal encoding, plotting mean target values per bin shows a linear trend:  
```python
pd.concat([train_t, y_train], axis=1).groupby('DIS')['MEDV'].mean().plot()
```

---

### Key Workflow Integration
1. **Discretization**: Apply `EqualFrequencyDiscretiser` to create bins.  
2. **Ordinal Encoding**: Use `OrdinalEncoder` to reorder bins based on target correlation.  
3. **Validation**: Verify monotonic relationships via grouped mean plots.  

**Linked Concepts**:  
- [[Discretization (Binning)]] → [[Equal-Frequency Discretization]] → [[Ordinal Encoding]] → [[Monotonic Relationship]]  
- Tools: `Feature-engine`, `KBinsDiscretizer`, `scikit-learn` datasets (e.g., Boston Housing).  

--- 

This summary integrates code examples, mathematical reasoning, and conceptual definitions for educational clarity.

---

---

## 2026-06-17 11:49 — Practical 5.4 - Arbitrary-interval-discretization.ipynb
**Style:** structured_academic (experimenting)

# Summary: Arbitrary Interval Discretization  

## Term: **Arbitrary Interval Discretization**  
### Definition  
A method of discretizing continuous variables where the interval boundaries are manually defined by the user, rather than determined algorithmically (e.g., equal-width or equal-frequency). This approach allows for domain-specific or strategic grouping of values.  

### Formula  
No explicit mathematical formula is required. Instead, the process involves:  
- Defining interval boundaries (`bins`) and optional labels.  
- Using `pandas.cut()` with parameters:  
  ```python  
  pd.cut(x, bins, labels=None, include_lowest=True)  
  ```  
  Where:  
  - `x`: Input continuous variable.  
  - `bins`: List of interval edges (e.g., `[0, 10, 20, np.Inf]`).  
  - `labels`: Optional descriptive names for intervals.  

### Example  
**Code Implementation**:  
```python  
# Define custom intervals and labels  
intervals = [0, 10, 20, 30, np.Inf]  
labels = ['0-10', '10-20', '20-30', '>30']  

# Apply arbitrary interval discretization  
data['lstat_labels'] = pd.cut(data['LSTAT'], bins=intervals, labels=labels, include_lowest=True)  

# View discretized results  
data[['LSTAT', 'lstat_labels']].head()  
```  

**Output**:  
| LSTAT   | lstat_labels |  
|---------|---------------|  
| 5.0     | 0-10          |  
| 4.5     | 0-10          |  
| 11.3    | 10-20         |  

**Distribution Check**:  
```python  
data['lstat_labels'].value_counts()  
```  
Output:  
```  
0-10    100  
10-20   80  
20-30   50  
>30     20  
```  

---

## Related Concepts  
- [[Equal-width Discretization]]: Intervals of fixed width.  
- [[Equal-frequency Discretization]]: Intervals with equal observation counts.  
- [[pandas cut()]]: Function for discretization.  
- [[value_counts()]]: Method to analyze distribution of discretized bins.  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).

---

---

## 2026-06-17 11:57 — Practical 6.1 - Outlier-Trimming.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the content:

---

## **Trimming Outliers**

### **Trimming**
**Definition**: The process of removing observations identified as outliers in one or more variables of a dataset.  
**Formula**: Not applicable (method-dependent).  
**Example**:  
```python
# Trimming dataset by removing rows with outliers in 'RM'
boston_trimmed = boston.loc[~outliers_RM]
```

---

### **Method 1: Standard Deviation Boundaries**
**Definition**: Outliers are defined as data points beyond **mean ± 3 × standard deviation (σ)**, assuming normal distribution (covers ~99% of data).  
**Formula**:  
\[
\text{Lower Boundary} = \mu - 3\sigma \quad \text{Upper Boundary} = \mu + 3\sigma
\]  
**Example**:  
```python
# Function to calculate boundaries using standard deviation
def find_boundaries(df, variable, distance):
    lower_boundary = df[variable].mean() - (df[variable].std() * distance)
    upper_boundary = df[variable].mean() + (df[variable].std() * distance)
    return upper_boundary, lower_boundary

# Applying for 'RM' with distance=3
RM_upper_limit, RM_lower_limit = find_boundaries(boston, 'RM', 3)
```

---

### **Method 2: Interquartile Range (IQR) Proximity Rule**
**Definition**: Outliers are data points outside **Q1 − 1.5×IQR** or **Q3 + 1.5×IQR**, where **IQR = Q3 − Q1** (works for normal and skewed distributions).  
**Formula**:  
\[
\text{IQR} = Q3 - Q1, \quad \text{Lower Boundary} = Q1 - 1.5 \times \text{IQR}, \quad \text{Upper Boundary} = Q3 + 1.5 \times \text{IQR}
\]  
**Example**:  
```python
# Function to calculate IQR-based boundaries
def find_boundaries(df, variable, distance):
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)
    lower_boundary = df[variable].quantile(0.25) - (IQR * distance)
    upper_boundary = df[variable].quantile(0.75) + (IQR * distance)
    return upper_boundary, lower_boundary

# Applying for 'LSTAT' with distance=1.5
LSTAT_upper_limit, LSTAT_lower_limit = find_boundaries(boston, 'LSTAT', 1.5)
```

---

### **Method 3: Arbitrary Percentile Boundaries**
**Definition**: Outliers are defined as data points below the **5th percentile** or above the **95th percentile**.  
**Formula**:  
\[
\text{Lower Boundary} = \text{Quantile}(0.05), \quad \text{Upper Boundary} = \text{Quantile}(0.95)
\]  
**Example**:  
```python
# Function to calculate percentile-based boundaries
def find_boundaries(df, variable):
    lower_boundary = df[variable].quantile(0.05)
    upper_boundary = df[variable].quantile(0.95)
    return upper_boundary, lower_boundary

# Applying for 'CRIM'
CRIM_upper_limit, CRIM_lower_limit = find_boundaries(boston, 'CRIM')
```

---

### **Key Notes**
1. **Trimming Across Multiple Variables**: Outliers can be removed based on multiple variables simultaneously:  
   ```python
   # Trim rows with outliers in any of the variables
   boston_trimmed = boston.loc[~(outliers_RM + outliers_LSTAT + outliers_CRIM), :]
   ```
2. **Persistent Outliers After Trimming**: Dots beyond whiskers in boxplots post-trimming may indicate outliers in other variables or method limitations (e.g., IQR sensitivity to quartile values).

---

### **Wikilinks**
- [[Trimming]]  
- [[Interquartile Range (IQR)]]  
- [[Standard Deviation]]  
- [[Percentile]]  
- [[Outlier Detection]]

---

---

## 2026-06-17 12:07 — Practical 6.2 - Winsorisation.ipynb
**Style:** structured_academic (experimenting)

### Winsorization

**Term:** Winsorization  
**Definition:** Winsorization is the process of transforming data by limiting extreme values or outliers to a certain arbitrary value closer to the mean. Unlike trimming, where outliers are removed, winsorizing replaces these extreme values with less extreme ones. A typical approach involves setting all data below a specified percentile to that percentile's value and all data above another specified percentile to that percentile's value.

**Formula:**
\[ \text{winsorized\_value} = 
  \begin{cases} 
   \text{lower\_limit} & \text{if } x < \text{lower\_limit} \\
   x & \text{if } \text{lower\_limit} \leq x \leq \text{upper\_limit} \\
   \text{upper\_limit} & \text{if } x > \text{upper\_limit}
  \end{cases} \]

**Example:**
```python
# Winsorizing the 'RM' variable with a 95th percentile upper limit and a 5th percentile lower limit

boston['RM'] = winsorise(boston, 'RM', boston['RM'].quantile(0.95), boston['RM'].quantile(0.05))
```

### Winsorization with Feature-engine

**Term:** Winsorizer  
**Definition:** The `Winsorizer` class from the `feature_engine.outliers` module in Python is used to perform winsorization on continuous variables by replacing extreme values with less extreme ones, thus reducing their influence.

**Formula:**
\[ \text{winsorized\_value} = 
  \begin{cases} 
   \text{lower\_limit} & \text{if } x < \text{lower\_limit} \\
   x & \text{if } \text{lower\_limit} \leq x \leq \text{upper\_limit} \\
   \text{upper\_limit} & \text{if } x > \text{upper\_limit}
  \end{cases} \]

**Example:**
```python
# Loading and preparing the data

boston = pd.read_csv("./data/boston_local.csv")
boston = boston[['RM', 'LSTAT', 'CRIM']]

# Creating a Winsorizer object with specific parameters
windsorizer = Winsorizer(capping_method='quantiles', 
                         tail='both',  # Cap both tails
                         fold=0.05,    # Set the fold to 5%
                         variables=['RM', 'LSTAT', 'CRIM'])

# Fitting and transforming the data
windsorizer.fit(boston)
boston_t = windsorizer.transform(boston)

# Inspecting the caps
print(windsorizer.left_tail_caps_)
print(windsorizer.right_tail_caps_)
```

### Summary

Winsorization is a method to handle outliers by replacing extreme values with less extreme ones, rather than removing them. This approach helps in preserving more data points and can improve model performance. The `Winsorizer` class from the `feature_engine.outliers` module provides an efficient way to perform this task in Python. By setting appropriate capping methods and folds, outliers can be managed effectively while maintaining the integrity of the dataset.

---

---

## 2026-06-17 12:13 — Practical 6.3 - Capping.ipynb
**Style:** structured_academic (experimenting)

# Academic Summary: Outlier Capping Techniques

## **Capping (Data Capping)**  
**Definition**: The process of replacing extreme outlier values with predefined maximum or minimum thresholds (caps) to mitigate their impact on statistical models.  
**Formula**: N/A (implemented via specific methods)  
**Example**:  
```python
boston['RM'] = np.where(boston['RM'] > RM_upper_limit, RM_upper_limit, 
                         np.where(boston['RM'] < RM_lower_limit, RM_lower_limit, boston['RM']))
```
This code caps 'RM' values beyond the calculated limits using `np.where`.

---

## **Interquartile Range (IQR) Method**  
**Definition**: A technique to identify outliers using the interquartile range (IQR), defined as the difference between the 75th (Q3) and 25th (Q1) percentiles.  
**Formula**:  
$$
\text{IQR} = Q3 - Q1 \\
\text{Lower Boundary} = Q1 - (\text{IQR} \times \text{distance}) \\
\text{Upper Boundary} = Q3 + (\text{IQR} \times \text{distance})
$$  
**Example**:  
```python
def find_skewed_boundaries(df, variable, distance):
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)
    lower_boundary = df[variable].quantile(0.25) - (IQR * distance)
    upper_boundary = df[variable].quantile(0.75) + (IQR * distance)
    return upper_boundary, lower_boundary
```

---

## **Gaussian (Standard Deviation) Method**  
**Definition**: A method assuming normal distribution, using mean (μ) and standard deviation (σ) to calculate outlier boundaries.  
**Formula**:  
$$
\text{Upper Boundary} = \mu + (\text{distance} \times \sigma) \\
\text{Lower Boundary} = \mu - (\text{distance} \times \sigma)
$$  
**Example**:  
```python
def find_normal_boundaries(df, variable, distance):
    upper_boundary = df[variable].mean() + df[variable].std() * distance
    lower_boundary = df[variable].mean() - df[variable].std() * distance
    return upper_boundary, lower_boundary
```

---

## **Winsorizer**  
**Definition**: A transformer from the `feature-engine` library that implements capping using methods like Gaussian or IQR.  
**Formula**: N/A (implementation tool)  
**Example**:  
```python
windsorizer = Winsorizer(capping_method='gaussian', tail='both', fold=3, variables=['RM', 'LSTAT', 'CRIM'])
windsorizer.fit(boston)
boston_t = windsorizer.transform(boston)
```

---

## **Censoring (Top and Bottom Coding)**  
**Definition**: Synonymous with capping; involves replacing extreme values with cutoffs (e.g., mean ± 3σ or IQR-based limits).  
**Formula**: Same as [[Capping (Data Capping)]] and its methods.  
**Example**:  
The notebook uses "censoring" interchangeably with capping, as seen in the description of the Winsorizer’s functionality.

---

## **Key Links**  
- [[Interquartile Range (IQR) Method]]  
- [[Gaussian (Standard Deviation) Method]]  
- [[Winsorizer]]  
- [[Capping (Data Capping)]]  
- [[Censoring (Top and Bottom Coding)]]

---

---

## 2026-06-17 12:16 — Practical 6.4 - Zero-coding.ipynb
**Style:** structured_academic (experimenting)

Here's a structured summary of the content using the requested format:

---

### **Zero-coding**  
**Definition**: A variant of bottom-coding where the lower tail of a variable is capped at **zero**, typically used for variables that cannot logically take negative values (e.g., income, age).  
**Formula**:  
For all values \( x < 0 \), replace with \( 0 \):  
\[ x_{\text{capped}} = \max(x, 0) \]  
**Example**:  
```python  
# Cap negative values at 0 for all columns  
data.loc[data['x'] < 0, 'x'] = 0  
data.loc[data['y'] < 0, 'y'] = 0  
data.loc[data['z'] < 0, 'z'] = 0  
```  

---

### **ArbitraryOutlierCapper**  
**Definition**: A class from the `Feature-engine` library used to cap outliers at specified thresholds for either or both tails of a distribution.  
**Formula**:  
- **Parameters**:  
  - `min_capping_dict`: Dictionary specifying minimum caps (e.g., `{'x': 0}`).  
  - `max_capping_dict`: Dictionary specifying maximum caps (e.g., `{'x': 7}`).  
**Example**:  
```python  
# Cap minimum at 0 and maximum at 7 for all columns  
capper = ArbitraryOutlierCapper(  
    min_capping_dict={'x': 0, 'y': 0, 'z': 0},  
    max_capping_dict={'x': 7, 'y': 7, 'z': 7}  
)  
data_t = capper.fit_transform(data)  
```  

---

### **Top-coding & Bottom-coding**  
**Definition**:  
- **Top-coding**: Capping values above a specified threshold (right tail).  
- **Bottom-coding**: Capping values below a specified threshold (left tail).  
**Relationship**:  
- Zero-coding is a special case of **bottom-coding** where the threshold is 0.  
- Both are forms of [[Capping]] (also called censoring or capping).  
**Example**:  
```python  
# Bottom-coding at 0 (equivalent to zero-coding)  
data.loc[data['x'] < 0, 'x'] = 0  

# Top-coding at 7  
data.loc[data['x'] > 7, 'x'] = 7  
```  

---

### **Key Workflow Steps**  
1. **Visualize Data**: Use histograms to identify negative values (`data.hist()`).  
2. **Apply Capping**:  
   - Manual capping with `DataFrame.loc`.  
   - Automated capping with `ArbitraryOutlierCapper`.  
3. **Validate Results**:  
   - Check minimum/maximum values post-capping (`data.min()`, `data.max()`).  
   - Inspect caps via `capper.left_tail_caps_` and `capper.right_tail_caps_`.  

---

### **Solution to Q4**  
To cap both tails (min at 0, max at 7):  
```python  
# Modified capper for min and max thresholds  
capper = ArbitraryOutlierCapper(  
    min_capping_dict={'x': 0, 'y': 0, 'z': 0},  
    max_capping_dict={'x': 7, 'y': 7, 'z': 7}  
)  
data_t = capper.fit_transform(data)  
```  

---

### **Related Concepts**  
- [[Winsorization]]: Caps values at specified percentiles (e.g., 5th and 95th).  
- [[Outliers]]: Values that deviate significantly from the majority.  
- [[Capping]]: General term for threshold-based value replacement.  

This summary integrates methods from the notebook with foundational concepts for handling outliers in datasets.

---

---

## 2026-06-17 12:21 — Practical 3.1 - One-Hot-Encoding.ipynb
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

---

---

## 2026-06-17 12:26 — Practical 3.2 - One-Hot-Encoding-Top-Categories.ipynb
**Style:** structured_academic (experimenting)

### One-Hot Encoding  
**Definition:** A technique to represent categorical variables as binary variables, where each category is assigned a binary column (1 if present, 0 otherwise).  
**Formula:** For a categorical variable with \( N \) categories, \( N \) binary columns are created. When limiting to top \( K \) categories, only \( K \) binary columns are generated.  
**Example:**  
```python  
# Create binary variables for top 5 categories in 'A6'  
top_5 = X_train['A6'].value_counts().sort_values(ascending=False).head(5).index  
for label in top_5:  
    X_train[f'A6_{label}'] = np.where(X_train['A6'] == label, 1, 0)  
```  

---

### Top Categories Encoding  
**Definition:** A variant of one-hot encoding that encodes only the most frequent categories to reduce dimensionality, grouping less frequent categories into a single "Other" category.  
**Formula:** Select top \( K \) categories by frequency, encode them as binary variables, and treat remaining categories as a collective group.  
**Example:**  
```python  
# Select top 5 categories for 'A6'  
top_5 = X_train['A6'].value_counts().sort_values(ascending=False).head(5).index  
# Encode top categories in train and test sets  
for label in top_5:  
    X_train[f'A6_{label}'] = np.where(X_train['A6'] == label, 1, 0)  
    X_test[f'A6_{label}'] = np.where(X_test['A6'] == label, 1, 0)  
```  

---

### Feature-engine OneHotEncoder  
**Definition:** A class from the [[Feature-engine]] library that performs one-hot encoding for specified variables, with options to limit encoding to top frequent categories.  
**Formula:** Initialized with parameters such as `top_categories` (number of categories to encode) and `variables` (columns to encode).  
**Example:**  
```python  
# Initialize encoder for top 5 categories in 'A6' and 'A7'  
ohe_enc = OneHotEncoder(  
    top_categories=5,  
    variables=['A6', 'A7'],  
    drop_last=False  
)  
# Fit and transform data  
ohe_enc.fit(X_train)  
X_train_enc = ohe_enc.transform(X_train)  
```  

---

### Frequency-based Category Selection  
**Definition:** The process of identifying the most frequent categories in a dataset using frequency counts, often for dimensionality reduction in encoding.  
**Formula:** \( \text{Top } K \text{ categories} = \text{Sort categories by frequency in descending order and select first } K \).  
**Example:**  
```python  
# Get top 5 most frequent categories in 'A6'  
top_5 = X_train['A6'].value_counts().sort_values(ascending=False).head(5).index  
print(top_5)  
```  

---

### Dimensionality Reduction in Encoding  
**Definition:** Techniques to minimize the number of features generated during encoding, such as limiting one-hot encoding to frequent categories.  
**Formula:** Reduces \( N \) categories to \( K \) binary columns (\( K < N \)).  
**Example:**  
```python  
# Before: 'A6' has 10 categories → 10 binary columns  
# After: Encode only top 5 categories → 5 binary columns  
```  

---

### [[Feature-engine]]  
**Definition:** A Python library for feature engineering tasks, including encoding, imputation, and transformation.  
**Formula:** N/A (library/tool).  
**Example:**  
```python  
# Import OneHotEncoder from Feature-engine  
from feature_engine.encoding import OneHotEncoder  
```  

---

### [[Grouping Rare or Infrequent Categories]]  
**Definition:** A method to combine less frequent categories into a single "Other" category to reduce noise and dimensionality.  
**Formula:** \( \text{Rare categories} \rightarrow \text{Grouped as "Other"} \).  
**Example:**  
```python  
# Implicitly achieved by encoding only top categories; remaining categories are treated as a group.  
```  

--- 

This summary connects key concepts like [[One-Hot Encoding]], [[Feature-engine]], and [[Grouping Rare or Infrequent Categories]] for cohesive understanding.

---

---

## 2026-06-17 12:33 — Practical 3.3 - Replacing-categories-by-ordinal-numbers.ipynb
**Style:** structured_academic (experimenting)

# Summary: Ordinal Encoding in Data Preprocessing

## [[Ordinal Encoding]]  
**Definition**: A technique to convert categorical variables into numerical values by assigning each category an arbitrary integer (e.g., 0 to \( k-1 \), where \( k \) is the number of unique categories). Suitable for non-linear models.  
**Formula**:  
\[ \text{Assigned Value} = i \quad \text{for category } k \text{ at index } i \]  
**Example**:  
```python
# Using pandas to map categories to integers
ordinal_mapping = {k: i for i, k in enumerate(X_train['A7'].unique(), 0)}
X_train['A7'] = X_train['A7'].map(ordinal_mapping)
```

---

## [[Nominal Categorical Variables]]  
**Definition**: Categorical variables without intrinsic order (e.g., "Gender", "City").  
**Formula**: N/A  
**Example**:  
```python
# Example of nominal variable 'A7' in the dataset
print(X_train['A7'].unique())  # Outputs: ['A', 'B', 'C', ...] (no inherent order)
```

---

## [[Ordinal Categorical Variables]]  
**Definition**: Categorical variables with a meaningful order (e.g., "Grade: A > B > C").  
**Formula**: N/A  
**Example**:  
```python
# Hypothetical ordinal variable mapping
grade_mapping = {'Fail': 0, 'C': 1, 'B': 2, 'A': 3}
```

---

## [[Category Mapping]]  
**Definition**: The process of creating a dictionary to map category labels to numerical values.  
**Formula**:  
\[ \text{Mapping} = \{k: i\} \quad \forall \text{categories } k \text{ in variable} \]  
**Example**:  
```python
# Manual mapping for variable 'A7'
ordinal_mapping = {k: i for i, k in enumerate(X_train['A7'].unique(), 0)}
# Output: {'A': 0, 'B': 1, 'C': 2, ...}
```

---

## [[Scikit-learn OrdinalEncoder]]  
**Definition**: A class from `sklearn.preprocessing` for ordinal encoding.  
**Formula**: N/A  
**Example**:  
```python
from sklearn.preprocessing import OrdinalEncoder
le = OrdinalEncoder()
le.fit(X_train[vars_categorical])  # Learn mappings
X_train_enc = le.transform(X_train[vars_categorical])  # Apply encoding
```

---

## [[Feature-engine OrdinalEncoder]]  
**Definition**: An encoder from the `Feature-engine` library for ordinal encoding.  
**Formula**: N/A  
**Example**:  
```python
from feature_engine.encoding import OrdinalEncoder
ordinal_enc = OrdinalEncoder(encoding_method='arbitrary', variables=vars_categorical)
ordinal_enc.fit(X_train)  # Fit to training data
X_train = ordinal_enc.transform(X_train)  # Transform datasets
```

---

## [[Train-Test Split]]  
**Definition**: Dividing a dataset into training and testing subsets to evaluate model performance.  
**Formula**:  
\[ \text{Test Size} \in (0, 1) \quad \text{(e.g., 0.3 for 30% test data)} \]  
**Example**:  
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    data.drop('A16', axis=1),  # Features
    data['A16'],               # Target
    test_size=0.3,             # 30% for testing
    random_state=0             # Reproducibility
)
```

---

## Key Concepts Interconnectivity  
- **Ordinal Encoding** is applied to **Nominal** or **Ordinal Categorical Variables**.  
- **Category Mapping** is the core step in **Ordinal Encoding**.  
- **Scikit-learn** and **Feature-engine** provide implementations of **Ordinal Encoding**.  
- **Train-Test Split** ensures encoding is fit only on training data to prevent data leakage.

---

---

## 2026-06-17 12:35 — Practical 3.4 - replacing-categories-by-counts-frequency.ipynb
**Style:** structured_academic (experimenting)

Here's a structured summary of the content following the requested format:

---

### **Count Encoding**  
**Definition**: A technique where categorical variable categories are replaced with their **occurrence counts** in the dataset. This captures the frequency of each category as a numerical value.  
**Formula**:  
\[ \text{Count}(c) = \text{Number of observations with category } c \]  
**Example**:  
```python
# Using pandas to create count mappings
count_map = X_train['A7'].value_counts().to_dict()
X_train['A7'] = X_train['A7'].map(count_map)
```  
**Wikilinks**: [[Frequency Encoding]], [[Categorical Variable]]

---

### **Frequency Encoding**  
**Definition**: A method where categories are replaced with their **relative frequency** (proportion of total observations). This normalizes counts to a [0,1] scale.  
**Formula**:  
\[ \text{Frequency}(c) = \frac{\text{Count}(c)}{\text{Total Observations}} \]  
**Example**:  
```python
# Calculating frequency mappings
frequency_map = (X_train['A6'].value_counts() / len(X_train)).to_dict()
X_train['A6'] = X_train['A6'].map(frequency_map)
```  
**Wikilinks**: [[Count Encoding]], [[Data Normalization]]

---

### **CountFrequencyEncoder (Feature-engine)**  
**Definition**: A class from the `Feature-engine` library that automates count or frequency encoding. It stores mappings and applies them to training/test sets.  
**Formula**:  
- **Count Mode**: \( \text{Encoded Value} = \text{Count}(c) \)  
- **Frequency Mode**: \( \text{Encoded Value} = \frac{\text{Count}(c)}{N} \)  
**Example**:  
```python
# Using Feature-engine for count encoding
count_enc = CountFrequencyEncoder(encoding_method='count')
count_enc.fit(X_train)
X_train_enc = count_enc.transform(X_train)
```  
**Wikilinks**: [[Pandas]], [[One-Hot Encoding]]

---

### **Key Functions for Encoding**  
**Definition**: Custom functions to streamline encoding workflows:  
1. **`count_mappings`**: Generates count dictionaries.  
2. **`frequency_mappings`**: Generates frequency dictionaries.  
3. **`encode`**: Applies mappings to train/test sets.  
**Example**:  
```python
# Applying encoding to multiple variables
for variable in vars_categorical:
    mappings = count_mappings(X_train, variable)
    encode(X_train, X_test, variable, mappings)
```  
**Wikilinks**: [[Data Preprocessing]]

---

### **Applications**  
- **Advantages**:  
  - Reduces dimensionality compared to [[One-Hot Encoding]].  
  - Captures category representation patterns.  
- **Use Cases**: Predictive modeling where category frequency correlates with the target (e.g., credit approval datasets).  

**Wikilinks**: [[Rare Categories]], [[Ordinal Encoding]]  

--- 

This summary links to related concepts (e.g., [[One-Hot Encoding]], [[Ordinal Encoding]]) for cross-referencing. Let me know if further refinements are needed!

---

---

## 2026-06-17 12:39 — Practical 3.5 - ordered-ordinal-encoding.ipynb
**Style:** structured_academic (experimenting)

# Summary: Ordered Integer Encoding for Linear Models

## **Ordered Integer Encoding**
**Definition**: A method of encoding categorical variables by assigning integers (0 to k-1) to categories based on their mean target value. Categories are ordered from lowest to highest mean target, ensuring a monotonic relationship with the target variable.  
**Formula**:  
Mean target per category:  
\[ \text{mean\_target} = \frac{\sum \text{target values in category}}{\text{number of observations in category}} \]  
**Example**:  
```python
# Create ordered mapping for 'A7' based on mean target
ordered_labels = X_train.groupby(['A7'])['A16'].mean().sort_values().index
ordinal_mapping = {k: i for i, k in enumerate(ordered_labels, 0)}
X_train['A7'] = X_train['A7'].map(ordinal_mapping)
```

## **Monotonic Relationship**
**Definition**: A consistent, step-wise relationship between the encoded integers and the target variable, where higher integers correspond to higher (or lower) target means. This is critical for linear models to interpret the encoded variables correctly.  
**Formula**: Sorted mean targets must follow a non-decreasing or non-increasing order.  
**Example**:  
```python
# Plot showing monotonic relationship after encoding
X_train.groupby(['A7'])['A16'].mean().plot()
plt.title('Monotonic Relationship Between A7 and Target')
```

## **OrdinalEncoder (Feature-engine)**
**Definition**: A class in the `Feature-engine` library that automates ordered integer encoding by fitting on the training data and target variable. It stores mappings for each categorical variable.  
**Formula**: N/A (Process involves fitting to target and transforming categories).  
**Example**:  
```python
from feature_engine.encoding import OrdinalEncoder
ordinal_enc = OrdinalEncoder(encoding_method='ordered')
ordinal_enc.fit(X_train, y_train)  # Requires target for ordering
X_train_enc = ordinal_enc.transform(X_train)
```

## **Target-Based Encoding**
**Definition**: A category encoding strategy that uses target variable information (e.g., mean, median) to assign values to categorical levels. Ordered integer encoding is a type of target-based encoding.  
**Formula**: Same as `mean_target` in Ordered Integer Encoding.  
**Example**:  
```python
# Calculate mean target per category for encoding
category_means = X_train.groupby(['A7'])['A16'].mean().sort_values()
```

---

### **Key Concept Links**  
- [[Ordinal Encoding]]: Arbitrary assignment of integers (previous method).  
- [[Linear Models]]: Benefit from monotonic relationships created by ordered encoding.  
- [[Target-Based Encoding]]: Broader category including ordered integer encoding.  

### **Comparison with Arbitrary Ordinal Encoding**  
| **Aspect**               | **Ordered Integer Encoding**                          | **Arbitrary Ordinal Encoding**          |  
|--------------------------|----------------------------------------------------------|-----------------------------------------|  
| **Basis for Assignment** | Mean target value of categories                         | Random or default order                |  
| **Suitability**          | Linear models (monotonic relationship)                  | Non-linear models (e.g., tree-based)   |  
| **Implementation**       | Requires target variable during fitting                 | No target dependency                   |  

This method ensures categorical variables are transformed in a way that aligns with the assumptions of linear models, enhancing their interpretability and performance.

---

---

## 2026-06-17 12:42 — Practical 3.6 - target-mean-encoding.ipynb
**Style:** structured_academic (experimenting)

# Summary: Target Mean Encoding

## Term: [[Target Mean Encoding]]  
**Definition**: A technique where categorical variables are replaced by the average value of the target variable associated with each category. This method leverages the relationship between categories and the target to create numerical features.  
**Formula**:  
\[
\text{Mean Encoding} = \frac{\sum_{i=1}^{n} y_i}{n} \quad \text{for category } c
\]  
Where \( y_i \) are target values for category \( c \), and \( n \) is the number of observations in \( c \).  
**Example**:  
```python
# Using pandas to compute and apply target means
ordered_labels = X_train.groupby(['A7'])['A16'].mean().to_dict()
X_train['A7'] = X_train['A7'].map(ordered_labels)
X_test['A7'] = X_test['A7'].map(ordered_labels)
```

---

## Term: [[MeanEncoder (Feature-engine)]]  
**Definition**: A class from the `Feature-engine` library that automates target mean encoding. It encodes categorical variables by fitting to the training data and applying the learned means to the test set.  
**Formula**: Same as Target Mean Encoding.  
**Example**:  
```python
# Using Feature-engine's MeanEncoder
mean_enc = MeanEncoder(variables=None)  # Encode all categorical variables
mean_enc.fit(X_train, y_train)         # Fit using target
X_train_enc = mean_enc.transform(X_train)
X_test_enc = mean_enc.transform(X_test)
```

---

## Term: [[Manual Mean Encoding with Pandas]]  
**Definition**: A manual approach to target mean encoding using pandas, involving calculating category means and mapping them to original categories.  
**Formula**: Same as Target Mean Encoding.  
**Example**:  
```python
# Calculate target mean per category
X_train[["A7", "A16"]][X_train["A7"]=="n"]  # Inspect data
ordered_labels = X_train.groupby(['A7'])['A16'].mean().to_dict()
# Apply encoding
X_train['A7'] = X_train['A7'].map(ordered_labels)
X_test['A7'] = X_test['A7'].map(ordered_labels)
```

---

## Key Concepts and Links  
- **[[Categorical Variable]]**: Non-numeric feature requiring encoding (e.g., `A7` in the dataset).  
- **[[Target Variable]]**: The variable to predict (e.g., `A16` in the dataset).  
- **[[Scikit-learn]]**: Integration with libraries like `Feature-engine` for pipeline compatibility.  
- **[[Overfitting Risk]]**: Target mean encoding may introduce overfitting if not properly regularized.  

This summary aligns with the notebook’s focus on encoding categorical variables using target means, demonstrating both manual and automated methods.

---

---

## 2026-06-17 12:49 — Practical 3.7 - grouping-rare-categories.ipynb
**Style:** structured_academic (experimenting)

# Summary: Grouping Rare or Infrequent Categories

## [[Rare Values]]
**Definition**: Categories present in a small percentage of observations, typically defined as those with less than 5% frequency in the dataset.  
**Formula**:  
\[
\text{Percentage} = \frac{\text{Count of category}}{\text{Total observations}} < 0.05
\]  
**Example**: In variable `A7`, categories with a frequency below 5% are labeled as "Rare" (e.g., `X_train['A7'].value_counts() / len(X_train)` identifies rare categories).

---

## [[Grouping Rare Categories]]
**Definition**: The process of combining infrequent categories into a single "Rare" or "Other" category to reduce overfitting and improve model robustness.  
**Formula**: Not applicable (process-based).  
**Example**: Using `np.where` to replace non-frequent categories in `A7` with "Rare":  
```python
X_train['A7'] = np.where(X_train['A7'].isin(frequent_cat), X_train['A7'], 'Rare')
```

---

## [[Count Encoding]]
**Definition**: Replacing categorical labels with their frequency (or count) of occurrence in the dataset.  
**Formula**:  
\[
\text{Frequency} = \frac{\text{Number of observations with category}}{\text{Total observations}}
\]  
**Example**: Calculating frequencies for `A7` categories using `X_train['A7'].value_counts() / len(X_train)`.

---

## [[One-Hot Encoding with Feature-engine]]
**Definition**: Applying one-hot encoding to the most frequent categories while grouping rare categories into a single "Rare" category using the `Feature-engine` library.  
**Formula**: Not directly applicable (threshold-based).  
**Example**: Using `RareLabelEncoder` to encode top categories:  
```python
rare_encoder = RareLabelEncoder(tol=0.05, n_categories=4)
```

---

## [[RareLabelEncoder]]
**Definition**: A `Feature-engine` transformer that groups rare categories into a single category based on a tolerance threshold (e.g., 5%).  
**Formula**: Parameters include `tol` (threshold for rare categories) and `n_categories` (number of top categories to retain).  
**Example**:  
```python
rare_encoder = RareLabelEncoder(tol=0.05, n_categories=4)
rare_encoder.fit(X_train)
X_train_enc = rare_encoder.transform(X_train)
```

---

## Key Takeaways
- **Rare Values**: Identified using a frequency threshold (e.g., 5%).  
- **Grouping**: Reduces dimensionality and prevents overfitting by merging rare categories.  
- **Count/Frequency Encoding**: Quantifies category representation for modeling.  
- **RareLabelEncoder**: Automates grouping of rare categories during preprocessing.  

[[Data Wrangling]] | [[Categorical Encoding]] | [[Feature Engineering]]

---

---

## 2026-06-17 12:51 — Practical 4.1 - logarithmic-transformation.ipynb
**Style:** structured_academic (experimenting)

```markdown
# Summary: Transforming Numerical Variables with Logarithmic Transformation

## [[Logarithmic Transformation]]
**Definition**: A mathematical transformation applied to positive variables to alter the shape of their distribution, often making it more Gaussian-like. It is particularly effective for right-skewed data and can help unmask linear relationships in regression models.

**Formula**: 
\[
X_t = \log(X)
\]
where \(X\) is the original variable and \(X_t\) is the transformed variable.

**Example**:  
- Applied to columns `LSTAT`, `NOX`, `DIS`, and `RM` in the Boston House Price dataset using:  
  - **NumPy**: `np.log(data[['LSTAT', 'NOX', 'DIS', 'RM']])`  
  - **Scikit-learn**: `FunctionTransformer(np.log)`  
  - **Feature-engine**: `LogTransformer(variables=[...])`  

---

## [[Q-Q Plot]]
**Definition**: A quantile-quantile plot used to compare the distribution of a variable against a theoretical normal distribution. It assesses whether the variable follows a Gaussian distribution by plotting its quantiles against the expected quantiles of a normal distribution.

**Formula**: No direct mathematical formula; based on comparing empirical quantiles (\(Q_{\text{observed}}\)) to theoretical normal quantiles (\(Q_{\text{expected}}\)).

**Example**:  
Generated using `scipy.stats.probplot` within the `diagnostic_plots` function to evaluate the normality of variables like `LSTAT` before and after transformation.

---

## [[Diagnostic Plots]]
**Definition**: A combination of visualizations (histogram and Q-Q plot) used to diagnose the distributional characteristics of a variable. These plots help evaluate the effectiveness of transformations in achieving normality.

**Formula**: Not applicable, as it is a visualization tool.

**Example**:  
The `diagnostic_plots` function generates:  
1. A histogram (left subplot) to visualize the variable's distribution.  
2. A Q-Q plot (right subplot) to compare quantiles against a normal distribution.  
```python
def diagnostic_plots(df, variable):
    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    df[variable].hist(bins=30)
    plt.subplot(1, 2, 2)
    stats.probplot(df[variable], dist="norm", plot=plt)
    plt.show()
```
**Usage**: `diagnostic_plots(data, 'LSTAT')` to compare distributions pre- and post-logarithmic transformation.

---

## Key Libraries and Tools
- **NumPy**: Directly applies logarithmic transformation via `np.log()`.  
- **Scikit-learn**: Uses `FunctionTransformer` to wrap `np.log` for pipeline compatibility.  
- **Feature-engine**: Provides `LogTransformer` for robust, column-specific transformations.
```

---

---

## 2026-06-17 12:54 — Practical 4.2 - reciprocal-transformation.ipynb
**Style:** structured_academic (experimenting)

### Summary: Reciprocal Transformation and Diagnostic Plots

#### [[Reciprocal Transformation]]
**Definition:**  
A mathematical transformation that applies the reciprocal function \( \frac{1}{X} \) to variables, drastically altering their distribution. It is undefined for \( X = 0 \) but can be applied to negative values.  

**Formula:**  
\[
X_t = \frac{1}{X}
\]

**Examples:**  
1. **NumPy Implementation:**  
   ```python
   data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.reciprocal(data[['LSTAT', 'NOX', 'DIS', 'RM']])
   ```
2. **scikit-learn (FunctionTransformer):**  
   ```python
   transformer = FunctionTransformer(np.reciprocal, validate=True)
   data_tf = pd.DataFrame(transformer.transform(data[cols]), columns=cols)
   ```
3. **Feature-engine (ReciprocalTransformer):**  
   ```python
   rt = ReciprocalTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])
   data_tf = rt.transform(data)
   ```

---

#### [[Diagnostic Plot]]
**Definition:**  
A visualization tool combining a histogram and a Q-Q plot to evaluate the distribution of a variable before and after transformation.  

**Formula:**  
N/A  

**Example:**  
```python
def diagnostic_plots(df, variable):
    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    df[variable].hist(bins=30)
    plt.subplot(1, 2, 2)
    stats.probplot(df[variable], dist="norm", plot=plt)
    plt.show()
```
**Usage:**  
```python
diagnostic_plots(data_tf, 'DIS')  # To assess the effect of reciprocal transformation on 'DIS'
```

---

### Key Concepts Linked  
- [[Logarithmic Transformation]] (for comparison with other transformations)  
- [[Box-Cox Transformation]] / [[Yeo-Johnson Transformation]] (alternative methods for normalizing data)  
- [[Q-Q Plot]] (statistical tool within diagnostic plots)

---

---

## 2026-06-17 12:57 — Practical 4.3 - square-cube-root.ipynb
**Style:** structured_academic (experimenting)

### Summary: Square and Cube Root Transformations

#### **Square Root Transformation**  
**Definition**: A power transformation with an exponent of \( \frac{1}{2} \), used to reduce positive skewness in a dataset. It is only applicable to non-negative variables, as negative values would result in undefined or complex numbers.  
**Formula**:  
\[ X_t = X^{1/2} \]  
**Example**:  
- **NumPy**: Apply `np.sqrt()` to variables (e.g., `data[['LSTAT', 'NOX']] = np.sqrt(data[['LSTAT', 'NOX']])`).  
- **Scikit-learn**: Use `FunctionTransformer` with `np.sqrt` to transform selected columns.  
- **Feature-engine**: Utilize `PowerTransformer` with `exp=1/2` for cube root.  

#### **Cube Root Transformation**  
**Definition**: A power transformation with an exponent of \( \frac{1}{3} \), effective for variables with moderate skewness. Like the square root, it requires non-negative input values.  
**Formula**:  
\[ X_t = X^{1/3} \]  
**Example**:  
- **NumPy**: Apply `np.cbrt()` to variables (e.g., `data[['LSTAT', 'NOX']] = np.cbrt(data[['LSTAT', 'NOX']])`).  
- **Scikit-learn**: Implement `FunctionTransformer` with `np.cbrt` for transformation.  
- **Feature-engine**: Configure `PowerTransformer` with `exp=1/3` to achieve cube root.  

---

### Key Implementation Notes  
1. **Diagnostic Plots**: Use histograms and Q-Q plots (via `diagnostic_plots` function) to evaluate the effect of transformations on variable distributions.  
2. **Library Integration**:  
   - **NumPy**: Directly apply `np.sqrt()` or `np.cbrt()` for element-wise transformations.  
   - **Scikit-learn**: Leverage `FunctionTransformer` for flexible pipeline integration.  
   - **Feature-engine**: Use `PowerTransformer` for robust, exponent-specific transformations.  

3. **Constraints**: Both transformations are undefined for negative values, necessitating prior handling of negative data points (e.g., addition of a constant).  

[[Power Transformation]]  
[[NumPy]]  
[[Scikit-learn]]  
[[Feature-engine]]  
[[Q-Q Plot]]  

*Source: Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*

---

---

## 2026-06-17 13:04 — Practical 4.4 - power-transformation.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured summary of the content following the academic format:

---

### [[Power Transformation]]
**Definition**: A mathematical transformation where a variable \( X \) is raised to an exponent \( \lambda \) (lambda) to achieve normality or improve model performance.  
**Formula**:  
\[
X_t = X^{\lambda}
\]  
**Example**:  
```python
# Apply power transformation with λ=0.3 using NumPy
data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.power(data[['LSTAT', 'NOX', 'DIS', 'RM']], 0.3)
```

---

### [[Square Root Transformation]]
**Definition**: A specific power transformation where \( \lambda = \frac{1}{2} \), used for right-skewed data. Not defined for negative values.  
**Formula**:  
\[
X_t = X^{1/2}
\]  
**Example**:  
```python
# Apply square root transformation
data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.sqrt(data[['LSTAT', 'NOX', 'DIS', 'RM']])
```

---

### [[Cube Root Transformation]]
**Definition**: A specific power transformation where \( \lambda = \frac{1}{3} \), suitable for moderately skewed data.  
**Formula**:  
\[
X_t = X^{1/3}
\]  
**Example**:  
```python
# Apply cube root transformation
data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.cbrt(data[['LSTAT', 'NOX', 'DIS', 'RM']])
```

---

### [[FunctionTransformer (Scikit-learn)]]
**Definition**: A scikit-learn class for applying custom-defined functions (e.g., power transformations) to data.  
**Formula**: N/A (user-defined function)  
**Example**:  
```python
# Initialize FunctionTransformer for λ=0.3
transformer = FunctionTransformer(lambda x: np.power(x, 0.3), validate=True)
data_tf = transformer.transform(data[cols])
```

---

### [[PowerTransformer (Feature-engine)]]
**Definition**: A Feature-engine class for applying power transformations with specified exponents to selected variables.  
**Formula**: Follows \( X_t = X^{\lambda} \)  
**Example**:  
```python
# Initialize PowerTransformer with λ=0.3
et = PowerTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'], exp=0.3)
data_tf = et.transform(data)
```

---

### [[Pipeline (Scikit-learn)]]
**Definition**: A scikit-learn tool for chaining multiple transformations or models into a single workflow.  
**Formula**: N/A  
**Example**:  
```python
# Pipeline with different exponents for different features
pipe = Pipeline([
    ('power1', PowerTransformer(variables=['LSTAT', 'NOX'], exp=0.3)),
    ('power2', PowerTransformer(variables=['DIS'], exp=0.4)),
    ('power3', PowerTransformer(variables=['RM'], exp=0.5)),
])
data_tf = pipe.transform(data)
```

---

### Key Notes:
1. **Purpose**: Power transformations (including square/cube roots) are used to normalize data distributions or unmask linear relationships for linear/logistic regression models.
2. **Implementation**: 
   - **NumPy**: Direct array operations (e.g., `np.power`, `np.sqrt`).
   - **Scikit-learn**: `FunctionTransformer` for custom lambdas.
   - **Feature-engine**: `PowerTransformer` for scalable, pipeline-friendly transformations.
3. **Constraints**: Square root requires non-negative values; choose \( \lambda \) based on data skewness.  

Related concepts: [[Normality Assumption]], [[Linear Regression]], [[Data Preprocessing]].

---

---

## 2026-06-17 13:10 — Practical 4.5 - Box-Cox-transformation.ipynb
**Style:** structured_academic (experimenting)

### Summary: Box-Cox Transformation and Related Concepts

---

#### [[Box-Cox Transformation]]
**Definition**: A power transformation method that normalizes data by applying a family of functions parameterized by λ (lambda). It generalizes the logarithm for λ=0 and handles positive values. The optimal λ is selected to achieve the best normalization.  
**Formula**:  
\[
X_t = 
\begin{cases} 
\frac{X^{\lambda} - 1}{\lambda} & \text{if } \lambda \neq 0 \\
\log(X) & \text{if } \lambda = 0 
\end{cases}
\]  
**Example**:  
- **SciPy**:  
  ```python
  data_tf['LSTAT'], param = stats.boxcox(data['LSTAT'])
  ```  
- **Scikit-learn**:  
  ```python
  transformer = PowerTransformer(method='box-cox', standardize=False)
  data_tf = transformer.transform(data[cols])
  ```  
- **Feature-engine**:  
  ```python
  bct = BoxCoxTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])
  data_tf = bct.transform(data)
  ```  

---

#### [[Power Transformation]]
**Definition**: A family of transformations using exponent functions (\(X_t = X^{\lambda}\)) to modify variable distributions. Special cases include square root (\(\lambda = 1/2\)) and cube root (\(\lambda = 1/3\)).  
**Formula**:  
\[
X_t = X^{\lambda}
\]  
**Example**:  
- **Square Root**: \(X_t = \sqrt{X}\)  
- **Cube Root**: \(X_t = \sqrt[3]{X}\)  
- **Box-Cox**: A generalized power transformation (see above).  

---

#### [[Optimal Lambda]]
**Definition**: The value of λ that maximizes normality in the transformed data, determined via maximum likelihood estimation.  
**Formula**: Derived from the likelihood function of the data.  
**Example**:  
- **SciPy**: Printed via `param` in `stats.boxcox()`.  
- **Scikit-learn**: Accessed through `transformer.lambdas_`.  
- **Feature-engine**: Stored in `bct.lambda_dict_`.  

---

#### [[Diagnostic Plots]]
**Definition**: Visual tools (e.g., histograms, Q-Q plots) to assess the distribution of variables before and after transformation.  
**Formula**: N/A (visual diagnostic tool).  
**Example**:  
```python
def diagnostic_plots(df, variable):
    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    df[variable].hist(bins=30)
    plt.subplot(1, 2, 2)
    stats.probplot(df[variable], dist="norm", plot=plt)
    plt.show()
```  

---

### Key Links  
- [[Logarithmic Transformation]] (special case of power/Box-Cox for λ=0).  
- [[Power Transformation]] (general family of transformations).  
- [[Scikit-learn]], [[SciPy]], [[Feature-engine]] (libraries for implementation).

---

---

## 2026-06-17 13:13 — Practical 4.6 - Yeo-Johnson-transformation.ipynb
**Style:** structured_academic (experimenting)

# Summary: Yeo-Johnson Transformation

## Term 
[[Yeo-Johnson Transformation]]

---

### Definition 
The Yeo-Johnson transformation is an extension of the [[Box-Cox Transformation]] that generalizes power transformations to accommodate **variables with zero and negative values**, in addition to positive values. It applies different power functions based on the sign of the input data and the transformation parameter λ, aiming to stabilize variance and normalize data distributions.

---

### Formula 
The transformation is defined as a piecewise function:  
\[
X_t = 
\begin{cases} 
\frac{(X+1)^\lambda - 1}{\lambda} & \text{if } \lambda \neq 0, \, X \geq 0 \\
\log(X+1) & \text{if } \lambda = 0, \, X \geq 0 \\
-\frac{(-X+1)^{2-\lambda} - 1}{2-\lambda} & \text{if } \lambda \neq 2, \, X < 0 \\
-\log(-X+1) & \text{if } \lambda = 2, \, X < 0 \\
\end{cases}
\]  
where \(X\) is the original variable and \(\lambda\) is the transformation parameter optimized for normality.

---

### Example 

#### 1. **SciPy Implementation**  
```python
import scipy.stats as stats  

# Apply Yeo-Johnson to 'LSTAT' and retrieve optimal λ
data_tf['LSTAT'], param = stats.yeojohnson(data['LSTAT'])
print('Optimal λ:', param)  # Outputs the best λ for normalization
```

#### 2. **Scikit-learn (PowerTransformer)**  
```python
from sklearn.preprocessing import PowerTransformer  

# Initialize transformer with Yeo-Johnson method
transformer = PowerTransformer(method='yeo-johnson', standardize=False)

# Fit to selected columns (e.g., ['LSTAT', 'NOX', 'DIS', 'RM'])
transformer.fit(data[cols])

# Transform data and extract learned λ values
data_tf = pd.DataFrame(transformer.transform(data[cols]), columns=cols)
print('Lambdas:', transformer.lambdas_)  # Optimal λ for each variable
```

#### 3. **Feature-engine (YeoJohnsonTransformer)**  
```python
from feature_engine.transformation import YeoJohnsonTransformer  

# Initialize and fit transformer
yjt = YeoJohnsonTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])
yjt.fit(data)

# Transform data and inspect parameters
data_tf = yjt.transform(data)
print('Lambda dict:', yjt.lambda_dict_)  # Optimal λ per variable
```

---

### Key Notes 
- **Diagnostic Plots**: Use histograms and Q-Q plots (via `diagnostic_plots`) to compare distributions before/after transformation.  
- **Advantage**: Handles negative/zero values unlike [[Box-Cox Transformation]].  
- **Parameter Optimization**: Libraries like SciPy and Feature-engine automatically estimate the optimal λ for each variable.  

[[Power Transformation]] | [[Logarithmic Transformation]] | [[Box-Cox Transformation]]

---

---

## 2026-06-17 13:15 — Exercise_7 - Performing Feature Scaling.ipynb
**Style:** structured_academic (experimenting)

# Feature Scaling Techniques Summary

## [[Feature Scaling]]
### Definition
Process of standardizing the range of independent variables (features) in a dataset to ensure algorithms perform optimally. Critical for models sensitive to feature magnitude, such as linear regression, clustering, and principal component analysis (PCA).

### Formula
Varies by technique (see specific methods below)

### Example
```python
# Example from Exercise 7 (airbnb_sg dataset)
from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()
X_train_scaled = scaler.fit_transform(X_train)
```

---

## [[Standard Scaling (Z-score Normalization)]]
### Definition
Rescales data to have a mean (μ) of 0 and standard deviation (σ) of 1. Robust to outliers but assumes normal distribution.

### Formula
\[ z = \frac{x - \mu}{\sigma} \]

### Example
```python
# From Practical 7.1 - Standardization.ipynb
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Visualization
sns.kdeplot(X_train['RM'], label='Before')
sns.kdeplot(X_train_scaled['RM'], label='After')
```

---

## [[Robust Scaling]]
### Definition
Scales data using median and interquartile range (IQR), making it suitable for datasets with outliers.

### Formula
\[ x' = \frac{x - \text{median}(x)}{\text{IQR}(x)} \]
where IQR = Q3 - Q1

### Example
```python
# From Practical 7.5 - Robust-Scaling.ipynb
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Visualization for 'AGE' feature
sns.kdeplot(X_train['AGE'], label='Before')
sns.kdeplot(X_train_scaled['AGE'], label='After')
```

---

## [[Min-Max Scaling]]
### Definition
Scales data to a fixed range (typically [0, 1]) by adjusting to the minimum and maximum values.

### Formula
\[ x' = \frac{x - \min(x)}{\max(x) - \min(x)} \]

### Example
```python
# From Practical 7.3 - MinMaxScaling.ipynb
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Visualization for 'NOX' feature
sns.kdeplot(X_train['NOX'], label='Before')
sns.kdeplot(X_train_scaled['NOX'], label='After')
```

---

## [[MaxAbs Scaling]]
### Definition
Scales data by the maximum absolute value in the feature, preserving sparsity and useful for datasets with mixed positive/negative values.

### Formula
\[ x' = \frac{x}{\max(|x|)} \]

### Example
```python
# From Exercise 7 (airbnb_sg dataset)
scaler = MaxAbsScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Visualization for 'id' feature
sns.kdeplot(X_train['id'], label='Before')
sns.kdeplot(X_train_scaled['id'], label='After')
```

---

## [[KDE Plot (Kernel Density Estimate)]]
### Definition
Visualization tool used to compare feature distributions before and after scaling. Shows probability densities of continuous features.

### Formula
Non-parametric estimate of the probability density function:
\[ \hat{f}(x) = \frac{1}{n h} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right) \]
where \( K \) = kernel function, \( h \) = bandwidth

### Example
```python
# From Practical 7.4 - Maximum-Absolute-Scaling.ipynb
fig, (ax1, ax2) = plt.subplots(ncols=2)
sns.kdeplot(X_train['AGE'], ax=ax1)
sns.kdeplot(X_train_scaled['AGE'], ax=ax2)
```

---

---

## 2026-06-17 13:18 — Exercise_8 - Applying Mathematical Computations to Features.ipynb
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

---

---

## 2026-06-17 20:20 — Exercise_1 - Foreseeing Variable Problems When building ML Models.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the provided **Data Wrangling** notebook:

---

### **Term: Variable**  
**Definition**: A characteristic, number, or quantity measurable or countable in a dataset.  
**Formula**: N/A  
**Example**: In the Airbnb Singapore dataset (`airbnb_sg.csv`), variables include `price`, `neighbourhood`, and `reviews_per_month`.  

---

### **Term: Numerical Variable**  
**Definition**: A variable taking numeric values, either discrete (countable, e.g., number of bedrooms) or continuous (measurable, e.g., price).  
**Formula**: N/A  
**Example**: `price` (continuous) and `number_of_reviews` (discrete) in the dataset.  

---

### **Term: Categorical Variable**  
**Definition**: A variable with values selected from predefined categories (labels), e.g., text or ordinal labels.  
**Formula**: N/A  
**Example**: `neighbourhood` (e.g., "Downtown", "Orchard") in the Airbnb dataset.  

---

### **Term: Missing Data**  
**Definition**: Absent or null values in a dataset, often represented as `NaN` or empty cells.  
**Formula**: N/A  
**Example**: Identified using `data.isnull().mean()`; handled by dropping rows with `clean = data.dropna()`.  

---

### **Term: Cardinality**  
**Definition**: The number of unique categories in a categorical variable.  
**Formula**: N/A  
**Example**: Visualized using `clean.nunique().plot.bar()` to compare uniqueness across variables.  

---

### **Term: Rare Categories**  
**Definition**: Categories with very low frequency in a dataset, often requiring merging or removal.  
**Formula**: N/A  
**Example**: Neighbourhoods with <1% of Airbnb listings were highlighted using `label_freq.sort_values().plot.bar()` with a threshold line at `y=0.01`.  

---

### **Term: Linear Relationship**  
**Definition**: A straight-line relationship between two variables, indicating constant rate of change.  
**Formula**: \( y = mx + b \) (where \( m \) = slope, \( b \) = intercept)  
**Example**: Checked between `reviews_per_month` and `price` using `sns.lmplot()`, revealing a non-linear relationship.  

---

### **Term: Normal Distribution**  
**Definition**: A symmetric, bell-shaped probability distribution where most values cluster around the mean.  
**Formula**: \( f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}} \) (Gaussian function)  
**Example**: `price` was tested via `sns.histplot()` with `kde=True`, showing a non-normal skewed distribution.  

---

### **Term: Outlier Detection (IQR Method)**  
**Definition**: Identifying data points far from the median, often using the Interquartile Range (IQR).  
**Formula**:  
- \( IQR = Q3 - Q1 \)  
- Lower Bound: \( Q1 - 1.5 \times IQR \)  
- Upper Bound: \( Q3 + 1.5 \times IQR \)  
**Example**: Outliers in `price` were found using `find_boundaries()` and `np.where()`.  

---

### **Term: Feature Engineering**  
**Definition**: Transforming raw variables into formats suitable for machine learning models.  
**Formula**: N/A  
**Example**: Handling missing data via `dropna()`, encoding categorical variables, or scaling numerical features.  

---

### **Key Wikilinks**  
- [[Missing Data]] → [[Handling Missing Data]]  
- [[Categorical Variable]] → [[One-Hot Encoding]]  
- [[Outlier Detection]] → [[Interquartile Range (IQR)]]  
- [[Normal Distribution]] → [[Feature Scaling]]  

--- 

This summary aligns with the notebook’s focus on identifying variable characteristics (missingness, cardinality, distributions, outliers) to guide feature engineering for ML models.

---

---

## 2026-06-17 20:25 — Exercise_2 - Imputing Missing Data.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content on missing data imputation:

```markdown
# Key Concepts in Missing Data Imputation

## 1. [[Missing Data]]
**Definition**: Absent values in a dataset where no measurement or entry exists.  
**Formula**: Not applicable (phenomenological concept)  
**Example**: In `airbnb_sg.csv`, missing values were artificially introduced in columns like 'neighbourhood' and 'room_type' for demonstration.

## 2. [[Imputation]]
**Definition**: Process of replacing missing data with substituted values to create complete datasets for analysis.  
**Formula**: Not applicable (general process)  
**Example**: Using `SimpleImputer` to replace missing values in numerical columns with median or constants.

## 3. [[SimpleImputer (Scikit-learn)]]
**Definition**: Class for completing missing values in numeric/numeric data using strategies like mean, median, or constant.  
**Formula**: 
```python
imputer = SimpleImputer(strategy='median')  # or 'mean', 'constant'
```
**Example**: 
```python
imputer_num_med = Pipeline([('imputer', SimpleImputer(strategy='median'))])
```

## 4. [[ColumnTransformer]]
**Definition**: Scikit-learn class to apply different transformers to different columns of a dataset.  
**Formula**: 
```python
preprocessor = ColumnTransformer([
    ('num_med', imputer, num_median)
])
```
**Example**: Used to apply different imputation strategies to numerical vs categorical columns.

## 5. [[Pipeline (Scikit-learn)]]
**Definition**: Chain of data transformation steps executed sequentially.  
**Formula**: 
```python
pipeline = Pipeline([('step1', transformer1), ('step2', transformer2)])
```
**Example**: Combining imputers and transformers for numerical/missing categories.

## 6. [[Feature Engine]]
**Definition**: Advanced feature engineering library with specialized imputers.  
**Formula**: Not applicable (library reference)  
**Example**: Using `ArbitraryNumberImputer` and `CategoricalImputer` in a pipeline.

## 7. [[Arbitrary Number Imputer]]
**Definition**: Replaces missing values with user-specified arbitrary numbers.  
**Formula**: 
```python
ArbitraryNumberImputer(variables=columns, arbitrary_number=0)
```
**Example**: Used for `calculated_host_listings_count` and `host_id` with fill value 0.

## 8. [[Mean/Median Imputer]]
**Definition**: Replaces missing values with column mean or median.  
**Formula**: 
```python
MeanMedianImputer(imputation_method='median')
```
**Example**: Applied to `number_of_reviews` and `id` columns.

## 9. [[Categorical Imputer]]
**Definition**: Handles missing values in categorical data using frequency-based or placeholder strategies.  
**Formula**: 
```python
CategoricalImputer(imputation_method='most_frequent')
```
**Example**: 
- `most_frequent` for 'host_name' 
- 'Missing' placeholder for 'room_type'

## 10. [[Data Preprocessing Pipeline]]
**Definition**: Integrated workflow combining data splitting, transformation, and imputation.  
**Formula**: 
```python
pipe = Pipeline(steps=[...])
pipe.fit_transform(data)
```
**Example**: Complete pipeline from train/test split to final imputed datasets.
```

This summary connects key concepts through wikilinks while maintaining the required term-definition-formula-example structure. The content focuses on practical implementation details from the notebook while emphasizing statistical and machine learning principles.

---

---

## 2026-06-17 20:31 — Exercise_3 - Encoding Categorical Variables.ipynb
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

---

---

## 2026-06-17 20:39 — Exercise_4 - Transforming Numerical Variables.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured summary of the content using the required academic format:

---

### [[Data Transformation]]
**Definition**: Mathematical processes applied to modify the distribution of numerical variables to approximate normality, enhancing the performance of linear machine learning models.  
**Formula**: N/A (General concept)  
**Example**: Applying Yeo-Johnson transformation to `minimum_nights` and `number_of_reviews` in the `airbnb_sg` dataset to reduce skewness.

---

### [[Normal Distribution]]
**Definition**: A probability distribution where values are symmetrically distributed around the mean, forming a bell-shaped curve. Assumed by linear and logistic regression models for optimal performance.  
**Formula**:  
$$ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} $$  
**Example**: Diagnostic plots (histograms and Q-Q plots) revealed non-normal distributions for `minimum_nights` and `number_of_reviews` before transformation.

---

### [[Yeo-Johnson Transformation]]
**Definition**: A power transformation method that generalizes the Box-Cox transformation by allowing logarithmic transformations for negative values, making it suitable for datasets with zero or negative values.  
**Formula**:  
$$ y(\lambda) = \begin{cases} 
\frac{(x+1)^{\lambda} - 1}{\lambda} & \text{if } \lambda \neq 0 \text{ and } x \geq 0 \\
-\log(-x+1) & \text{if } \lambda = 0 \text{ and } x \geq 0 \\
\frac{(x+1)^{\lambda} - 1}{\lambda} & \text{if } \lambda \neq 0 \text{ and } x < 0 \\
-\log(-x+1) & \text{if } \lambda = 0 \text{ and } x < 0 
\end{cases} $$  
**Example**: Implemented via `PowerTransformer(method='yeo-johnson')` in Python to normalize distributions of `minimum_nights` and `number_of_reviews`.

---

### [[Q-Q Plot (Quantile-Quantile Plot)]]
**Definition**: A graphical tool to compare the distribution of a dataset against a theoretical distribution (e.g., normal) by plotting their quantiles. Deviations from the diagonal line indicate non-normality.  
**Formula**: N/A (Visual diagnostic tool)  
**Example**: Used in `diagnostic_plots()` function to assess normality of variables before and after Yeo-Johnson transformation.

---

### [[PowerTransformer]]
**Definition**: A scikit-learn class that applies power transformations (e.g., Yeo-Johnson, Box-Cox) to stabilize variance or normalize data distributions.  
**Formula**: N/A (Algorithmic implementation)  
**Example**:  
```python
transformer = PowerTransformer(method='yeo-johnson', standardize=False)
data_tf = transformer.fit_transform(data[['minimum_nights','number_of_reviews']])
```

---

### Key Observations from the Exercise:
1. **Before Transformation**:  
   - `minimum_nights` and `number_of_reviews` exhibited right-skewed distributions (non-normal).  
2. **After Yeo-Johnson Transformation**:  
   - Distributions became more symmetric, with reduced outliers and improved alignment to the normal distribution (observed via Q-Q plots).  
   - Values were "more evenly distributed" as noted in Task 7.  

---

This summary links critical concepts and demonstrates their application in the context of the `airbnb_sg` dataset. For deeper exploration of related methods, see [[Box-Cox Transformation]] or [[Feature Engineering]].

---

---

## 2026-06-17 20:44 — Exercise_5 - Performing Variable Discretization.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content on **Variable Discretization**:

---

### [[Discretization (Binning)]]
**Definition**:  
The process of converting continuous variables into discrete intervals (bins) to reduce the impact of outliers, handle skewed distributions, and improve model performance by creating homogeneous groups.

**Formula**:  
No direct formula, but involves dividing the range of a variable into intervals. For **equal-frequency bins**:  
\[ \text{Bin boundaries} = \text{Quantiles of the variable at intervals of } \frac{100\%}{\text{Number of bins}} \]  
For **equal-width bins**:  
\[ \text{Bin width} = \frac{\text{Max value} - \text{Min value}}{\text{Number of bins}} \]

**Example**:  
In the `airbnb_sg` dataset, `availability_365` and `calculated_host_listings_count` were binned using `EqualFrequencyDiscretiser` (10 bins):  
```python
disc = EqualFrequencyDiscretiser(q=10, variables=['availability_365', 'calculated_host_listings_count'])
```

---

### [[Equal Frequency Discretiser]]
**Definition**:  
An unsupervised discretization method that splits data into bins with **equal number of observations**, regardless of value ranges.

**Formula**:  
Bin boundaries are determined by quantiles:  
\[ Q_i = \text{Quantile}\left(\frac{i}{n}, 0 \leq i \leq n\right) \]  
where \( n \) = number of bins.

**Example**:  
```python
# Creates 10 bins with ~10% of data each
disc = EqualFrequencyDiscretiser(q=10, variables=['availability_365'])
```

---

### [[Equal Width Discretiser]]
**Definition**:  
An unsupervised discretization method that splits the variable’s range into bins of **equal size** (width).

**Formula**:  
\[ \text{Bin width} = \frac{\text{Max}(X) - \text{Min}(X)}{n} \]  
where \( n \) = number of bins.

**Example**:  
For a variable ranging from 0 to 100 with 10 bins:  
```python
# Bin widths = (100-0)/10 = 10
disc = EqualWidthDiscretiser(n_bins=10, variables=['price'])
```

---

### [[OrdinalEncoder (Ordered)]]
**Definition**:  
A supervised discretization method that orders categorical bins based on the **mean of the target variable**, ensuring a monotonic relationship.

**Formula**:  
Ranks bins by \( \mathbb{E}[Y | \text{Bin}_i] \), where \( Y \) is the target variable.

**Example**:  
```python
enc = OrdinalEncoder(encoding_method='ordered')
enc.fit(train_t, y_train)  # Orders bins by mean 'price'
```

---

### [[Monotonic Relationship]]
**Definition**:  
A relationship where an increase in one variable consistently corresponds to an increase (or decrease) in another variable. In discretization, this ensures ordered bins show a steady trend in the target.

**Formula**:  
For consecutive bins \( i \) and \( i+1 \):  
\[ \mathbb{E}[Y | \text{Bin}_i] \leq \mathbb{E}[Y | \text{Bin}_{i+1}] \]

**Example**:  
After applying `OrdinalEncoder`, the mean `price` by `availability_365` bins shows a steady increasing/decreasing trend:  
```python
pd.concat([train_t, y_train], axis=1).groupby('availability_365')['price'].mean().plot()
```

---

### Key Connections [[Wikilinks]]
- **Discretization** reduces the impact of [[Outliers]] and addresses [[Skewed Data]].  
- **Equal Frequency Discretiser** and **Equal Width Discretiser** are **unsupervised** methods, unlike supervised approaches like **OrdinalEncoder**.  
- **Monotonic Relationship** is critical for models requiring ordered categorical features (e.g., gradient-boosted trees).  

--- 

This summary aligns with the code and theory in the provided notebook, emphasizing practical implementation and theoretical foundations.

---

---

## 2026-06-17 20:49 — Exercise_6 - Working with Outliers.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured summary of the content using the requested academic format:

---

### **Outlier**  
**Definition**: A data point significantly different from the rest of the dataset, often influencing statistical parameters (e.g., mean, variance) and machine learning model performance.  
**Formula**: N/A  
**Example**: In the `airbnb_sg` dataset, extreme values in the `price` column (e.g., $10,000/night) were identified as outliers using boxplots.  

---

### **Trimming**  
**Definition**: A technique to remove observations containing outliers from the dataset.  
**Formula**: N/A  
**Example**: Not directly applied in the code, but discussed as an alternative to capping.  

---

### **Capping (Winsorization)**  
**Definition**: Replacing outlier values with a specified threshold (e.g., percentile-based caps) to limit their influence.  
**Formula**:  
- Lower cap: \( \text{Quantile}(1 - \text{fold}) \)  
- Upper cap: \( \text{Quantile}(\text{fold}) \)  
**Example**:  
```python
windsorizer = Winsorizer(capping_method='quantiles', tail='both', fold=0.05, variables=['price'])
data_t = windsorizer.transform(data)
```  
Here, `price` values beyond the 5th and 95th percentiles were capped.  

---

### **Interquartile Range (IQR)**  
**Definition**: A measure of statistical dispersion, calculated as the difference between the 75th percentile (Q3) and 25th percentile (Q1) of a dataset. Used to detect outliers.  
**Formula**:  
\[ \text{IQR} = Q3 - Q1 \]  
**Example**: In Exercise 1, IQR was used to define outlier boundaries:  
```python
lower_boundary = Q1 - (IQR * distance)  
upper_boundary = Q3 + (IQR * distance)
```  

---

### **Boxplot**  
**Definition**: A graphical representation showing the distribution of data through quartiles, medians, and outliers.  
**Formula**: N/A  
**Example**:  
```python
sns.boxplot(y=data['price'])  # Visualized outliers in the original data
```  

---

### **Winsorization**  
**Definition**: A specific form of capping where outliers are replaced with the nearest non-outlier values (e.g., 5th or 95th percentile).  
**Formula**:  
- Capped value = \( \max(\min(x, \text{Upper Cap}), \text{Lower Cap}) \)  
**Example**: Applied in Code Cell 11 to limit `price` outliers using 5% folds.  

---

### **Diagnostic Plots**  
**Definition**: Visual tools (histogram, Q-Q plot, boxplot) to compare data distributions before and after outlier handling.  
**Formula**: N/A  
**Example**:  
```python
diagnostic_plots(data_t, 'price')  # Compared distributions pre/post Winsorization
```  

---

### Key Connections  
- Outliers are often detected using [[Interquartile Range (IQR)]] or boxplots.  
- Handling techniques include [[Trimming]], [[Capping]], or [[Winsorization]].  
- [[Winsorization]] is implemented via libraries like `feature_engine` in Python.  

Let me know if you need further refinements!

---

---

## 2026-06-17 20:55 — Practical 1.0 - Data Preparation_Titanic.ipynb
**Style:** structured_academic (experimenting)

# Structured Academic Summary  

## [[Data Preprocessing]]  
**Definition**: The process of cleaning, transforming, and preparing raw data for analysis or modeling.  
**Formula**: Not applicable.  
**Example**:  
```python  
# Cabin extraction function  
def get_first_cabin(row):  
    try:  
        return row.split()[0]  
    except:  
        return np.nan  

# Handling missing data  
data = data.replace('?', np.nan)  

# Applying custom function  
data['cabin'] = data['cabin'].apply(get_first_cabin)  
```  

---

## [[NumPy]]  
**Definition**: A library for numerical computing in Python, providing support for arrays, matrices, and mathematical operations.  
**Formula**: `np.array([1, 2, 3])` (creates a NumPy array).  
**Example**:  
```python  
import numpy as np  # Importing NumPy  
```  

---

## [[Pandas]]  
**Definition**: A library for data manipulation and analysis in Python, built on NumPy.  
**Formula**: `pd.DataFrame(data)` (creates a Pandas DataFrame).  
**Example**:  
```python  
import pandas as pd  # Importing Pandas  
```  

---

## [[Feature Engineering]]  
**Definition**: The process of transforming raw data into meaningful features for machine learning models.  
**Formula**: Not applicable.  
**Example**:  
```python  
# Installing Feature Engine (commented)  
# pip install feature_engine  
```  

---

## [[Cabin Extraction Function]]  
**Definition**: A custom function to extract the first character from a cabin string (e.g., "C123" → "C").  
**Formula**: `row.split()[0]` (splits the string and returns the first element).  
**Example**:  
```python  
def get_first_cabin(row):  
    try:  
        return row.split()[0]  
    except:  
        return np.nan  
```  

---

## [[Data Loading from URL]]  
**Definition**: The process of loading data directly from a web URL into a Pandas DataFrame.  
**Formula**: `pd.read_csv('URL')` (loads CSV data from a URL).  
**Example**:  
```python  
data = pd.read_csv('https://www.openml.org/data/get_csv/16826755/phpMYEkMl')  
```  

---

## [[Handling Missing Data]]  
**Definition**: The process of identifying and addressing missing or invalid values in a dataset.  
**Formula**: `data.replace('value', np.nan)` (replaces specified values with NaN).  
**Example**:  
```python  
data = data.replace('?', np.nan)  
```  

---

## [[Applying Custom Function to Column]]  
**Definition**: Using the `.apply()` method to transform values in a DataFrame column with a custom function.  
**Formula**: `data['column'].apply(function_name)`.  
**Example**:  
```python  
data['cabin'] = data['cabin'].apply(get_first_cabin)  
```  

---

## [[Saving DataFrame to CSV]]  
**Definition**: Exporting a Pandas DataFrame to a CSV file for storage or sharing.  
**Formula**: `data.to_csv('path/to/file.csv', index=False)`.  
**Example**:  
```python  
data.to_csv('data/titanic.csv', index=False)  # Save to "data" subfolder  
```  

--- 

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).

---

---

## 2026-06-17 21:04 — Practical 1.1 - Identifying-Variables-Types.ipynb
**Style:** structured_academic (experimenting)

### Identifying Variable Types

#### Numerical Variables
- **Definition**: Variables that can take on any value within a range.
  - **Discrete**: Countable values with finite steps. E.g., `sibsp` (number of siblings/spouses aboard).
  - **Continuous**: Any value in an interval, often measured. E.g., `fare`.
  
#### Categorical Variables
- **Definition**: Non-numeric variables that represent categories or labels.
  - **Example**: `embarked`, representing the boarding port.

#### Mixed Variables
- **Definition**: Variables with mixed types or values that do not fit neatly into numerical or categorical categories. E.g., `cabin`.

### Key Code Examples

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic dataset
data = pd.read_csv("./data/titanic.csv")

# Print variable types
data.dtypes

# Inspect unique values - discrete variable
data['sibsp'].unique()

# Inspect unique values - continuous variable
data['fare'].unique()[0:20]

# Inspect unique values - categorical variable
data['embarked'].unique()

# Inspect unique values - mixed variable
data['cabin'].unique()[0:20]

# Plot histograms of discrete variables
data['sibsp'].hist(bins=20)

# Plot histogram of continuous variable
data['fare'].hist(bins=50)

# Bar plot for categorical variables
data['embarked'].value_counts().plot.bar()
plt.xticks(rotation=0)
plt.ylabel('Number of passengers')
plt.title('Embarked - Port')
```

### Example from Exercise_2 - Imputing Missing Data.ipynb (data_wrangling):

```python
# Task 2: find categorical variables 
cat_cols = [c for c in X_train.columns if data[c].dtypes=='O'] # This approach of populating cat_cols is called list comprehension.
X_train[cat_cols].head()
print(cat_cols)
```

### Summary

- **Discrete Variables**: `sibsp`
- **Continuous Variables**: `fare`
- **Categorical Variables**: `embarked`, `cabin`
- **Mixed Variables**: `cabin` (mixed alphanumeric data)

These examples demonstrate how to identify and visualize different types of variables in the Titanic dataset using Python libraries like pandas and matplotlib.

---

---

## 2026-06-17 21:10 — Practical 1.2 - Quantifying-Missing-Data.ipynb
**Style:** structured_academic (experimenting)

# Summary of Key Concepts in Data Wrangling

## [[Missing Data]]
**Definition**: The absence of values for certain observations within a variable, commonly encountered in real-world datasets.  
**Formula**: Not applicable (descriptive concept).  
**Example**:  
```python
# Detect missing values in the dataset
data.isnull().sum()  # Quantify total missing values per variable
data.isnull().mean()  # Calculate percentage of missing values per variable
```

---

## [[Quantifying Missing Values]]
**Definition**: The process of measuring the extent of missing data in a dataset, either as absolute counts or relative percentages.  
**Formula**:  
- Absolute count: \( \text{Total Missing} = \sum (\text{isnull()}) \)  
- Percentage: \( \text{Percentage Missing} = \frac{\text{Total Missing}}{\text{Total Observations}} \times 100 \)  
**Example**:  
```python
# Calculate percentage of missing values per variable
data.isnull().mean().plot.bar(figsize=(12,6))
plt.ylabel('Percentage of Missing Values')
plt.xlabel('Variables')
plt.title('Quantifying Missing Data')
```

---

## [[Visualizing Missing Data]]
**Definition**: Representing the distribution and proportion of missing values graphically to identify patterns or outliers.  
**Formula**: Not applicable (visualization technique).  
**Example**:  
```python
# Bar plot of missing value percentages
data.isnull().mean().plot.bar(figsize=(12,6))
plt.ylabel('Percentage of Missing Values')
plt.xlabel('Variables')
plt.title('Visualizing Missing Data')
plt.show()
```

---

## [[Variables]]
**Definition**: Characteristics or attributes measured in a dataset, categorized into numerical or categorical types.  
**Subtypes**:  
- **Numerical Variables**: Discrete (countable, e.g., `NUMCHLD`) or continuous (measurable, e.g., `INCOME`).  
- **Categorical Variables**: Represented by labels (e.g., `MBCRAFT`).  
**Example**:  
```python
# Select and load specific variables from the dataset
cols = ['AGE', 'NUMCHLD', 'INCOME', 'WEALTH1', 'MBCRAFT', 'MBGARDEN', 'MBBOOKS', 'MBCOLECT', 'MAGFAML', 'MAGFEM', 'MAGMALE']
data = pd.read_csv('./data/cup98LRN.txt', usecols=cols)
```

---

## [[Imputation]]
**Definition**: The process of replacing missing values with statistical estimates to create a complete dataset for machine learning models.  
**Formula**: Not applicable (process-dependent, e.g., mean imputation: \( \text{Imputed Value} = \text{Mean of Observed Values} \)).  
**Example**:  
```python
# Example of mean imputation (not shown in provided code)
data['COLUMN_NAME'].fillna(data['COLUMN_NAME'].mean(), inplace=True)
```

---

## Related Concepts  
- [[Scikit-learn]]: A Python library that requires complete numerical data, necessitating imputation or removal of missing values.  
- [[Outliers]]: Data points significantly deviating from the norm, often addressed alongside missing data.  

This summary integrates concepts from the provided notebooks, emphasizing practical implementation in Python.

---

---

## 2026-06-17 21:15 — Practical 1.3 - Determining-Cardinality.ipynb
**Style:** structured_academic (experimenting)

# Summary: Cardinality and Categorical Variables  

## [[Cardinality]]  
**Definition**: The number of unique categories present in a categorical variable.  
**Formula**:  
\[ \text{Cardinality} = \text{Number of distinct categories} \]  
**Example**:  
- Variable `GENDER` with categories `['male', 'female']` has a cardinality of **2**.  
- Variable `civil status` with categories `['married', 'divorced', 'single', 'widow']` has a cardinality of **4**.  

---

## [[Categorical Variable]]  
**Definition**: A variable whose values represent categories or labels (e.g., "male/female," "city names"). These can be **nominal** (no intrinsic order) or **ordinal** (ordered categories).  
**Formula**: N/A  
**Example**:  
- `GENDER` (values: "male," "female") is a **nominal** categorical variable.  
- `Student's grade` (values: "A," "B," "C," "Fail") is an **ordinal** categorical variable.  

---

## [[Missing Data]]  
**Definition**: The absence of values for certain observations in a variable, often represented as `NaN` (Not a Number) in datasets.  
**Formula**: N/A  
**Example**:  
- Empty strings (`' '`) in the dataset were replaced with `np.nan` to standardize missing values:  
  ```python  
  data = data.replace(' ', np.nan)  
  ```  

---

## [[Data Visualization]]  
**Definition**: The graphical representation of data to identify patterns or insights (e.g., bar charts for cardinality).  
**Formula**: N/A  
**Example**:  
- A bar chart visualizing cardinality across variables:  
  ```python  
  data.nunique().plot.bar(figsize=(12,6))  
  plt.ylabel('Number of unique categories')  
  plt.xlabel('Variables')  
  plt.title('Cardinality')  
  ```  

---

## Key Code Concepts  
1. **`nunique()`**: Pandas function to calculate cardinality (ignores `NaN` by default).  
   ```python  
   data.nunique()  # Excludes missing values  
   data.nunique(dropna=False)  # Includes missing values as a category  
   ```  
2. **`unique()`**: Retrieves unique categories in a variable:  
   ```python  
   data['GENDER'].unique()  # Returns array of unique labels  
   ```  

--- 

This summary integrates concepts from data wrangling, emphasizing the importance of understanding variable characteristics for machine learning workflows. Related terms like [[Variable Types]] and [[Feature Engineering]] may further contextualize these ideas.

---

---

## 2026-06-17 21:20 — Practical 1.4 - Pinpointing-Rare-Categories.ipynb
**Style:** structured_academic (experimenting)

# Summary: Identifying Rare Categories and Cardinality in Datasets

## **1. Rare Categories**  
**Definition**: Categories in a dataset that represent a tiny minority of observations, typically defined as those occurring in less than **5% or 1%** of the total data points.  
**Formula**:  
Frequency of a category = \( \frac{\text{Count of category}}{\text{Total number of observations}} \)  
**Example**:  
In the Car Evaluation dataset, the frequency of the "class" categories (e.g., "unacc", "acc", "good", "vgood") is calculated using:  
```python
label_freq = data['class'].value_counts() / len(data)
```  
A horizontal line at `y=0.05` in the bar plot visualizes the 5% threshold for rare categories.

---

## **2. Cardinality**  
**Definition**: The number of **unique categories** present in a categorical variable.  
**Formula**:  
Cardinality = \( \text{Number of unique values in a variable} \)  
**Example**:  
For the "class" variable in the Car Evaluation dataset:  
```python
data['class'].nunique()  # Output: 4 (e.g., "unacc", "acc", "good", "vgood")
```  

---

## **3. Frequency Calculation**  
**Definition**: The proportion of observations belonging to each category in a dataset.  
**Formula**:  
Frequency = \( \frac{\text{Count of category}}{\text{Total observations}} \)  
**Example**:  
```python
total_cars = len(data)  # Total observations
label_freq = data['class'].value_counts() / total_cars  # Frequency per category
```  

---

## **4. Visualization of Category Frequencies**  
**Definition**: A graphical representation (e.g., bar chart) to compare the frequency of categories and identify rare ones.  
**Formula**: N/A  
**Example**:  
```python
fig = label_freq.sort_values(ascending=False).plot.bar()
fig.axhline(y=0.05, color='red')  # 5% threshold line
fig.set_title('Identifying Rare Categories')
plt.show()
```  
This plot highlights categories below the 5% threshold as rare.

---

## **Key Links**  
- [[Variable Types]]: Distinguishes categorical vs. numerical variables.  
- [[Data Preprocessing]]: Context for handling rare categories in ML workflows.  
- [[Cardinality]]: Further implications of high/low cardinality in models.

---

---

## 2026-06-17 21:28 — Practical 1.5 - Identifying-a-Linear-Relationship.ipynb
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

---

---

## 2026-06-17 21:33 — Practical 1.6 - Identifying-a-Normal-Distribution.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the content, organized by key terms with definitions, formulas, and examples:

---

### [[Normal Distribution]]  
**Definition**: A continuous probability distribution characterized by a symmetric, bell-shaped curve, where data points cluster around the mean and taper toward the extremes. It is foundational for many statistical assumptions, including those in linear models.  
**Formula**:  
The probability density function (PDF) is given by:  
$$ f(x \mid \mu, \sigma^2) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} $$  
where $\mu$ is the mean, $\sigma^2$ is the variance, and $x$ is the variable.  
**Example**:  
In Code Cell 6, a simulated variable `x` is generated using `np.random.randn(n)`, which follows a standard normal distribution ($\mu=0$, $\sigma=1$). This serves as a benchmark for assessing normality in other variables (e.g., `RM`, `LSTAT` in the Boston dataset).

---

### [[Histogram]]  
**Definition**: A graphical representation of the distribution of a dataset, where data is divided into bins, and the frequency or density of values in each bin is displayed. Used to visually assess normality.  
**Formula**: Not directly applicable, but related to density estimation:  
$$ \text{Density} = \frac{\text{Frequency}}{\text{Bin Width} \times \text{Total Observations}} $$  
**Example**:  
In Code Cell 4, `sns.histplot(boston['RM'], bins=30, kde=True)` generates a histogram for the `RM` variable (average number of rooms per dwelling) with a kernel density estimate (KDE) overlay to compare against a normal distribution. Similarly, Code Cell 5 visualizes `LSTAT` (lower status population percentage).

---

### [[Q-Q Plot]]  
**Definition**: A quantile-quantile plot used to compare the distribution of a dataset against a theoretical distribution (e.g., normal) or another dataset. Deviations from the reference line indicate non-normality.  
**Formula**:  
Theoretical quantiles ($Q_{\text{theoretical}}$) vs. sample quantiles ($Q_{\text{sample}}$):  
$$ Q_{\text{theoretical}} = F^{-1}(F(Q_{\text{sample}})) $$  
where $F$ is the cumulative distribution function (CDF) of the reference distribution.  
**Example**:  
In Exercise_4’s `diagnostic_plots` function, `stats.probplot(df[variable], dist="norm")` generates Q-Q plots for variables like `minimum_nights` and `number_of_reviews` to check alignment with a normal distribution.

---

### [[Linear Relationship]]  
**Definition**: A relationship between two variables where the dependent variable changes in a straight-line fashion relative to the independent variable. Linear models assume such relationships.  
**Formula**:  
$$ y = \beta_0 + \beta_1 x + \epsilon $$  
where $\beta_0$ is the intercept, $\beta_1$ is the slope, and $\epsilon$ represents error terms.  
**Example**:  
In Practical 1.5, `sns.lmplot(x="LSTAT", y="MEDV")` visualizes a scatter plot of `LSTAT` (independent variable) vs. `MEDV` (dependent variable, median house value) with a regression line, demonstrating a linear relationship.

---

### Key Connections  
- **Normality Assessment**: Histograms and Q-Q plots are tools to verify if variables (e.g., `RM`, `LSTAT`, simulated `x`) meet the normality assumption required for linear models.  
- **Linear Models**: The assumption of linearity (e.g., `LSTAT` vs. `MEDV`) relies on variables adhering to distributions that support such relationships.  

For further exploration of related concepts, see [[Outliers]], [[Data Transformation]], and [[Scatter Plot]].

---

---

## 2026-06-17 21:39 — Practical 1.7 - Distinguishing-Variable-Distribution.ipynb
**Style:** structured_academic (experimenting)

# Summary of Practical: Visualizing Variable Distributions  

## **Data Visualization**  
**Definition**: The practice of representing data graphically to identify patterns, trends, and relationships.  
**Formula**: N/A  
**Example**:  
```python  
import matplotlib.pyplot as plt  
# Generate histograms for all variables in the Boston dataset  
boston.hist(bins=30, figsize=(12,12), density=True)  
plt.show()  
```  
**Link**: [[Histogram]]  

---

## **Histogram**  
**Definition**: A graphical representation showing the distribution of numerical data by grouping values into bins. The `density=True` parameter normalizes the histogram to form a probability density curve.  
**Formula**:  
Probability Density = $ \frac{\text{Frequency of Bin}}{\text{Bin Width} \times \text{Total Observations}} $  
**Example**:  
```python  
# Create a histogram for the Boston dataset with 30 bins and density normalization  
boston.hist(bins=30, figsize=(12,12), density=True)  
plt.show()  
```  
**Link**: [[Data Visualization]]  

---

## **Boston Housing Dataset**  
**Definition**: A classic dataset containing housing prices and features (e.g., crime rates, number of rooms) for Boston suburbs, commonly used for regression analysis and exploratory data analysis.  
**Formula**: N/A  
**Example**:  
```python  
# Load the Boston Housing Dataset  
boston = pd.read_csv("./data/boston_local.csv")  
boston.head()  # Display the first few rows  
```  
**Link**: [[Regression Analysis]]  

---

## **Density Plot**  
**Definition**: A visualization that smooths the data to show the probability density of a variable, often overlaid on histograms. In this context, `density=True` in `hist()` achieves a similar effect.  
**Formula**: Same as [[Histogram]] probability density formula.  
**Example**:  
```python  
# Histogram with density normalization (approximating a density plot)  
boston.hist(bins=30, figsize=(12,12), density=True)  
plt.show()  
```  
**Link**: [[Histogram]]  

---

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)

---

---

## 2026-06-17 21:47 — Practical 1.8 - Highlighting-Outliers.ipynb
**Style:** structured_academic (experimenting)

# Summary: Outlier Detection and Handling

## [[Outlier]]  
**Definition**: A data point that significantly deviates from the rest of the data, potentially arising from a different mechanism (Hawkins, 1980).  
**Formula**: Not applicable directly; detected using statistical rules like the IQR proximity rule.  
**Example**:  
```python  
# Identify outliers in 'RM' column using IQR  
outliers = np.where(boston['RM'] > upper_boundary, True, np.where(boston['RM'] < lower_boundary, True, False))  
```  

---

## [[Boxplot]]  
**Definition**: A graphical tool displaying the distribution of data, highlighting the inter-quartile range (IQR), median, and outliers via whiskers and boxes.  
**Formula**: Not applicable.  
**Example**:  
```python  
# Generate boxplot for 'RM'  
sns.boxplot(y=boston['RM'])  
plt.title('Boxplot')  
```  

---

## [[Inter-quartile Range (IQR)]]  
**Definition**: The range between the 25th percentile (Q1) and 75th percentile (Q3) of a dataset.  
**Formula**:  
\[ \text{IQR} = Q3 - Q1 \]  
**Example**:  
```python  
# Calculate IQR for 'RM'  
IQR = boston['RM'].quantile(0.75) - boston['RM'].quantile(0.25)  
```  

---

## [[Inter-quartile Range Proximity Rule]]  
**Definition**: A method to identify outliers as data points lying outside \( \text{Q1} - 1.5 \times \text{IQR} \) or \( \text{Q3} + 1.5 \times \text{IQR} \).  
**Formula**:  
- Upper boundary: \( \text{Q3} + 1.5 \times \text{IQR} \)  
- Lower boundary: \( \text{Q1} - 1.5 \times \text{IQR} \)  
**Example**:  
```python  
# Define boundaries with distance parameter  
def find_boundaries(df, variable, distance):  
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)  
    lower = df[variable].quantile(0.25) - (IQR * distance)  
    upper = df[variable].quantile(0.75) + (IQR * distance)  
    return upper, lower  
```  

---

## [[Discretization]]  
**Definition**: The process of converting continuous variables into discrete intervals (bins) to reduce the impact of outliers.  
**Formula**: Not applicable.  
**Example**: Refer to Practical 5 for techniques like equal-frequency binning, which groups outliers into extreme bins, treating them similarly to other tail values.  

---

# Connections to Related Concepts  
- Outliers can distort statistical measures (e.g., mean) and affect models like [[Linear Regression]].  
- Handling outliers may involve [[Discretization]] or [[Imputation]] (see Practical 2).  
- Boxplots visually identify outliers using the IQR proximity rule.

---

---

## 2026-06-17 21:51 — Practical 1.9 - Comparing-Feature-Magnitude.ipynb
**Style:** structured_academic (experimenting)

```markdown
# Summary: Feature Scaling and Statistical Analysis in Machine Learning

## [[Feature Scaling]]  
**Definition**: The process of normalizing the range of independent variables (features) in a dataset to ensure machine learning algorithms perform effectively. Algorithms like SVM, KNN, and gradient descent are sensitive to feature scales.  
**Formula**: Standardization (Z-score normalization):  
$$
X_{\text{scaled}} = \frac{X - \mu}{\sigma}
$$  
where \( \mu \) is the mean and \( \sigma \) is the standard deviation.  
**Example**: In the Boston Housing dataset, features like `CRIM` (0–89), `CHAS` (0–1), and `RM` (3.5–8.8) exhibit vastly different scales, necessitating scaling for consistent model performance.

---

## [[Statistical Metrics]]  
**Definition**: Quantitative measures used to summarize the distribution and characteristics of a dataset’s features. Key metrics include mean, standard deviation, quartiles, minimum, and maximum values.  
**Formula**:  
- Mean: \( \mu = \frac{1}{n} \sum_{i=1}^{n} x_i \)  
- Standard Deviation: \( \sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2} \)  
- Interquartile Range (IQR): \( Q3 - Q1 \)  
**Example**: The `boston.describe()` output provides summary statistics (e.g., `CRIM` has a mean of 3.6, std of 8.6, and range 0–89).

---

## [[Feature Magnitude]]  
**Definition**: The scale or range of values a feature takes, which impacts model training. Features with larger magnitudes can dominate others if not scaled.  
**Formula**: N/A (observed via statistical metrics).  
**Example**: In the Boston dataset, `CRIM` (crime rate) has a much larger magnitude (0–89) compared to `CHAS` (Charles River proximity, 0–1), indicating a need for scaling.

---

## [[Range of Variables]]  
**Definition**: The difference between the maximum and minimum values of a feature, indicating its spread.  
**Formula**:  
$$
\text{Range} = \max(X) - \min(X)
$$  
**Example**: The code `boston.max() - boston.min()` calculates the range for each feature (e.g., `CRIM` range = 89 - 0 = 89).

---

## Key Takeaways  
- Machine learning algorithms often require **feature scaling** to handle varying feature magnitudes.  
- **Statistical metrics** (mean, std, quartiles) and **range** provide insights into feature distributions.  
- The Boston Housing dataset illustrates how unscaled features (e.g., `CRIM`, `RM`) can distort model training.
```

---

---

## 2026-06-17 21:56 — Practical 2.0 - Data Preparation_CreditApprovalUCI.ipynb
**Style:** structured_academic (experimenting)

# Summary: Credit Approval Dataset Preparation

## [[Data Preprocessing]]
**Definition**: Steps taken to transform raw data into a suitable format for analysis, including handling missing values, converting data types, and encoding variables.  
**Example**:  
```python
data = pd.read_csv('./data/crx.data', header=None)  # Load raw data
data.replace('?', np.nan)  # Handle missing values
data['A2'] = data['A2'].astype('float')  # Convert data types
```

---

## [[Missing Data Handling]]
**Definition**: Process of addressing absent or undefined values in a dataset.  
**Formula**: Not applicable (procedural step).  
**Example**:  
```python
data = data.replace('?', np.nan)  # Replace placeholder '?' with NaN
random.seed(9001)
values = list(set([random.randint(0, len(data)) for p in range(0, 100)]))
for var in ['A3', 'A8', 'A9', 'A10']: 
    data.loc[values, var] = np.nan  # Introduce artificial missing values
```

---

## [[Variable Type Conversion]]
**Definition**: Transforming variables into appropriate numerical or categorical formats.  
**Example**:  
```python
data['A2'] = data['A2'].astype('float')  # Convert column A2 to float
data['A14'] = data['A14'].astype('float')  # Convert column A14 to float
```

---

## [[Target Variable Encoding]]
**Definition**: Converting categorical target variables into numerical binary values (0/1).  
**Example**:  
```python
data['A16'] = data['A16'].map({'+':1, '-':0})  # Map '+' to 1 and '-' to 0
```

---

## [[Categorical Variable Identification]]
**Definition**: Identifying variables with non-numeric (object) data types.  
**Example**:  
```python
cat_cols = [c for c in data.columns if data[c].dtypes=='O']  # List categorical columns
data[cat_cols].head()  # Display first 5 rows of categorical variables
```

---

## [[Numerical Variable Identification]]
**Definition**: Identifying variables with integer or numeric data types.  
**Example**:  
```python
num_cols = [n for n in data.columns if data[n].dtypes=='int']  # List numerical columns
data[num_cols].head()  # Display first 5 rows of numerical variables
```

---

## [[Artificial Missing Data Generation]]
**Definition**: Introducing random missing values to simulate real-world data challenges.  
**Example**:  
```python
random.seed(9001)
values = list(set([random.randint(0, len(data)) for p in range(0, 100)]))
for var in ['A3', 'A8', 'A9', 'A10']: 
    data.loc[values, var] = np.nan  # Assign NaN to random positions
```

---

## [[Data Saving]]
**Definition**: Exporting processed data to a file for future use.  
**Example**:  
```python
data.to_csv('./data/creditApprovalUCI.csv', index=False)  # Save as CSV
```

---

**Source**: Adapted from *Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*.  
**Dataset Source**: [UCI Credit Approval Dataset](http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/)

---

---

## 2026-06-17 22:02 — Practical 2.10 - Assembling-an-imputation-pipeline-with-Feature-Engine.ipynb
**Style:** structured_academic (experimenting)

## Summary: Imputation Techniques with Feature-engine

### [[Arbitrary Number Imputer]]  
**Definition**: Replaces missing values in numerical features with a user-specified arbitrary constant (e.g., 0, -999).  
**Formula**: \( X_{\text{missing}} = c \) (where \( c \) is the chosen constant).  
**Example**:  
```python
('imp_num_arbitrary', mdi.ArbitraryNumberImputer(variables = features_num_arbitrary))
```

---

### [[Mean/Median Imputer]]  
**Definition**: Imputes missing values in numerical features using either the mean or median of the observed data.  
**Formula**:  
- Median: \( X_{\text{missing}} = \text{median}(X) \)  
- Mean: \( X_{\text{missing}} = \text{mean}(X) \)  
**Example**:  
```python
('imp_num_median', mdi.MeanMedianImputer(imputation_method = 'median', variables=features_num_median))
```

---

### [[Categorical Imputer (Frequent)]]  
**Definition**: Fills missing values in categorical features with the most frequent category (mode) observed in the data.  
**Formula**: \( X_{\text{missing}} = \text{mode}(X) \)  
**Example**:  
```python
('imp_cat_frequent', mdi.CategoricalImputer(variables = features_cat_frequent, imputation_method='frequent'))
```

---

### [[Categorical Imputer (Missing)]]  
**Definition**: Replaces missing values in categorical features with a placeholder value (e.g., "Missing").  
**Formula**: \( X_{\text{missing}} = \text{"Missing"} \)  
**Example**:  
```python
('imp_cat_missing', mdi.CategoricalImputer(variables=features_cat_missing, imputation_method='missing'))
```

---

### [[Pipeline (Scikit-learn)]]  
**Definition**: A sequential workflow that chains multiple preprocessing steps (e.g., imputers) into a single object. Each step is applied in order.  
**Formula**: \( \text{Pipeline} = \text{Step1} \rightarrow \text{Step2} \rightarrow \ldots \rightarrow \text{StepN} \)  
**Example**:  
```python
pipe = Pipeline(steps=[ 
    ('imp_num_arbitrary', mdi.ArbitraryNumberImputer(variables = features_num_arbitrary)),
    ('imp_num_median', mdi.MeanMedianImputer(imputation_method = 'median', variables=features_num_median)),
    ('imp_cat_frequent', mdi.CategoricalImputer(variables = features_cat_frequent, imputation_method='frequent')),
    ('imp_cat_missing', mdi.CategoricalImputer(variables=features_cat_missing, imputation_method='missing'))
])
```

---

### [[Credit Approval Dataset]]  
**Definition**: A dataset used for demonstrating imputation techniques, containing numerical and categorical features with missing values.  
**Example**:  
```python
data = pd.read_csv("./data/creditApprovalUCI.csv")
```

---

### Key Workflow Steps  
1. **Data Splitting**:  
   ```python
   X_train, X_test, y_train, y_test = train_test_split(data.drop('A16', axis=1), data['A16'], test_size=0.3, random_state=0)
   ```
2. **Imputation Pipeline**:  
   - Fit the pipeline to training data: `pipe.fit(X_train)`  
   - Transform train/test data: `X_train = pipe.transform(X_train)`  

---

### Outcome  
- Missing values are replaced based on feature type (numerical/categorical) and imputation strategy.  
- Final dataset retains original column order (as per Feature-engine behavior).

---

---

## 2026-06-17 22:08 — Practical 2.2 - Performing-mean-or-median-imputation.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

## **Mean Imputation**  
**Definition**: A technique replacing missing values in numerical variables with the **mean** (average) of observed values in the training set.  
**Formula**:  
\[
\text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n}
\]  
**Example**:  
```python
# Using pandas
for var in ['A2', 'A3', 'A8', 'A11', 'A15']:
    value = X_train[var].mean()
    X_train[var] = X_train[var].fillna(value)
    X_test[var] = X_test[var].fillna(value)
```

---

## **Median Imputation**  
**Definition**: A technique replacing missing values in numerical variables with the **median** (middle value) of observed values in the training set.  
**Formula**:  
\[
\text{Median} = 
\begin{cases} 
x_{\frac{n}{2}} & \text{if } n \text{ is even} \\
\frac{x_{\frac{n}{2}-1} + x_{\frac{n}{2}}}{2} & \text{if } n \text{ is odd}
\end{cases}
\]  
**Example**:  
```python
# Using Feature-engine's MeanMedianImputer
median_imputer = MeanMedianImputer(imputation_method='median', variables=['A2', 'A3', 'A8', 'A11', 'A15'])
median_imputer.fit(X_train)
X_train = median_imputer.transform(X_train)
```

---

## **SimpleImputer (Scikit-learn)**  
**Definition**: A scikit-learn class for imputation that supports strategies like `mean`, `median`, or `constant`. Learns imputation values from the training set.  
**Formula**: N/A (Implementation-dependent)  
**Example**:  
```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
imputer.fit(X_train)  # Learns median values
X_train = imputer.transform(X_train)  # Imputes missing values
```

---

## **MeanMedianImputer (Feature-engine)**  
**Definition**: A Feature-engine transformer for mean or median imputation, providing additional functionality like storing imputation values in a dictionary.  
**Formula**: N/A (Implementation-dependent)  
**Example**:  
```python
from feature_engine.imputation import MeanMedianImputer
median_imputer = MeanMedianImputer(imputation_method='median', variables=['A2', 'A3', 'A8', 'A11', 'A15'])
median_imputer.fit(X_train)
print(median_imputer.imputer_dict_)  # Stores learned median values
```

---

## **Imputation Pipeline**  
**Definition**: A sequence of steps combining data preprocessing techniques (e.g., imputation, scaling) into a single workflow to ensure consistency across training and testing sets.  
**Formula**: N/A  
**Example**:  
```python
from sklearn.pipeline import Pipeline
pipe = Pipeline(steps=[
    ('imputer', MeanMedianImputer(imputation_method='median', variables=['A2', 'A3', 'A8', 'A11', 'A15']))
])
pipe.fit(X_train)
X_train = pipe.transform(X_train)
X_test = pipe.transform(X_test)
```

---

### Key Links  
- [[Imputation Techniques]]  
- [[Scikit-learn Pipeline]]  
- [[Feature-engine Library]]  
- [[Handling Missing Data]]  

This summary integrates concepts from the provided notebooks, emphasizing practical implementation and theoretical foundations for polytechnic students.

---

---

## 2026-06-17 22:14 — Practical 2.3 - Implementing-mode-or-frequent-category-imputation.ipynb
**Style:** structured_academic (experimenting)

# Summary: Frequent Category Imputation

## [[Frequent Category Imputation]]
**Definition**: A method for handling missing values in categorical variables by replacing them with the **mode** (most frequently occurring category) of the training dataset. This ensures consistency across train, test, and future datasets by storing the learned mode values.  
**Formula**: Mode = The value with the highest frequency in the training set.  
**Example**:  
```python
# Using pandas
for var in ['A4', 'A5', 'A6', 'A7']:
    value = X_train[var].mode()[0]
    X_train[var] = X_train[var].fillna(value)
    X_test[var] = X_test[var].fillna(value)
```

---

## [[Mode Imputation]]
**Definition**: Synonymous with Frequent Category Imputation; replaces missing values with the mode. Often used interchangeably but may apply to both categorical and numerical data (though less common for the latter).  
**Formula**: Same as Frequent Category Imputation.  
**Example**:  
```python
# Using scikit-learn's SimpleImputer
imputer = SimpleImputer(strategy='most_frequent')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## [[SimpleImputer (scikit-learn)]]
**Definition**: A scikit-learn class for imputation that supports strategies like `most_frequent` for categorical data. Learns the mode during `.fit()` and applies it during `.transform()`.  
**Formula**: N/A (method-based).  
**Example**:  
```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='most_frequent')
imputer.fit(X_train)  # Learns mode values
X_train = imputer.transform(X_train)
```

---

## [[CategoricalImputer (Feature-engine)]]
**Definition**: A Feature-engine transformer specifically designed for categorical imputation, including `frequent` strategy. Stores imputation mappings in `imputer_dict_`.  
**Formula**: N/A (method-based).  
**Example**:  
```python
from feature_engine.imputation import CategoricalImputer
mode_imputer = CategoricalImputer(variables=['A4', 'A5', 'A6', 'A7'], imputation_method='frequent')
mode_imputer.fit(X_train)
X_train = mode_imputer.transform(X_train)
```

---

## [[Train/Test Split]]
**Definition**: The process of dividing data into training and testing subsets to evaluate model performance. Critical for imputation to avoid data leakage.  
**Formula**: N/A (process-based).  
**Example**:  
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=0)
```

---

## [[Mode Calculation]]
**Definition**: The process of identifying the most frequent category in a dataset. Used in Frequent Category Imputation to determine replacement values.  
**Formula**:  
\[
\text{Mode} = \text{Value with } \max(\text{Frequency})
\]  
**Example**:  
```python
# Extract mode for a variable
mode_value = X_train['A4'].mode()[0]
```

---

## Key Links
- [[Data Wrangling]]  
- [[Missing Data Imputation]]  
- [[Scikit-learn Pipeline]]  
- [[Feature-engine Transformers]]

---

---

## 2026-06-17 22:20 — Practical 2.4 - Replacing-missing-values-by-an-arbitrary-number.ipynb
**Style:** structured_academic (experimenting)

# Summary: Arbitrary Number Imputation

## [[Arbitrary Number Imputation]]
**Definition**: A technique where missing values in a dataset are replaced with a predefined arbitrary constant (e.g., 99, -1) that is not typically present in the data distribution. This method is suitable for numerical variables and avoids introducing values close to the mean/median of the data.

**Formula**:  
\[
\text{Imputed Value} = 
\begin{cases} 
x & \text{if } x \text{ is not missing} \\
c & \text{if } x \text{ is missing}
\end{cases}
\]  
where \( c \) is the chosen arbitrary constant.

**Example**:  
Replacing missing values in variables `A2`, `A3`, `A8`, `A11` with 99 using pandas:  
```python
for var in ['A2','A3', 'A8', 'A11']:
    X_train[var] = X_train[var].fillna(99)
    X_test[var] = X_test[var].fillna(99)
```

---

## [[Pandas Arbitrary Imputation]]
**Definition**: Implementation of arbitrary number imputation using pandas' `fillna()` method to replace missing values in a DataFrame.

**Formula**:  
`DataFrame[var].fillna(c, inplace=True)`  
where `c` is the arbitrary value.

**Example**:  
```python
# Replace missing values in specified columns with 99
for var in ['A2','A3', 'A8', 'A11']:
    X_train[var] = X_train[var].fillna(99)
    X_test[var] = X_test[var].fillna(99)
```

---

## [[Scikit-learn Arbitrary Imputation]]
**Definition**: Use of Scikit-learn's `SimpleImputer` class with `strategy='constant'` to impute missing values with a user-defined constant.

**Formula**:  
`SimpleImputer(strategy='constant', fill_value=c).fit_transform(X)`  
where `c` is the arbitrary constant.

**Example**:  
```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='constant', fill_value=99)
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## [[Feature-engine Arbitrary Imputation]]
**Definition**: Application of Feature-engine's `ArbitraryNumberImputer` transformer to replace missing values with a specified number, enabling pipeline integration.

**Formula**:  
`ArbitraryNumberImputer(arbitrary_number=c, variables=[vars]).fit_transform(X)`  
where `c` is the arbitrary constant and `vars` are target variables.

**Example**:  
```python
from feature_engine.imputation import ArbitraryNumberImputer

imputer = ArbitraryNumberImputer(
    arbitrary_number=99,
    variables=['A2','A3', 'A8', 'A11']
)
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## Key Considerations
- **Variable Selection**: Arbitrary imputation is typically applied to numerical variables. Categorical variables require separate handling (e.g., using frequent or missing category imputation).
- **Value Choice**: The arbitrary constant (e.g., 99) should not overlap with valid data values to avoid misinterpretation.
- **Pipeline Compatibility**: Feature-engine and Scikit-learn implementations are designed for integration into machine learning pipelines.

---

---

## 2026-06-17 22:25 — Practical 2.5 - Capturing-missing-values-in-a-bespoke-category.ipynb
**Style:** structured_academic (experimenting)

# Summary: Bespoke Category Imputation for Missing Data  

## [[Bespoke Category Imputation]]  
**Definition**: A technique for handling missing values in categorical variables by replacing them with a custom category (e.g., "Missing"). This approach treats missingness as a distinct category, preserving the variable’s categorical nature.  

**Formula**:  
\[
\text{Missing value} \rightarrow \text{"Missing"}
\]

**Example**:  
```python
# Using pandas to replace missing values with "Missing"
for var in ['A4', 'A5', 'A6', 'A7']:
    X_train[var] = X_train[var].fillna('Missing')
    X_test[var] = X_test[var].fillna('Missing')
```  

---

## [[CategoricalImputer (Feature-engine)]]  
**Definition**: A transformer from the `feature_engine` library designed to impute missing categorical values with a specified bespoke category (e.g., "Missing"). It learns the imputation value from the training set.  

**Formula**:  
\[
\text{Missing value} \rightarrow \text{User-defined category (e.g., "Missing")}
\]

**Example**:  
```python
# Initialize and apply CategoricalImputer
imputer = CategoricalImputer(variables=['A4', 'A5', 'A6', 'A7'], fill_with='Missing')
imputer.fit(X_train)
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)
```  

---

## [[SimpleImputer (scikit-learn)]]  
**Definition**: Scikit-learn’s `SimpleImputer` with a `constant` strategy allows replacing missing values with a user-specified value (e.g., "Missing"). Note that it returns a NumPy array.  

**Formula**:  
\[
\text{Missing value} \rightarrow \text{Constant (e.g., "Missing")}
\]

**Example**:  
```python
# Using SimpleImputer with constant strategy
imputer = SimpleImputer(strategy='constant', fill_value='Missing')
imputer.fit(X_train)
X_train = imputer.transform(X_train)  # Returns NumPy array
X_test = imputer.transform(X_test)
```  

---

## Key Workflow Steps  
1. **Data Splitting**: Use `train_test_split` to separate data into training and testing sets.  
2. **Imputation**: Apply imputation technique (pandas, Feature-engine, or scikit-learn) to replace missing values.  
3. **Validation**: Verify absence of missing values using `isnull().sum()` or `isnull().mean()`.  

**Context**: Demonstrated on the `creditApprovalUCI.csv` dataset, targeting categorical variables (e.g., `A4`, `A5`, `A6`, `A7`).  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).  

--- 

[[Imputation Methods]] | [[Missing Data Handling]] | [[Categorical Variables]]

---

---

## 2026-06-17 22:27 — Practical 2.6 - Replacing-missing-values-by-a-value-at-the-end-of-the-distribution.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content following the requested format:

---

### **End-of-Tail Imputation**  
**Definition**: A method to replace missing values with statistically derived extreme values from the variable's distribution, using either the interquartile range (IQR) or standard deviation. This avoids arbitrary value selection while preserving data distribution characteristics.  
**Formula**:  
- For IQR-based imputation (right tail): \( \text{Value} = Q3 + 1.5 \times \text{IQR} \)  
- For IQR-based imputation (left tail): \( \text{Value} = Q1 - 1.5 \times \text{IQR} \)  
- IQR calculation: \( \text{IQR} = Q3 - Q1 \)  
**Example**:  
```python  
# Using pandas to replace missing values in variables ['A2', 'A3', 'A8', 'A11', 'A15']  
for var in ['A2', 'A3', 'A8', 'A11', 'A15']:  
    IQR = X_train[var].quantile(0.75) - X_train[var].quantile(0.25)  
    value = X_train[var].quantile(0.75) + 1.5 * IQR  # Right tail  
    X_train[var].fillna(value, inplace=True)  
    X_test[var].fillna(value, inplace=True)  
```  

---

### **Interquartile Range (IQR)**  
**Definition**: A measure of statistical dispersion, representing the range between the 25th percentile (Q1) and 75th percentile (Q3) of a dataset.  
**Formula**:  
\[ \text{IQR} = Q3 - Q1 \]  
**Example**:  
```python  
# Calculating IQR for variable 'A2'  
Q1 = X_train['A2'].quantile(0.25)  
Q3 = X_train['A2'].quantile(0.75)  
IQR = Q3 - Q1  
```  

---

### **IQR Proximity Rule**  
**Definition**: A criterion to identify extreme values (potential outliers or imputation targets) based on the IQR. Values beyond \( Q1 - 1.5 \times \text{IQR} \) (left tail) or \( Q3 + 1.5 \times \text{IQR} \) (right tail) are considered extreme.  
**Formula**:  
- Right tail threshold: \( Q3 + 1.5 \times \text{IQR} \)  
- Left tail threshold: \( Q1 - 1.5 \times \text{IQR} \)  
**Example**:  
```python  
# Using IQR proximity rule for right tail imputation  
value = Q3 + 1.5 * IQR  
print(f"Imputation value for right tail: {value}")  
```  

---

### **EndTailImputer (Feature-engine)**  
**Definition**: A class in the Feature-engine library that automates end-of-tail imputation. It learns imputation values from the training set and applies them to test/future data.  
**Formula**: N/A (implementation-specific)  
**Example**:  
```python  
from feature_engine.imputation import EndTailImputer  

imputer = EndTailImputer(  
    imputation_method='iqr',  
    tail='right',  
    fold=1.5,  
    variables=['A2', 'A3', 'A8', 'A11', 'A15']  
)  
imputer.fit(X_train)  
X_train = imputer.transform(X_train)  
X_test = imputer.transform(X_test)  
```  

---

### **Train/Test Split**  
**Definition**: The process of dividing a dataset into training and testing subsets to evaluate machine learning models. The training set is used for imputation parameter estimation, while the test set simulates unseen data.  
**Formula**: N/A  
**Example**:  
```python  
from sklearn.model_selection import train_test_split  

X_train, X_test, y_train, y_test = train_test_split(  
    data.drop('A16', axis=1),  
    data['A16'],  
    test_size=0.3,  
    random_state=0  
)  
```  

---

### **Key Links**  
- [[Imputation Techniques]]  
- [[Feature-engine]]  
- [[Interquartile Range (IQR)]]  
- [[Train/Test Split]]  

This summary integrates theoretical concepts and practical implementations from the notebook, emphasizing statistical foundations and code-based workflows.

---

---

## 2026-06-17 22:32 — Practical 2.7 - Implementing-random-sample-imputation.ipynb
**Style:** structured_academic (experimenting)

Here's a structured summary of the content following the requested format:

---

### [[Random Sample Imputation]]
**Definition**:  
A missing data imputation technique that replaces missing values with random observations drawn from the existing values of the same variable. This method preserves the original data distribution and works for both numerical and categorical variables.

**Formula**:  
No explicit mathematical formula. The method involves:  
1. Counting missing values in a variable (e.g., `number_missing = X_train['A2'].isnull().sum()`)  
2. Sampling random observed values (with replacement or without) equal to the number of missing values  
3. Assigning these sampled values to missing data points while maintaining original distribution properties

**Example**:  
```python
# Using pandas (manual implementation)
number_missing = X_train['A2'].isnull().sum()
random_sample = X_train['A2'].dropna().sample(number_missing, random_state=0)
X_train.loc[X_train['A2'].isnull(), 'A2'] = random_sample.values

# Using Feature Engine (automated pipeline)
imputer = RandomSampleImputer()
imputer.fit(X_train)
X_train = imputer.transform(X_train)
```

---

### Related Concepts  
- [[Imputation Techniques]]: Parent category including methods like [[Mean/Median Imputation]] and [[Frequent Category Imputation]]  
- [[Data Distribution Preservation]]: Key advantage of random sample imputation vs. mean/median methods  
- [[Feature Engine]]: Library providing specialized imputation transformers  
- [[SimpleImputer]]: Scikit-learn's basic imputation tool (less flexible than Feature Engine)  

---

### Key Implementation Steps  
1. **Data Preparation**:  
   - Split data into train/test sets  
   - Identify variables with missing values (`X_train.isnull().mean()`)  

2. **Manual Implementation (Pandas)**:  
   - Calculate missing values per variable  
   - Sample random observed values  
   - Reindex and replace missing values  

3. **Automated Implementation (Feature Engine)**:  
   - Create `RandomSampleImputer` object  
   - Fit to training data  
   - Transform train/test sets  

4. **Validation**:  
   - Confirm missing values removed (`X_train.isnull().mean()`)  

---

This summary connects to previous imputation techniques discussed in the course materials while emphasizing the unique distribution-preserving properties of random sample imputation. The code examples demonstrate both low-level pandas operations and high-level library implementations.

---

---

## 2026-06-17 22:37 — Practical 2.8 - Adding-a-missing-value-indicator-variable.ipynb
**Style:** structured_academic (experimenting)

## Missing Value Indicator Variable  
**Definition**: A binary feature that indicates whether an observation's value was missing (1) or present (0) in the original dataset. It preserves information about missingness while allowing imputation (e.g., [[Mean/Median Imputation]]) to fill missing values.  

**Formula**:  
\[
\text{Indicator}_i = 
\begin{cases} 
1 & \text{if } x_i \text{ is missing} \\ 
0 & \text{otherwise} 
\end{cases}
\]

**Example**:  
```python
# Using pandas and numpy to create indicators
X_train[var+'_NA'] = np.where(X_train[var].isnull(), 1, 0)
X_test[var+'_NA'] = np.where(X_test[var].isnull(), 1, 0)
```

---

## AddMissingIndicator (Feature-engine)  
**Definition**: A transformer class in the `Feature-engine` library that automatically adds missing value indicator variables to columns with missing data.  

**Formula**: N/A (method-based implementation)  

**Example**:  
```python
from feature_engine.imputation import AddMissingIndicator
imputer = AddMissingIndicator()
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)
```

---

## MissingIndicator (Scikit-learn)  
**Definition**: A Scikit-learn transformer that generates binary indicators for missing values in the dataset. It identifies columns with missing values and creates corresponding indicator features.  

**Formula**: N/A (method-based implementation)  

**Example**:  
```python
from sklearn.impute import MissingIndicator
indicator = MissingIndicator(error_on_new=True, features='missing-only')
X_train_ind = indicator.fit_transform(X_train)
# Concatenate indicators to original data
indicator_cols = [c+'_NA' for c in X_train.columns[indicator.features_]]
X_train = pd.concat([X_train, pd.DataFrame(X_train_ind, columns=indicator_cols)], axis=1)
```

---

## Key Concepts & Links  
- **[[Missing Data Imputation Techniques]]**: Context for using indicators alongside imputation.  
- **[[Mean/Median Imputation]]**: Often paired with indicators to handle missing values.  
- **[[IQR Proximity Rule]]**: Alternative imputation method for non-normal distributions.  
- **[[Random Sample Imputation]]**: Another technique for filling missing data.

---

---

## 2026-06-17 22:43 — Practical 2.9 - Assembling-an-imputation-pipeline-with-Scikit-learn.ipynb
**Style:** structured_academic (experimenting)

## Summary: Assembling an Imputation Pipeline with Scikit-Learn

### [[Imputation Pipeline]]
**Definition**: A structured workflow that chains multiple data preprocessing steps (e.g., imputation strategies) to handle missing values in different subsets of a dataset.  
**Formula**: N/A  
**Example**:  
```python
preprocessor = ColumnTransformer(transformers=[
    ('imp_num_arbitrary', imputer_num_arbitrary, features_num_arbitrary),
    ('imp_num_median', imputer_num_median, features_num_median),
    ('imp_cat_frequent', imputer_cat_frequent, features_cat_frequent),
    ('imp_cat_missing', imputer_cat_missing, features_cat_missing)
])
```

---

### [[ColumnTransformer]]
**Definition**: A scikit-learn class that applies distinct transformers to specific columns of a dataset, enabling tailored preprocessing for numerical and categorical features.  
**Formula**: N/A  
**Example**:  
```python
preprocessor = ColumnTransformer(
    transformers=[
        ('imp_num_arbitrary', Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value=99))]), ['A3', 'A8'])
    ],
    remainder='passthrough'
)
```

---

### [[SimpleImputer]]
**Definition**: A scikit-learn class for filling missing values using strategies like mean, median, most frequent, or constant values.  
**Formula**:  
- **Median Imputation**: \( \text{Replace missing values with } \mu = \text{median}(x) \)  
- **Most Frequent Imputation**: \( \text{Replace missing values with mode}(x) \)  
**Example**:  
```python
imputer_num_median = Pipeline(steps=[('imputer', SimpleImputer(strategy='median'))])
```

---

### [[Arbitrary Number Imputation]]
**Definition**: Replaces missing numerical values with a user-defined constant (e.g., 99).  
**Formula**: \( x_{\text{missing}} \rightarrow c \) (where \( c \) is a constant)  
**Example**:  
```python
SimpleImputer(strategy='constant', fill_value=99)
```

---

### [[Median Imputation]]
**Definition**: Replaces missing numerical values with the median of the column.  
**Formula**: \( x_{\text{missing}} \rightarrow \mu = \text{median}(x) \)  
**Example**:  
```python
SimpleImputer(strategy='median')
```

---

### [[Most Frequent Imputation (Categorical)]]
**Definition**: Replaces missing categorical values with the most frequent category in the column.  
**Formula**: \( x_{\text{missing}} \rightarrow \text{mode}(x) \)  
**Example**:  
```python
SimpleImputer(strategy='most_frequent')
```

---

### [[Missing Category Imputation]]
**Definition**: Adds a new category (e.g., "Missing") to represent missing values in categorical variables.  
**Formula**: N/A  
**Example**:  
```python
SimpleImputer(strategy='constant', fill_value='Missing')
```

---

### [[Train-Test Split]]
**Definition**: Divides a dataset into training and testing subsets to evaluate model performance without data leakage.  
**Formula**: N/A  
**Example**:  
```python
X_train, X_test, y_train, y_test = train_test_split(
    data.drop('A16', axis=1), data['A16'], test_size=0.3, random_state=0
)
```

---

### [[Handling Missing Data]]
**Definition**: The process of addressing missing values in a dataset through imputation, deletion, or other methods to ensure data quality for analysis.  
**Formula**: N/A  
**Example**:  
```python
# Identifying missing values
X_train.isnull().mean()
# Imputing missing values
X_train = preprocessor.transform(X_train)
``` 

---

### Key Notes:
1. **Column Order**: Scikit-learn transformers may reorder columns and return NumPy arrays instead of DataFrames.  
2. **Strategies by Variable Type**:  
   - **Numerical**: Arbitrary number, median.  
   - **Categorical**: Most frequent, "Missing" category.  
3. **Pipeline Integration**: Combines preprocessing steps (e.g., imputation) with model training in a single workflow.  

[[Data Leakage]] should be avoided by fitting the pipeline only on the training data before transforming test data.

---

---

## 2026-06-17 22:52 — Practical 7.1 - Standardization.ipynb
**Style:** structured_academic (experimenting)

# Summary of Key Concepts in Feature Standardization and Model Diagnostics

## **Standardization (Z-score Standardization)**  
**Definition**: A method to transform data such that each feature has a mean of 0 and a standard deviation of 1, enabling comparability across features.  
**Formula**:  
\[ z = \frac{x - \text{mean}(x)}{\text{std}(x)} \]  
**Example**:  
```python  
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
X_train_scaled = scaler.fit_transform(X_train)  
```  
**Link**: [[Z-score]], [[Mean]], [[Standard Deviation]]

---

## **Z-score**  
**Definition**: The result of standardization, representing the number of standard deviations an observation is from the mean.  
**Formula**: Same as above.  
**Example**: Scaled features in `X_train_scaled` after applying `StandardScaler`.  
**Link**: [[Standardization]]

---

## **Mean (mean_)**  
**Definition**: The average value of a feature, calculated as the sum of all values divided by the number of values.  
**Formula**:  
\[ \text{mean}(x) = \frac{\sum_{i=1}^{n} x_i}{n} \]  
**Example**:  
```python  
scaler.mean_  # Returns the mean of each feature learned from the training data  
```  
**Link**: [[Standardization]]

---

## **Standard Deviation (scale_)**  
**Definition**: A measure of the spread of a dataset, indicating how much values deviate from the mean.  
**Formula**:  
\[ \text{std}(x) = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \text{mean}(x))^2} \]  
**Example**:  
```python  
scaler.scale_  # Returns the standard deviation of each feature  
```  
**Link**: [[Standardization]]

---

## **Feature-wise Normalization**  
**Definition**: Normalizing each feature individually (e.g., via standardization) to ensure equal contribution in models.  
**Formula**: Same as [[Standardization]].  
**Example**: Applying `StandardScaler` to the Boston housing dataset to homogenize feature scales.  
**Link**: [[Standardization]]

---

## **Coefficient (β)**  
**Definition**: In logistic regression, represents the influence of a predictor on the outcome. Sign indicates direction (positive/negative), magnitude indicates strength.  
**Formula**: Not explicitly provided, but part of the logistic regression equation:  
\[ \text{Logit}(p) = \beta_0 + \beta_1 x_1 + \dots + \beta_n x_n \]  
**Example**: A positive β for "RM" (average rooms) in house pricing models suggests larger rooms increase prices.  
**Link**: [[Confidence Interval]], [[Standard Error]]

---

## **Standard Error (SE)**  
**Definition**: Measures uncertainty in a coefficient estimate. Smaller SE implies higher confidence.  
**Formula**:  
\[ \text{SE} = \frac{\sigma}{\sqrt{n}} \]  
(where σ is sample standard deviation, n is sample size).  
**Example**: Reported in model summaries (e.g., `summary()` in statsmodels).  
**Link**: [[Confidence Interval]], [[Coefficient]]

---

## **Confidence Interval (CI)**  
**Definition**: Range of plausible values for a coefficient at a given confidence level (e.g., 95%).  
**Formula**:  
\[ \text{CI} = \beta \pm (1.96 \times \text{SE}) \]  
**Example**: A 95% CI of [0.2, 0.5] for β indicates the true value likely lies in this interval.  
**Link**: [[Coefficient]], [[Standard Error]]

---

## **Z statistic (Wald test)**  
**Definition**: Tests if a coefficient is significantly different from zero. Larger |Z| values indicate stronger evidence.  
**Formula**:  
\[ Z = \frac{\beta}{\text{SE}} \]  
**Example**: A Z statistic of 3.5 for "LSTAT" suggests it significantly affects house prices.  
**Link**: [[Coefficient]], [[Standard Error]]

---

This summary integrates concepts from both feature preprocessing (standardization) and model diagnostics (coefficient analysis), linking related terms for cohesive understanding.

---

---

## 2026-06-17 23:05 — Practical 7.2 - Mean-normalization.ipynb
**Style:** structured_academic (experimenting)

### Mean Normalization

**Term:** Mean Normalization  
**Definition:** A data preprocessing technique that centers the variable at zero and rescales the distribution to a value range. This involves subtracting the mean from each observation and then dividing by the difference between the minimum and maximum values.

\[
x_{scaled} = \frac{x - mean(x)}{max(x) - min(x)}
\]

**Formula:** 
1. Calculate the mean of each feature:
   \[
   \text{means} = X_train.mean(axis=0)
   \]
2. Determine the range (difference between maximum and minimum values):
   \[
   \text{ranges} = X_train.max(axis=0) - X_train.min(axis=0)
   \]
3. Scale the training set:
   \[
   X_train_scaled = \frac{X_train - means}{ranges}
   \]
4. Apply the same transformation to the test set:
   \[
   X_test_scaled = \frac{X_test - means}{ranges}
   \]

**Example:**
```python
# Load dataset and split into training and testing sets
data = pd.read_csv("./data/boston_local.csv")
X_train, X_test, y_train, y_test = train_test_split(data.drop('MEDV', axis=1), data['MEDV'], test_size=0.3, random_state=0)

# Calculate mean and range for the training set
means = X_train.mean(axis=0)
ranges = X_train.max(axis=0) - X_train.min(axis=0)

# Scale the training and testing sets
X_train_scaled = (X_train - means) / ranges
X_test_scaled = (X_test - means) / ranges

# Visualize distributions before and after scaling
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

# Before scaling
ax1.set_title('Before Scaling')
sns.kdeplot(X_train['RM'], ax=ax1, label='RM')
sns.kdeplot(X_train['LSTAT'], ax=ax1, label='LSTAT')
sns.kdeplot(X_train['CRIM'], ax=ax1, label='CRIM')
ax1.legend()

# After scaling
ax2.set_title('After Scaling')
sns.kdeplot(X_train_scaled['RM'], ax=ax2, label='RM')
sns.kdeplot(X_train_scaled['LSTAT'], ax=ax2, label='LSTAT')
sns.kdeplot(X_train_scaled['CRIM'], ax=ax2, label='CRIM')
ax2.legend()
plt.show()

# Repeat for other features
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

# Before scaling
ax1.set_title('Before Scaling')
sns.kdeplot(X_train['AGE'], ax=ax1, label='AGE')
sns.kdeplot(X_train['DIS'], ax=ax1, label='DIS')
sns.kdeplot(X_train['NOX'], ax=ax1, label='NOX')
ax1.legend()

# After scaling
ax2.set_title('After Scaling')
sns.kdeplot(X_train_scaled['AGE'], ax=ax2, label='AGE')
sns.kdeplot(X_train_scaled['DIS'], ax=ax2, label='DIS')
sns.kdeplot(X_train_scaled['NOX'], ax=ax2, label='NOX')
ax2.legend()
plt.show()
```

**References:**
- *Source: Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*

[[Pandas]] [[Scikit-Learn]] [[StandardScaler]] [[RobustScaler]]

---

---

## 2026-06-17 23:12 — Practical 7.3 - MinMaxScaling.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### [[Min-Max Scaling]]
**Definition**: A technique that transforms feature values to a fixed range (typically [0, 1]) by subtracting the minimum value and dividing by the range (max - min).  
**Formula**:  
$$ x_{\text{scaled}} = \frac{x - \min(x)}{\max(x) - \min(x)} $$  
**Example**:  
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
```

---

### [[MinMaxScaler (Scikit-learn)]]
**Definition**: A Scikit-learn class implementing Min-Max scaling that learns `min_` and `data_max_` attributes from training data.  
**Formula**: N/A (Implementation of Min-Max scaling)  
**Example**:  
```python
scaler = MinMaxScaler()
scaler.fit(X_train)  # Learns min/max values
X_test_scaled = scaler.transform(X_test)  # Applies same scaling
```

---

### [[Train/Test Split]]
**Definition**: Method to partition data into training and testing subsets to evaluate model performance.  
**Formula**: N/A  
**Example**:  
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)
```

---

### [[Data Transformation]]
**Definition**: Process of applying learned scaling parameters to convert raw data into scaled values.  
**Formula**: N/A  
**Example**:  
```python
X_train_scaled = scaler.transform(X_train)  # Scales training data
X_test_scaled = scaler.transform(X_test)   # Scales test data
```

---

### [[Kernel Density Estimate (KDE) Plot]]
**Definition**: Statistical visualization showing the probability density function of a variable.  
**Formula**: N/A  
**Example**:  
```python
import seaborn as sns
sns.kdeplot(X_train['RM'], label='Before Scaling')
sns.kdeplot(X_train_scaled['RM'], label='After Scaling')
```

---

### Key Observations from Visualizations:
1. **Before Scaling**: Features like `RM`, `LSTAT`, and `CRIM` exhibit varying scales and distributions.  
2. **After Scaling**: All features are compressed to [0, 1] range, resulting in overlapping KDE plots with similar spreads.

---

### Attribute Inspection:
```python
scaler.data_min_  # Minimum values learned from training data
scaler.data_max_  # Maximum values learned from training data
scaler.data_range_  # Range (max - min) for each feature
```

This summary connects concepts like [[Feature Scaling]], [[Data Preprocessing]], and [[Exploratory Data Analysis (EDA)]] through standardization techniques.

---

---

## 2026-06-17 23:20 — Practical 7.4 - Maximum-Absolute-Scaling.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content:

---

### **Maximum Absolute Scaling**  
**Definition**: A scaling technique that transforms data by dividing each feature value by the maximum absolute value of that feature, ensuring all values fall within the range [-1, 1]. Recommended for data centered at zero or sparse datasets.  
**Formula**:  
\[ x_{\text{scaled}} = \frac{x}{\max(|x|)} \]  
**Example**:  
```python  # Code Cell 5
scaler = MaxAbsScaler()
X_train_scaled = scaler.transform(X_train)
```  
Visualized via KDE plots (Code Cells 9-10, 14-15) to compare distributions before/after scaling.

---

### **Centering**  
**Definition**: Adjusting data by subtracting the mean (μ) of each feature, shifting the distribution to have a mean of zero.  
**Formula**:  
\[ x_{\text{centered}} = x - \mu \]  
**Example**:  
```python  # Code Cell 12
scaler_mean = StandardScaler(with_mean=True, with_std=False)
X_train_centered = scaler_mean.transform(X_train)
```  

---

### **Combined Scaling (Centering + MaxAbsScaling)**  
**Definition**: A two-step process that first centers the data (mean removal) and then applies Maximum Absolute Scaling. This ensures data is both zero-centered and scaled to [-1, 1].  
**Formula**:  
1. \( x_{\text{centered}} = x - \mu \)  
2. \( x_{\text{scaled}} = \frac{x_{\text{centered}}}{\max(|x_{\text{centered}}|)} \)  
**Example**:  
```python  # Code Cell 12
X_train_scaled = scaler_maxabs.transform(scaler_mean.transform(X_train))
```  
Resulting distributions are visualized in Code Cells 14-15.

---

### **Key Concepts & Links**  
- [[Maximum Absolute Scaling]] is distinct from [[Min-Max Scaling]] (which uses the range \( \max(x) - \min(x) \)) and [[Standardization]] (which uses z-scores).  
- [[Centering]] is often a precursor to scaling in pipelines.  
- Visualization via [[KDE Plots]] (Kernel Density Estimation) demonstrates the impact of scaling on feature distributions.  

---

This summary integrates the theoretical and practical aspects of the notebook, emphasizing the implementation of **Maximum Absolute Scaling** and its combination with centering for robust feature engineering.

---

---

## 2026-06-17 23:30 — Practical 7.5 - Robust-Scaling.ipynb
**Style:** structured_academic (experimenting)

### Robust Scaling

**Term -> Definition:** 
Robust scaling is a method of scaling variables to the median and quantiles. It removes the median value from the observations and divides by the inter-quartile range (IQR), which is the range between the 1st quartile (25th quantile) and the 3rd quartile (75th quantile).

**Formula:**
\begin{equation}
x_{scaled} = \frac{x - median(x)}{x.quantile(0.75) - x.quantile(0.25)}
\end{equation}

This method is robust to outliers and recommended when the data contains extreme values.

**Example:**

```python
import pandas as pd

from sklearn.model_selection import train_test_split

# Importing the scaler for robust scaling
from sklearn.preprocessing import RobustScaler

# Load the Boston House price data
data = pd.read_csv("./data/boston_local.csv")

# Splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('MEDV', axis=1),
                                                    data['MEDV'],
                                                    test_size=0.3,
                                                    random_state=0)

# Set up the scaler for robust scaling
scaler = RobustScaler()

# Fit the scaler to the training set and transform both sets
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Displaying the median values learned by the scaler from the training set
scaler.center_

# Displaying the IQR values learned by the scaler from the training set
scaler.scale_

# Transforming the scaled data back into DataFrames for easier handling
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

# Visualizing the distribution of variables before and after scaling
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

# Before scaling
ax1.set_title('Before Scaling')
sns.kdeplot(X_train['RM'], ax=ax1, label='RM')
sns.kdeplot(X_train['LSTAT'], ax=ax1, label='LSTAT')
sns.kdeplot(X_train['CRIM'], ax=ax1, label='CRIM')
ax1.legend()

# After scaling
ax2.set_title('After Scaling')
sns.kdeplot(X_train_scaled['RM'], ax=ax2, label='RM')
sns.kdeplot(X_train_scaled['LSTAT'], ax=ax2, label='LSTAT')
sns.kdeplot(X_train_scaled['CRIM'], ax=ax2, label='CRIM')
ax2.legend()
plt.show()

# Visualizing the distribution of variables before and after standard scaling
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

# Before scaling
ax1.set_title('Before Scaling')
sns.kdeplot(X_train['AGE'], ax=ax1, label='AGE')
sns.kdeplot(X_train['DIS'], ax=ax1, label='DIS')
sns.kdeplot(X_train['NOX'], ax=ax1, label='NOX')
ax1.legend()

# After scaling
ax2.set_title('After Standard Scaling')
sns.kdeplot(X_train_scaled['AGE'], ax=ax2, label='AGE')
sns.kdeplot(X_train_scaled['DIS'], ax=ax2, label='DIS')
sns.kdeplot(X_train_scaled['NOX'], ax=ax2, label='NOX')
ax2.legend()
plt.show()
```

**Source:** Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)

---

---

## 2026-06-17 23:39 — Practical 8.1 - Add-Multiply-Features.ipynb
**Style:** structured_academic (experimenting)

### Combining Multiple Features with Statistical Operations

**Term -> Definition -> Formula -> Example**

#### Addition
- **Definition:** Summing up the values of multiple features.
- **Formula:** \[ \text{added\_features} = \sum_{i=1}^{n} \text{feature}_i \]
- **Example:**
    ```python
    df['added_features'] = df[features].sum(axis=1)
    ```

#### Product
- **Definition:** Multiplying the values of multiple features.
- **Formula:** \[ \text{prod\_features} = \prod_{i=1}^{n} \text{feature}_i \]
- **Example:**
    ```python
    df['prod_features'] = df[features].prod(axis=1)
    ```

#### Average (Mean)
- **Definition:** Calculating the average value of multiple features.
- **Formula:** \[ \text{mean\_features} = \frac{\sum_{i=1}^{n} \text{feature}_i}{n} \]
- **Example:**
    ```python
    df['mean_features'] = df[features].mean(axis=1)
    ```

#### Standard Deviation
- **Definition:** Calculating the standard deviation of multiple features.
- **Formula:** \[ \text{std\_features} = \sqrt{\frac{\sum_{i=1}^{n} (\text{feature}_i - \bar{x})^2}{n}} \]
- **Example:**
    ```python
    df['std_features'] = df[features].std(axis=1)
    ```

#### Maximum
- **Definition:** Finding the maximum value among multiple features.
- **Formula:** \[ \text{max\_features} = \max(\text{feature}_1, \text{feature}_2, \ldots, \text{feature}_n) \]
- **Example:**
    ```python
    df['max_features'] = df[features].max(axis=1)
    ```

#### Minimum
- **Definition:** Finding the minimum value among multiple features.
- **Formula:** \[ \text{min\_features} = \min(\text{feature}_1, \text{feature}_2, \ldots, \text{feature}_n) \]
- **Example:**
    ```python
    df['min_features'] = df[features].min(axis=1)
    ```

#### Aggregating Multiple Operations
- **Definition:** Performing multiple statistical operations (sum, product, mean, std, max, min) on a set of features.
- **Formula:** \[ \text{df\_t} = \text{df}[features].agg(['sum', 'prod','mean','std', 'max', 'min'], axis='columns') \]
- **Example:**
    ```python
    df_t = df[features].agg(['sum', 'prod','mean','std', 'max', 'min'], axis='columns')
    df_t.head()
    ```

### Related Concepts

- [[Feature Engineering]]
- [[Statistical Operations]]
- [[Data Aggregation]]

This summary provides a structured overview of combining multiple features using various statistical operations, illustrating each operation with code examples and formulas.

---

---

## 2026-06-17 23:45 — Practical 8.2 - Substraction-Quotient-Features.ipynb
**Style:** structured_academic (experimenting)

# Structured Academic Summary  

## [[Feature Engineering]]  
**Definition**: The process of creating new features (variables) from existing data to enhance the predictive power of machine learning models.  
**Formula**: N/A (general concept)  
**Example**: Creating `difference` (subtraction of features) and `quotient` (division of features) in the breast cancer dataset.  

---

## [[Subtraction of Features]]  
**Definition**: A method to derive a new feature by subtracting the values of one column from another.  
**Formula**:  
\[ \text{New Feature} = \text{Feature}_1 - \text{Feature}_2 \]  
**Example**:  
```python  
df['difference'] = df['worst compactness'].sub(df['mean compactness'])  # Code Cell 6  
```  

---

## [[Division of Features]]  
**Definition**: A method to derive a new feature by dividing the values of one column by another.  
**Formula**:  
\[ \text{New Feature} = \frac{\text{Feature}_1}{\text{Feature}_2} \]  
**Example**:  
```python  
df['quotient'] = df['worst radius'].div(df['mean radius'])  # Code Cell 9  
```  

---

## [[Aggregation of Features]]  
**Definition**: Combining multiple features into a single feature using statistical operations (e.g., summation).  
**Formula**:  
\[ \text{Aggregated Feature} = \sum_{i=1}^{n} \text{Feature}_i \]  
**Example**:  
```python  
df['worst'] = df[['worst smoothness', 'worst compactness', ...]].sum(axis=1)  # Code Cell 13  
```  

---

## [[Derived Ratios]]  
**Definition**: Creating ratios by dividing original features by an aggregated or reference feature.  
**Formula**:  
\[ \text{Ratio Feature} = \frac{\text{Original Feature}}{\text{Aggregated Feature}} \]  
**Example**:  
```python  
df[features] = df[features].div(df['worst'], axis=0)  # Code Cell 15  
```  

---

## Connections to Prior Concepts  
- [[Feature Engineering]] is a subset of [[Data Wrangling]].  
- [[Aggregation of Features]] relates to [[Statistical Operations]] (e.g., sum, mean).  
- [[Derived Ratios]] extend [[Division of Features]] to multiple variables.  

*Source: Soledad Galli, Python Feature Engineering Cookbook (Jan 2020)*

---

---

## 2026-06-17 23:52 — Practical 8.3 - PolynomialExpansion.ipynb
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

---

---

## 2026-06-18 08:50 — Practical 8.4 - PCA.ipynb
**Style:** structured_academic (experimenting)

### Summary: Principal Component Analysis (PCA)

#### [[Principal Component Analysis (PCA)]]
**Definition**: A dimensionality reduction technique that transforms high-dimensional data into a lower-dimensional subset of **Principal Components (PCs)**. These PCs are linear combinations of the original variables, orthogonal to each other, and ordered by the amount of variance they explain in the data.  
**Formula**:  
The transformation is derived from the eigenvalues and eigenvectors of the data’s covariance matrix. For a standardized dataset \( X \), the PCs are defined by:  
\[
\text{PC}_i = X \cdot w_i
\]  
where \( w_i \) is the eigenvector corresponding to the \( i \)-th largest eigenvalue of the covariance matrix. The **explained variance ratio** for each PC is:  
\[
\text{Explained Variance Ratio}_i = \frac{\lambda_i}{\sum_{j=1}^n \lambda_j}
\]  
where \( \lambda_i \) is the eigenvalue for the \( i \)-th PC.  
**Example**:  
In the provided code, PCA is applied to the Boston housing dataset after standardization:  
```python
# Initialize and train PCA
pca = PCA()
pca.fit(X_train_scaled)  # Fit to training data

# Transform data into principal components
train_t = pca.transform(X_train_scaled)
test_t = pca.transform(X_test_scaled)
```

---

#### [[Principal Components (PCs)]]
**Definition**: Linear combinations of the original features that capture the maximum variance in the data. Each PC is orthogonal to all others, ensuring no correlation between components.  
**Formula**:  
The first PC (\( \text{PC}_1 \)) maximizes the variance:  
\[
\text{PC}_1 = w_{1,1}x_1 + w_{1,2}x_2 + \dots + w_{1,n}x_n
\]  
Subsequent PCs maximize residual variance under the constraint of orthogonality to previous PCs.  
**Example**:  
The code extracts PCs and their explained variance:  
```python
# Access explained variance ratio
print(pca.explained_variance_ratio_)  # Output: Array of variance ratios for each PC
```

---

#### [[Explained Variance Ratio]]
**Definition**: The proportion of total variance in the data explained by each principal component. Used to determine the number of PCs needed to retain meaningful information.  
**Formula**:  
\[
\text{Explained Variance Ratio}_i = \frac{\lambda_i}{\sum \lambda}
\]  
where \( \lambda_i \) is the eigenvalue of the \( i \)-th PC.  
**Example**:  
The code visualizes the variance explained by each PC:  
```python
# Plot explained variance ratio
plt.plot(pca.explained_variance_ratio_, linewidth=2)
plt.title('Percentage of Variance Explained')
plt.xlabel('PC Index')
plt.ylabel('Variance Ratio')
plt.show()
```

---

#### [[Standardization]]
**Definition**: A preprocessing step that centers the data (mean = 0) and scales it to unit variance (std = 1). Critical for PCA since it ensures all features contribute equally to the variance.  
**Formula**:  
\[
z = \frac{x - \mu}{\sigma}
\]  
where \( \mu \) is the mean and \( \sigma \) the standard deviation.  
**Example**:  
The code standardizes the dataset using `StandardScaler`:  
```python
# Initialize and apply StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on training data
X_test_scaled = scaler.transform(X_test)        # Transform test data
```

---

### Key Workflow Integration
1. **Standardization** → **PCA Training** → **Component Extraction** → **Variance Analysis**  
2. **Wikilinks**: [[Standardization]] → [[Principal Component Analysis (PCA)]] → [[Explained Variance Ratio]] → [[Principal Components (PCs)]]

---

---

## 2026-06-18 08:55 — Practical 5.1 - Equal-width-discretization.ipynb
**Style:** structured_academic (experimenting)

# Summary: Equal-Width Discretization  

## [[Equal-Width Discretization]]  
**Definition**: A method of binning continuous variables into discrete intervals of **equal width**, where the range of the variable is divided into a specified number of bins. Outliers can be accommodated by extending the first and last bin limits to infinity.  
**Formula**:  
\[ \text{Bin Width} = \frac{\text{Max}(X) - \text{Min}(X)}{\text{Number of Bins}} \]  
**Example**:  
For `LSTAT` (Min = 4.0, Max = 37.0) with 10 bins:  
```python  
width = (37.0 - 4.0) / 10 = 3.3  
intervals = [4.0, 7.3, 10.6, ..., 37.0]  
X_train['lstat_disc'] = pd.cut(X_train['LSTAT'], bins=intervals, include_lowest=True)  
```  

---

## [[Bin Width]]  
**Definition**: The uniform size of each interval in equal-width discretization, calculated as the total range of the variable divided by the number of bins.  
**Formula**:  
\[ \text{Bin Width} = \frac{\text{Max}(X) - \text{Min}(X)}{k} \]  
where \( k \) = number of bins.  
**Example**:  
For `LSTAT` with \( k = 10 \):  
```python  
lstat_range = X_train['LSTAT'].max() - X_train['LSTAT'].min()  
bin_width = lstat_range / 10  
```  

---

## [[Interval Edges]]  
**Definition**: The boundaries defining each bin in equal-width discretization. These are derived from the variable’s range and bin width.  
**Formula**: N/A (computed as \( \text{Min}(X) + i \times \text{Bin Width} \) for \( i = 0, 1, ..., k \)).  
**Example**:  
For `LSTAT` with 10 bins:  
```python  
min_value, max_value = 4.0, 37.0  
intervals = list(range(min_value, max_value + bin_width, int(bin_width)))  
# Output: [4, 7, 10, 14, 17, 20, 23, 27, 30, 33, 37]  
```  

---

## [[pd.cut()]]  
**Definition**: A pandas function to discretize continuous variables into bins defined by `include_lowest=True` ensures the first bin includes the lowest value.  
**Formula**: N/A (implementation-based).  
**Example**:  
```python  
X_train['lstat_disc'] = pd.cut(  
    X_train['LSTAT'],  
    bins=intervals,  
    include_lowest=True  # Captures values ≥ first interval edge  
)  
```  

---

## [[EqualWidthDiscretiser (Feature-engine)]]  
**Definition**: A `Feature-engine` transformer that automates equal-width discretization for multiple variables. Stores bin edges in `binner_dict_`.  
**Formula**: N/A (method-based).  
**Example**:  
```python  
disc = EqualWidthDiscretiser(bins=10, variables=['LSTAT', 'DIS', 'RM'])  
disc.fit(X_train)  
train_t = disc.transform(X_train)  # Transforms specified variables  
```  

---

## [[KBinsDiscretizer (scikit-learn)]]  
**Definition**: A scikit-learn method for equal-width discretization, returning NumPy arrays. Requires encoding strategy (e.g., `ordinal` for integer codes).  
**Formula**: N/A (method-based).  
**Example**:  
```python  
disc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')  
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])  
train_t = disc.transform(X_train[['LSTAT', 'DIS', 'RM']])  # Output: NumPy array  
```  

---

## [[Train-Test Split Consistency]]  
**Definition**: Ensuring discretization intervals are consistent between training and test sets to avoid data leakage. Intervals are determined on the training set and applied to the test set.  
**Formula**: N/A (process-based).  
**Example**:  
```python  
# Fit discretizer on training data  
disc.fit(X_train)  
# Transform both sets  
train_t = disc.transform(X_train)  
test_t = disc.transform(X_test)  
```  

---

## [[pandas Interval Object]]  
**Definition**: The data type used by pandas to represent discrete bins (e.g., `(34.0, 37.0]`). Includes methods to check membership (e.g., `34.0 in interval`).  
**Formula**: N/A (object-based).  
**Example**:  
```python  
test_interval = X_train["lstat_disc"].iloc[0]  
print(34.0 in test_interval)  # True  
print(37.1 in test_interval)  # False  
```  

---

### **Key Concepts**  
- **[[Feature Engineering]]**: Process of transforming raw data into meaningful features (e.g., discretization).  
- **[[Data Preprocessing]]**: Steps like train-test splitting and standardization before modeling.  
- **[[Outliers]]**: Values outside expected ranges, accommodated via expanded interval edges.  

### **Visualization**  
- **Bar Plots**: Used to compare observation counts per bin between train and test sets.  
- **Value Counts**: `value_counts()` checks distribution balance across bins.  

### **Workflow Integration**  
1. **Train-Test Split** → **Interval Calculation** → **Discretization** → **Distribution Validation**.  
2. Tools: `pandas`, `Feature-engine`, `scikit-learn`.  

### **Wikilinks**  
- [[Equal-Width Discretization]] → [[Feature Engineering]] → [[Data Preprocessing]]  
- [[pd.cut()]] → [[KBinsDiscretizer]] → [[EqualWidthDiscretiser]]  
- [[Interval Edges]] → [[Bin Width]] → [[Outliers]]  

This summary aligns with the notebook’s focus on implementing equal-width discretization using multiple libraries while ensuring consistency between datasets.

---

---

## 2026-06-18 08:58 — Practical 5.2 - Equal-frequency-discretization.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the notebook content on **Equal-Frequency Discretization**:

---

### **Equal-Frequency Discretization**  
**Definition**: A technique to divide continuous variables into intervals (bins) such that each bin contains an equal proportion of observations. Bin edges are determined using quantiles, leading to variable bin widths. This method is particularly effective for skewed distributions.  
**Formula**: For \( N \) bins, the \( i \)-th quantile is calculated as:  
\[ Q_i = \text{Value at } \frac{i}{N} \text{-th percentile} \]  
**Example**:  
```python  
# Using pandas qcut for 10 equal-frequency bins  
X_train['lstat_disc'], intervals = pd.qcut(  
    X_train['LSTAT'], 10,  
    retbins=True, precision=3, duplicates='raise'  
)  
```  

---

### **Quantiles**  
**Definition**: Points dividing the data into intervals with equal probabilities (e.g., deciles for 10 intervals). Used to determine bin edges in equal-frequency discretization.  
**Formula**: The \( k \)-th quantile is computed as:  
\[ Q_k = (1 - \alpha) \cdot \text{min}(X) + \alpha \cdot \text{max}(X) \]  
where \( \alpha = \frac{k}{N} \), \( N \) = number of observations.  
**Example**:  
```python  
# Extracting quantile-based intervals for test set  
X_test['lstat_disc'] = pd.cut(X_test['LSTAT'], bins=intervals)  
```  

---

### **pandas.qcut**  
**Definition**: A pandas function to perform equal-frequency discretization by dividing data into quantiles.  
**Formula**: N/A (implementation-based).  
**Example**:  
```python  
# Discretizing 'LSTAT' into 10 bins with pandas  
X_train['lstat_disc'] = pd.qcut(X_train['LSTAT'], 10)  
```  

---

### **Feature-engine.EqualFrequencyDiscretiser**  
**Definition**: A `Feature-engine` transformer that automates equal-frequency discretization for multiple variables.  
**Formula**: N/A (method-based).  
**Example**:  
```python  
# Applying to multiple features (LSTAT, DIS, RM)  
disc = EqualFrequencyDiscretiser(q=10, variables=['LSTAT', 'DIS', 'RM'])  
disc.fit(X_train)  
train_t = disc.transform(X_train)  
```  

---

### **scikit-learn KBinsDiscretizer**  
**Definition**: A scikit-learn method for binning continuous features using quantile strategy.  
**Formula**: N/A (implementation-based).  
**Example**:  
```python  
# Quantile-based discretization with KBinsDiscretizer  
disc = KBinsDiscretizer(n_bins=10, strategy='quantile')  
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])  
train_t = disc.transform(X_train[['LSTAT', 'DIS', 'RM']])  
```  

---

### **Bin Edges**  
**Definition**: The boundaries defining each interval in discretization. In equal-frequency methods, these are determined by quantiles.  
**Formula**: N/A (derived from quantile calculations).  
**Example**:  
```python  
# Accessing bin edges from pandas qcut  
print(intervals)  # Outputs the quantile-based edges  
```  

---

### **Train-Test Distribution Comparison**  
**Definition**: Ensuring that discretization applied to the test set uses bin edges derived from the training set to avoid data leakage.  
**Formula**: N/A (process-based).  
**Example**:  
```python  
# Comparing bin distributions between train and test  
t1 = X_train['lstat_disc'].value_counts() / len(X_train)  
t2 = X_test['lstat_disc'].value_counts() / len(X_test)  
tmp = pd.concat([t1, t2], axis=1).plot.bar()  
```  

---

### **Answer to Q2: Leftmost Columns Difference**  
**Explanation**: The leftmost bins (lowest values) often capture outliers or extreme values in skewed distributions. Differences between train and test sets may arise due to:  
1. **Sampling Variability**: The test set might have fewer observations in the tail due to random splitting.  
2. **Quantile Edge Cases**: Bin edges derived from training data may not perfectly align with test data distributions.  

---

### **Key Concepts**  
- **[[Equal-Frequency Discretization]]**: Focuses on equal observation counts per bin.  
- **[[Quantiles]]**: Basis for determining bin edges.  
- **[[Feature Engineering]]**: Process of transforming raw data into meaningful features.  
- **[[Data Leakage]]**: Avoided by fitting bin edges only on the training set.  

---

### **Visualization**  
- **Bar Plots**: Used to compare the proportion of observations per bin between train and test sets.  
- **Interval Inspection**: `intervals` or `bin_edges_` attributes show quantile-derived boundaries.  

This summary aligns with the notebook’s focus on implementing equal-frequency discretization using multiple libraries while ensuring consistency between train and test sets. Related concepts include [[Binning]], [[Skewness]], and [[Stratified Sampling]].

---

---

## 2026-06-18 09:03 — Practical 5.3 - Discretization-plus-categorical-encoding.ipynb
**Style:** structured_academic (experimenting)

### Summary: Discretization and Categorical Encoding

#### [[Discretization (Binning)]]
**Definition**: The process of converting continuous variables into discrete intervals (bins) to reduce the impact of outliers, handle skewed distributions, and improve model performance.  
**Formula**: No direct formula; depends on the method (e.g., equal-width or equal-frequency).  
**Example**:  
```python
# Using KBinsDiscretizer for equal-frequency discretization
disc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='quantile')
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])
```

---

#### [[Equal-Frequency Discretization]]
**Definition**: A discretization method where each bin contains an equal number of observations, achieved by splitting data at quantiles.  
**Formula**: Bin edges defined by quantiles:  
$$
\text{Quantile positions} = \left\{0, \frac{1}{n}, \frac{2}{n}, \ldots, 1\right\}
$$
**Example**:  
```python
# Using Feature-engine for equal-frequency discretization
disc = EqualFrequencyDiscretiser(q=10, variables=['LSTAT', 'DIS', 'RM'], return_object=True)
disc.fit(X_train)
```

---

#### [[Equal-Width Discretization]]
**Definition**: A discretization method where bins have equal range intervals, calculated as (max - min)/number of bins.  
**Formula**: Bin width =  
$$
\text{Width} = \frac{\text{max}(X) - \text{min}(X)}{n_{\text{bins}}}
$$
**Example**:  
```python
# Using KBinsDiscretizer for equal-width discretization
disc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
disc.fit(X_train[['LSTAT', 'DIS', 'RM']])
```

---

#### [[Ordinal Encoding (Ordered)]]
**Definition**: Assigning integer codes to categorical bins in a way that reflects the monotonic relationship with the target variable.  
**Formula**: No direct formula; based on sorting bin means of the target.  
**Example**:  
```python
# Reordering bins to achieve monotonicity
enc = OrdinalEncoder(encoding_method='ordered')
enc.fit(train_t, y_train)
train_t = enc.transform(train_t)
```

---

#### [[Monotonic Relationship]]
**Definition**: A relationship where an increase in one variable consistently corresponds to an increase (or decrease) in another variable.  
**Example**:  
```python
# Plotting mean target values after ordinal encoding
pd.concat([train_t, y_train], axis=1).groupby('DIS')['MEDV'].mean().plot()
plt.ylabel('Mean House Price')
```
**Outcome**: The plot shows a steady increase/decrease in target values across bins, confirming monotonicity.

---

### Key Concepts Linkage  
- Discretization methods ([[Equal-Frequency Discretization]] and [[Equal-Width Discretization]]) are used to bin continuous variables.  
- [[Ordinal Encoding (Ordered)]] ensures bins are ordered to create a [[Monotonic Relationship]] with the target.  
- Outliers are minimized by grouping extreme values into bins with other observations.  
- Libraries like `Feature-engine` and `scikit-learn` implement these techniques.

---

---

## 2026-06-18 09:05 — Practical 5.4 - Arbitrary-interval-discretization.ipynb
**Style:** structured_academic (experimenting)

# Summary: Arbitrary Interval Discretization  

## Term: [[Arbitrary Interval Discretization]]  
**Definition**: A method of discretizing continuous variables where the interval boundaries are manually defined by the user, rather than derived from statistical properties of the data (e.g., quantiles or equal width). This approach allows for domain-specific or context-driven binning.  

**Formula**: No fixed mathematical formula; intervals are explicitly specified by the user. The general process involves:  
1. Defining interval edges (e.g., `[0, 10, 20, 30, ∞]`).  
2. Applying these edges to categorize data using a function like `pd.cut()`.  

**Example**:  
- **Code**:  
  ```python  
  intervals = [0, 10, 20, 30, np.Inf]  
  labels = ['0-10', '10-20', '20-30', '>30']  
  data['lstat_labels'] = pd.cut(data['LSTAT'], bins=intervals, labels=labels, include_lowest=True)  
  ```  
- **Output**: The `LSTAT` variable (lower status of the population) is binned into user-defined ranges (e.g., `0-10`, `10-20`).  
- **Observation Counts**:  
  ```python  
  data['lstat_labels'].value_counts()  
  ```  
  This shows the number of observations in each arbitrary interval.  

---

## Related Concepts  
- **[[Equal-width Discretization]]**: Bins of equal size (e.g., width = (max - min)/bins).  
- **[[Equal-frequency Discretization]]**: Bins with equal number of observations (quantile-based).  
- **[[pandas cut()]]**: Function used to implement arbitrary interval discretization.  
- **[[Boston Housing Dataset]]**: Dataset used in examples, containing features like `LSTAT` (percentage of lower status of the population).  

---

## Key Parameters in `pd.cut()`  
- `bins`: User-defined interval edges (e.g., `[0, 10, 20, 30, ∞]`).  
- `labels`: Optional custom labels for bins (e.g., `['0-10', '10-20']`).  
- `include_lowest=True`: Ensures the first bin includes the minimum value.  

This method is useful for aligning discretization with business rules or domain knowledge rather than purely statistical criteria.

---

---

## 2026-06-18 09:12 — Practical 6.1 - Outlier-Trimming.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

## [[Outlier]]
**Definition**: A data point significantly different from the majority of observations, potentially arising from a different mechanism. Outliers can distort statistical measures (e.g., mean, variance) and affect machine learning model performance.

---

## [[Trimming (Outlier Trimming)]]
**Definition**: The process of removing observations containing outliers in one or more variables. Three common boundary-setting methods are used:
1. **Standard Deviation Method** (normal distributions)
2. **Inter-Quartile Range (IQR) Proximity Rule** (any distribution)
3. **Arbitrary Percentile Method** (direct quantile limits)

---

## [[Inter-Quartile Range (IQR) Proximity Rule]]
**Definition**: A method to identify outliers using quartiles, robust to non-normal distributions.  
**Formula**:  
- IQR = Q₃ (75th percentile) - Q₁ (25th percentile)  
- Lower boundary = Q₁ - (IQR × distance)  
- Upper boundary = Q₃ + (IQR × distance)  
*Typical distance = 1.5 (or 3 for extreme outliers)*  

**Example**:  
```python
def find_boundaries_IQR(df, variable, distance=1.5):
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)
    lower = df[variable].quantile(0.25) - (IQR * distance)
    upper = df[variable].quantile(0.75) + (IQR * distance)
    return upper, lower
```

---

## [[Standard Deviation Method]]
**Definition**: A parametric method assuming normal distribution, flagging data beyond ±3 standard deviations from the mean.  
**Formula**:  
- Lower boundary = mean - (3 × std)  
- Upper boundary = mean + (3 × std)  

**Example**:  
```python
def find_boundaries_SD(df, variable, distance=3):
    lower = df[variable].mean() - (df[variable].std() * distance)
    upper = df[variable].mean() + (df[variable].std() * distance)
    return upper, lower
```

---

## [[Arbitrary Percentile Method]]
**Definition**: A non-parametric approach using fixed percentiles (e.g., 5th and 95th) as boundaries.  
**Formula**:  
- Lower boundary = 5th percentile  
- Upper boundary = 95th percentile  

**Example**:  
```python
def find_boundaries_percentiles(df, variable):
    lower = df[variable].quantile(0.05)
    upper = df[variable].quantile(0.95)
    return upper, lower
```

---

## [[Outlier Flagging & Trimming Implementation]]
**Definition**: Process of identifying and removing outliers using boolean masking.  
**Example**:  
```python
# Flag outliers in 'RM' column using IQR boundaries
outliers_RM = np.where(boston['RM'] > RM_upper_limit, True,
                       np.where(boston['RM'] < RM_lower_limit, True, False))

# Trim dataset (remove rows with outliers in any variable)
boston_trimmed = boston.loc[~(outliers_RM + outliers_LSTAT + outliers_CRIM), :]
```

---

## Key Observations
- **Boxplots** visualize outliers as points beyond the whiskers (1.5×IQR).
- **Trimming** may not remove all extreme values if variables are skewed or multivariate relationships exist.
- Method choice depends on data distribution and context (e.g., IQR for skewed data, SD for normal distributions).

--- 

All terms are interconnected via [[Wikilinks]] for cross-referencing. Formulas and code examples are derived directly from the provided notebooks.

---

---

## 2026-06-18 09:14 — Practical 6.2 - Winsorisation.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content:

---

## **Winsorization**  
**Definition**: A technique to handle [[Outliers]] by capping extreme values at specified percentiles instead of removing them. Unlike trimming, Winsorization replaces outliers with a cutoff value (e.g., 5th or 95th percentile), preserving dataset size.  
**Formula**:  
For a variable \( X \):  
\[
X_{\text{winsorized}} = 
\begin{cases} 
\text{Lower Bound} & \text{if } X < \text{Lower Bound} \\
X & \text{if } \text{Lower Bound} \leq X \leq \text{Upper Bound} \\
\text{Upper Bound} & \text{if } X > \text{Upper Bound}
\end{cases}
\]  
**Example**:  
```python
# Using numpy to winsorize 'RM' column
boston['RM'] = np.where(
    boston['RM'] > boston['RM'].quantile(0.95),  # Upper bound: 95th percentile
    boston['RM'].quantile(0.95), 
    np.where(
        boston['RM'] < boston['RM'].quantile(0.05),  # Lower bound: 5th percentile
        boston['RM'].quantile(0.05), 
        boston['RM']
    )
)
```

---

## **Outliers**  
**Definition**: Data points that significantly deviate from the majority of observations in a dataset. Outliers can skew statistical measures (e.g., mean) and affect machine learning model performance.  
**Formula**: Outliers are often identified using:  
- **Interquartile Range (IQR)**: \( \text{Lower Bound} = Q1 - 1.5 \times \text{IQR} \), \( \text{Upper Bound} = Q3 + 1.5 \times \text{IQR} \)  
- **Z-score**: \( Z = \frac{X - \mu}{\sigma} \), where \( |Z| > 3 \) indicates an outlier  
**Example**:  
```python
# Flagging outliers in 'LSTAT' using percentiles
outliers_LSTAT = np.where(
    boston['LSTAT'] > LSTAT_upper_limit, True,
    np.where(boston['LSTAT'] < LSTAT_lower_limit, True, False)
)
```

---

## **Percentile Capping**  
**Definition**: A method to limit extreme values by setting them to a specified percentile (e.g., 5th or 95th percentile). This is a key step in Winsorization.  
**Formula**:  
\[
\text{Capped Value} = 
\begin{cases} 
P_{\alpha} & \text{if } X > P_{\alpha} \\
P_{\beta} & \text{if } X < P_{\beta} \\
X & \text{otherwise}
\end{cases}
\]  
where \( P_{\alpha} \) and \( P_{\beta} \) are the upper and lower percentile bounds.  
**Example**:  
```python
# Using Feature-engine's Winsorizer with 5% fold (95th and 5th percentiles)
windsorizer = Winsorizer(capping_method='quantiles', tail='both', fold=0.05, variables=['RM', 'LSTAT', 'CRIM'])
boston_t = windsorizer.transform(boston)
```

---

## **Feature-engine Winsorizer**  
**Definition**: A Python library tool (`Winsorizer` from `feature_engine.outliers`) that automates Winsorization using configurable parameters like `capping_method` (quantiles, Gaussian, skewed) and `fold` (percentile threshold).  
**Formula**: N/A (implementation-specific)  
**Example**:  
```python
# Inspecting caps after fitting Winsorizer
print(windsorizer.right_tail_caps_)  # Shows upper bounds for each variable
print(windsorizer.left_tail_caps_)   # Shows lower bounds for each variable
```

---

### **Key Connections**  
- [[Winsorization]] addresses [[Outliers]] via [[Percentile Capping]].  
- [[Feature-engine Winsorizer]] provides an automated implementation of [[Winsorization]].  
- Diagnostic plots (histograms, Q-Q plots, boxplots) are used to visualize [[Outliers]] before and after Winsorization.  

--- 

This summary aligns with the notebook's focus on handling outliers through Winsorization, using both manual implementations (NumPy/Pandas) and the Feature-engine library.

---

---

## 2026-06-18 09:19 — Practical 6.3 - Capping.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### **Capping (Censoring/Top and Bottom Coding)**  
**Definition**: A method to replace extreme outlier values with predefined maximum or minimum thresholds, using statistical rules like Interquartile Range (IQR) or standard deviation (SD).  
**Formula**:  
- **IQR-based**:  
  Lower boundary = Q1 − (IQR × distance)  
  Upper boundary = Q3 + (IQR × distance)  
  Where IQR = Q3 − Q1 (Q1 = 25th percentile, Q3 = 75th percentile)  
- **Gaussian-based**:  
  Lower boundary = Mean − (SD × distance)  
  Upper boundary = Mean + (SD × distance)  
**Example**:  
```python
# Capping 'RM' using Gaussian boundaries (distance=3)
boston['RM'] = np.where(boston['RM'] > RM_upper_limit, RM_upper_limit, 
                         np.where(boston['RM'] < RM_lower_limit, RM_lower_limit, boston['RM']))
```

---

### **Interquartile Range (IQR)**  
**Definition**: A measure of statistical dispersion, representing the range between the first quartile (Q1) and third quartile (Q3) of a dataset.  
**Formula**:  
IQR = Q3 − Q1  
**Example**:  
```python
# Calculating IQR boundaries for skewed distributions
def find_skewed_boundaries(df, variable, distance):
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)
    lower_boundary = df[variable].quantile(0.25) - (IQR * distance)
    upper_boundary = df[variable].quantile(0.75) + (IQR * distance)
    return upper_boundary, lower_boundary
```

---

### **Gaussian (Normal Distribution) Boundaries**  
**Definition**: Outlier detection method assuming data follows a Gaussian distribution, using mean and standard deviation to define thresholds.  
**Formula**:  
Upper boundary = Mean + (SD × distance)  
Lower boundary = Mean − (SD × distance)  
**Example**:  
```python
# Calculating Gaussian boundaries (distance=3)
def find_normal_boundaries(df, variable, distance):
    upper_boundary = df[variable].mean() + df[variable].std() * distance
    lower_boundary = df[variable].mean() - df[variable].std() * distance
    return upper_boundary, lower_boundary
```

---

### **Winsorizer (Feature-engine)**  
**Definition**: A tool from the `feature_engine` library to cap outliers using either IQR or Gaussian methods.  
**Parameters**:  
- `capping_method`: 'iqr' or 'gaussian'  
- `tail`: 'left', 'right', or 'both'  
- `fold`: Multiplier for IQR or SD (e.g., 1.5, 3)  
**Example**:  
```python
# Applying Winsorizer to cap outliers in Boston dataset
windsorizer = Winsorizer(capping_method='gaussian', tail='both', fold=3, variables=['RM', 'LSTAT', 'CRIM'])
boston_t = windsorizer.transform(boston)
```

---

### **Boston Housing Dataset**  
**Definition**: A classical dataset containing housing prices and attributes in Boston, often used for regression and outlier analysis.  
**Example**:  
```python
# Loading Boston dataset with selected variables
boston = pd.read_csv("./data/boston_local.csv")
boston = boston[['RM', 'LSTAT', 'CRIM', 'MEDV']]
```

---

### Key Links  
- [[Capping]] is related to [[Winsorizer]] and [[Interquartile Range (IQR)]]  
- [[Gaussian Boundaries]] use [[Standard Deviation]] for outlier detection  
- [[Boston Housing Dataset]] is commonly used with outlier handling techniques like [[Capping]] and [[Winsorizer]]  

--- 

This summary integrates statistical concepts, code implementations, and domain-specific tools for outlier capping.

---

---

## 2026-06-18 09:22 — Practical 6.4 - Zero-coding.ipynb
**Style:** structured_academic (experimenting)

### Summary: Zero-Coding and Capping Techniques

#### [[Zero-Coding]]
- **Definition**: A variant of bottom-coding where the lower bound of a variable is set to zero, typically for variables that cannot logically take negative values (e.g., age, income). This ensures all values are non-negative while preserving the distribution shape above zero.
- **Formula**: Not applicable (method-based).
- **Example**:  
  ```python
  # Manual zero-coding
  data.loc[data['x'] < 0, 'x'] = 0
  data.loc[data['y'] < 0, 'y'] = 0
  data.loc[data['z'] < 0, 'z'] = 0
  ```
  Using `ArbitraryOutlierCapper`:
  ```python
  capper = ArbitraryOutlierCapper(min_capping_dict={'x':0, 'y':0, 'z':0})
  data_t = capper.transform(data)
  ```

#### [[Bottom-Coding]]
- **Definition**: The process of capping the lower tail of a variable’s distribution at a specified threshold (e.g., zero or a percentile-based value). Used to handle outliers or ensure logical bounds.
- **Formula**: Threshold = \( \text{mean} - k \times \text{std} \) or \( \text{quantile}(p) \), where \( k \) and \( p \) are parameters.
- **Example**:  
  Using `ArbitraryOutlierCapper` with a custom threshold (e.g., 0 for zero-coding):
  ```python
  capper = ArbitraryOutlierCapper(min_capping_dict={'x': 0})
  ```

#### [[Top-Coding]]
- **Definition**: The process of capping the upper tail of a variable’s distribution at a specified threshold (e.g., a fixed value or percentile). Complements bottom-coding for full distribution capping.
- **Formula**: Threshold = \( \text{mean} + k \times \text{std} \) or \( \text{quantile}(1-p) \).
- **Example**:  
  To cap values above 7:
  ```python
  capper = ArbitraryOutlierCapper(max_capping_dict={'x':7, 'y':7, 'z':7})
  ```

#### [[ArbitraryOutlierCapper]]
- **Definition**: A class from the `Feature-engine` library used to cap outliers at user-defined thresholds for specified variables. Supports both bottom and top coding.
- **Formula**: Not applicable (implementation-based).
- **Example**:  
  Capping both tails:
  ```python
  capper = ArbitraryOutlierCapper(
      min_capping_dict={'x':0, 'y':0, 'z':0},
      max_capping_dict={'x':7, 'y':7, 'z':7}
  )
  data_t = capper.transform(data)
  ```

#### [[Capping Methods]]
- **Definition**: Strategies for determining capping thresholds, including:
  - **Gaussian Method**: Uses \( \text{mean} \pm k \times \text{std} \).
  - **Skewed Method**: Uses \( \text{quartile} \pm k \times \text{IQR} \).
  - **Quantile Method**: Uses specific percentiles (e.g., 5th and 95th).
- **Formula**: 
  - Gaussian: \( \text{Threshold} = \mu \pm k\sigma \)
  - Skewed: \( \text{Threshold} = Q \pm k \times \text{IQR} \)
  - Quantile: \( \text{Threshold} = \text{Quantile}(p) \)
- **Example**:  
  Winsorization using quantiles (linked to [[Winsorization]]):
  ```python
  from feature_engine.outliers import Winsorizer
  winsorizer = Winsorizer(capping_method='quantiles', fold=0.05, variables=['price'])
  ```

---

### Key Links
- [[Winsorization]]: For comparison with other outlier handling techniques.
- [[Interquartile Range (IQR)]]: Used in skewed method thresholds.
- [[Standard Deviation]]: Basis for Gaussian method thresholds.

---

---

## 2026-06-18 09:26 — Practical 3.2 - One-Hot-Encoding-Top-Categories.ipynb
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

---

---

## 2026-06-18 09:29 — Practical 3.3 - Replacing-categories-by-ordinal-numbers.ipynb
**Style:** structured_academic (experimenting)

# Summary: Ordinal Encoding Techniques

## **Ordinal Encoding**
**Definition**: A method of converting categorical variables into numerical values by assigning each category an arbitrary integer (e.g., 0 to k-1 or 1 to k), where k is the number of unique categories.  
**Formula**:  
\[ \text{Mapping} = \{ k_i \rightarrow m_i \mid k_i \in \text{Categories}, m_i \in \mathbb{Z} \} \]  
**Example**:  
```python
ordinal_mapping = {k: i for i, k in enumerate(X_train['A7'].unique(), 0)}
X_train['A7'] = X_train['A7'].map(ordinal_mapping)
```

---

## **Pandas Ordinal Encoding**
**Definition**: Implementing ordinal encoding using pandas’ `map()` function and manual dictionary creation to replace categories with integers.  
**Formula**:  
\[ \text{Encoded Value} = \text{Category} \mapsto \text{Integer via Dictionary} \]  
**Example**:  
```python
def find_category_mappings(df, variable):
    return {k: i for i, k in enumerate(df[variable].unique(), 0)}

def integer_encode(train, test, variable, ordinal_mapping):
    train[variable] = train[variable].map(ordinal_mapping)
    test[variable] = test[variable].map(ordinal_mapping)
```

---

## **Scikit-learn OrdinalEncoder**
**Definition**: A scikit-learn class (`OrdinalEncoder`) that automatically maps categories to integers in a specified order.  
**Formula**:  
\[ X_{\text{encoded}} = \text{OrdinalEncoder().fit_transform}(X_{\text{categorical}}) \]  
**Example**:  
```python
from sklearn.preprocessing import OrdinalEncoder
le = OrdinalEncoder()
le.fit(X_train[vars_categorical])
X_train_enc = le.transform(X_train[vars_categorical])
```

---

## **Feature-engine OrdinalEncoder**
**Definition**: An encoder from the `feature_engine` library that applies arbitrary ordinal encoding while retaining category-to-integer mappings.  
**Formula**:  
\[ X_{\text{encoded}} = \text{OrdinalEncoder}(\text{encoding_method='arbitrary')}.transform(X) \]  
**Example**:  
```python
from feature_engine.encoding import OrdinalEncoder
ordinal_enc = OrdinalEncoder(encoding_method='arbitrary', variables=vars_categorical)
ordinal_enc.fit(X_train)
X_train = ordinal_enc.transform(X_train)
```

---

## **Integer Encoding**
**Definition**: Synonym for ordinal encoding, emphasizing the conversion of categorical labels to integers.  
**Formula**: Same as [[Ordinal Encoding]].  
**Example**:  
```python
for variable in vars_categorical:
    if variable != 'A7':
        mappings = find_category_mappings(X_train, variable)
        integer_encode(X_train, X_test, variable, mappings)
```

---

## **Category Mapping**
**Definition**: The dictionary that defines the relationship between original categories and their assigned integers.  
**Formula**:  
\[ \text{Mapping} = \{ \text{Category} : \text{Integer} \} \]  
**Example**:  
```python
ordinal_mapping = {k: i for i, k in enumerate(X_train['A7'].unique(), 0)}
# Output: {'A7_Category1': 0, 'A7_Category2': 1, ...}
```

---

## **Key Notes**
- **Use Case**: Preferred for non-linear models that can handle arbitrary integer assignments.  
- **Libraries**: [[Pandas]], [[Scikit-learn]], and [[Feature-engine]] provide distinct implementations.  
- **Caution**: Arbitrary mappings may not preserve ordinal relationships unless explicitly defined.  

[[Categorical Variables]] vs. [[Ordinal Variables]] distinctions are critical for choosing encoding methods.

---

---

## 2026-06-18 09:32 — Practical 3.4 - replacing-categories-by-counts-frequency.ipynb
**Style:** structured_academic (experimenting)

### Summary: Count and Frequency Encoding in Categorical Variable Processing

---

#### [[Count Encoding]]  
**Definition**: A technique in categorical variable encoding where each category is replaced by the number of times it appears in the dataset. This method assumes that the frequency of a category may correlate with the target variable.  
**Formula**:  
\[
\text{Count}(c) = \text{Number of occurrences of category } c \text{ in the dataset}
\]  
**Example**:  
```python  
# Using pandas to perform count encoding on column 'A7'  
count_map = X_train['A7'].value_counts().to_dict()  
X_train['A7'] = X_train['A7'].map(count_map)  
X_test['A7'] = X_test['A7'].map(count_map)  
```  
**Link**: [[Frequency Encoding]], [[Categorical Variable Encoding]]  

---

#### [[Frequency Encoding]]  
**Definition**: A variant of count encoding where categories are replaced by their relative frequency (proportion) in the dataset. This normalization helps in comparing categories across datasets of different sizes.  
**Formula**:  
\[
\text{Frequency}(c) = \frac{\text{Count}(c)}{\text{Total number of observations}} = \frac{\text{Count}(c)}{N}
\]  
**Example**:  
```python  
# Calculating frequency map for column 'A6'  
frequency_map = (X_train['A6'].value_counts() / len(X_train)).to_dict()  
X_train['A6'] = X_train['A6'].map(frequency_map)  
X_test['A6'] = X_test['A6'].map(frequency_map)  
```  
**Link**: [[Count Encoding]], [[Categorical Variable Encoding]]  

---

#### [[CountFrequencyEncoder]]  
**Definition**: A class from the `Feature-engine` library that automates count or frequency encoding. It allows specification of the encoding method (`'count'` or `'frequency'`) and handles fitting/transforming datasets.  
**Formula**: Same as [[Count Encoding]] or [[Frequency Encoding]], depending on the `encoding_method` parameter.  
**Example**:  
```python  
# Using Feature-engine for count encoding  
count_enc = CountFrequencyEncoder(encoding_method='count')  
count_enc.fit(X_train)  
X_train_enc = count_enc.transform(X_train)  
X_test_enc = count_enc.transform(X_test)  
```  
**Link**: [[Count Encoding]], [[Frequency Encoding]]  

---

#### [[Categorical Variable Encoding]]  
**Definition**: The general process of converting categorical variables into numerical representations to enable use in machine learning models. Includes techniques like [[Count Encoding]], [[Frequency Encoding]], one-hot encoding, and ordinal encoding.  
**Formula**: N/A (umbrella term for encoding methods).  
**Example**:  
- Applying [[Count Encoding]] to variables `['A1', 'A4', 'A5', ...]` in a dataset.  
**Link**: [[Count Encoding]], [[Frequency Encoding]], [[Ordinal Encoding]], [[One-Hot Encoding]]  

---

### Key Concepts Recap  
- **Count vs. Frequency Encoding**: Count uses raw frequencies, while frequency normalizes by total observations.  
- **Implementation Tools**: Pandas (manual mapping) and `Feature-engine` (automated via `CountFrequencyEncoder`).  
- **Use Case**: Reduces dimensionality compared to one-hot encoding and retains category importance.  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020).

---

---

## 2026-06-18 09:38 — Practical 3.5 - ordered-ordinal-encoding.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the content:

---

### **Ordered Integer Encoding**  
**Definition**: A technique where categorical variables are encoded as integers based on the mean value of the target variable for each category. Categories are sorted by their target mean and assigned digits from `0` to `k-1` (where `k` is the number of categories), creating a monotonic relationship with the target.  
**Formula**:  
Mean target per category = \(\frac{\text{Sum of target values in category}}{\text{Number of observations in category}}\)  
**Example**:  
```python  
# Sort categories by target mean and create mappings  
ordered_labels = X_train.groupby(['A7'])['A16'].mean().sort_values().index  
ordinal_mapping = {k: i for i, k in enumerate(ordered_labels, 0)}  
```  

---

### **Monotonic Relationship**  
**Definition**: A relationship where the encoded integer values of a categorical variable consistently increase or decrease alongside the target variable’s mean values. This ensures linear models can interpret the encoded values meaningfully.  
**Formula**: N/A (Conceptual)  
**Example**:  
```python  
# Plot after encoding shows ordered target means  
X_train.groupby(['A7'])['A16'].mean().plot()  
plt.title('Monotonic relationship between A7 and target')  
```  

---

### **Target-Based Encoding**  
**Definition**: Encoding categorical variables by leveraging the target variable’s distribution. Categories are ranked by their association with the target (e.g., mean target value) to assign integers.  
**Formula**:  
Sorted categories = \( \text{Categories ordered by } \frac{\sum y}{n} \) (where \(y\) = target, \(n\) = observations per category)  
**Example**:  
```python  
# Calculate target mean per category and sort  
X_train.groupby(['A7'])['A16'].mean().sort_values()  
```  

---

### **Feature-engine OrdinalEncoder**  
**Definition**: A scikit-learn-compatible transformer from the `Feature-engine` library that performs ordered integer encoding by fitting on the training data and the target variable.  
**Formula**: N/A (Algorithmic)  
**Example**:  
```python  
ordinal_enc = OrdinalEncoder(encoding_method='ordered')  
ordinal_enc.fit(X_train, y_train)  # Requires target for ordering  
X_train_enc = ordinal_enc.transform(X_train)  
```  

---

### **Key Connections**  
- [[Ordinal Encoding]] (previous method) assigns arbitrary integers, while **Ordered Integer Encoding** uses target-based ordering.  
- **Monotonic Relationship** is critical for linear models, as it ensures encoded values align with the target’s trend.  
- **Feature-engine OrdinalEncoder** automates the ordered encoding process, integrating with scikit-learn pipelines.  

--- 

This summary links encoding techniques to their mathematical foundations and practical implementations, emphasizing their suitability for different model types (linear vs. non-linear).

---

---

## 2026-06-18 09:40 — Practical 3.6 - target-mean-encoding.ipynb
**Style:** structured_academic (experimenting)

Here is a structured academic summary of the content:

---

### **Target Mean Encoding**  
**Definition**: A technique where categorical variable categories are replaced by the average target value observed for each category. This method leverages the relationship between categorical features and the target variable to create informative numerical representations.  

**Formula**:  
For a categorical feature \( X \) with category \( c \) and target variable \( y \):  
\[
\text{Encoded value} = \mu_c = \frac{\sum_{i: X_i = c} y_i}{N_c}
\]  
where \( N_c \) is the number of observations in category \( c \).  

**Example**:  
- **Pandas Implementation**:  
  ```python
  # Calculate target mean per category for 'A7'
  ordered_labels = X_train.groupby(['A7'])['A16'].mean().to_dict()
  # Replace categories with target means
  X_train['A7'] = X_train['A7'].map(ordered_labels)
  X_test['A7'] = X_test['A7'].map(ordered_labels)
  ```  
- **Feature-engine Implementation**:  
  ```python
  # Initialize and fit MeanEncoder
  mean_enc = MeanEncoder(variables=None)
  mean_enc.fit(X_train, y_train)
  # Transform datasets
  X_train_enc = mean_enc.transform(X_train)
  X_test_enc = mean_enc.transform(X_test)
  ```  

---

### **MeanEncoder (Feature-engine)**  
**Definition**: A class from the `Feature-engine` library that automates target mean encoding. It calculates the mean of the target variable for each category during fitting and applies the transformation to the data.  

**Formula**: Same as [[Target Mean Encoding]].  

**Example**:  
```python
# After splitting data into X_train, X_test, y_train, y_test:
mean_enc = MeanEncoder(variables=None)
mean_enc.fit(X_train, y_train)  # Learns category means
X_train_enc = mean_enc.transform(X_train)  # Applies encoding
```  

---

### **Key Considerations**  
1. **Data Splitting**: Always fit the encoder on the training data only to prevent data leakage.  
2. **Handling Unseen Categories**: The encoder assigns a default value (e.g., mean of target) to unseen categories in the test set.  
3. **Related Concepts**: [[Categorical Variables]], [[Target Encoding]], [[Feature Engineering]], [[Mean Normalization]].  

--- 

This summary integrates theoretical definitions, mathematical formulations, and practical code examples for implementing target mean encoding using both pandas and Feature-engine.

---

---

## 2026-06-18 09:44 — Practical 3.7 - grouping-rare-categories.ipynb
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

---

---

## 2026-06-18 09:46 — Practical 4.1 - logarithmic-transformation.ipynb
**Style:** structured_academic (experimenting)

Here's a structured summary of the content using the requested academic format:

---

### [[Logarithmic Transformation]]
**Definition**: A mathematical method used to reduce right-skewness in data by applying the logarithm function. It is applicable only to positive values and helps approximate a normal distribution.  
**Formula**:  
$$ X_t = \log(X) $$  
**Example**:  
```python
# Using NumPy
data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.log(data[['LSTAT', 'NOX', 'DIS', 'RM']])
```

---

### [[Q-Q Plot]]
**Definition**: A graphical tool to compare the distribution of a dataset against a theoretical normal distribution. Quantiles of the data are plotted against quantiles of a normal distribution.  
**Formula**: Not applicable (visual diagnostic tool)  
**Example**:  
```python
# Integrated into diagnostic_plots function
stats.probplot(df[variable], dist="norm", plot=plt)
```

---

### [[Diagnostic Plots]]
**Definition**: A combined visualization (histogram + Q-Q plot) to assess the distribution of a variable before and after transformation.  
**Formula**: Not applicable (visual diagnostic tool)  
**Example**:  
```python
def diagnostic_plots(df, variable):
    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    df[variable].hist(bins=30)
    plt.subplot(1, 2, 2)
    stats.probplot(df[variable], dist="norm", plot=plt)
    plt.show()
```

---

### [[FunctionTransformer (scikit-learn)]]
**Definition**: A scikit-learn class that allows application of arbitrary functions (e.g., logarithm) to transform data.  
**Formula**: Not applicable (implementation tool)  
**Example**:  
```python
from sklearn.preprocessing import FunctionTransformer
transformer = FunctionTransformer(np.log, validate=True)
data_tf = transformer.transform(data[cols])
```

---

### [[LogTransformer (Feature-engine)]]
**Definition**: A specialized transformer from the Feature-engine library for applying logarithmic transformations while handling errors for non-positive values.  
**Formula**: Not applicable (implementation tool)  
**Example**:  
```python
from feature_engine.transformation import LogTransformer
lt = LogTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])
data_tf = lt.transform(data)
```

---

### [[Normal Distribution]]
**Definition**: A probability distribution characterized by a symmetric bell-shaped curve, assumed by many statistical models (e.g., linear regression).  
**Formula**:  
$$ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} $$  
**Example**:  
Referenced in Q-Q plots (`dist="norm"`) to compare data against a theoretical normal distribution.

---

### Key Concept Links
- [[Logarithmic Transformation]] is used to approach [[Normal Distribution]].
- [[Q-Q Plot]] and [[Diagnostic Plots]] are used to evaluate the need for transformations.
- [[FunctionTransformer]] and [[LogTransformer]] are implementation tools for applying transformations.

---

---

## 2026-06-18 09:48 — Practical 4.2 - reciprocal-transformation.ipynb
**Style:** structured_academic (experimenting)

### Summary: Reciprocal Transformation

#### **Term**: [[Reciprocal Transformation]]  
**Definition**: A mathematical transformation that applies the reciprocal function (\( X_t = 1/X \)) to variables. It drastically alters the distribution of variables and is undefined for \( X = 0 \), but applicable to negative values. It is often used to normalize skewed data or unmask linear relationships in regression models.  

**Formula**:  
\[
X_t = \frac{1}{X}
\]  

**Example**:  
1. **NumPy Implementation**:  
   ```python  
   data_tf[['LSTAT', 'NOX', 'DIS', 'RM']] = np.reciprocal(data[['LSTAT', 'NOX', 'DIS', 'RM']])  
   ```  
   Applies the reciprocal to specified columns in a DataFrame.  

2. **Scikit-learn (`FunctionTransformer`)**:  
   ```python  
   transformer = FunctionTransformer(np.reciprocal, validate=True)  
   data_tf = pd.DataFrame(transformer.transform(data[cols]), columns=cols)  
   ```  
   Transforms selected columns using scikit-learn’s `FunctionTransformer`.  

3. **Feature-engine (`ReciprocalTransformer`)**:  
   ```python  
   rt = ReciprocalTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])  
   data_tf = rt.transform(data)  
   ```  
   Uses Feature-engine’s dedicated `ReciprocalTransformer` for the transformation.  

**Evaluation**:  
The effect of the transformation is assessed using [[Diagnostic Plots]] (histogram and Q-Q plots) to compare the distribution before and after applying the reciprocal function.  

---

### Key Concepts:  
- **[[Diagnostic Plots]]**: Visual tools (histogram + Q-Q plot) to evaluate distributional changes.  
- **[[NumPy]]**: Library for numerical computations in Python.  
- **[[scikit-learn]]**: Machine learning library providing preprocessing tools like `FunctionTransformer`.  
- **[[Feature-engine]]**: Library specialized in feature engineering, including `ReciprocalTransformer`.  
- **[[Box-Cox Transformation]]**: Another common transformation for normalizing data (requires positive values).  

--- 

This summary aligns with the structured academic format and connects related concepts via wikilinks for cross-referencing.

---

---

## 2026-06-18 09:51 — Practical 4.3 - square-cube-root.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### **Square Root Transformation**  
**Definition**: A power transformation with an exponent of \( \frac{1}{2} \), used to reduce right skewness in variables. Requires non-negative values to avoid NaN/errors.  
**Formula**:  
\[ X_t = X^{1/2} \]  
**Example**:  
- **NumPy**: `np.sqrt(data[['LSTAT', 'NOX']])`  
- **scikit-learn**: `FunctionTransformer(np.sqrt)`  
- **Feature-engine**: `PowerTransformer(exp=0.5)`  

---

### **Cube Root Transformation**  
**Definition**: A power transformation with an exponent of \( \frac{1}{3} \), less aggressive than square root for reducing skewness. Also requires non-negative values.  
**Formula**:  
\[ X_t = X^{1/3} \]  
**Example**:  
- **NumPy**: `np.cbrt(data[['DIS', 'RM']])`  
- **Feature-engine**: `PowerTransformer(exp=1/3)`  

---

### **Diagnostic Plots**  
**Definition**: Visual tools to evaluate the effect of transformations on variable distributions. Includes histograms and Q-Q plots.  
**Formula**: N/A  
**Example**:  
```python  
def diagnostic_plots(df, variable):  
    plt.figure(figsize=(15,6))  
    plt.subplot(1, 2, 1)  
    df[variable].hist(bins=30)  
    plt.subplot(1, 2, 2)  
    stats.probplot(df[variable], dist="norm", plot=plt)  
    plt.show()  
```  

---

### **Key Libraries & Tools**  
1. **[[NumPy]]**: Direct implementation of transformations (e.g., `np.sqrt`, `np.cbrt`).  
2. **[[scikit-learn]]**: `FunctionTransformer` for custom transformations.  
3. **[[Feature-engine]]**: `PowerTransformer` for flexible power/exponent adjustments.  

---

### **Workflow Steps**  
1. **Check original distribution**: Use `diagnostic_plots` on raw data.  
2. **Apply transformation**: Select method (NumPy, scikit-learn, or Feature-engine).  
3. **Visualize transformed data**: Re-run `diagnostic_plots` to assess normality.  

---

This summary links transformations to their mathematical foundations, implementation tools, and diagnostic techniques. Use [[Wikilinks]] to explore related concepts like [[Power Transformation]], [[Q-Q Plot]], or [[Data Preprocessing]] in other notes.

---

---

## 2026-06-18 09:56 — Practical 4.4 - power-transformation.ipynb
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### [[Power Transformation]]
**Definition**: A mathematical transformation where a variable is raised to an exponent λ (lambda), used to make data more normally distributed or improve model performance.  
**Formula**:  
\[ X_t = X^{\lambda} \]  
**Examples**:  
- Square root: \( \lambda = 1/2 \)  
- Cube root: \( \lambda = 1/3 \)  
- Arbitrary exponent (e.g., \( \lambda = 0.3 \))  

---

### [[Square Root Transformation]]  
**Definition**: A specific power transformation with \( \lambda = 1/2 \), used for right-skewed data. Not defined for negative values.  
**Formula**:  
\[ X_t = X^{1/2} \]  
**Example**:  
```python
data_tf[['LSTAT', 'NOX']] = np.sqrt(data[['LSTAT', 'NOX']])
```  

---

### [[Cube Root Transformation]]  
**Definition**: A specific power transformation with \( \lambda = 1/3 \), suitable for moderately skewed data.  
**Formula**:  
\[ X_t = X^{1/3} \]  
**Example**:  
```python
data_tf[['DIS', 'RM']] = np.cbrt(data[['DIS', 'RM']])
```  

---

### [[Exponential Transformation with NumPy]]  
**Definition**: Applying power transformations using NumPy's `np.power()` function.  
**Formula**:  
\[ X_t = X^{\lambda} \]  
**Example**:  
```python
data_tf[['LSTAT', 'NOX']] = np.power(data[['LSTAT', 'NOX']], 0.3)
```  

---

### [[Exponential Transformation with Scikit-learn]]  
**Definition**: Using `FunctionTransformer` to apply custom power transformations.  
**Formula**:  
\[ X_t = X^{\lambda} \]  
**Example**:  
```python
transformer = FunctionTransformer(lambda x: np.power(x, 0.3), validate=True)
data_tf = pd.DataFrame(transformer.transform(data[cols]), columns=cols)
```  

---

### [[Exponential Transformation with Feature-engine]]  
**Definition**: Applying power transformations via `PowerTransformer` from the Feature-engine library.  
**Formula**:  
\[ X_t = X^{\lambda} \]  
**Example**:  
```python
et = PowerTransformer(variables=['LSTAT', 'NOX'], exp=0.3)
data_tf = et.transform(data)
```  

---

### [[Applying Different Power Transformations]]  
**Definition**: Using a pipeline to apply varying exponents to different features.  
**Formula**:  
\[ X_t = X^{\lambda_i} \quad \text{for feature } i \]  
**Example**:  
```python
pipe = Pipeline([
    ('power1', PowerTransformer(variables=['LSTAT'], exp=0.3)),
    ('power2', PowerTransformer(variables=['RM'], exp=0.5))
])
data_tf = pipe.transform(data)
```  

---

### Key Notes:
1. **Diagnostic Plots**: Use histograms and Q-Q plots (via `diagnostic_plots()`) to assess distributional changes post-transformation.  
2. **Constraints**: Square root requires non-negative values; cube root can handle negatives but may not fully normalize data.  
3. **Libraries**: NumPy (direct computation), Scikit-learn (flexible transformers), Feature-engine (dedicated power tools).  

All transformations aim to improve normality or linearity for regression models like linear/logistic regression.

---

---

## 2026-06-18 10:03 — Practical 4.5 - Box-Cox-transformation.ipynb
**Style:** structured_academic (experimenting)

Here’s a structured summary of the content using the requested format:

---

### **Box-Cox Transformation**  
**Definition**: A power transformation method used to normalize data by applying a family of functions parameterized by λ (lambda). It generalizes the logarithm and power transformations.  
**Formula**:  
\[
X_t = 
\begin{cases} 
\frac{X^{\lambda} - 1}{\lambda} & \text{if } \lambda \neq 0 \\
\log(X) & \text{if } \lambda = 0 
\end{cases}
\]  
**Example**:  
- Applied to the `LSTAT` variable in the Boston House Price dataset using SciPy:  
  ```python
  data_tf['LSTAT'], param = stats.boxcox(data['LSTAT'])
  ```  
- Optimal λ is printed and stored in `param` or `transformer.lambdas_` (scikit-learn).  

---

### **Power Transformation**  
**Definition**: A broader class of transformations where a variable \(X\) is raised to a power \(\lambda\) to improve normality.  
**Formula**:  
\[
X_t = X^{\lambda}
\]  
**Example**:  
- Special cases include square root (\(\lambda = 0.5\)) and cube root (\(\lambda = 1/3\)).  
- Implemented via `PowerTransformer` in scikit-learn:  
  ```python
  transformer = PowerTransformer(method='box-cox', standardize=False)
  ```  

---

### **Diagnostic Plots**  
**Definition**: Visual tools to assess the distribution of a variable before and after transformation.  
**Formula**: N/A  
**Example**:  
- A custom function generates histograms and Q-Q plots:  
  ```python
  def diagnostic_plots(df, variable):
      plt.figure(figsize=(15,6))
      plt.subplot(1, 2, 1)
      df[variable].hist(bins=30)
      plt.subplot(1, 2, 2)
      stats.probplot(df[variable], dist="norm", plot=plt)
      plt.show()
  ```  
- Used to compare `LSTAT` distributions pre- and post-transformation.  

---

### **Optimal Lambda (λ)**  
**Definition**: The value of λ that maximizes normality in the transformed data, selected via maximum likelihood estimation.  
**Formula**: Determined algorithmically (e.g., via `scipy.stats.boxcox`).  
**Example**:  
- SciPy returns λ in `param` after fitting:  
  ```python
  print('Optimal λ: ', param)
  ```  
- Scikit-learn stores λ values in `transformer.lambdas_`.  

---

### **Libraries & Tools**  
#### **1. SciPy**  
**Definition**: Library for scientific computing, including statistical transformations.  
**Example**:  
- `stats.boxcox()` applies the Box-Cox transformation:  
  ```python
  from scipy.stats import boxcox
  ```  

#### **2. Scikit-learn**  
**Definition**: Machine learning library with preprocessing utilities.  
**Example**:  
- `PowerTransformer` with `method='box-cox'`:  
  ```python
  from sklearn.preprocessing import PowerTransformer
  ```  

#### **3. Feature-engine**  
**Definition**: Open-source library for feature engineering tasks.  
**Example**:  
- `BoxCoxTransformer` for direct application:  
  ```python
  from feature_engine.transformation import BoxCoxTransformer
  ```  

---

### **Boston House Price Dataset**  
**Definition**: A classic dataset containing housing prices and attributes (e.g., `LSTAT`, `NOX`).  
**Example**:  
- Loaded and transformed in the notebook:  
  ```python
  data = pd.read_csv("./data/boston_local.csv")
  ```  

---

### **Key Connections**  
- [[Box-Cox Transformation]] is a special case of [[Power Transformation]].  
- [[Logarithmic Transformation]] is equivalent to Box-Cox when \(\lambda = 0\).  
- Libraries like [[SciPy]], [[Scikit-learn]], and [[Feature-engine]] provide implementations.  
- [[Diagnostic Plots]] evaluate transformation effectiveness.  

--- 

This summary links concepts hierarchically and emphasizes practical implementation details. Let me know if you need expansions!

---

---

## 2026-06-18 10:09 — Practical 4.6 - Yeo-Johnson-transformation.ipynb
**Style:** structured_academic (experimenting)

### Summary: Yeo-Johnson Transformation

#### Term: [[Yeo-Johnson Transformation]]  
**Definition**:  
An extension of the [[Box-Cox Transformation]] that can handle variables with zero and negative values, in addition to positive values. It applies different power transformation formulas based on the sign of the input variable \( X \) and the transformation parameter \( \lambda \).  

**Formula**:  
\[
X_t = 
\begin{cases} 
\frac{(X+1)^{\lambda} - 1}{\lambda} & \text{if } \lambda \neq 0, X \geq 0 \\ 
\log(X+1) & \text{if } \lambda = 0, X \geq 0 \\ 
-\frac{(-X+1)^{2-\lambda} - 1}{2-\lambda} & \text{if } \lambda \neq 2, X < 0 \\ 
-\log(-X+1) & \text{if } \lambda = 2, X < 0 \\ 
\end{cases}
\]  
where \( X \) is the original variable and \( \lambda \) is the optimal transformation parameter.  

**Examples**:  

1. **Using SciPy**  
   ```python  
   from scipy import stats  
   data_tf['LSTAT'], param = stats.yeojohnson(data['LSTAT'])  
   print('Optimal λ:', param)  
   ```  
   - Applies the transformation directly and returns the optimal \( \lambda \).  

2. **Using Scikit-learn (`PowerTransformer`)**  
   ```python  
   from sklearn.preprocessing import PowerTransformer  
   transformer = PowerTransformer(method='yeo-johnson', standardize=False)  
   transformer.fit(data[cols])  # cols = ['LSTAT', 'NOX', 'DIS', 'RM']  
   data_tf = transformer.transform(data[cols])  
   ```  
   - Fits the transformer to select \( \lambda \) for each variable and transforms the data.  

3. **Using Feature-engine (`YeoJohnsonTransformer`)**  
   ```python  
   from feature_engine.transformation import YeoJohnsonTransformer  
   yjt = YeoJohnsonTransformer(variables=['LSTAT', 'NOX', 'DIS', 'RM'])  
   yjt.fit(data)  
   data_tf = yjt.transform(data)  
   ```  
   - Stores learned \( \lambda \) values in `yjt.lambda_dict_` for each variable.  

**Purpose**:  
Used to stabilize variance, normalize distributions, or prepare data for models requiring normality (e.g., linear regression). Unlike [[Box-Cox Transformation]], it accommodates non-positive values.  

**Visualization**:  
Diagnostic plots (histograms and Q-Q plots) are used to compare distributions before and after transformation (via `diagnostic_plots` function).  

**Key Libraries**:  
- `scipy.stats.yeojohnson`  
- `sklearn.preprocessing.PowerTransformer`  
- `feature_engine.transformation.YeoJohnsonTransformer`  

**Related Concepts**:  
- [[Power Transformation]]  
- [[Box-Cox Transformation]]  
- [[Data Preprocessing]]  
- [[Normality Assumption]]

---

---

## 2026-06-18 10:15 — Exercise_7 - Performing Feature Scaling.ipynb
**Style:** structured_academic (experimenting)

### Data Wrangling: Feature Scaling

#### Term -> Definition -> Formula -> Example

**Standard Scaling (Z-Score Normalization)**
- **Definition:** Standard scaling transforms features by subtracting the mean and then scaling to unit variance.
  - Formula: \( Z = \frac{x - \mu}{\sigma} \)
    - Where \( x \) is the feature value, \( \mu \) is the mean of the feature, and \( \sigma \) is the standard deviation of the feature.

- **Example:** 
  ```python
  from sklearn.preprocessing import StandardScaler
  
  # Initialize scaler
  scaler = StandardScaler()
  
  # Fit and transform training data
  X_train_scaled = scaler.fit_transform(X_train)
  ```

**Robust Scaling**
- **Definition:** Robust scaling uses the median and the interquartile range (IQR) to scale features, making it robust to outliers.
  - Formula: \( Z = \frac{x - Q_1}{Q_3 - Q_1} \times (Q_{75} - Q_{25}) + Q_{25} \)
    - Where \( Q_1 \) is the first quartile, and \( Q_3 \) is the third quartile of the feature.

- **Example:** 
  ```python
  from sklearn.preprocessing import RobustScaler
  
  # Initialize scaler
  scaler = RobustScaler()
  
  # Fit and transform training data
  X_train_scaled = scaler.fit_transform(X_train)
  ```

**MinMax Scaling (Min-Max Normalization)**
- **Definition:** MinMax scaling scales features to a fixed range, typically [0, 1].
  - Formula: \( Z = \frac{x - x_{min}}{x_{max} - x_{min}} \)
    - Where \( x_{min} \) and \( x_{max} \) are the minimum and maximum values of the feature.

- **Example:** 
  ```python
  from sklearn.preprocessing import MinMaxScaler
  
  # Initialize scaler
  scaler = MinMaxScaler()
  
  # Fit and transform training data
  X_train_scaled = scaler.fit_transform(X_train)
  ```

**Maximum Absolute Scaling**
- **Definition:** Maximum absolute scaling scales features to the range [-1, 1] by dividing each feature by its maximum absolute value.
  - Formula: \( Z = \frac{x}{\max(|x|)} \)

- **Example:** 
  ```python
  from sklearn.preprocessing import MaxAbsScaler
  
  # Initialize scaler
  scaler = MaxAbsScaler()
  
  # Fit and transform training data
  X_train_scaled = scaler.fit_transform(X_train)
  ```

---

### Practical Implementation

**Exercise: Feature Scaling in AirBnb Dataset**

1. **Load the Dataset**
   ```python
   import pandas as pd
   
   data = pd.read_csv('./data/airbnb_sg.csv')
   data.head()
   ```

2. **Identify Numerical Variables**
   ```python
   num_cols = [c for c in data.columns if data[c].dtypes != 'O']
   data[num_cols].isnull().mean().sort_values()
   ```

3. **Separate into Training and Testing Sets**
   ```python
   from sklearn.model_selection import train_test_split
   
   X_train, X_test, y_train, y_test = train_test_split(
       data[num_cols].drop('price', axis=1), data['price'], test_size=0.3, random_state=0)
   
   X_train.shape, X_test.shape
   ```

4. **Apply Maximum Absolute Scaling**
   ```python
   from sklearn.preprocessing import MaxAbsScaler
   
   scaler = MaxAbsScaler()
   scaler.fit(X_train)
   X_train_scaled = scaler.transform(X_train)
   X_test_scaled = scaler.transform(X_test)

   X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
   X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)
   ```

5. **Visualize Distribution Before and After Scaling**
   ```python
   fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
   
   # Before scaling
   ax1.set_title('Before Scaling')
   sns.kdeplot(X_train['id'], ax=ax1, label='id')
   sns.kdeplot(X_train['host_id'], ax=ax1, label='host_id')
   sns.kdeplot(X_train['latitude'], ax=ax1, label='latitude')
   sns.kdeplot(X_train['longitude'], ax=ax1, label='longitude')
   ax1.legend()
   
   # After scaling
   ax2.set_title('After Scaling')
   sns.kdeplot(X_train_scaled['id'], ax=ax2, label='id')
   sns.kdeplot(X_train_scaled['host_id'], ax=ax2, label='host_id')
   sns.kdeplot(X_train_scaled['latitude'], ax=ax2, label='latitude')
   sns.kdeplot(X_train_scaled['longitude'], ax=ax2, label='longitude')
   ax2.legend()
   
   plt.show()
   ```

6. **Repeat for Other Numerical Variables**
   ```python
   fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
   
   # Before scaling
   ax1.set_title('Before Scaling')
   sns.kdeplot(X_train['minimum_nights'], ax=ax1, label='minimum_nights')
   sns.kdeplot(X_train['number_of_reviews'], ax=ax1, label='number_of_reviews')
   sns.kdeplot(X_train['reviews_per_month'], ax=ax1, label='reviews_per_month')
   sns.kdeplot(X_train['calculated_host_listings_count'], ax=ax1, label='calculated_host_listings_count')
   sns.kdeplot(X_train['availability_365'], ax=ax1, label='availability_365')
   ax1.legend()
   
   # After scaling
   ax2.set_title('After Scaling')
   sns.kdeplot(X_train_scaled['minimum_nights'], ax=ax2, label='minimum_nights')
   sns.kdeplot(X_train_scaled['number_of_reviews'], ax=ax2, label='number_of_reviews')
   sns.kdeplot(X_train_scaled['reviews_per_month'], ax=ax2, label='reviews_per_month')
   sns.kdeplot(X_train_scaled['availability_365'], ax=ax2, label='availability_365')
   ax2.legend()
   
   plt.show()
   ```

This example demonstrates how to perform and visualize feature scaling using different techniques in the context of the AirBnb dataset.

---

---

## 2026-06-18 10:18 — Exercise_8 - Applying Mathematical Computations to Features.ipynb
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

---

