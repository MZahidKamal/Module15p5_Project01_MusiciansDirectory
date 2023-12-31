from django.db import models

# Create your models here.
class Instrument_Model(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Musician_Model(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    instrument_type = models.ManyToManyField(Instrument_Model)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # python .\manage.py makemigrations
    # python .\manage.py migrate
    # python .\manage.py createsuperuser
