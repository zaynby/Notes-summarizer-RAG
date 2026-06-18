# Practical 5-using_a_pretrained_convnet_Suggested Solution_INCEPTION_Apr2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Let's go through your code step-by-step, starting with an overview of the key parts you've implemented:

### Feature Extraction Without Data Augmentation

1. **Model Architecture**:
    - You start by freezing all layers in the pre-trained InceptionV3 model and adding two dense layers on top.
    - This setup ensures that only the added dense layers are trained during the initial training phase.

2. **Training Process**:
    - Training is done using the `binary_crossentropy` loss function and Adam optimizer with a learning rate of \(2 \times 10^{-5}\).
    - You train for 30 epochs, which results in high training accuracy but lower validation accuracy, indicating some overfitting.

### Feature Extraction With Data Augmentation

1. **Model Architecture**:
    - Similar to the previous setup, you freeze all layers in the pre-trained InceptionV3 model and add two dense layers on top.
    - This time, data augmentation is applied during training using a series of transformations like flipping, rotating, zooming, shearing, and translation.

2. **Training Process**:
    - Data augmentation helps to improve validation accuracy by reducing overfitting.
    - You train for 30 epochs, which results in better performance on the validation set compared to the previous setup.

### Fine-Tuning

1. **Model Architecture**:
    - All layers after `mixed6` are now trainable, allowing the model to learn more complex features from the data.
    
2. **Training Process**:
    - You use a lower learning rate ( \(2 \times 10^{-5}\) ) for fine-tuning to avoid destabilizing the pre-trained weights.
    - Training is done using the same augmented dataset and results in improved validation accuracy.

### Summary of Key Points

- **Feature Extraction Without Data Augmentation**:
    - Overfitting is observed due to high training accuracy but lower validation accuracy.
    - Validation loss starts increasing after a certain point, indicating overfitting.

- **Feature Extraction With Data Augmentation**:
    - Data augmentation significantly reduces the gap between training and validation performance.
    - This setup helps in achieving better generalization on unseen data.

- **Fine-Tuning**:
    - Fine-tuning all layers after `mixed6` can further improve model performance but requires careful tuning of learning rates to avoid overfitting.

### Code Implementation

Here is the complete code with comments and explanations:

```python
import tensorflow as tf
from keras import layers, Input, Model
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Load pre-trained model
base_model = InceptionV3(weights='imagenet', include_top=False)

# Feature Extraction Without Data Augmentation
model = tf.keras.models.Sequential()
model.add(base_model)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

# Freeze the base model layers
base_model.trainable = False

model.compile(optimizer=tf.optimizers.Adam(learning_rate=2e-5),
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(
    train_dataset.map(lambda x, y: data_augmentation(x, y)),
    epochs=30,
    validation_data=(validation_dataset.map(data_preprocess)),
    verbose=1)

# Plot training and validation accuracy
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()
# Plot training and validation loss
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()

# Save the model
model.save('/content/drive/My Drive/DLIR/Inception_cats_and_dogs_small_aug1.keras')

# Feature Extraction With Data Augmentation

# Create data augmentation layers
data_augmentation_layers = [
    layers.RandomFlip("horizontal"),
    layers.RandomRotation([-0.1, 0.1]),
    layers.RandomZoom(0.2),
    layers.RandomShear(0.2),
    layers.RandomTranslation([-0.2, 0.2], [-0.2, 0.2])
]

def data_augmentation(images, targets):
    for layer in data_augmentation_layers:
        images = layer(images)
    return images, targets

def data_preprocess(images, targets):
    preprocessed_images = tf.keras.applications.inception_v3.preprocess_input(images)
    return preprocessed_images, targets

augmented_train_dataset = train_dataset.map(data_augmentation, num_parallel_calls=8)
validation_dataset = validation_dataset.map(data_preprocess, num_parallel_calls=8)

model.compile(optimizer=tf.optimizers.Adam(learning_rate=2e-5),
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(
    augmented_train_dataset,
    epochs=30,
    validation_data=validation_dataset,
    verbose=1)

# Plot training and validation accuracy
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()

# Plot training and validation loss
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()

# Save the model
model.save('/content/drive/My Drive/DLIR/Inception_cats_and_dogs_small_aug2.keras')

# Fine-Tuning

# Rebuild the model with all layers trainable after mixed6
base_model.trainable = True
set_trainable = False
for layer in base_model.layers:
    if layer.name == 'mixed6':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False

model.compile(optimizer=tf.optimizers.Adam(learning_rate=2e-5),
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(
    augmented_train_dataset,
    epochs=30,
    validation_data=validation_dataset,
    verbose=1)

# Plot training and validation accuracy
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()

# Plot training and validation loss
loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()

# Save the model
model.save('/content/drive/My Drive/DLIR/Inception_cats_and_dogs_small_aug2.keras')
```

### Key Points to Note

1. **Data Augmentation**: It helps in reducing overfitting by providing more diverse training samples.
2. **Fine-Tuning**: Carefully fine-tune the model with a lower learning rate to avoid destabilizing pre-trained weights.

This approach should help you achieve better performance and generalization on your dataset. If you encounter issues, consider adjusting hyperparameters like learning rates or increasing data augmentation complexity.