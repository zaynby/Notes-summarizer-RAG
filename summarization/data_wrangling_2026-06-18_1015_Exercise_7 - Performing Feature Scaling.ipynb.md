# Exercise_7 - Performing Feature Scaling.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Data Wrangling: Feature Scaling

#### Term -> Definition -> Formula -> Example

**Standard Scaling (Z-Score Normalization)**
- **Definition:** Standard scaling transforms features by subtracting the mean and then scaling to unit variance.
  - Formula: \( Z = \frac{x - \mu}{\sigma} \)
    - Where \( x \) is the feature value, \( \mu \) is the mean of the feature, and \( \sigma \) is the standard deviation of the feature.

- **Example:** 
  ```python
  from sklearn.preprocessing import StandardScaler
  
  # Initialize scaler
  scaler = StandardScaler()
  
  # Fit and transform training data
  X_train_scaled = scaler.fit_transform(X_train)
  ```

**Robust Scaling**
- **Definition:** Robust scaling uses the median and the interquartile range (IQR) to scale features, making it robust to outliers.
  - Formula: \( Z = \frac{x - Q_1}{Q_3 - Q_1} \times (Q_{75} - Q_{25}) + Q_{25} \)
    - Where \( Q_1 \) is the first quartile, and \( Q_3 \) is the third quartile of the feature.

- **Example:** 
  ```python
  from sklearn.preprocessing import RobustScaler
  
  # Initialize scaler
  scaler = RobustScaler()
  
  # Fit and transform training data
  X_train_scaled = scaler.fit_transform(X_train)
  ```

**MinMax Scaling (Min-Max Normalization)**
- **Definition:** MinMax scaling scales features to a fixed range, typically [0, 1].
  - Formula: \( Z = \frac{x - x_{min}}{x_{max} - x_{min}} \)
    - Where \( x_{min} \) and \( x_{max} \) are the minimum and maximum values of the feature.

- **Example:** 
  ```python
  from sklearn.preprocessing import MinMaxScaler
  
  # Initialize scaler
  scaler = MinMaxScaler()
  
  # Fit and transform training data
  X_train_scaled = scaler.fit_transform(X_train)
  ```

**Maximum Absolute Scaling**
- **Definition:** Maximum absolute scaling scales features to the range [-1, 1] by dividing each feature by its maximum absolute value.
  - Formula: \( Z = \frac{x}{\max(|x|)} \)

- **Example:** 
  ```python
  from sklearn.preprocessing import MaxAbsScaler
  
  # Initialize scaler
  scaler = MaxAbsScaler()
  
  # Fit and transform training data
  X_train_scaled = scaler.fit_transform(X_train)
  ```

---

### Practical Implementation

**Exercise: Feature Scaling in AirBnb Dataset**

1. **Load the Dataset**
   ```python
   import pandas as pd
   
   data = pd.read_csv('./data/airbnb_sg.csv')
   data.head()
   ```

2. **Identify Numerical Variables**
   ```python
   num_cols = [c for c in data.columns if data[c].dtypes != 'O']
   data[num_cols].isnull().mean().sort_values()
   ```

3. **Separate into Training and Testing Sets**
   ```python
   from sklearn.model_selection import train_test_split
   
   X_train, X_test, y_train, y_test = train_test_split(
       data[num_cols].drop('price', axis=1), data['price'], test_size=0.3, random_state=0)
   
   X_train.shape, X_test.shape
   ```

4. **Apply Maximum Absolute Scaling**
   ```python
   from sklearn.preprocessing import MaxAbsScaler
   
   scaler = MaxAbsScaler()
   scaler.fit(X_train)
   X_train_scaled = scaler.transform(X_train)
   X_test_scaled = scaler.transform(X_test)

   X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
   X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)
   ```

5. **Visualize Distribution Before and After Scaling**
   ```python
   fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
   
   # Before scaling
   ax1.set_title('Before Scaling')
   sns.kdeplot(X_train['id'], ax=ax1, label='id')
   sns.kdeplot(X_train['host_id'], ax=ax1, label='host_id')
   sns.kdeplot(X_train['latitude'], ax=ax1, label='latitude')
   sns.kdeplot(X_train['longitude'], ax=ax1, label='longitude')
   ax1.legend()
   
   # After scaling
   ax2.set_title('After Scaling')
   sns.kdeplot(X_train_scaled['id'], ax=ax2, label='id')
   sns.kdeplot(X_train_scaled['host_id'], ax=ax2, label='host_id')
   sns.kdeplot(X_train_scaled['latitude'], ax=ax2, label='latitude')
   sns.kdeplot(X_train_scaled['longitude'], ax=ax2, label='longitude')
   ax2.legend()
   
   plt.show()
   ```

6. **Repeat for Other Numerical Variables**
   ```python
   fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
   
   # Before scaling
   ax1.set_title('Before Scaling')
   sns.kdeplot(X_train['minimum_nights'], ax=ax1, label='minimum_nights')
   sns.kdeplot(X_train['number_of_reviews'], ax=ax1, label='number_of_reviews')
   sns.kdeplot(X_train['reviews_per_month'], ax=ax1, label='reviews_per_month')
   sns.kdeplot(X_train['calculated_host_listings_count'], ax=ax1, label='calculated_host_listings_count')
   sns.kdeplot(X_train['availability_365'], ax=ax1, label='availability_365')
   ax1.legend()
   
   # After scaling
   ax2.set_title('After Scaling')
   sns.kdeplot(X_train_scaled['minimum_nights'], ax=ax2, label='minimum_nights')
   sns.kdeplot(X_train_scaled['number_of_reviews'], ax=ax2, label='number_of_reviews')
   sns.kdeplot(X_train_scaled['reviews_per_month'], ax=ax2, label='reviews_per_month')
   sns.kdeplot(X_train_scaled['availability_365'], ax=ax2, label='availability_365')
   ax2.legend()
   
   plt.show()
   ```

This example demonstrates how to perform and visualize feature scaling using different techniques in the context of the AirBnb dataset.