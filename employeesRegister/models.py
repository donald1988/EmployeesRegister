from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title


class Employee (models.Model):
    lastName = models.CharField(max_length=25)
    firstName = models.CharField(max_length=25)
    emp_code = models.CharField(max_length=5)
    mobile = models.CharField(max_length=10)
    department = models.CharField(max_length=25)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

