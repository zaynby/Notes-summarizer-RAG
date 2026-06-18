# Practical 7.2 - Mean-normalization.ipynb
**Module:** data_wrangling
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