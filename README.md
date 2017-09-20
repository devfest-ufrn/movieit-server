# Movie it

## Setup

Tenha instalado o python e o pip

Clone o projeto 

`https://github.com/devfest-ufrn/movie-it.git && cd movie-it`

Crie um ambiente virtual e ative-o

`virtualenv myenv`
`source myenv/bin/activate`

Instale as dependências

`pip install -r requirements.txt`

Configure o banco de dados

`python manage.py makemigrations`

`python manage.py migrate`

Rode o sistema
`python manage.py runserver`
