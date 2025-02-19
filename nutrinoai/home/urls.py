from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name="index"),
    path('mental-health/', views.mentalHealth, name="mental-health"),
    path('nutritionist/', views.nutritionist, name="nutritionist"),
    path("chatbot/", views.chatbot, name="chatbot"),
    path("team/", views.team, name="team"),
    path("nutritionist/calorie/", views.calorie, name="calorie"),
    # path('sem/<int:sem>', views.semester, name="semester"), slug
]
urlpatterns += staticfiles_urlpatterns()
