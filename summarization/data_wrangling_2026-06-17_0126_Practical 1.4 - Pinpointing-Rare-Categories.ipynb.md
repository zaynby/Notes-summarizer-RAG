# Practical 1.4 - Pinpointing-Rare-Categories.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Identifying Rare Categories and Cardinality  

## **Rare Categories**  
**Definition**: Categories in a categorical variable that represent a tiny minority of observations in the dataset, typically defined as those with a frequency below a threshold (e.g., 5% or 1%).  
**Formula**:  
Frequency of a category = \(\frac{\text{Count of category}}{\text{Total number of observations}}\)  
**Example**:  
In the Car Evaluation dataset, categories in the `class` variable with frequencies below 5% are flagged as rare. The code calculates frequencies using:  
```python  
label_freq = data['class'].value_counts() / len(data)  
```  
A bar plot with a red line at \(y=0.05\) visualizes categories below this threshold.  

## **Cardinality**  
**Definition**: The number of unique categories present in a categorical variable (e.g., the variable `class` in the Car Evaluation dataset has a cardinality of 4 if it has 4 unique labels).  
**Formula**:  
Cardinality = \(\text{Number of unique categories}\)  
**Example**:  
For the `class` variable in the dataset:  
```python  
data['class'].nunique()  # Returns the count of unique categories  
```  

## **Frequency Calculation**  
**Definition**: The process of determining the proportion of observations each category represents in a dataset.  
**Formula**:  
Frequency = \(\frac{\text{Number of occurrences of a category}}{\text{Total number of observations}}\)  
**Example**:  
```python  
total_cars = len(data)  
label_freq = data['class'].value_counts() / total_cars  
```  

## **Visualization of Rare Categories**  
**Definition**: A graphical method to identify rare categories by plotting their frequencies and overlaying a threshold line (e.g., 5%).  
**Formula**: N/A (Method involves sorting frequencies and plotting).  
**Example**:  
```python  
fig = label_freq.sort_values(ascending=False).plot.bar()  
fig.axhline(y=0.05, color='red')  # Threshold line for 5%  
```  

---

### **Key Links**  
- [[Cardinality]] is critical for understanding the diversity of categories.  
- [[Frequency Calculation]] directly determines whether a category is classified as rare.  
- Rare categories often require special handling in machine learning pipelines, such as merging or removing them to improve model performance.