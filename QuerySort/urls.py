from django.urls import path, include

from QuerySort import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new-data', views.new_data, name='new-data'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
