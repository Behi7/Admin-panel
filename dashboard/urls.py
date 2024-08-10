from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboards'),
    path('xodimlar', views.table, name='table'),
    path('yoqlama', views.vizit, name='vizit'),
    path('kirish', views.login_user, name='login'),
    path('chiqish', views.log_out, name='logout'),
    path('yangilsh/<int:id>', views.update, name='update'),
    path('qoshish', views.create, name = 'create'),
    path('ochirish/<int:id>', views.delete, name='delete'),
    path('profil', views.change_password, name='userupdate'),
]