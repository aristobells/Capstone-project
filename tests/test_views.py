from django.test import TestCase
from restaurant.models import  Menu

class MenuViewTest(TestCase):
 def setUp(self):
  Menu.objects.create(title = 'Item1', price = 60, inventory = 80)
  Menu.objects.create(title = 'Item2', price = 30, inventory =170)
  Menu.objects.create(title = 'Item3', price = 60, inventory =270)
  
 def test_getall(self):
  all_menus = Menu.objects.all()
  
  self.assertEqual(all_menus.count(), 3)
  