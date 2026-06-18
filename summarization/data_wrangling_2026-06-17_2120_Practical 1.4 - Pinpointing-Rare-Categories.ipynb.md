# Practical 1.4 - Pinpointing-Rare-Categories.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Identifying Rare Categories and Cardinality in Datasets

## **1. Rare Categories**  
**Definition**: Categories in a dataset that represent a tiny minority of observations, typically defined as those occurring in less than **5% or 1%** of the total data points.  
**Formula**:  
Frequency of a category = \( \frac{\text{Count of category}}{\text{Total number of observations}} \)  
**Example**:  
In the Car Evaluation dataset, the frequency of the "class" categories (e.g., "unacc", "acc", "good", "vgood") is calculated using:  
```python
label_freq = data['class'].value_counts() / len(data)
```  
A horizontal line at `y=0.05` in the bar plot visualizes the 5% threshold for rare categories.

---

## **2. Cardinality**  
**Definition**: The number of **unique categories** present in a categorical variable.  
**Formula**:  
Cardinality = \( \text{Number of unique values in a variable} \)  
**Example**:  
For the "class" variable in the Car Evaluation dataset:  
```python
data['class'].nunique()  # Output: 4 (e.g., "unacc", "acc", "good", "vgood")
```  

---

## **3. Frequency Calculation**  
**Definition**: The proportion of observations belonging to each category in a dataset.  
**Formula**:  
Frequency = \( \frac{\text{Count of category}}{\text{Total observations}} \)  
**Example**:  
```python
total_cars = len(data)  # Total observations
label_freq = data['class'].value_counts() / total_cars  # Frequency per category
```  

---

## **4. Visualization of Category Frequencies**  
**Definition**: A graphical representation (e.g., bar chart) to compare the frequency of categories and identify rare ones.  
**Formula**: N/A  
**Example**:  
```python
fig = label_freq.sort_values(ascending=False).plot.bar()
fig.axhline(y=0.05, color='red')  # 5% threshold line
fig.set_title('Identifying Rare Categories')
plt.show()
```  
This plot highlights categories below the 5% threshold as rare.

---

## **Key Links**  
- [[Variable Types]]: Distinguishes categorical vs. numerical variables.  
- [[Data Preprocessing]]: Context for handling rare categories in ML workflows.  
- [[Cardinality]]: Further implications of high/low cardinality in models.