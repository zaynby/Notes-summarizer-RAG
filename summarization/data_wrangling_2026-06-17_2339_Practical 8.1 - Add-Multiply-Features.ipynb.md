# Practical 8.1 - Add-Multiply-Features.ipynb
**Module:** data_wrangling
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