# Django-Quiz-App

Simple quiz-app that was made on Django framework.
# Screenshots:
![alt text](https://github.com/Baesak/django-quiz-app/blob/master/pictures/quiz1.png)
![alt text](https://github.com/Baesak/django-quiz-app/blob/master/pictures/quiz2.png)
![alt text](https://github.com/Baesak/django-quiz-app/blob/master/pictures/quiz3.png)
![alt text](https://github.com/Baesak/django-quiz-app/blob/master/pictures/quiz4.png)
![alt text](https://github.com/Baesak/django-quiz-app/blob/master/pictures/quiz5.png)

# Installations:
To run this app you should have python 3 with django installed on your pc.

# Run server:
This app can be opened in local server. To do this you should write in console: `python3 manage.py runserver` and click on the link that will apear.

# Admin mode:
If you want to use admin mode, you need to create new "superuser". To do so, write in console: `python3 manage.py createsuperuser`. Then, create username and password, and login in Quiz-app. "Login" button is on top right corner.

# Managing questions:
You can add new questions in the 2 ways: 
1. From the Quiz-app: 
  To do so, click on the button "Create question". It will be on the top bar if you are logged in. Then fill out the forms that appear. You can use "Random question" button, this will fill forms automaticaly. "Random" button will not work without internet connection.
2. From the Django Admin page.

If you want to delete question, change existing question, or watch list of all questions, you can do it from Django Admin page.
To reach it, click on the "Admin mod" button on the top bar. It will also be aveliable only when user logged in.
