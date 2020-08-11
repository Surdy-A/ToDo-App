from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
	path('', views.index, name="list"),
	path('home/', HomePageView.as_view(), name="home"),

	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
]