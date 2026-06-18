# Wk 4.1 - Decision Trees.pdf
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the content:

---

### [[Decision Tree]]  
**Definition**: A supervised machine learning algorithm used for classification and regression tasks. It splits data into hierarchical nodes based on feature conditions to achieve maximum purity in terminal nodes.  
**Formula**: N/A (structural algorithm)  
**Example**: Classifying Titanic passenger survival using features like age, gender, and fare (image source: [Titanic Heuristic](https://bigwhalelearning.files.wordpress.com/2014/11/titanic_heuristic.png)).  

---

### [[CART (Classification and Regression Tree)]]  
**Definition**: A decision tree algorithm using **binary splits** for both classification (Gini impurity) and regression (Mean Square Error).  
**Formula**:  
- **Classification**: Gini Impurity = \(1 - \sum_{c=1}^{m} p_c^2\)  
- **Regression**: MSE = \(\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2\)  
**Example**: Scikit-learn’s `DecisionTreeClassifier` uses CART to split data, e.g., predicting housing prices (regression) or loan approval (classification).  

---

### [[Gini Impurity Index]]  
**Definition**: Measures node purity in classification tasks. Lower values indicate better splits.  
**Formula**:  
For a node with \(m\) classes:  
\(I(A) = 1 - \sum_{c=1}^{m} p_c^2\)  
**Example**:  
- Node A (300 Y=1, 700 Y=2): \(I(A) = 1 - (0.3^2 + 0.7^2) = 0.42\)  
- Node B (100 Y=1, 400 Y=2, 500 Y=3): \(I(B) = 1 - (0.1^2 + 0.4^2 + 0.5^2) = 0.58\)  

---

### [[Overfitting & Pruning]]  
**Definition**: Overfitting occurs when a tree grows too deep, memorizing noise. Pruning prevents this by trimming low-value branches.  
**Formula**: N/A  
**Example**:  
- **Pre-pruning**: Stop splitting when max depth=3 or min samples per leaf=10.  
- **Post-pruning**: Remove branches that reduce accuracy on validation data.  

---

### [[Decision Tree Stopping Conditions]]  
**Definition**: Criteria to halt tree growth and avoid overfitting.  
**Formula**: N/A  
**Example**:  
- Max tree depth = 5  
- Min records in leaf node = 20  
- Node purity (Gini=0)  

---

### [[Decision Tree Algorithms]]  
**Definition**: Variants include AID, CHAID, CART, ID3, C4.5, C5.0, QUEST.  
**Formula**: N/A  
**Example**:  
- **CHAID**: Uses chi-square tests for splits.  
- **ID3**: Uses information gain (entropy).  

---

### [[Strengths & Limitations of Decision Trees]]  
**Definition**: Trade-offs in using decision trees.  
**Formula**: N/A  
**Example**:  
- **Strength**: Interpretable visual structure for explaining loan denial decisions.  
- **Limitation**: Unstable trees (small data changes alter structure).  

---

### [[Reduction in Gini Impurity]]  
**Definition**: Measures improvement in node purity after a split.  
**Formula**:  
\(\Delta I = I_{\text{Parent}} - \left( \frac{n_B}{n_A} I_B + \frac{n_C}{n_A} I_C \right)\)  
**Example**:  
For Activity 1 (page 21):  
- Node A: \(I_A = 0.42\)  
- Node B: \(I_B = 1 - (0^2 + 1^2) = 0\)  
- Node C: \(I_C = 1 - (1^2 + 0^2) = 0\)  
\(\Delta I = 0.42 - \left( \frac{700}{1000} \times 0 + \frac{300}{1000} \times 0 \right) = 0.42\)  

---

### [[Ensemble Methods (Random Forest)]]  
**Definition**: Combines multiple decision trees to improve accuracy and stability.  
**Formula**: N/A  
**Example**:  
- Random Forest for fraud detection: 100 trees vote on whether a transaction is fraudulent.  

--- 

All key terms are linked for cross-reference. Let me know if you need further refinements!