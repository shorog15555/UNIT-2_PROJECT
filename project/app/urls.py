from django.urls import path
from . import views
app_name="app"


urlpatterns = [
path("project/aboutMe/", views.aboutMe, name="aboutMe"),
path("project/hello/", views.hello, name="hello"),
path("", views.hello, name="hello_page"),
path("project/SitesDesign/", views.SitesDesign, name="SitesDesign"),
path("project/sports/", views.sports, name="sports"),
path("project/TryToBeCalm/", views.TryToBeCalm, name="TryToBeCalm"),
]
 