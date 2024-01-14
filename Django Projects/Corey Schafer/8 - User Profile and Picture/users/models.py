from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    # make one to one relationship b/w Profile and User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# For Profile we do
# 1) create model
# 2) Attach it to admin page
# 3) Make profile for some user in admin page
# 4) ...
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
