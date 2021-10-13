from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
  

    def __str__(self):
        return self.name


# now we have to regiter our model in admin.py file first import model than ragister        
