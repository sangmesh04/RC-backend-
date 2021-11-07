from django.db import models

# Create your models here.
class Student(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        user_name = models.CharField(max_length=100, unique=True)
        college_name = models.CharField(max_length=100)
        year_of_study = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
        responses = models.JSONField(default={})
        def __str__(self):
            return self.first_name + " " + self.last_name 