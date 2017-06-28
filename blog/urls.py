from django.conf.urls import include, url #Importa as urls do Django
from . import views #Importa os view

urlpatterns = [
    url(r'^$', views.post_list),
]