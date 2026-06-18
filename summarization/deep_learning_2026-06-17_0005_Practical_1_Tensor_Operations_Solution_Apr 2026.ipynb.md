# Practical_1_Tensor_Operations_Solution_Apr 2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

# Summary of Tensor Operations in Deep Learning

---

### **Tensor**  
**Definition**: Fundamental data structure in deep learning, representing numeric data in a multi-dimensional array format.  
**Formula**: N/A  
**Example**: A 3D tensor `train_images` from MNIST dataset with shape `(60000, 28, 28)`.  
**[[Wikilink]]**: [[Scalars (0D tensors)]], [[Vectors (1D tensors)]], [[Matrices (2D tensors)]], [[3D Tensors]]  

---

### **Scalars (0D tensors)**  
**Definition**: A tensor containing a single numeric value (e.g., `12`).  
**Formula**: N/A  
**Example**:  
```python  
x = np.array(12)  
print('Dimension:', x.ndim, 'Shape:', x.shape)  
```  
**[[Wikilink]]**: [[Tensor]]  

---

### **Vectors (1D tensors)**  
**Definition**: A linear array of numeric values (e.g., `[12, 3, 6, 14, 25]`).  
**Formula**: N/A  
**Example**:  
```python  
x = np.array([12, 3, 6, 14, 25])  
print('Dimension:', x.ndim, 'Shape:', x.shape)  
```  
**[[Wikilink]]**: [[Tensor]]  

---

### **Matrices (2D tensors)**  
**Definition**: A grid of numbers arranged in rows and columns (e.g., a 3x5 matrix).  
**Formula**: N/A  
**Example**:  
```python  
x = np.array([[5, 78, 2, 34, 0], [6, 79, 3, 35, 1], [7, 80, 4, 36, 2]])  
print('Dimension:', x.ndim, 'Shape:', x.shape)  
```  
**[[Wikilink]]**: [[Tensor]]  

---

### **3D Tensors**  
**Definition**: A cube-like structure containing multiple matrices (e.g., a batch of images).  
**Formula**: N/A  
**Example**:  
```python  
x = np.array([[[5, 78, 2], [6, 79, 3], [7, 80, 4]],  
              [[5, 78, 2], [6, 79, 3], [7, 80, 4]],  
              [[5, 78, 2], [6, 79, 3], [7, 80, 4]]])  
print('Dimension:', x.ndim, 'Shape:', x.shape)  
```  
**[[Wikilink]]**: [[Tensor]]  

---

### **Tensor Attributes**  
**Definition**: Key properties of a tensor:  
- **`ndim`**: Number of axes (rank).  
- **`shape`**: Dimensions along each axis.  
- **`dtype`**: Data type (e.g., `uint8`).  
**Formula**: N/A  
**Example**:  
```python  
print(train_images.ndim)  # Output: 3  
print(train_images.shape)  # Output: (60000, 28, 28)  
print(train_images.dtype)  # Output: uint8  
```  
**[[Wikilink]]**: [[Tensor]]  

---

### **Tensor Slicing**  
**Definition**: Selecting subsets of a tensor using index ranges.  
**Formula**: N/A  
**Example**:  
```python  
# Slice first 90 MNIST images (excluding index 90)  
my_slice = train_images[10:100]  
print(my_slice.shape)  # Output: (90, 28, 28)  
```  
**[[Wikilink]]**: [[Tensor]]  

---

### **Element-wise Operations**  
**Definition**: Operations applied individually to corresponding elements of two tensors (e.g., addition, subtraction).  
**Formula**: N/A  
**Example**:  
```python  
x = np.array([3, 4, 7, 8])  
y = x + 2  # Element-wise addition  
print(y)  # Output: [5 6 9 10]  
```  
**[[Wikilink]]**: [[Broadcasting]]  

---

### **Broadcasting**  
**Definition**: Automatically aligning tensors of different shapes for operations by "expanding" smaller tensors.  
**Formula**: N/A  
**Example**:  
```python  
x = np.random.randint(10, size=(3, 2, 5))  
y = np.random.randint(10, size=(2, 5))  
z = x + y  # y is broadcasted to match x's shape  
```  
**[[Wikilink]]**: [[Element-wise Operations]]  

---

### **Tensor Dot Product**  
**Definition**: Matrix multiplication of two tensors (e.g., `np.dot(x, y)`).  
**Formula**: For matrices \( A \) (m×n) and \( B \) (n×p), the dot product \( C = A \cdot B \) where \( C_{ij} = \sum_{k=1}^n A_{ik}B_{kj} \).  
**Example**:  
```python  
x = np.array([[5, 78, 2], [6, 79, 3]])  
y = np.array([[1, 2], [3, 4], [5, 6]])  
z = np.dot(x, y)  
```  
**[[Wikilink]]**: [[Tensor Operations]]  

---

### **Tensor Reshaping**  
**Definition**: Changing a tensor’s shape without altering its data.  
**Formula**: Total elements must remain constant (e.g., reshaping a 3x4 tensor to 2x6).  
**Example**:  
```python  
x = np.array([[0., 1.], [2., 3.], [4., 5.]])  
x_reshaped = x.reshape((6, 1))  
print(x_reshaped.shape)  # Output: (6, 1)  
```  
**[[Wikilink]]**: [[Tensor]]  

---

### **Key Outcomes**  
1. **Tensors** generalize scalars, vectors, and matrices to higher dimensions.  
2. **Operations** like slicing, broadcasting, and reshaping are foundational for manipulating data in deep learning.  
3. **Attributes** (`ndim`, `shape`, `dtype`) are critical for understanding tensor structure.  

**[[Wikilinks]]**  
- [[Tensor]] → [[Scalars (0D tensors)]], [[Vectors (1D tensors)]], [[Matrices (2D tensors)]], [[3D Tensors]]  
- [[Element-wise Operations]] → [[Broadcasting]]  
- [[Tensor Dot Product]] → [[Tensor Operations]]  
- [[Tensor Reshaping]] → [[Tensor]]