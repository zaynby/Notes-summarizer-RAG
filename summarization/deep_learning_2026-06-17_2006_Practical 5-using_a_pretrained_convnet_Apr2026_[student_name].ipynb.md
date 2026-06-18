# Practical 5-using_a_pretrained_convnet_Apr2026_[student_name].ipynb
**Module:** deep_learning
**Style:** structured_academic (experimenting)

It looks like the code was cut off at the end. Let's complete it and ensure we can properly evaluate the fine-tuned model on the test data.

Here's the continuation of your code:

```python
import keras
from keras.applications.vgg16 import preprocess_input

model = keras.models.load_model('/content/drive/My Drive/DLIR/vgg16_cats_and_dogs_small_ft.keras')

# Note that the test data should not be augmented!
def data_preprocess(images, targets):
    preprocessed_images = preprocess_input(images)
    return preprocessed_images, targets

test_dataset = test_dataset.map(
    data_preprocess, num_parallel_calls=8
)

test_loss, test_acc = model.evaluate(test_dataset, steps=50)
print('Test accuracy:', test_acc)
```

This code will load the fine-tuned VGG16 model and evaluate it on the test dataset. The `steps` parameter in `evaluate` is set to 50 because we have 2,000 images in the test dataset (as mentioned earlier), so setting steps=50 means we'll process batches of size 40 (since 2000 / 50 = 40).

Let's go through the code step-by-step:

1. **Load the model**: We load the fine-tuned VGG16 model that was saved earlier.
2. **Preprocess the test dataset**: We preprocess the test images using the `preprocess_input` function from Keras, which is necessary for the VGG16 model.
3. **Evaluate the model**: We evaluate the model on the test dataset and print the test accuracy.

Let's run this code to see the final test accuracy of the fine-tuned model.
```python
import keras
from keras.applications.vgg16 import preprocess_input

# Load the model
model = keras.models.load_model('/content/drive/My Drive/DLIR/vgg16_cats_and_dogs_small_ft.keras')

# Note that the test data should not be augmented!
def data_preprocess(images, targets):
    preprocessed_images = preprocess_input(images)
    return preprocessed_images, targets

test_dataset = test_dataset.map(
    data_preprocess, num_parallel_calls=8
)

# Evaluate the model on the test dataset
test_loss, test_acc = model.evaluate(test_dataset, steps=50)
print('Test accuracy:', test_acc)
```

This should give you the final test accuracy of the fine-tuned VGG16 model. If everything is set up correctly, you should see a high accuracy close to 99%.