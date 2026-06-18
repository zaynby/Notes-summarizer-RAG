# Lecture 4 - CNN I_Apr 2026 (2).pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Here’s a structured summary of the lecture content on **Convolutional Neural Networks (ConvNets)** using the specified academic format:

---

### **Term** -> **Definition** -> **Formula** -> **Example**

#### [[Convolution Operation]]  
**Definition**: A mathematical operation where a filter (kernel) slides over an input image to compute feature maps by element-wise multiplication and summation.  
**Formula**:  
Output Feature Map = σ((Input × Filter) + Bias)  
(where σ is an activation function like ReLU)  
**Example**:  
A 5x5 input image with a 3x3 filter produces a 3x3 output feature map (assuming no padding/stride=1).  

---

#### [[Padding]]  
**Definition**: Adding zeros around the input image borders to preserve spatial dimensions or control output size.  
**Formula**:  
Output Size = (Input Size + 2×Padding - Filter Size) / Stride + 1  
**Example**:  
Input=5x5, Filter=3x3, Padding=1 → Output=5x5 (stride=1).  

---

#### [[Stride]]  
**Definition**: The step size of the filter as it moves over the input image. Larger strides reduce output spatial dimensions.  
**Formula**:  
Output Size = (Input Size - Filter Size + 2×Padding) / Stride + 1  
**Example**:  
Input=5x5, Filter=3x3, Stride=2 → Output=2x2 (no padding).  

---

#### [[Max-Pooling]]  
**Definition**: A downsampling technique that reduces spatial dimensions by selecting the maximum value in a defined window (e.g., 2x2).  
**Formula**:  
Output = max(Input[Window])  
**Example**:  
A 4x4 feature map with 2x2 pooling reduces to 2x2.  

---

#### [[Output Size Calculation]]  
**Definition**: Formula to compute the dimensions of the output feature map after convolution.  
**Formula**:  
Output Size = (Input Size + 2×Padding - Filter Size) / Stride + 1  
**Example**:  
For MNIST (28x28 input, 3x3 filter, padding=0, stride=1):  
Output = (28 - 3 + 0)/1 + 1 = 26x26.  

---

#### [[Local vs. Global Patterns]]  
**Definition**:  
- **Local Patterns**: Edges, textures (learned via convolution layers).  
- **Global Patterns**: High-level combinations (learned via dense layers).  
**Example**:  
Early ConvNet layers detect edges; later layers combine them into shapes (e.g., eyes, ears in cat/dog images).  

---

#### [[Data Augmentation]]  
**Definition**: Applying transformations (e.g., flipping, cropping) to training data to increase diversity and reduce overfitting.  
**Example**:  
Horizontally flipping images of cats/dogs to simulate new examples without collecting additional data.  

---

#### [[ConvNet Architecture]]  
**Definition**: A hierarchical structure with convolution layers (feature extraction), pooling layers (downsampling), and dense layers (classification).  
**Example**:  
A typical MNIST model:  
`Input → Conv Layer → Max-Pooling → Flatten → Dense Layer → Output`.  

---

### **Key Takeaways**  
1. **Convolution Layers** extract local features (edges → textures → shapes).  
2. **Padding** and **Stride** control output spatial dimensions.  
3. **Max-Pooling** reduces computation and overfitting.  
4. **Data Augmentation** improves generalization on small datasets (e.g., 2,000 cat/dog images).  
5. **Overfitting** risks increase with deeper networks or insufficient data.  

---

### **Related Concepts**  
- [[Neural Networks]]  
- [[Deep Learning]]  
- [[Activation Function]]  
- [[Dropout]]  
- [[Loss Function]]  

Use `[[Term]]` links to navigate between related notes.