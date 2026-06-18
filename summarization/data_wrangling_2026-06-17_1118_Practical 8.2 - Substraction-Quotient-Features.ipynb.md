# Practical 8.2 - Substraction-Quotient-Features.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### **Feature Engineering with Mathematical Operations**

#### **1. Subtraction of Features**  
**Definition**: Creating a new feature by subtracting one numerical feature from another to derive meaningful differences (e.g., disposable income = income - debt).  
**Formula**:  
\[ \text{New Feature} = F_1 - F_2 \]  
**Example**:  
```python  
# Code Cell 6 & 7  
df['difference'] = df['worst compactness'].sub(df['mean compactness'])  
# or  
df['difference'] = df['worst compactness'] - df['mean compactness']  
```  
Visualized using a violin plot to compare differences across target classes.

---

#### **2. Division of Features**  
**Definition**: Generating a ratio-based feature by dividing one feature by another (e.g., debt-to-income ratio = total debt / total income).  
**Formula**:  
\[ \text{New Feature} = \frac{F_1}{F_2} \]  
**Example**:  
```python  
# Code Cell 9 & 10  
df['quotient'] = df['worst radius'].div(df['mean radius'])  
# or  
df['quotient'] = df['worst radius'] / df['mean radius']  
```  
Visualized using a violin plot to analyze quotient distributions.

---

#### **3. Aggregation of Features**  
**Definition**: Combining multiple features into a single value using statistical operations (e.g., summing "worst" features to create a composite metric).  
**Formula**:  
\[ \text{Aggregated Feature} = \sum_{i=1}^{n} F_i \]  
**Example**:  
```python  
# Code Cell 13  
df['worst'] = df[['worst smoothness', 'worst compactness', ...]].sum(axis=1)  
```  

---

#### **4. Ratio Calculation with Multiple Features**  
**Definition**: Deriving ratios by dividing multiple features against a reference feature (e.g., comparing mean features to an aggregated "worst" feature).  
**Formula**:  
\[ \text{Ratio Feature} = \frac{F_{\text{mean}}}{F_{\text{reference}}} \]  
**Example**:  
```python  
# Code Cell 15  
df[['mean smoothness', 'mean compactness', ...]].div(df['worst'], axis=0)  
```  

---

### **Key Concepts**  
- **[[Feature Engineering]]**: Process of creating new features from raw data to improve model performance.  
- **[[Mathematical Operations]]**: Includes subtraction, division, and aggregation for deriving insights.  
- **[[Reference Variable]]**: A base feature (e.g., "worst" aggregate) against which other features are compared.  

---

### **Visualization**  
- **Violin Plots**: Used to visualize distributions of new features (e.g., `difference`, `quotient`) across target classes.  

---

This summary aligns with the notebook's focus on using pandas for feature engineering via mathematical operations and aggregation. Related concepts like [[Outlier Detection]] (from prior examples) may also apply in preprocessing.