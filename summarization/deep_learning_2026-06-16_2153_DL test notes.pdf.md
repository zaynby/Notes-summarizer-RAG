# DL test notes.pdf
**Module:** deep_learning
**Style:** structured_academic (experimenting)

This comprehensive code snippet provides a detailed guide on building and training various types of neural networks, including fully connected feedforward networks (FFNs), convolutional neural networks (CNNs), and fine-tuning pre-trained models. Below is an organized breakdown of the key sections:

### 1. **Fully Connected Feedforward Networks (FFNs)**
#### Data Preparation
- **Image Preprocessing**: Resizing images to a standard size.
- **Data Augmentation**: Using `ImageDataGenerator` for image transformations.

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)
```

#### Model Building and Training
- **Model Definition**: Defining the FFN architecture.
- **Training**: Using `ImageDataGenerator` for data augmentation.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(img_size*img_size*3,)))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_generator,
    steps_per_epoch=100,
    epochs=30,
    validation_data=validation_generator,
    validation_steps=50
)
```

### 2. **Convolutional Neural Networks (CNNs)**
#### Data Preparation and Preprocessing
- **Image Augmentation**: Using `ImageDataGenerator` for image transformations.

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)
```

#### Model Building and Training
- **Model Definition**: Defining the CNN architecture.
- **Training**: Using `ImageDataGenerator` for data augmentation.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_size, img_size, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer=optimizers.RMSprop(learning_rate=1e-4), loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_generator,
    steps_per_epoch=100,
    epochs=30,
    validation_data=validation_generator,
    validation_steps=50
)
```

### 3. **Fine-Tuning Pre-trained Models**
#### Data Preparation and Preprocessing
- **Image Augmentation**: Using `ImageDataGenerator` for image transformations.

```python
from tensorflow.keras.applications import InceptionV3

img_size = 150

conv_base = InceptionV3(weights='imagenet', include_top=False, input_shape=(img_size, img_size, 3))

def extract_features(directory, sample_count):
    features = np.zeros(shape=(sample_count, 3, 3, 2048))
    labels = np.zeros(shape=(sample_count))
    generator = test_datagen.flow_from_directory(
        directory,
        target_size=(img_size, img_size),
        batch_size=batch_size,
        class_mode='binary')
    i = 0
    for inputs_batch, labels_batch in generator:
        features_batch = conv_base.predict(inputs_batch, verbose=0)
        features[i * batch_size : (i + 1) * batch_size] = features_batch
        labels[i * batch_size : (i + 1) * batch_size] = labels_batch
        i += 1
        if i * batch_size >= sample_count:
            break
    return features, labels

train_features, train_labels = extract_features(train_dir, 2000)
validation_features, validation_labels = extract_features(validation_dir, 1000)
test_features, test_labels = extract_features(test_dir, 1000)
```

#### Model Building and Training
- **Model Definition**: Defining the fine-tuning architecture.
- **Training**: Fine-tuning the pre-trained model.

```python
conv_base.trainable = True

set_trainable = False
for layer in conv_base.layers:
    if layer.name == 'mixed6':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False

model.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(learning_rate=1e-5), metrics=['acc'])

history = model.fit(
    train_generator,
    steps_per_epoch=100,
    epochs=100,
    validation_data=validation_generator,
    validation_steps=50
)
```

### Summary
This code covers the process of building and training neural networks, including handling image data with preprocessing and augmentation. It also demonstrates how to fine-tune pre-trained models like InceptionV3 for better performance on specific tasks.