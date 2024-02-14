from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

class Floor(models.Model):
    floor = models.IntegerField()
    section = models.AutoField()
    floor_name = models.CharField(max_length=30)



    def __str__(self):
        return self.username
    class Meta:
        db_table = 'users'