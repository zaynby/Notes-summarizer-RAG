# Practical 1.1 - Identifying-Variables-Types.ipynb
**Module:** data_wrangling
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