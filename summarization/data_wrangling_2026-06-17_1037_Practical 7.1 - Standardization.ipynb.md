# Practical 7.1 - Standardization.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

### Standardization (Z-score normalization)  
**Definition**: A method to rescale features by subtracting the mean and dividing by the standard deviation, resulting in a distribution centered at 0 with unit variance. This ensures features contribute equally to model training and improves convergence in algorithms like neural networks.  

**Formula**:  
\[
z = \frac{x - \mu}{\sigma}
\]  
where \( z \) is the standardized value, \( x \) is the original value, \( \mu \) is the mean, and \( \sigma \) is the standard deviation.  

**Example**:  
```python
from sklearn.preprocessing import StandardScaler  

# Initialize scaler  
scaler = StandardScaler()  

# Fit to training data and transform  
X_train_scaled = scaler.fit_transform(X_train)  

# Apply same transformation to test data  
X_test_scaled = scaler.transform(X_test)  
```  
This code uses `StandardScaler` to standardize features. The scaler computes mean (`scaler.mean_`) and standard deviation (`scaler.scale_`) from the training set and applies the same transformation to the test set to prevent data leakage.  

**Visualization Insight**:  
After standardization, distributions are centered at 0 but retain their original shape (e.g., skewed or Gaussian). This is verified using kernel density plots (`sns.kdeplot`) comparing distributions before and after scaling.  

**Key Notes**:  
- **Why Standardize?** Prevents features with larger scales from dominating the model.  
- **Wikilinks**: [[Z-score]], [[Feature Scaling]], [[Data Preprocessing]]  

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)