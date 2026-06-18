# Practical 6.4 - Zero-coding.ipynb
**Module:** data_wrangling
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