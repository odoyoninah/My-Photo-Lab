from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def save_category(self):
        self.save()

class Photo(models.Model):
    description = models.TextField()
    image = models.ImageField(null=False,blank=False)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.description
    def save_photo(self):
        self.save()