import os, django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'condominio.settings')
django.setup()

from faker import Faker
import random
from pessoa.models import Pessoa
from garagem.models import Veiculo

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        num_tel = fake.unique.random_int()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        telefone = int(num_tel)
        p = Pessoa(nome=nome, email=email, telefone=telefone)
        p.save()

criando_pessoas(50)
print('Gerado seed de pessoas')


def criando_veiculo(quantidade_de_veiculo):
    fake = Faker('pt_BR')
    my_word_list = ['Chevrolet Onix', 'Hyundai HB20', 'Chevrolet Onix Plus', 'Fiat Strada', 'Volkswagen Gol',
                'Ford Ka', 'Fiat Argo', 'Volkswagen T-Cross', 'Jeep Renegade', 'Fiat Toro',
                'Jeep Compass', 'Renault Kwid', 'Chevrolet Tracker', 'Hyundai Creta']
    
    Faker.seed(10)
    for _ in range(quantidade_de_veiculo):
        tipo = random.choice(['M', 'C'])
        modelo = my_word_list[fake.random_int(min=0, max=13)]
        ano_veiculo = fake.random_int()
        cor = fake.color_name()
        placa = fake.random_int()
        visivel = random.choice([True, False]) #fake.unique.boolean() 
        p = Veiculo(tipo=tipo, modelo=modelo, ano_veiculo=ano_veiculo, cor= cor, placa=placa, visivel = visivel)
        p.save()

criando_veiculo(50)
print('Gerado seed de veiculo')