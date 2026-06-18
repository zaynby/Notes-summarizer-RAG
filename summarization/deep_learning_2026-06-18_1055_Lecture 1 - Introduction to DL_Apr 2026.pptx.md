# Lecture 1 - Introduction to DL_Apr 2026.pptx
**Module:** deep_learning
**Style:** structured_academic (experimenting)

 # Deep Learning: Introduction to AI, Machine Learning & Deep Learning

## Week 1 Summary (AY26/27 Apr Sem)

---

## Core Concepts

### [[Artificial Intelligence]] (AI)
- **Definition**: Field of creating systems that automate intellectual tasks normally performed by humans
- **Scope**: General field encompassing [[Machine Learning]], [[Deep Learning]], and non-learning approaches (e.g., [[rule-based systems]])
- **Evolution**: [[Symbolic AI]] (1950s-1980s) → [[Machine Learning]] (1990s-now) → [[Deep Learning]] (2010-now)

---

### [[Machine Learning]] (ML)
- **Definition**: Systems where rules/models can be applied to new data to produce original answers; learning representations from data
- **Three Basic Components**:
  1. **[[Inputs]]**: Input data points (e.g., image files)
  2. **[[Labels]]**: Examples of expected output (e.g., cat or dog)
  3. **[[Loss Function]]**: Measures whether algorithm is doing a good job; used as feedback signal to adjust how algorithm works

- **Learning Process**: 
  - Meaningfully transform data → learn useful representations → get closer to expected output

| Aspect | [[Shallow Learning]] | [[Deep Learning]] |
|--------|---------------------|-------------------|
| Layers | 1-2 layers of representations | Multiple layered/hierarchical representations |

---

### [[Deep Learning]] (DL)
- **Definition**: Layered representations learning or hierarchical representations learning using [[neural networks]] parameterized by [[weights]]
- **Key Mechanism**:
  - [[Loss function]] measures quality of network's output
  - [[Loss score]] used as feedback signal to adjust [[weights]]

#### Why Deep Learning? Why Now?
| Factor | Description |
|--------|-------------|
| [[Hardware]] | Increased computational power (GPUs) |
| [[Datasets and benchmarks]] | Large-scale labeled data available |
| [[Algorithmic advances]] | Better optimization techniques |
| [[Simplicity]] | End-to-end learning with less manual feature engineering |
| [[Scalability]] | Performance improves with more data and larger models |
| [[Versatility and reusability]] | Transfer learning, pre-trained models |

---

## [[Universal Workflow of Machine Learning]]

### 1. Define the Problem
- **[[Inputs and outputs]]**: Identify what to predict from what data
- **[[Data availability]]**: Often the limiting factor
- **Problem Types**:
  - [[Classification]]: [[Binary classification]] or [[Multiclass classification]]
  - [[Regression]]: [[Scalar regression]] or [[Vector regression]]
- **Assumptions**: Stationary problems where outputs can be predicted by inputs; available data sufficiently informative

### 2. Choose Success Metric
- Guides choice of [[loss function]]
- **Examples**:
  - [[RMSE]] (Root Mean Squared Error), [[MAE]] (Mean Absolute Error) for regression
  - [[Accuracy]] for classification
  - [[Customized metrics]]

### 3. Choose Evaluation Protocol
| Method | When to Use |
|--------|-------------|
| [[Hold-out validation set]] | Plenty of data |
| [[K-fold cross-validation]] | Too few samples |
| [[Iterated K-fold validation]] | Highly accurate evaluation with little data |

### 4. Prepare the Data
- Format as [[tensors]]
- **[[Scaling]]**: Values to [-1, 1] or [0, 1] range
- **[[Normalization]]**: Different features to similar ranges
- **[[Feature engineering]]**: Especially for small-data problems

### 5. Develop Baseline Model
- Refer to problem type to determine:
  - [[Last-layer activation function]]
  - [[Loss function]]
  - [[Optimization configuration]]
- **Default**: [[Adam optimizer]] with default learning rate

### 6. Develop Model That Overfits
- **Goal**: Find border between [[optimization]] and [[generalization]]; [[underfitting]] and [[overfitting]]
- **Methods to induce overfitting**:
  - Add layers
  - Increase number of units/nodes
  - Train for more epochs
- **Detection**: Monitor training and validation metrics; validation metrics begin to degrade

