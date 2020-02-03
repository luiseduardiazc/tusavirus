# Tusavirus outbreak in Colombia.



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://tusavirusluis.herokuapp.com/)

### Local Installation

Tusavirus requires [Python3](https://www.python.org/) v3+ to run.


Clone this repository

```sh
$ git clone https://github.com/luiseduardiazc/tusavirus.git
```
Create virtualenv and Install the dependencies.

```sh
$ cd tusavirus
$ python3 -m pip install --upgrade pip
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$(venv) pip install -r requirements.txt 
```

make migrations
```sh
$ ./manage.py makemigrations
$ ./manage.py migrate
```
Run 
```sh
$ ./manage.py runserver 0.0.0.0:8000
```
### Deployment
Creating a 'Deploy to Heroku' 

Install the Heroku CLI
```sh
$ sudo snap install --classic heroku
```
If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
```sh
$ heroku login
$ heroku create app_name
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```