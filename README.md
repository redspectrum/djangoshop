# Pizza Shop

## Description

Simple pizza-shop. 
Used django2.1.7.
Used Django REST.

Upload on heroku:
https://fastfoodshop.herokuapp.com

## Installation

pip install -r requirements.txt

Warning:
Don't use DjangoWhiteNoise in wsgi.py*
================================
## Heroku

heroku login
git push heroku master

heroku run python manage.py migrate

heroku run python manage.py createsuperuser

heroku logs --tail
check logs
================================
## Django REST
Login with Facebook(Oauth2)

/convert-token (Sign in / Sign up)

/revoke-token (Sign out)

login
http://localhost:8000/api/social/revoke-token?grant_type=convert_token
&client_id=XXX
&client_secret=XXXX
&backend=facebook
&token=XXX

Example:

http://localhost:8000/api/client/pizzashops/
http://localhost:8000/api/client/pizzas/<int:pizzashop_id>/
---------------

