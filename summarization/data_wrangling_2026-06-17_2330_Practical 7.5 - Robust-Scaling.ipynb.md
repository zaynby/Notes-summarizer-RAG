# Practical 7.5 - Robust-Scaling.ipynb
**Module:** data_wrangling
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