from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 60)

    # class Meta:
    #     ordering = ['first_name']
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

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
       images = Image.objects.all()
       return images
       print(images)

    @classmethod
    def get_image_by_id(self,image):
       image= Image.objects.get(id = id)
       return image

    @classmethod
    def search_by_Category(cls,search_term):
       images = cls.objects.filter(Category__name__icontains=search_term)
       return images

    @classmethod
    def filter_by_location(cls,location):
       images = cls.objects.filter(Category__name__icontains=location)
       return images
       
    def __str__(self):
       return self.name
   