# Week 1.1 - Universal Workflow of ML.pdf
**Module:** machine_learning
**Style:** structured_academic (experimenting)

Here’s a structured summary of the **Universal Workflow of Machine Learning** using the specified academic format:

---

### **Universal Workflow of Machine Learning**  
**Term**: CRISP-DM Framework  
**Definition**: Industry-standard strategic methodology for ML projects with six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment.  
**Formula**: N/A  
**Example**: Aligning business goals with data quality assessments before model development.  
[[CRISP-DM Framework]]  

---

### **Step 1: Define the Problem & Assemble Data**  
**Term**: Problem Definition  
**Definition**: Identify inputs (features) and outputs (targets), problem type (classification/regression/clustering), and assumptions (e.g., outputs predictable from inputs).  
**Formula**: N/A  
**Example**: Predicting house prices (output) using features like size and location (inputs).  
[[Problem Definition]]  

---

### **Step 2: Choose Measure of Success**  
**Term**: Evaluation Metrics  
**Definition**: Metrics to optimize model performance (e.g., RMSE, Accuracy).  
**Formula**:  
- **RMSE**: \(\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2}\)  
- **Accuracy**: \(\frac{\text{True Positives + True Negatives}}{\text{Total Predictions}}\)  
**Example**: Using **Accuracy** for a spam detection classifier.  
[[Evaluation Metrics]]  

---

### **Step 3: Decide Evaluation Protocol**  
**Term**: Evaluation Protocol  
**Definition**: Method to split data for training/validation/testing.  
**Options**:  
- **Hold-Out Validation**: Suitable for large datasets.  
- **K-Fold Cross-Validation**: For small datasets (e.g., K=5).  
**Formula**: N/A  
**Example**: Applying 5-fold cross-validation to a dataset with 1,000 samples.  
[[Cross-Validation]]  

---

### **Step 4: Prepare Data**  
**Term**: Data Preprocessing  
**Definition**: Transform raw data into model-ready format via:  
- **Encoding**: One-hot/binary encoding for categorical data.  
- **Normalization**: Min-max scaling: \(x_{\text{scaled}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}\).  
- **Feature Engineering**: Creating new features (e.g., polynomial terms).  
**Example**: Converting "Color" (red, blue, green) to binary vectors.  
[[Data Preprocessing]]  

---

### **Step 5: Build Baseline Model**  
**Term**: Baseline Model  
**Definition**: Simple model with default hyperparameters to establish performance benchmark.  
**Formula**: Gradient Descent Update: \(w_{t+1} = w_t - \eta \nabla L(w_t)\) (where \(\eta\) = learning rate).  
**Example**: Training a linear regression model with default hyperparameters.  
[[Gradient Descent]]  

---

### **Step 6: Overfit the Model**  
**Term**: Overfitting  
**Definition**: Model performs well on training data but poorly on validation data.  
**Formula**: N/A  
**Example**: A model with 100% training accuracy but 60% validation accuracy.  
[[Overfitting]]  

---

### **Step 7: Regularize & Tune Hyperparameters**  
**Term**: Regularization  
**Definition**: Techniques (e.g., L2 regularization) to prevent overfitting by penalizing complex models.  
**Formula**: L2 Regularization Loss: \(L_{\text{reg}} = L + \lambda \sum w_i^2\).  
**Example**: Using grid search to optimize learning rate (\(\eta\)) and regularization strength (\(\lambda\)).  
[[Regularization]]  

---

### **Key Takeaways**  
1. **CRISP-DM** guides strategic project planning.  
2. **Universal Workflow** ensures systematic tactical execution.  
3. **Iterate**: Continuously refine models via hyperparameter tuning and validation.  
4. **Document**: Track decisions for reproducibility and future reference.  

--- 

**Wikilinks**:  
- [[CRISP-DM Framework]]  
- [[Evaluation Metrics]]  
- [[Cross-Validation]]  
- [[Data Preprocessing]]  
- [[Gradient Descent]]  
- [[Overfitting]]  
- [[Regularization]]