# Practical_4-using-convnets-with-small-datasets_colab_Solution_Apr2026.ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

It seems like the code execution was cut off at the end. Let's complete it by plotting the training and validation accuracy curves for Scenario A.

```python
# Task 4: Plot the accuracy (training and validation) and loss curves (training and validation)
import matplotlib.pyplot as plt
%matplotlib inline

acc = history_aug_sa.history['acc']
val_acc = history_aug_sa.history['val_acc']
loss = history_aug_sa.history['loss']
val_loss = history_aug_sa.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'r--', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy for Scenario A (batch_size=10)')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'r--', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss for Scenario A (batch_size=10)')
plt.legend()

plt.show()
```

### Comments:
- **Scenario A**: By reducing the batch size from 20 to 10, we are effectively increasing the number of epochs per epoch in terms of data exposure. This can help with training stability but might also increase computational cost due to more frequent updates.
- **Accuracy and Loss Curves**: The curves will show how the model performs during training and validation. Typically, reducing the batch size can lead to slightly different convergence behavior.

Now, let's move on to Scenario B:

### 2.2 Scenario B: Increase Optimizer Learning Rate from `1e-4` to `2*1e-4`

# Code Cell 43
```python
# Task 1: Build and Compile the Model with increased learning rate

model_aug_sb = models.Sequential()
model_aug_sb.add(Input(shape=(img_size, img_size, 3)))
model_aug_sb.add(layers.Rescaling(1.0 / 255))
model_aug_sb.add(layers.Conv2D(32, (3, 3), activation='relu'))
model_aug_sb.add(layers.MaxPooling2D((2, 2)))
model_aug_sb.add(layers.Conv2D(64, (3, 3), activation='relu'))
model_aug_sb.add(layers.MaxPooling2D((2, 2)))
model_aug_sb.add(layers.Conv2D(128, (3, 3), activation='relu'))
model_aug_sb.add(layers.MaxPooling2D((2, 2)))
model_aug_sb.add(layers.Conv2D(128, (3, 3), activation='relu'))
model_aug_sb.add(layers.MaxPooling2D((2, 2)))
model_aug_sb.add(layers.Flatten())
model_aug_sb.add(layers.Dense(512, activation='relu'))
model_aug_sb.add(layers.Dropout(0.5))
model_aug_sb.add(layers.Dense(1, activation='sigmoid'))

model_aug_sb.compile(loss='binary_crossentropy',
              optimizer=optimizers.Adam(learning_rate=2e-4),
              metrics=['acc'])
```

# Code Cell 44
```python
# Task 2: Do Data preprocessing and Data Augmentation (same as before)

augmented_train_dataset = train_dataset.map(
    data_augmentation, num_parallel_calls=8
)
```

# Code Cell 45
```python
# Task 3: Fit the model with increased learning rate

history_aug_sb = model_aug_sb.fit(
      augmented_train_dataset,
      epochs=100,
      validation_data=validation_dataset)
```

# Code Cell 46
```python
# Task 4: Plot the accuracy (training and validation) and loss curves (training and validation)

acc = history_aug_sb.history['acc']
val_acc = history_aug_sb.history['val_acc']
loss = history_aug_sb.history['loss']
val_loss = history_aug_sb.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'r--', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy for Scenario B (learning_rate=2e-4)')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'r--', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss for Scenario B (learning_rate=2e-4)')
plt.legend()

plt.show()
```

### Comments:
- **Scenario B**: By increasing the learning rate from `1e-4` to `2*1e-4`, we are making larger updates during each training step. This can help with faster convergence but might also lead to instability and overfitting if not carefully managed.
- **Accuracy and Loss Curves**: The curves will show how the model performs during training and validation. Typically, increasing the learning rate can lead to more rapid changes in the loss function, potentially leading to better or worse performance depending on the specific dataset.

By comparing these two scenarios, you can observe the impact of different hyperparameters on your model's performance. ```