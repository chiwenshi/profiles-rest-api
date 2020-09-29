from django.contrib import admin
from profiles_api import models

# this tells the Django admin to register our user profile model with the admin
# site so make it accessible through the admin interface
admin.site.register(models.UserProfile)
