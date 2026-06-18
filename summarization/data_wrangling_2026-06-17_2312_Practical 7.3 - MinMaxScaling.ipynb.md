# Practical 7.3 - MinMaxScaling.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### [[Min-Max Scaling]]
**Definition**: A technique that transforms feature values to a fixed range (typically [0, 1]) by subtracting the minimum value and dividing by the range (max - min).  
**Formula**:  
$$ x_{\text{scaled}} = \frac{x - \min(x)}{\max(x) - \min(x)} $$  
**Example**:  
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
```

---

### [[MinMaxScaler (Scikit-learn)]]
**Definition**: A Scikit-learn class implementing Min-Max scaling that learns `min_` and `data_max_` attributes from training data.  
**Formula**: N/A (Implementation of Min-Max scaling)  
**Example**:  
```python
scaler = MinMaxScaler()
scaler.fit(X_train)  # Learns min/max values
X_test_scaled = scaler.transform(X_test)  # Applies same scaling
```

---

### [[Train/Test Split]]
**Definition**: Method to partition data into training and testing subsets to evaluate model performance.  
**Formula**: N/A  
**Example**:  
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)
```

---

### [[Data Transformation]]
**Definition**: Process of applying learned scaling parameters to convert raw data into scaled values.  
**Formula**: N/A  
**Example**:  
```python
X_train_scaled = scaler.transform(X_train)  # Scales training data
X_test_scaled = scaler.transform(X_test)   # Scales test data
```

---

### [[Kernel Density Estimate (KDE) Plot]]
**Definition**: Statistical visualization showing the probability density function of a variable.  
**Formula**: N/A  
**Example**:  
```python
import seaborn as sns
sns.kdeplot(X_train['RM'], label='Before Scaling')
sns.kdeplot(X_train_scaled['RM'], label='After Scaling')
```

---

### Key Observations from Visualizations:
1. **Before Scaling**: Features like `RM`, `LSTAT`, and `CRIM` exhibit varying scales and distributions.  
2. **After Scaling**: All features are compressed to [0, 1] range, resulting in overlapping KDE plots with similar spreads.

---

### Attribute Inspection:
```python
scaler.data_min_  # Minimum values learned from training data
scaler.data_max_  # Maximum values learned from training data
scaler.data_range_  # Range (max - min) for each feature
```

This summary connects concepts like [[Feature Scaling]], [[Data Preprocessing]], and [[Exploratory Data Analysis (EDA)]] through standardization techniques.