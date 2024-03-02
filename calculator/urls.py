from django.urls import path

from calculator import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_data', views.submit_data, name='submit_data')
]