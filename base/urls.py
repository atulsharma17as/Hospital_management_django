from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.add_patient, name='add_patient'),
    path('search', views.search, name='search'),
    path('read', views.read, name='read'),
    path('update/<int:s_id>',views.update,name='update'),
    path('deletE/<int:s_id>',views.deleting,name='deleting'),

]