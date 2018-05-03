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

Viewset-uses model operations for functions:
list, create, retrieve, update, partial update, destroy.  Takes care a lot of typical logic for you. Perfect for standard database operations. Fastest way to make a database interface. 
need a simple CRUD interface to your database. quick and simple API. need little to no customization on the logic. Working with standard data structures.

go to 127.0.0.1:8080/api/hello-view
 127.0.0.1:8080/api/profile
127.0.0.1:8080/api/profile/2
Added Name: 
input name and it will display as a post

go to api/profile, and create new user(Email, name, password)
api/profile and click filters. Search for name


