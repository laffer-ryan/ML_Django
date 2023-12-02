from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
penguins = (
        ('Adelie', 'Adelie Penguin'),
        ('Chinstrap', 'Chinstrap Penguin'),
        ('Gentoo', 'Gentoo Penguin'),
    )

islands = (
    ('Biscoe', 'Biscoe Island'),
    ('Dream', 'Dream Island'),
    ('Torgersen', 'Torgersen Island'),
)


class User(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)


    avatar = models.ImageField(null=True, default="avatar.svg")    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




class Penguin(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    species = models.CharField(max_length=20, choices=penguins, default="Adelie", blank=False, null=False)
    island = models.CharField(max_length=20, choices = islands, default= "Biscoe")
    bill_length_mm = models.FloatField(blank=False, null=False)
    bill_depth_mm = models.FloatField(blank=False, null=False)
    flipper_length_mm = models.FloatField(blank=False, null=False)
    body_mass_g = models.FloatField(blank=False, null=False)
    sex = models.CharField(max_length=10, choices= (
        ('Male', 'Male'),
        ('Female', 'Female'),
    ), default="Male")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.species

    class Meta():
        ordering = ['-updated', '-created']
        verbose_name_plural = 'Penguin'
        

