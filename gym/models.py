from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    expertise = models.CharField(max_length=100)
    image = models.ImageField(upload_to='trainers/')

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