### 7. Regularize and Tune
- **Methods**:
  - [[Dropout]]
  - Different [[architectures]] (add/remove layers, adjust units)
  - [[L1 regularization]] and/or [[L2 regularization]]
  - Adjust [[hyperparameters]]: learning rate, epochs, [[batch size]]
- **Caution**: Avoid [[overfitting to validation dataset]]

---

## [[Tensors]]: Data Representation

### Definition
**[[Tensor]]**: A container for numbers; multidimensional array

### Types by Dimension
| Type | Dimension | Example |
|------|-----------|---------|
| [[Scalar]] | 0D tensor | Single number |
| [[Vector]] | 1D tensor | Array of numbers |
| [[Matrix]] | 2D tensor | Table of numbers |
| [[3D tensor]] | 3D tensor | Time series, sequences |
| [[Higher-dimensional tensor]] | 4D+ | Images, video |

### Key Attributes
- **[[Number of axes]]** ([[rank]])
- **[[Shape]]**
- **[[Data type]]**

### Real-World Data Tensors
| Data Type | Tensor Shape |
|-----------|-------------|
| [[Vector data]] | `(samples, features)` — 2D |
| [[Time series data]] / [[Sequence data]] | `(samples, timestamps, features)` — 3D |
| [[Images]] | `(samples, height, width, channels)` or `(samples, channels, height, width)` — 4D |
| [[Video]] | `(samples, frames, height, width, channels)` or `(samples, frames, channels, height, width)` — 5D |

---

## Tensor Operations

| Operation | Description |
|-----------|-------------|
| [[Element-wise operations]] | Apply function to each element independently |
| [[Broadcasting]] | Operations between tensors of different shapes by "stretching" smaller tensor |
| [[Tensor dot]] ([[matrix multiplication]]) | Standard matrix product |
| [[Tensor reshaping]] | Rearrange elements into new shape; total elements remain same |

---

## Neural Network Building Blocks

### [[Weight]] (W) and [[Bias]] (b)
- **Definition**: Tensors/attributes of the layer; trainable parameters
- **Role**: Contain information learned from training data

### [[Gradient-based Optimization]]

#### [[Random Initialization]]
- Assign small random values to weights

#### [[Training Loop]]
1. Draw batch of training samples `x` and targets `y`
2. **[[Forward pass]]**: Run model on `x` → obtain `y_pred`
3. Compute [[loss]]: mismatch between `y_pred` and `y`
4. **[[Backpropagation]]**: Update weights to slightly reduce loss on this batch

---

## Case Study: [[MNIST]]

### Problem
- **"Hello World" of deep learning**
- Classify grayscale images of handwritten digits (28×28 pixels) into 10 categories (0-9)
- **Dataset**: 60,000 training images + 10,000 test images

### Workflow Steps
1. **[[Input Data]]** → Prepare tensors
2. **[[Build the model]]** ("network") → Define layers
3. **[[Compile]]** → Configure loss, optimizer, metrics
4. **[[Training]]** → Fit model to data
5. **[[Evaluate]]** → Assess performance on test set
6. **[[Predict]]** → Make predictions on new data

---

## Key Takeaways

| Concept | Summary |
|---------|---------|
| [[AI]] ⊇ [[ML]] ⊇ [[DL]] | Hierarchical relationship |
| ML Components | [[Inputs]], [[Labels]], [[Loss Function]] |
| DL Objective | Learn useful representations through multiple layered networks |
| Data Representation | [[Tensors]] — multidimensional arrays |
| Computations | All done through [[tensor operations]] |

---

## Further Reading & Resources

- **Chollet, F.** *Deep Learning with Python, 3rd Edition*
  - Chapter 1: What is Deep Learning?
  - Chapter 2: Mathematical Building Blocks of Neural Networks
  - Chapter 5: Fundamentals of Machine Learning
  - Chapter 6: Universal Workflow of Machine Learning

- **Online**:
  - [Understanding Hyperparameters in Machine Learning](https://medium.com/@ilyurek/understanding-hyperparameters-in-machine-learning-6ae699fcbdd1)
  - [Why and how to Cross Validate a Model?](https://medium.com/data-science/why-and-how-to-cross-validate-a-model-d6424b45261f)

---

## Practical Assignment

**`Practical_1_Tensor_Operations_[student_name].ipynb`** — Submit via POLITEMall