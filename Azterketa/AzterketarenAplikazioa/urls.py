from django.urls import path
from . import views
urlpatterns = [
    path('', views.paziente_list, name='base'), 
    path('Paziente/list/', views.paziente_list, name='paziente_zerrenda'),
    path('Paziente/new/', views.paziente_new, name='zerrenda-paziente-new'),   
    path ('Paziente/delete/<int:id>/', views.ezabatu_paziente, name='ezabatu_paziente'),
    path('Paziente/edit/<int:id>/', views.editpaziente, name='zerrenda-paziente-edit'),
    path('Mediku/list/', views.mediku_list, name='mediku_zerrenda'),
    path('Mediku/new/', views.mediku_new, name='zerrenda-mediku-new'),
    path ('Mediku/delete/<int:id>/', views.ezabatu_mediku, name='ezabatu_mediku'),
    path('Mediku/edit/<int:id>/', views.edit_mediku, name='zerrenda-mediku-edit'),
]