# Practical 1.7 - Distinguishing-Variable-Distribution.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary of Practical: Visualizing Variable Distributions  

## **Data Visualization**  
**Definition**: The practice of representing data graphically to identify patterns, trends, and relationships.  
**Formula**: N/A  
**Example**:  
```python  
import matplotlib.pyplot as plt  
# Generate histograms for all variables in the Boston dataset  
boston.hist(bins=30, figsize=(12,12), density=True)  
plt.show()  
```  
**Link**: [[Histogram]]  

---

## **Histogram**  
**Definition**: A graphical representation showing the distribution of numerical data by grouping values into bins. The `density=True` parameter normalizes the histogram to form a probability density curve.  
**Formula**:  
Probability Density = $ \frac{\text{Frequency of Bin}}{\text{Bin Width} \times \text{Total Observations}} $  
**Example**:  
```python  
# Create a histogram for the Boston dataset with 30 bins and density normalization  
boston.hist(bins=30, figsize=(12,12), density=True)  
plt.show()  
```  
**Link**: [[Data Visualization]]  

---

## **Boston Housing Dataset**  
**Definition**: A classic dataset containing housing prices and features (e.g., crime rates, number of rooms) for Boston suburbs, commonly used for regression analysis and exploratory data analysis.  
**Formula**: N/A  
**Example**:  
```python  
# Load the Boston Housing Dataset  
boston = pd.read_csv("./data/boston_local.csv")  
boston.head()  # Display the first few rows  
```  
**Link**: [[Regression Analysis]]  

---

## **Density Plot**  
**Definition**: A visualization that smooths the data to show the probability density of a variable, often overlaid on histograms. In this context, `density=True` in `hist()` achieves a similar effect.  
**Formula**: Same as [[Histogram]] probability density formula.  
**Example**:  
```python  
# Histogram with density normalization (approximating a density plot)  
boston.hist(bins=30, figsize=(12,12), density=True)  
plt.show()  
```  
**Link**: [[Histogram]]  

---

**Source**: Soledad Galli, *Python Feature Engineering Cookbook* (Jan 2020)