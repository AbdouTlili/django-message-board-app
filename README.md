# django-message-board-app
message board with admin CMS

##### built mainely with :
- PostgreSQL
- Django 3.1
- Gunicorn 19.0

##### deployment in heroku
-you need to be logged in heroku CLI 

1- create your heroku app :
```
heroku create <my-heroku-app>
```

2- add the remote :
```
heroku git:remote <my-heroku-app>
```

3- commit any changes you did  :
```
git commit -m "post deployment changes"
```


4- push the changes to heroku :
```
git push heroku master
```

5- since we're using postgrSQL database for production you need to do the initial migrations in the postgreSQL database that Heroku created for us taht is linked with the Dyno (the heroku app container) :
```
heroku run python manage.py migrate
```

and you're almost done !

you just need to create a super user account to access to the CLI !
```
heroku run python manage.py createsuperuser 
```
then enter the infos of the user

and you're done, you can visit the app at < my-heroku-app >.herokuapp.com or simply by typing ```  heroku open ``` in your terminal. :D