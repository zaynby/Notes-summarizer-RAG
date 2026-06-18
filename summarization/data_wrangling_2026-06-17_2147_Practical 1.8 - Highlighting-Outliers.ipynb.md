# Practical 1.8 - Highlighting-Outliers.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Outlier Detection and Handling

## [[Outlier]]  
**Definition**: A data point that significantly deviates from the rest of the data, potentially arising from a different mechanism (Hawkins, 1980).  
**Formula**: Not applicable directly; detected using statistical rules like the IQR proximity rule.  
**Example**:  
```python  
# Identify outliers in 'RM' column using IQR  
outliers = np.where(boston['RM'] > upper_boundary, True, np.where(boston['RM'] < lower_boundary, True, False))  
```  

---

## [[Boxplot]]  
**Definition**: A graphical tool displaying the distribution of data, highlighting the inter-quartile range (IQR), median, and outliers via whiskers and boxes.  
**Formula**: Not applicable.  
**Example**:  
```python  
# Generate boxplot for 'RM'  
sns.boxplot(y=boston['RM'])  
plt.title('Boxplot')  
```  

---

## [[Inter-quartile Range (IQR)]]  
**Definition**: The range between the 25th percentile (Q1) and 75th percentile (Q3) of a dataset.  
**Formula**:  
\[ \text{IQR} = Q3 - Q1 \]  
**Example**:  
```python  
# Calculate IQR for 'RM'  
IQR = boston['RM'].quantile(0.75) - boston['RM'].quantile(0.25)  
```  

---

## [[Inter-quartile Range Proximity Rule]]  
**Definition**: A method to identify outliers as data points lying outside \( \text{Q1} - 1.5 \times \text{IQR} \) or \( \text{Q3} + 1.5 \times \text{IQR} \).  
**Formula**:  
- Upper boundary: \( \text{Q3} + 1.5 \times \text{IQR} \)  
- Lower boundary: \( \text{Q1} - 1.5 \times \text{IQR} \)  
**Example**:  
```python  
# Define boundaries with distance parameter  
def find_boundaries(df, variable, distance):  
    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)  
    lower = df[variable].quantile(0.25) - (IQR * distance)  
    upper = df[variable].quantile(0.75) + (IQR * distance)  
    return upper, lower  
```  

---

## [[Discretization]]  
**Definition**: The process of converting continuous variables into discrete intervals (bins) to reduce the impact of outliers.  
**Formula**: Not applicable.  
**Example**: Refer to Practical 5 for techniques like equal-frequency binning, which groups outliers into extreme bins, treating them similarly to other tail values.  

---

# Connections to Related Concepts  
- Outliers can distort statistical measures (e.g., mean) and affect models like [[Linear Regression]].  
- Handling outliers may involve [[Discretization]] or [[Imputation]] (see Practical 2).  
- Boxplots visually identify outliers using the IQR proximity rule.