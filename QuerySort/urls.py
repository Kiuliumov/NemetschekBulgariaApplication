from django.urls import path, include

from QuerySort import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', include([
        path('lector/', views.lector, name='add-lector'),
        path('data/', views.add_data, name='add-data'),
    ]
    ))
]