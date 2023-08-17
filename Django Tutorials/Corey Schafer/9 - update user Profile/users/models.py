from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save() # run save method the parent class
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            """ override the resized image and saved it in the file path"""
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# For Profile we do
# 1) create model
# 2) Attach it to admin page
# 3) Make profile for some user in admin page
# 4) create signals to make a profile object for a newly created user
#

# upload_to  -> means upload directory
# this will create profile_pics directory at MEDIA_URL( path in setting file) and save files there.

# *****************

# for images, it will automatically create this path in the project if MEDIA_URL is not set manually:
# django_project\profile_pics

# *****************

# we can change this path to 'django_project\media\profile_pics'  by:
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

# *********************

# django will access default='default.jpg' file in django_project\media\default.jpg'

# *********************
