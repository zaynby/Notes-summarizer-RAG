# Practical 1.6 - Identifying-a-Normal-Distribution.ipynb
**Module:** data_wrangling
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