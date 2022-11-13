# Dell Hack-2-Hire Team 7

### Problem statement : Image Annotation

We had to build a model that could analyse an image and detect objects present in the
image and convert it into a human readable form.
This is part of a bigger project that aims to help visually impaired people appreciate and
understand the beauty of images.

### Solution strategy
Our approach to the problem was through understanding how the data in a image is
process. Since, we were performing image annotation, we decided to go with the
Convolutional Neural Network. The CNN model is capable of identifying and extracting
features of the image without compromising its quality. In fact, CNN model was build
keeping image processing in mind. This is why we selected the CNN model
In level 1, the solution demanded us to identify a single object present in the image.
For this, we used Multi-class Image Classification CNN model. This enabled us to identify the
object present in the image. In level 2, the solution demanded us to identify multiple objects
present in the image. For this, we used Multi-label Image Classification CNN Model. Now, by
making the system understand that certain objects are related to each other, we identified
the relation they shared and provided the relation as output
We took the dataset (Fashion) from Kaggle which has multiple labels related to it.
We processed this and finally we trained our model to identify multiple aspects of the
image. We then saved the trained model and used it in our backend which was formed with
Flask. Finally, our site was able to identify multiple objects with the files being uploaded
directly through the website

Don't forget to hit the :star:, If you like this repo.
