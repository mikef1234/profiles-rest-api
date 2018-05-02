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