from rest_framework.test import APITestCase
from pessoa.models import Pessoa
from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
#import factory

class PessoasTestCase(APITestCase):
    
    def setUp(self):
        self.list_url= reverse('Pessoa-list')
        self.pessoa_ana =Pessoa.objects.create(nome= 'Ana',telefone= 11111, email= 'ana@ana.com')
        self.pessoa_beatriz =Pessoa.objects.create(nome= 'Beatriz',telefone= 22222, email= 'beatriz@beatriz.com')
        
        #self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        
    def test_req_get_lista_pessoas(self):
        
        #User = get_user_model()
        #import pdb; pdb.set_trace()
        #self.assertTrue(False)
        #self.assertTrue(self.username == 'john')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
