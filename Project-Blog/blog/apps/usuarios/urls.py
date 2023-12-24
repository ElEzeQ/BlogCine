from django.urls import path

# importar views
from . import views

app_name= "usuarios"

urlpatterns = [path("registro/", views.registro, name="registro")]
