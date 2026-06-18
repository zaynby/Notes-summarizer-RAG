# Exercise_2 - Imputing Missing Data.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content on missing data imputation:

```markdown
# Key Concepts in Missing Data Imputation

## 1. [[Missing Data]]
**Definition**: Absent values in a dataset where no measurement or entry exists.  
**Formula**: Not applicable (phenomenological concept)  
**Example**: In `airbnb_sg.csv`, missing values were artificially introduced in columns like 'neighbourhood' and 'room_type' for demonstration.

## 2. [[Imputation]]
**Definition**: Process of replacing missing data with substituted values to create complete datasets for analysis.  
**Formula**: Not applicable (general process)  
**Example**: Using `SimpleImputer` to replace missing values in numerical columns with median or constants.

## 3. [[SimpleImputer (Scikit-learn)]]
**Definition**: Class for completing missing values in numeric/numeric data using strategies like mean, median, or constant.  
**Formula**: 
```python
imputer = SimpleImputer(strategy='median')  # or 'mean', 'constant'
```
**Example**: 
```python
imputer_num_med = Pipeline([('imputer', SimpleImputer(strategy='median'))])
```

## 4. [[ColumnTransformer]]
**Definition**: Scikit-learn class to apply different transformers to different columns of a dataset.  
**Formula**: 
```python
preprocessor = ColumnTransformer([
    ('num_med', imputer, num_median)
])
```
**Example**: Used to apply different imputation strategies to numerical vs categorical columns.

## 5. [[Pipeline (Scikit-learn)]]
**Definition**: Chain of data transformation steps executed sequentially.  
**Formula**: 
```python
pipeline = Pipeline([('step1', transformer1), ('step2', transformer2)])
```
**Example**: Combining imputers and transformers for numerical/missing categories.

## 6. [[Feature Engine]]
**Definition**: Advanced feature engineering library with specialized imputers.  
**Formula**: Not applicable (library reference)  
**Example**: Using `ArbitraryNumberImputer` and `CategoricalImputer` in a pipeline.

## 7. [[Arbitrary Number Imputer]]
**Definition**: Replaces missing values with user-specified arbitrary numbers.  
**Formula**: 
```python
ArbitraryNumberImputer(variables=columns, arbitrary_number=0)
```
**Example**: Used for `calculated_host_listings_count` and `host_id` with fill value 0.

## 8. [[Mean/Median Imputer]]
**Definition**: Replaces missing values with column mean or median.  
**Formula**: 
```python
MeanMedianImputer(imputation_method='median')
```
**Example**: Applied to `number_of_reviews` and `id` columns.

## 9. [[Categorical Imputer]]
**Definition**: Handles missing values in categorical data using frequency-based or placeholder strategies.  
**Formula**: 
```python
CategoricalImputer(imputation_method='most_frequent')
```
**Example**: 
- `most_frequent` for 'host_name' 
- 'Missing' placeholder for 'room_type'

## 10. [[Data Preprocessing Pipeline]]
**Definition**: Integrated workflow combining data splitting, transformation, and imputation.  
**Formula**: 
```python
pipe = Pipeline(steps=[...])
pipe.fit_transform(data)
```
**Example**: Complete pipeline from train/test split to final imputed datasets.
```

This summary connects key concepts through wikilinks while maintaining the required term-definition-formula-example structure. The content focuses on practical implementation details from the notebook while emphasizing statistical and machine learning principles.