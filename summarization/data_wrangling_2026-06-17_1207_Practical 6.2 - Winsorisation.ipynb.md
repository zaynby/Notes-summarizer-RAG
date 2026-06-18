# Practical 6.2 - Winsorisation.ipynb
**Module:** data_wrangling
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