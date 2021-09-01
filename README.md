# Franq

API que cadastra pessoas e veiculos dentro de uma garagem.


Requisitos 
- venv
- postgres


subindo a aplicação 
No terminal digite pwd para descobri o caminho da sua aplicação
pwd
para ativar a venv coloque o codigo a baixo e substitua o {pdw} pelo retorno do comando a cima
source {pwd}/venv/bin/activate
No postgres crie um db com os seguintes dados de conexão
        NAME: condominio
        USER: postgres
        PASSWORD: 123
        HOST: localhost
A seguir dentro da venv suba aplicação
python manage.py runserver
Em outra aba do terminal
Rode as migrações do banco para criar as tabelas 
python manage.py migrate
crie um usuario admin
python manage.py createsuperuser


Rotas disponiveis 
http://localhost:8000/
http://localhost:8000/admin/login/?next=/admin/
http://localhost:8000/veiculos/
http://localhost:8000/garagens/
http://localhost:8000/pessoas/


Atualizando o requirements.txt
pip freeze > requirements.txt


TO DO 
- melhorar o visualiza veiculos de uma garagem 
- implementar caso seja moto para o usuario coloque o modelo ao invés da cor
- criar o acesso do consumidor
- melhorar o readme 
- ao criar pessoa criar a garagem