from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    about = models.TextField()
    type = models.CharField(max_length=30, choices=(('IT','IT'),('Non IT','Non IT')))
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name + "--" + self.location
    


class Employee(models.Model):
   
    name= models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    address = models.TextField()
    phone = models.IntegerField()
    about = models.TextField()
    position = models.CharField(max_length=25,choices=(('python developer','python developer'),
                                                       ('java developer','java developer'),
                                                       ('django developer','django developer')))    

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

 