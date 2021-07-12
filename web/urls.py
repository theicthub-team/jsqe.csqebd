
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('profile/', editors_profile, name='profile'),
    path('board-member/', board_member, name='board_member'),
    path('manuscript/', manuscript, name='manuscript'),
    path('contact/', contact, name='contact'),
]
