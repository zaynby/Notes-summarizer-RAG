# Practical_1_Tensor_Operations_Solution_Apr 2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Sure! Let's go through the tasks step by step to ensure you understand each concept and can complete them correctly.

### Task 1: Creating Tensors

1. **0D Tensor (Scalar):**
   ```python
   #Task 1: 0D tensor
   x = 12
   print(x)
   ```

2. **1D Tensor:**
   ```python
   #Task 2: 1D tensor
   x = np.array([3,4,7,8])
   print(x)
   ```

3. **2D Tensor:**
   ```python
   #Task 3: 2D tensor
   x = np.array([[5, 78, 2],
                [6, 79, 3],
                [7, 80, 4]])
   print(x)
   ```

4. **3D Tensor:**
   ```python
   #Task 4: 3D tensor
   x = np.array([[[5, 78, 2],
                  [6, 79, 3],
                  [7, 80, 4]],
                 [[5, 78, 2],
                  [6, 79, 3],
                  [7, 80, 4]],
                 [[5, 78, 2],
                  [6, 79, 3],
                  [7, 80, 4]]])

   print(x)
   ```

### Task 2: Tensor Slicing

1. **Tensor Slicing Example:**
   ```python
   # Task 1: Tensor Slicing
   y = x[0:2]
   print(y)
   ```

### Task 3: Tensor Operations

1. **Element-wise Operation (Addition):**
   ```python
   # Task 1: Element Wise Operation
   x1 = np.array([3,4,7,8])
   x2 = np.array([3,4,7,8])
   x3 = x1 + x2

   print(x3)
   ```

2. **Broadcasting Example:**
   ```python
   # Task 2: Broadcasting
   y1 = y + 2
   print(y1)
   ```

3. **Tensor Dot Product:**
   ```python
   # Task 3: Tensor Dot
   x1 = np.array([[5, 78, 2, 34],
                 [6, 79, 3, 35],
                 [7, 80, 4, 36]])

   x2 = np.array([1, 2, 3, 4])

   x3 = np.dot(x1, x2)
   print(x3)
   ```

4. **Tensor Reshaping:**
   ```python
   # Task 4: Tensor Reshaping
   print(x1.shape)
   x2 = x1.reshape((6, 2))
   print(x2)
   print(x2.shape)
   ```

### Explanation:

- **0D Tensor:** A scalar value.
- **1D Tensor:** An array of numbers (vector).
- **2D Tensor:** A matrix (2-dimensional array).
- **3D Tensor:** A 3-dimensional array, often used to represent a batch of matrices or images.

- **Slicing:** Extracting specific elements from the tensor. For example, `x[0:2]` extracts the first two rows.
  
- **Element-wise Operations:** Perform operations on each element individually (e.g., addition, subtraction).
  
- **Broadcasting:** Allows operations between tensors of different shapes by expanding the smaller tensor to match the larger one.

- **Tensor Dot Product:** A generalization of matrix multiplication for higher-dimensional arrays.

- **Reshaping:** Changing the shape of a tensor without changing its data. For example, converting a 2D array into a 1D array or vice versa.

These tasks should help you understand and practice creating and manipulating tensors in Python using NumPy!