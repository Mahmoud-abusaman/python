from django.db import models
from datetime import datetime
# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        for key, value in postData.items():
            if key != 'description' and (value == "" or value == None):
                errors[key] = f"{key.capitalize()} is required"
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters long"
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters long"
        if postData['release_date']:
            release_date = datetime.strptime(postData['release_date'], '%Y-%m-%d')
            if release_date > datetime.now():
                errors['release_date'] = "Release date cannot be in the future"
        if 'description' in postData and postData['description']:
            if len(postData['description']) < 10:
                errors['description'] = "Description must be at least 10 characters long"
        return errors

class Show(models.Model):
    title = models.CharField(unique=True,max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
    def __str__(self):
        return self.title