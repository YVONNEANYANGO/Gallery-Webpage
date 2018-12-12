from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt

 #Create our tests here
class ImageTestClass(TestCase):

    # Set up method
def setUp(self):
     
        # Creating a new image and saving it
        self.new_image= Image(name = 'Test Image',description = 'This is a random test Post', location ='UK', category = 'Fashion')
        self.new_image.save()

        # Creating a new tag and saving it 
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image.tags.add(self.new_tag)

def tearDown(self):
        Location.objects.all().delete()
        category.objects.all().delete()
        Image.objects.all().delete()

    # Testing instance
def test_instance(self):
    self.assertTrue(isinstance(self.nadia,Photographer))

    # Testing Save Method
def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

def test_delete_method(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


