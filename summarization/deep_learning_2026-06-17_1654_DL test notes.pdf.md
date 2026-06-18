# DL test notes.pdf
**Module:** deep_learning
**Style:** structured_academic (experimenting)

The provided code is an extensive example of how to build and train neural networks using Keras for various tasks, including image classification. Below are detailed explanations and additional context for each part:

### 1. **Data Preprocessing:**
   - **Image Resizing:** All images are resized to a fixed size (e.g., 150x150 pixels).
   - **Data Augmentation:** Techniques like rotation, shifting, shearing, zooming, and horizontal flipping are applied to increase the diversity of training data.
   - **Feature Extraction:** Using a pre-trained model like InceptionV3 to extract features from images.

### 2. **Building Models:**
   - **Dense Neural Network (DNN):** Used for basic classification tasks without convolutional layers.
   - **Convolutional Neural Network (CNN):** Used for image classification, with multiple convolution and pooling layers.
   - **Fine-Tuning Pre-trained Model:** Using a pre-trained model like InceptionV3 as a feature extractor and fine-tuning the last few layers.

### 3. **Training Models:**
   - **Model Compilation:** Defining loss functions, optimizers, and metrics.
   - **Model Training:** Training models with or without data augmentation.
   - **Validation:** Using validation generators to evaluate model performance.

### Detailed Code Breakdown:

#### Data Preprocessing:
```python
# Define image size
img_size = 150

# ImageDataGenerator for training and validation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

# Define directories
train_dir = 'path/to/train'
validation_dir = 'path/to/validation'

# Flow from directory with data augmentation and rescaling
train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(img_size, img_size),
        batch_size=20,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(img_size, img_size),
        batch_size=20,
        class_mode='binary')
```

#### Building and Compiling Models:

##### Dense Neural Network:
```python
from tensorflow.keras import layers
from tensorflow.keras import models

# Build a DNN model
model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(32,)))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

# Train the model
history = model.fit(
      train_generator,
      steps_per_epoch=100,
      epochs=30,
      validation_data=validation_generator,
      validation_steps=50)
```

##### Convolutional Neural Network:
```python
from tensorflow.keras import layers
from tensorflow.keras import models

# Build a CNN model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

# Train the model
history = model.fit(
      train_generator,
      steps_per_epoch=100,
      epochs=30,
      validation_data=validation_generator,
      validation_steps=50)
```

##### Fine-Tuning Pre-trained Model:
```python
from tensorflow.keras.applications import InceptionV3

# Load pre-trained InceptionV3 model without top layers
conv_base = InceptionV3(weights='imagenet', include_top=False, input_shape=(150, 150, 3))

# Feature extraction using the base model
train_features, train_labels = extract_features(train_dir, 2000)
validation_features, validation_labels = extract_features(validation_dir, 1000)

# Build a new model on top of the pre-trained base
model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))

# Freeze all layers in the base model
conv_base.trainable = False

# Compile the model
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

# Train the model (only top layers)
history = model.fit(
      train_features, train_labels,
      epochs=30,
      validation_data=(validation_features, validation_labels))

# Fine-tune the base model
conv_base.trainable = True

set_trainable = False
for layer in conv_base.layers:
    if layer.name == 'mixed6':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False

# Compile the model for fine-tuning
model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-5),
              metrics=['acc'])

# Train the model (fine-tune all layers)
history = model.fit(
      train_generator,
      steps_per_epoch=100,
      epochs=30,
      validation_data=validation_generator,
      validation_steps=50)
```

### Additional Notes:
- **Data Augmentation:** Helps in reducing overfitting by generating more training data.
- **Feature Extraction:** Utilizes pre-trained models to extract features, which can be used for further processing or fine-tuning.
- **Fine-Tuning:** Gradually unfreezing and retraining the model helps in adapting the pre-trained layers to the specific task.

This code provides a comprehensive approach to building and training neural networks using Keras, suitable for various machine learning tasks.