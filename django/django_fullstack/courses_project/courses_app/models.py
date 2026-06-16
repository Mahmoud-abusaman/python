from django.db import models


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) <= 5:
            errors['name'] = "Course name should be more than 5 characters"
        if len(postData['description']) <= 15:
            errors['description'] = "Course description should be more than 15 characters"
        return errors

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, related_name="course", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
