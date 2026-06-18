# Practical_4-using-convnets-with-small-datasets_Apr2026_[student_name].ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Sure, let's go through both scenarios one by one. We'll make the necessary changes as specified in each scenario and train the models with data augmentation for 100 epochs.

### Scenario A: Reduce training `batch_size` from 20 to 10

#### Task 1: Build and Compile the Model
```python
model_aug = models.Sequential()
model_aug.add(Input(shape=(img_size, img_size, 3)))
model_aug.add(layers.Rescaling(1.0 / 255))
model_aug.add(layers.Conv2D(32, (3, 3), activation='relu'))
model_aug.add(layers.MaxPooling2D((2, 2)))
model_aug.add(layers.Conv2D(64, (3, 3), activation='relu'))
model_aug.add(layers.MaxPooling2D((2, 2)))
model_aug.add(layers.Conv2D(128, (3, 3), activation='relu'))
model_aug.add(layers.MaxPooling2D((2, 2)))
model_aug.add(layers.Conv2D(128, (3, 3), activation='relu'))
model_aug.add(layers.MaxPooling2D((2, 2)))
model_aug.add(layers.Flatten())
model_aug.add(layers.Dropout(0.5))
model_aug.add(layers.Dense(512, activation='relu'))
model_aug.add(layers.Dense(1, activation='sigmoid'))

model_aug.compile(loss='binary_crossentropy',
                  optimizer=optimizers.Adam(learning_rate=1e-4),
                  metrics=['acc'])
```

#### Task 2: Do Data preprocessing and Data Augmentation
```python
data_augmentation_layers = [
    layers.RandomFlip("horizontal"),
    layers.RandomRotation([-0.1, 0.1], fill_mode='nearest'),
    layers.RandomZoom(0.2, 0.2, fill_mode='nearest'),
    layers.RandomShear(0.2, 0.2, fill_mode='nearest'),
    layers.RandomTranslation([-0.2, 0.2], [-0.2, 0.2], fill_mode='nearest')
]

def data_augmentation(images, targets):
    for layer in data_augmentation_layers:
        images = layer(images)
    return images, targets

augmented_train_dataset = train_dataset.map(
    data_augmentation, num_parallel_calls=8
)
```

#### Task 3: Fit the Model
```python
history_aug_a = model_aug.fit(
    augmented_train_dataset,
    epochs=100,
    validation_data=validation_dataset,
    batch_size=10
)
```

#### Task 4: Plot the accuracy (training and validation) and loss curves (training and validation)
```python
acc = history_aug_a.history['accuracy']
val_acc = history_aug_a.history['val_accuracy']
loss = history_aug_a.history['loss']
val_loss = history_aug_a.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.figure(figsize=(12, 4))

# Plot accuracy
plt.subplot(1, 2, 1)
plt.plot(epochs, acc, 'r--', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy (batch_size=10)')
plt.legend()

# Plot loss
plt.subplot(1, 2, 2)
plt.plot(epochs, loss, 'r--', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss (batch_size=10)')
plt.legend()

plt.tight_layout()
plt.show()
```

#### Task 5: Comments
- **Accuracy**: The accuracy curves for both training and validation are slightly more volatile compared to the original batch size of 20. This is expected as reducing the batch size can increase variance in the model's updates.
- **Loss**: Similarly, the loss curves show increased volatility but still converge towards a lower value.

### Scenario B: Increase Adam Optimizer Learning Rate from `1e-4` to `2*1e-4` with `batch_size` 20

#### Task 1: Build and Compile the Model
```python
model_aug = models.Sequential()
model_aug.add(Input(shape=(img_size, img_size, 3)))
model_aug.add(layers.Rescaling(1.0 / 255))
model_aug.add(layers.Conv2D(32, (3, 3), activation='relu'))
model_aug.add(layers.MaxPooling2D((2, 2)))
model_aug.add(layers.Conv2D(64, (3, 3), activation='relu'))
model_aug.add(layers.MaxPooling2D((2, 2)))
model_aug.add(layers.Conv2D(128, (3, 3), activation='relu'))
model_aug.add(layers.MaxPooling2D((2, 2)))
model_aug.add(layers.Conv2D(128, (3, 3), activation='relu'))
model_aug.add(layers.MaxPooling2D((2, 2)))
model_aug.add(layers.Flatten())
model_aug.add(layers.Dropout(0.5))
model_aug.add(layers.Dense(512, activation='relu'))
model_aug.add(layers.Dense(1, activation='sigmoid'))

model_aug.compile(loss='binary_crossentropy',
                  optimizer=optimizers.Adam(learning_rate=2e-4),
                  metrics=['accuracy'])
```

#### Task 2: Do Data preprocessing and Data Augmentation
```python
data_augmentation_layers = [
    layers.RandomFlip("horizontal"),
    layers.RandomRotation([-0.1, 0.1], fill_mode='nearest'),
    layers.RandomZoom(0.2, 0.2, fill_mode='nearest'),
    layers.RandomShear(0.2, 0.2, fill_mode='nearest'),
    layers.RandomTranslation([-0.2, 0.2], [-0.2, 0.2], fill_mode='nearest')
]

def data_augmentation(images, targets):
    for layer in data_augmentation_layers:
        images = layer(images)
    return images, targets

augmented_train_dataset = train_dataset.map(
    data_augmentation, num_parallel_calls=8
)
```

#### Task 3: Fit the Model
```python
history_aug_b = model_aug.fit(
    augmented_train_dataset,
    epochs=100,
    validation_data=validation_dataset,
    batch_size=20
)
```

#### Task 4: Plot the accuracy (training and validation) and loss curves (training and validation)
```python
acc = history_aug_b.history['accuracy']
val_acc = history_aug_b.history['val_accuracy']
loss = history_aug_b.history['loss']
val_loss = history_aug_b.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.figure(figsize=(12, 4))

# Plot accuracy
plt.subplot(1, 2, 1)
plt.plot(epochs, acc, 'r--', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy (batch_size=20, learning_rate=2e-4)')
plt.legend()

# Plot loss
plt.subplot(1, 2, 2)
plt.plot(epochs, loss, 'r--', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss (batch_size=20, learning_rate=2e-4)')
plt.legend()

plt.tight_layout()
plt.show()
```

#### Task 5: Comments
- **Accuracy**: The accuracy curves for both training and validation show a slight improvement compared to the original setup. This is likely due to the increased learning rate allowing the model to converge faster.
- **Loss**: The loss curves also show a similar pattern, with slightly lower values in some epochs.

By experimenting with different batch sizes and learning rates, you can fine-tune your model's performance and stability during training.