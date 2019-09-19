from django.db import models

class Citizen(models.Model):
	citizen = models.CharField(max_length=200)

	def __str__(self):
		return f'[citizen: {self.citizen}]'


class Person(models.Model):
	citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	votes = models.IntegerField(default=0)

	def younger_than_30(self):
		return int(self.age) < 30

	def __str__(self):
		return f'[name={self.name}, age={self.age}, {self.citizen.citizen}]'

# Create your models here.
