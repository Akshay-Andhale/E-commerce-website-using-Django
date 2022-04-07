from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add,name = 'add'),
    path('show/', views.show,name = 'show'),
    path('update/<int:id>/', views.update_data,name = 'update_data'),

    path('addp/', views.addp,name = 'addp'),
    path('showp/', views.showp,name = 'showp'),
    path('', views.showp),
    path('updatep/<int:id>/', views.update_datap,name = 'update_datap'),
    path('details/<int:id>/', views.details,name = 'details'),
    path('recommendation/<int:id>/', views.recommendation,name = 'recommendation'),
]