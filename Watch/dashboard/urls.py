
from django.urls import path
from . import views 


urlpatterns = [
    path('d_home', views.d_home, name="d_home"),
    path('d_catalog', views.d_catalog, name="d_catalog"),
    path('d_user', views.d_user, name="d_user"),

]
