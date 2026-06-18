# Practical 8.3 - PolynomialExpansion.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

```markdown
# Polynomial Feature Engineering Summary

## Polynomial Expansion
**Definition**: The process of generating new features by raising existing features to polynomial powers (e.g., squaring, cubing) or creating interaction terms between different features. This captures non-linear relationships and feature interactions.
**Formula**: For features \( x_1, x_2 \), examples include \( x_1^2 \), \( x_1^3 \), \( x_1x_2 \), \( x_1^2x_2 \), etc.
**Example**: Creating \( x^2 \) to model a quadratic relationship between \( x \) and the target variable \( y \), improving linear model performance.

## PolynomialFeatures
**Definition**: A scikit-learn transformer class used to automatically generate polynomial features from input data up to a specified degree.
**Formula**: N/A (method-based)
**Example**: 
```python
poly = PolynomialFeatures(degree=3, interaction_only=False, include_bias=False)
```
Generates all polynomial terms up to degree 3, including interactions and higher powers.

## Polynomial Degree
**Definition**: The highest exponent in the polynomial expansion. A degree \( d \) includes all terms where the sum of exponents across features is ≤ \( d \).
**Formula**: For \( d = 3 \), terms include \( x_1^3 \), \( x_1^2x_2 \), \( x_1x_2^2 \), etc.
**Example**: Setting `degree=3` in `PolynomialFeatures` to capture cubic relationships.

## Interaction-only Features
**Definition**: Features created by multiplying different base features (cross-product terms), excluding higher powers of individual features.
**Formula**: \( x_i x_j \) for \( i \neq j \).
**Example**: Using `interaction_only=True` to generate terms like \( \text{LSTAT} \times \text{RM} \).

## Bias Term
**Definition**: A constant feature (always 1) added to each sample to enable the model to learn an intercept term.
**Formula**: \( 1 \)
**Example**: Including a bias term via `include_bias=True` in `PolynomialFeatures`.

## Feature Transformation
**Definition**: The application of polynomial expansion to a dataset to derive new features.
**Formula**: N/A
**Example**: 
```python
train_t = poly.transform(X_train[['LSTAT', 'RM', 'NOX']])
```
Generates polynomial features for the training set.

## Feature Naming
**Definition**: The labeling of generated polynomial features with names reflecting their mathematical form (e.g., `LSTAT^2`, `LSTAT RM`).
**Formula**: N/A
**Example**: Using `poly.get_feature_names_out()` to retrieve descriptive names for transformed features.

## Correlation Analysis
**Definition**: Examining the linear relationships between features using statistical measures like Pearson correlation.
**Formula**: Pearson correlation coefficient \( r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}} \)
**Example**: Visualizing correlations with a heatmap via `sns.heatmap(data.corr())`.

## Train-Test Split
**Definition**: Dividing data into training and testing subsets to evaluate model performance.
**Formula**: N/A
**Example**: 
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
```
Splits data with 30% for testing.

## Feature-Target Visualization
**Definition**: Plotting individual features against the target variable to identify patterns or relationships.
**Formula**: N/A
**Example**: 
```python
plt.scatter(X_train['LSTAT'], y_train)
```
Visualizes the relationship between `LSTAT` and house prices (`MEDV`).
```