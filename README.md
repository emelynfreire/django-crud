#CRIANDO PROJETO DJANGO

## 0 Instalar python

## 1. criar ambiente virtual:

Na pasta dp projeto:
o VENV tem a responsabilidade de isolar o projeto do sistema operacional.

para criação do ambiente:

python -m venv nome_da_venv

Nisso vai criar uma pasta com nome_da_venv e dentro os módulos.

E para ativar:
No windows: source venv/Scripts/activate ou .\activate
No linux: source venv/bin/activate

para desativar: deactivate


Instalando pacote django:
pip install django

## 3. criando projeto django:
django-admin startproject nome_projeto . (o ponto final é pra ele não criar outra pasta)

Dentro da pasta nome_projeto vai tá as configurações do projeto django execute.


## 4. Migração de configuração com banco de dado local sqlite3: banco com estrutura base, com tabelas com sessões e controles de usuários.
python manage.py migrate

## 5. para rodar o sistema:
python manage.py runserver


## 6. Criação app

''' $ django-admin startapp core '''




## 6. Nisso agora criaremos um usuário super admin pra ter acesso ao sistema:
python manage.py createsuperuser admin
python manage.py createsuperuser 

Nesse momento adiciona >> usuario>>email>>senha

Após isso executar projeto e no link: http://127.0.0.1:8000/admin/
usuario:admin 
senha:minhasenha123



