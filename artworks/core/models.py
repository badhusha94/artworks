from django.db import models

class CustomerManager(models.Manager):
    def get_customers(self):
        qs = self.get_queryset()
        return qs

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    emailid = models.EmailField()
    address = models.TextField(max_length=500)
    contact = models.CharField(max_length=12)
    female = 0
    male = 1
    other = 2
    gender_choices = (
        (female,'Female'),
        (male,'Male'),
        (other,'Other')
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    objects = CustomerManager()
    def __str__(self):
        return '{0} {1}'.format(self.first_name,self.last_name)

