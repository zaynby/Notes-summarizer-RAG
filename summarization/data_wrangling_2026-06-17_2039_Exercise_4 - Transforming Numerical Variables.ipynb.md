# Exercise_4 - Transforming Numerical Variables.ipynb
**Module:** data_wrangling
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