from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("addStudy", views.addStudy, name='addStudy'),
    path("updateStudy/<int:id>/", views.updateStudy, name='updateStudy'),
    path("viewStudy/<int:id>/", views.viewStudy, name='viewStudy'),
    path('deleteStudy/', views.deleteStudy, name='deleteStudy')
]
