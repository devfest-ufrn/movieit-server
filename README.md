# Movie it

## Setup

-------------
#### Requirements
* Python 3.6+
* Virtualenvwrapper

-------------
#### Set Up
Clone esse projeto e crie um virtual environment:
~~~~bash
$ git clone https://github.com/devfest-ufrn/movie-it.git
$ mkvirtualenv movieitvenv
$ workon movieitvenv
~~~~
Install all dependencies
~~~~bash
$ pip install -r requirements.txt
~~~~
Setup database:
~~~~bash
cd movieit
python manage.py makemigrations
python manage.py migrate
~~~~
Testing:
~~~~bash
python manage.py test
~~~~

Running the app:
~~~~bash
$ python manage.py runserver
~~~~
Agora você pode ir até [http://localhost:8000](http://localhost:8000).

