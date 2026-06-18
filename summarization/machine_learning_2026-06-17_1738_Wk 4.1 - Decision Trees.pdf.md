# Wk 4.1 - Decision Trees.pdf
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided Decision Tree content:

---

### [[Decision Tree]]
**Definition**: A supervised machine learning algorithm used for classification and regression tasks. It splits data into homogeneous subgroups using a hierarchical tree structure with root nodes, internal nodes, and leaf nodes.  
**Formula**: N/A  
**Example**: Classifying users as potential hackers based on login time, location, and device (Page 3).

---

### [[Decision Tree Components]]
**Definition**:  
- **Root Node**: Starting point of the tree where initial data split occurs.  
- **Internal Nodes**: Represent conditions/tests on features.  
- **Leaf Nodes**: Terminal nodes representing final class labels or predictions.  
**Formula**: N/A  
**Example**: Titanic survival prediction tree (Page 5).

---

### [[Data Splitting]]
**Definition**: The process of dividing data into subgroups to maximize homogeneity.  
**Key Principles**:  
1. Splits aim for pure nodes (single class/continuous value).  
2. Recursive splitting until stopping conditions are met.  
3. Criteria differ for classification (impurity measures) vs. regression (MSE).  
**Formula**: N/A  
**Example**: Splitting users into "Hacker" or "Non-Hacker" based on features (Page 6).

---

### [[CART (Classification and Regression Tree)]]
**Definition**: A binary decision tree algorithm for classification and regression using binary splits.  
**Algorithm Steps**:  
1. Evaluate all input variables and split points.  
2. Select split with highest impurity reduction.  
3. Repeat until stopping conditions met.  
**Formula**: N/A  
**Example**: Scikit-learn’s `DecisionTreeClassifier` implementation (Page 12).

---

### [[Gini Impurity Index]]
**Definition**: A measure of node purity in classification trees. Lower values indicate higher purity.  
**Formula**:  
For a node with \( m \) classes:  
\[ I_A = 1 - \sum_{c=1}^m (p_c)^2 \]  
where \( p_c \) is the proportion of class \( c \).  
**Example**:  
- Node A (300 Y=1, 700 Y=2):  
  \( I_A = 1 - (0.3^2 + 0.7^2) = 0.42 \) (Page 16).

---

### [[Overfitting and Pruning]]
**Definition**:  
- **Overfitting**: Tree grows too complex, memorizing training data.  
- **Pruning**: Technique to reduce overfitting by removing weak branches.  
**Types**:  
1. **Pre-pruning**: Stop splitting early (e.g., max depth).  
2. **Post-pruning**: Trim branches after full growth.  
**Formula**: N/A  
**Example**: Using `max_depth` or `min_samples_leaf` in scikit-learn (Page 9).

---

### [[Stopping Conditions]]
**Definition**: Criteria to halt tree growth and prevent overfitting.  
**Common Conditions**:  
1. Maximum tree depth reached.  
2. Minimum records in leaf/parent nodes.  
3. Node purity achieved (\( Gini = 0 \)).  
**Formula**: N/A  
**Example**: Setting `min_samples_split=20` to avoid small nodes (Page 10).

---

### [[Types of Decision Trees]]
**Definition**: Variants of decision tree algorithms.  
**Key Types**:  
1. **CART**: Binary splits, used in scikit-learn.  
2. **CHAID**: Uses chi-square tests for splits.  
3. **ID3/C4.5**: Uses information gain/entropy.  
**Formula**: N/A  
**Example**: CHAID for market segmentation analysis (Page 11).

---

### [[Strengths and Limitations of Decision Trees]]
**Strengths**:  
- Easy to interpret and visualize.  
- Handles missing values and categorical data.  
**Limitations**:  
- Prone to overfitting and instability.  
- Struggles with linear relationships.  
**Formula**: N/A  
**Example**: Random Forest ensembles mitigate standalone tree weaknesses (Page 20).

---

### [[Gini Impurity Reduction Example]]
**Calculation**:  
Given a split into nodes B and C:  
\[ \Delta I = I_A - \left( \frac{n_B}{n_A} I_B + \frac{n_C}{n_A} I_C \right) \]  
**Example**:  
- Node A (300 Y=1, 700 Y=2) splits into B (100 Y=1, 600 Y=2) and C (200 Y=1, 100 Y=2).  
- Compute \( I_B \), \( I_C \), and \( \Delta I \) (Page 21).

---

### [[Activity: Split Decision Using Gini]]
**Scenario**: Choosing between splits for "Risk_Group" (high vs. {medium, low}) using Gini Impurity.  
**Steps**:  
1. Compute Gini for parent and child nodes.  
2. Select split with highest \( \Delta I \).  
**Example**: Analyze P1-P14 dataset to compare split options (Page 22).

---

This summary links core concepts like [[Decision Tree]], [[CART]], and [[Gini Impurity Index]], providing formulas and practical examples for clarity.