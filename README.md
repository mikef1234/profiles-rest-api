#Profiles Rest API
REST API providing basic functionality for managing user profiless

vagrant up
vagrant ssh
workon profiles_apis
#for migrations
python manage.py makemigrations
python manage.py migrate
cd vagrant/src/profiles_projects
python manage.py createsuperuser
Email, Name, Password

django admin
python manage.py runserver 0.0.0.0:8080
go to 127.0.0.1:8080
login into the email/password you entered in before

APIView defines function uses standard http methods, GET, PosT, PUT, PATCH, Delete and the viewset. Gives you the most control over the logic. full control over logic. PRocessing files and rendering a synchronous response. Calling external API's. Access local files or data

Viewset: 
