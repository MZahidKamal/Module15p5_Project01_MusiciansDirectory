from django.db import models
from musician_app.models import Musician_Model

# Create your models here.
class StarRatingModel(models.Model):
    rating = models.CharField(max_length=5)

    def __str__(self):
        return self.rating

class Album_Model(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician_Model, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.ForeignKey(StarRatingModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # python .\manage.py makemigrations
    # python .\manage.py migrate
    # python .\manage.py createsuperuser ★
