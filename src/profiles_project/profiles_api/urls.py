from django.conf.urls import urls
from . import views


urlpatterns = [

    url(r'^hello-view/', views.HelloApiView.as_view()),
]
