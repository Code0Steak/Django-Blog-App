# Django-Blog-App

## List of Commands:
Install Dango
pip install django
python -m django –version

Django Admin lists the commands that can be used to create project/app

Create New Project
django-admin startproject projectName 

Run project on default server
django manage.py runserver // python manage.py runserver

Create new app
Python manage.py startapp appName

## Django is a MVC Framework

A Typical URL Route mapper looks like this
```
urlpatterns = [
    path('',views.home, name='Blog Home')
]
```

The view file contains a route handler function called home. 
```
def home(request):
    context = {'posts' : Post.objects.all()}
    return render(request, 'Blog/BlogHome.html', context)
```

The context here is the data, but the handler can make a request to a database to retreive a model or make changes to the model.




