from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 60)

    # def __str__(self):
    #     return self.first_name

    # class Meta:
    #     ordering = ['first_name']

class Category(models.Model):
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()




    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 60)
    Description = models.TextField()
    Location = models.ForeignKey(Location)
    Category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)


    @classmethod
    def get_all_images(cls):
        images=Image.objects.all()
        return images

    
       

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__name__icontains=search_term)
        return photos
   