# Lecture 4 - CNN I_Apr 2026 (2).pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Here’s a structured summary of the provided Convolutional Neural Networks (ConvNets) material:

---

### **Convolutional Neural Network (ConvNet)**  
**Definition**: A deep learning model designed for image data, specializing in learning local patterns (e.g., edges, textures) through hierarchical feature extraction.  
**Formula**: None directly, but relies on convolution, pooling, and dense layers.  
**Example**: MNIST classification, where ConvNets identify handwritten digits by detecting edges and shapes.  
[[Convolutional Neural Network (ConvNet)]]  

---

### **Convolution Operation**  
**Definition**: A mathematical operation where a filter (kernel) slides over an input image to produce a feature map by computing dot products.  
**Formula**:  
Output dimension = \(\frac{\text{Input width} + 2 \times \text{Padding} - \text{Filter width}}{\text{Stride}} + 1\)  
**Example**: A \(5 \times 5\) input image with a \(3 \times 3\) filter, padding=1, stride=1 → output size = \(\frac{5 + 2(1) - 3}{1} + 1 = 5 \times 5\).  
[[Convolution Operation]]  

---

### **Padding**  
**Definition**: Adding zeros around the input image borders to preserve spatial dimensions or control output size.  
**Formula**: Incorporated into output size calculation (see Convolution Operation).  
**Example**: Padding=1 for a \(5 \times 5\) image ensures output retains \(5 \times 5\) size with a \(3 \times 3\) filter.  
[[Padding]]  

---

### **Stride**  
**Definition**: The number of pixels the filter moves during convolution. Larger strides reduce output spatial dimensions.  
**Formula**: Incorporated into output size calculation (see Convolution Operation).  
**Example**: Stride=2 for a \(5 \times 5\) image with a \(3 \times 3\) filter → output size = \(\frac{5 + 0 - 3}{2} + 1 = 2 \times 2\).  
[[Stride]]  

---

### **Max-Pooling**  
**Definition**: A downsampling technique that reduces spatial dimensions by taking the maximum value in a defined window (e.g., \(2 \times 2\)).  
**Formula**: None directly, but reduces parameters and computation.  
**Example**: A \(28 \times 28\) feature map with \(2 \times 2\) max-pooling → output size = \(14 \times 14\).  
[[Max-Pooling]]  

---

### **Output Size Calculation**  
**Definition**: Formula to compute the dimensions of the feature map after convolution.  
**Formula**:  
\[
\text{Output size} = \frac{\text{Input size} + 2 \times \text{Padding} - \text{Filter size}}{\text{Stride}} + 1
\]  
**Example**: Input=28, padding=0, filter=3, stride=1 → output = \(\frac{28 + 0 - 3}{1} + 1 = 26\).  
[[Output Size Calculation]]  

---

### **Data Augmentation**  
**Definition**: Technique to artificially increase dataset diversity by applying transformations (e.g., flipping, cropping) to existing images.  
**Formula**: None.  
**Example**: Horizontal flipping of cat/dog images to reduce overfitting in a small dataset.  
[[Data Augmentation]]  

---

### **Model Training from Scratch**  
**Definition**: Training a ConvNet without pre-trained weights, requiring careful regularization to avoid overfitting.  
**Formula**: None.  
**Example**: Model_1 (no augmentation) vs. Model_2 (with augmentation + dropout) for cat/dog classification.  
[[Model Training from Scratch]]  

---

### **Hierarchical Feature Learning**  
**Definition**: ConvNets learn features in stages, from simple edges (early layers) to complex patterns (deeper layers).  
**Formula**: None.  
**Example**: Early layers detect edges, middle layers identify textures, and deeper layers recognize object parts.  
[[Hierarchical Feature Learning]]  

---

### **Dense Layers**  
**Definition**: Fully connected layers that combine features from previous layers for final classification.  
**Formula**: None.  
**Example**: Flattening a \(4 \times 4 \times 32\) feature map into a 512-dimensional vector for classification.  
[[Dense Layers]]  

---

This summary connects key concepts for ConvNets, including mathematical operations, architectural components, and practical training considerations. Use [[Wikilinks]] to navigate related topics.