# Exercise_4 - Transforming Numerical Variables.ipynb
**Module:** data_wrangling
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