from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
# Pruebas unitarias
class ProfileTestCase(TestCase):

    def setUp(self):
        #Se prepara la prueba
       User.objects.create_user('test', 'test@test.com', 'test1234') 
    
    # Se ejecuta después de crear el usuario
    def test_profile_exist(self):
        exists = Profile.objects.filter(user__username='test').exists()
        # TestCase
        self.assertEqual(exists, True)

    # Test se ejecuta en el manage
    # python manage.py test NombreApp
