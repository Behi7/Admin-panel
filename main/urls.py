from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('keldi/<int:id>', views.createVisit, name='createvisit'),

]