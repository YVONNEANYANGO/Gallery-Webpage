from django.test import TestCase
from .models import Photographer,Image,tags
import datetime as dt

 #Create our tests here
class PhotographerTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new photographer and saving it
        self.nadia= Photographer(first_name = 'Nadia', last_name ='Buari', email ='nadiabuari@gmail.com')
        self.nadia.save_photographer()

        # Creating a new tag and saving it 
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',photographer = self.nadia)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)
def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

    def tearDown(self):
        Photographer.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nadia,Photographer))

    # Testing Save Method
    def test_save_method(self):
        self.nadia.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers) > 0)

    def test_get_photos_today(self):
        today_photos = Image.todays_photos()
        self.assertTrue(len(today_photos)>0)

    def test_get_photos_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Image.todays_photos(date)
        self.assertTrue(len(news_by_date) == 0)
