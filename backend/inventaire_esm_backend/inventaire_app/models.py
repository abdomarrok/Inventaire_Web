from django.db import models

# Create your models here.
# inventaire_app/models.py


class Category(models.Model):
    name_cat = models.CharField(max_length=255)

    def __str__(self):
        return self.name_cat

class Article(models.Model):
    name = models.CharField(max_length=255)
    unite = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()
    remarque = models.CharField(max_length=255, blank=True, null=True)
    id_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Location(models.Model):
    loc_name = models.CharField(max_length=255)
    id_service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    floor = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.loc_name

class Employer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class InventaireItem(models.Model):
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    id_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True, null=True)
    num_inventaire = models.CharField(max_length=255, blank=True, null=True)
    id_employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.id_article} at {self.id_location}"
