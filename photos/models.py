from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Photo(models.Model):
    description = models.TextField()
    image = models.ImageField(null=False,blank=False)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.description