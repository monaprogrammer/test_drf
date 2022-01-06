from django.urls import path, include
from . import views


app_name = 'contact'

urlpatterns = [

    path('', views.ShowContacts.as_view()),
    path('add/<int:pk>/', views.AddContacts.as_view())

]