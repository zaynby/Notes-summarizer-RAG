# Practical 1.6 - Identifying-a-Normal-Distribution.ipynb
**Module:** data_wrangling
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