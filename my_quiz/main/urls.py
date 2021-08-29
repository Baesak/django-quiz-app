from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='main/home.html'), name='home'),
    path('quiz', views.Quiz.as_view(), name='quiz'),
    path('new-quest', views.NewQuest.as_view(), name='new-quest'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('result/<int:correct>', TemplateView.as_view(template_name='main/result.html'), name='result'),
]
