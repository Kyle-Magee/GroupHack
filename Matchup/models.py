from django.db import models

# Create your models here.

class Language(models.Model):
    language_name = models.CharField(max_length=100)

    def __str__(self):
        return self.language_name

class Interest(models.Model):
    interest_name = models.CharField(max_length=100)

    def __str__(self):
        return self.interest_name
    
class User(models.Model):
    BEGINNER = 'BE'
    INTERMEDIATE = 'INT'
    ADVANCED = 'ADV'

    project_level_choices = (
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'))

    email = models.EmailField(max_length=300, primary_key=True)
    name = models.CharField(max_length=15, null=True)
    interests = models.ManyToManyField(Interest)
    languages = models.ManyToManyField(Language)
    project_level = models.CharField(max_length=13, 
                                        choices=project_level_choices,
                                        default=BEGINNER)
