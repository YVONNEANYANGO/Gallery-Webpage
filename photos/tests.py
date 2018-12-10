from django.test import TestCase
from .models import Photographer,Image,tags

 #Create our tests here
class PhotographerTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nadia= Photographer(first_name = 'Nadia', last_name ='Buari', email ='nadiabuari@gmail.com')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nadia,Photographer))

    # Testing Save Method
    def test_save_method(self):
        self.nadia.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)
        