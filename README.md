# RDT-Django-round

Steps for running the project

1.Go to project folder
2.Virtual environment can be activated by this command
source venv/bin/activate
3.Go to the manage.py location in the project 
4.run the command
python manage.py runserver
5.Take the url in webbrowser
http://127.0.0.1:8000/analysis/
6.When we click on any item, It will display stockprice list as well as top 5 volumes of that particular item


Steps for creation of the project

1.Create project folder
2.Go to the project folder path in terminal
3.Create the python virtual environment using the virtualenv utility by the command
virtualenv venv
4.Activate that environment by the command
source venv/bin/activate
5.Install django using the command
pip install Django==1.11.3
6.run the command in terminal
pip install pytz==2017.2
7.Create django project in virtual environment 
django-admin startproject stocks
8.To create an app
python manage.py startapp analysis
9.Add models and sqlite3 db in project
10.Add necessary logic in views
11.run the project using
python manage.py runserver