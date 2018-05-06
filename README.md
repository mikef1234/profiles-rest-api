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

runserver again if needed

go to /api/ 
login api is added, and click link
type in your email and password. It will come
back with a token number. Copy that token number.
Add Token to the Mod Header next to the word
Token 
go to api/profile/1/ and update content
Turn on off the authorization check box to test

#Create and run model migration
go to vagrant server and/or run
python manage.py makemigrations
python manage.py migrate

api/feed make a Status text for a created_on 
after pressing post
Video 57 or 58? for new token

#Pushing Project to Github
ssh-keygen
enter, enter
copy the public key location path
go to the location path on sublime
go to github, and then settings, SSH and GPG Keys. New SSH.
Put a title, and paste the contents from the id_rsa.pub file



JOBBBB
onet_jo_similarity.py for Client Pipeline
Future of work
future of work
project or 
data reprocessing, take a look- taking model results and manipulating the clients information, jobs/etc
proprietary folder - matches the jobs, doing the analyzes, steps to get to model output, modeling scripts

onet_jo_similarity.py for Client Pipeline, and onet_keyword_classification needs to cleaned up

from api.models import *

onet_jobs is a pickle file, that contains a massive python object for all onet jobs and attributes and 
values. Usable format compared to DB or mirror. Possible convert table in POSTGRES

Reference each clients schema...schema = "client"