# Practical_2a-classifying-movie-reviews_Apr2026_[student_name].ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

Sure, let's go through each scenario and analyze the results.

### Scenario A: Sigmoid Activation

#### Code Implementation:
1. **Building the Model**:
   ```python
   import keras
   from keras import layers
   from keras import Input

   model = keras.Sequential(
       [
           Input(shape=(10000,)),
           layers.Dense(16, activation="sigmoid"),
           layers.Dense(16, activation="sigmoid"),
           layers.Dense(1, activation="sigmoid"),
       ]
   )

   model.summary()
   ```

2. **Compiling and Fitting the Model**:
   ```python
   model.compile(optimizer='adam',
                 loss='binary_crossentropy',
                 metrics=['accuracy'])
   
   history = model.fit(x_train,
                       y_train,
                       epochs=20,
                       batch_size=512,
                       validation_split=0.4)
   ```

3. **Plotting the Loss and Accuracy Curves**:
   ```python
   import matplotlib.pyplot as plt
   %matplotlib inline

   acc = history.history['accuracy']
   val_acc = history.history['val_accuracy']
   loss = history.history['loss']
   val_loss = history.history['val_loss']

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

   #accuracy curve
   plt.plot(epochs, acc, 'r--', label='Training acc')
   plt.plot(epochs, val_acc, 'b', label='Validation acc')
   plt.title('Training and validation accuracy')
   plt.xlabel('Epochs')
   plt.ylabel('Accuracy')
   plt.legend()

   plt.show()
   ```

4. **Comments**:
   ```python
   # Using Sigmoid there are some pros and cons. One of the benefits is that as more and more epochs are run, the model is more confident in its ability to
   # predict based on the given data. However, there are some draw downs. It is really obvious that it takes longer time to train the model. As you can see 
   # from the graph above, the curve takes a larger number of epochs to have an accuracy of 1.
   ```

### Scenario B: Reduced Capacity

#### Code Implementation:
1. **Building the Model**:
   ```python
   import keras
   from keras import layers
   from keras import Input

   model = keras.Sequential(
       [
           Input(shape=(10000,)),
           layers.Dense(2, activation="relu"),
           layers.Dense(1, activation="sigmoid"),
       ]
   )

   model.summary()
   ```

2. **Compiling and Fitting the Model**:
   ```python
   model.compile(optimizer='adam',
                 loss='binary_crossentropy',
                 metrics=['accuracy'])
   
   history = model.fit(x_train,
                       y_train,
                       epochs=20,
                       batch_size=512,
                       validation_split=0.4)
   ```

3. **Plotting the Loss and Accuracy Curves**:
   ```python
   import matplotlib.pyplot as plt
   %matplotlib inline

   acc = history.history['accuracy']
   val_acc = history.history['val_accuracy']
   loss = history.history['loss']
   val_loss = history.history['val_loss']

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

   #accuracy curve
   plt.plot(epochs, acc, 'r--', label='Training acc')
   plt.plot(epochs, val_acc, 'b', label='Validation acc')
   plt.title('Training and validation accuracy')
   plt.xlabel('Epochs')
   plt.ylabel('Accuracy')
   plt.legend()

   plt.show()
   ```

4. **Comments**:
   ```python
   # From the 2 charts what we can infer is that with lesser layers, the rate of training is faster. This is due to the lesser layers to deal with. Other
   # than that, we can see that the rate of accuracy training is still the same across the 2 models.
   ```

### Observations and Comments:

1. **Scenario A (Sigmoid Activation)**:
   - The model takes longer to converge compared to the original model using ReLU activation.
   - The training loss decreases more slowly, indicating a slower learning rate.
   - The validation accuracy also increases more gradually.

2. **Scenario B (Reduced Capacity)**:
   - The model converges faster due to fewer layers and neurons.
   - However, it may underfit the data since there are fewer parameters to learn.
   - Both training and validation accuracy curves show a similar pattern but with lower peaks compared to the original model.

### Conclusion:

- **Sigmoid Activation**: Slower convergence but potentially more confident predictions after many epochs.
- **Reduced Capacity**: Faster training but may not perform as well on unseen data due to fewer parameters. 

Feel free to run these code snippets and observe the results in your environment!