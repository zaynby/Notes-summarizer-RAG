# Practical 1.3 - Determining-Cardinality.ipynb
**Module:** data_wrangling
**Style:** structured_academic (experimenting)

# Summary: Cardinality and Categorical Variables  

## [[Cardinality]]  
**Definition**: The number of unique categories present in a categorical variable.  
**Formula**:  
\[ \text{Cardinality} = \text{Number of distinct categories} \]  
**Example**:  
- Variable `GENDER` with categories `['male', 'female']` has a cardinality of **2**.  
- Variable `civil status` with categories `['married', 'divorced', 'single', 'widow']` has a cardinality of **4**.  

---

## [[Categorical Variable]]  
**Definition**: A variable whose values represent categories or labels (e.g., "male/female," "city names"). These can be **nominal** (no intrinsic order) or **ordinal** (ordered categories).  
**Formula**: N/A  
**Example**:  
- `GENDER` (values: "male," "female") is a **nominal** categorical variable.  
- `Student's grade` (values: "A," "B," "C," "Fail") is an **ordinal** categorical variable.  

---

## [[Missing Data]]  
**Definition**: The absence of values for certain observations in a variable, often represented as `NaN` (Not a Number) in datasets.  
**Formula**: N/A  
**Example**:  
- Empty strings (`' '`) in the dataset were replaced with `np.nan` to standardize missing values:  
  ```python  
  data = data.replace(' ', np.nan)  
  ```  

---

## [[Data Visualization]]  
**Definition**: The graphical representation of data to identify patterns or insights (e.g., bar charts for cardinality).  
**Formula**: N/A  
**Example**:  
- A bar chart visualizing cardinality across variables:  
  ```python  
  data.nunique().plot.bar(figsize=(12,6))  
  plt.ylabel('Number of unique categories')  
  plt.xlabel('Variables')  
  plt.title('Cardinality')  
  ```  

---

## Key Code Concepts  
1. **`nunique()`**: Pandas function to calculate cardinality (ignores `NaN` by default).  
   ```python  
   data.nunique()  # Excludes missing values  
   data.nunique(dropna=False)  # Includes missing values as a category  
   ```  
2. **`unique()`**: Retrieves unique categories in a variable:  
   ```python  
   data['GENDER'].unique()  # Returns array of unique labels  
   ```  

--- 

This summary integrates concepts from data wrangling, emphasizing the importance of understanding variable characteristics for machine learning workflows. Related terms like [[Variable Types]] and [[Feature Engineering]] may further contextualize these ideas.