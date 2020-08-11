from django.contrib import admin
from django.urls import path
from AppWithAsyncTask import views

urlpatterns = [
    path('async_task/', views.SampleAPI.as_view()),
]