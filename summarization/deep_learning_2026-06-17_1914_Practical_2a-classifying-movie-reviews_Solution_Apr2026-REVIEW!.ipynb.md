# Practical_2a-classifying-movie-reviews_Solution_Apr2026-REVIEW!.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

### Scenario A - Sigmoid Activation

Let's go through each step for Scenario A.

#### Code Cell 48: Build the Model with Sigmoid Activation
We'll build a new model where all activation functions in the first two layers are changed from "relu" to "sigmoid".

```python
import keras
from keras import layers
from keras import Input

model_sa = keras.Sequential(
    [
        Input(shape=(10000,)),
        layers.Dense(16, activation="sigmoid"),
        layers.Dense(16, activation="sigmoid"),
        layers.Dense(1, activation="sigmoid"),
    ]
)
```

#### Code Cell 49: Compile and Fit the Model
Next, we'll compile and fit this model.

```python
model_sa.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

history_sa = model_sa.fit(x_train,
                    y_train,
                    epochs=20,
                    batch_size=512,
                    validation_split=0.4)
```

#### Code Cell 50: Plot the Loss and Accuracy Curves
We'll plot the loss and accuracy curves to observe any changes.

```python
import matplotlib.pyplot as plt
%matplotlib inline

acc = history_sa.history['accuracy']
val_acc = history_sa.history['val_accuracy']
loss = history_sa.history['loss']
val_loss = history_sa.history['val_loss']

epochs = range(1, len(acc) + 1)

# "r--" is for "red dashes"
plt.plot(epochs, loss, 'r--', label='Training loss')
# b is for "solid blue line"
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.clf()   # clear figure
plt.plot(epochs, acc, 'r--', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()
```

#### Code Cell 51: Comments
```python
# We can see the loss value is decreasing slowly and the accuracy is increasing slowly.
# Overfitting starts later compared to when ReLU was used as the activation function. The smooth, bounded nature of sigmoid transitions reduces sharp decision boundaries, providing some regularization effect and better generalization initially.
# However, the model might be less effective in learning complex patterns due to the limited non-linearity introduced by the sigmoid function.
```

### Scenario B - Reduced Capacity

Now let's go through each step for Scenario B.

#### Code Cell 53: Build the Model with Reduced Capacity
We'll build a new model where one hidden layer is removed and the remaining layer uses only 2 units with ReLU activation.

```python
import keras
from keras import layers
from keras import Input

model_sb = keras.Sequential(
    [
        Input(shape=(10000,)),
        layers.Dense(2, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ]
)
```

#### Code Cell 54: Compile and Fit the Model
Next, we'll compile and fit this model.

```python
model_sb.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

history_sb = model_sb.fit(x_train,
                    y_train,
                    epochs=20,
                    batch_size=512,
                    validation_split=0.4)
```

#### Code Cell 55: Plot the Loss and Accuracy Curves
We'll plot the loss and accuracy curves to observe any changes.

```python
import matplotlib.pyplot as plt
%matplotlib inline

acc = history_sb.history['accuracy']
val_acc = history_sb.history['val_accuracy']
loss = history_sb.history['loss']
val_loss = history_sb.history['val_loss']

epochs = range(1, len(acc) + 1)

# "r--" is for "red dashes"
plt.plot(epochs, loss, 'r--', label='Training loss')
# b is for "solid blue line"
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.clf()   # clear figure
plt.plot(epochs, acc, 'r--', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()
```

#### Code Cell 56: Comments
```python
# Training loss/accuracy improve continuously, but validation loss plateaus and validation accuracy stagnates around 87% after epoch 6. This reflects underfitting.
# Model capacity is insufficient: Only 2 hidden units so the model cannot learn complex patterns from the 10,000 input dimensions.
# The wide gap between training and validation curves indicates the model memorizes training-specific patterns that don't generalize, despite being too simple to achieve high accuracy overall.
```

By comparing these scenarios, you can observe how different activation functions and model capacities affect the learning process and generalization performance. Scenario A shows a smoother transition but may still overfit, while Scenario B underfits due to insufficient capacity. Adjusting model parameters is crucial for achieving good performance on unseen data.