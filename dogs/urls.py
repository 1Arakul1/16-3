from django.urls import path
from . import views

app_name = 'dogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('breeds/', views.breeds, name='breeds'),
    path('dogs/', views.dogs_list, name='dogs_list'),
    path('dogs/create/', views.dog_create, name='dog_create'),
    path('dogs/<int:pk>/', views.dog_read, name='dog_read'),  # URL для чтения информации о собаке
    path('dogs/<int:pk>/update/', views.dog_update, name='dog_update'),  # URL для обновления информации о собаке
    path('dogs/<int:pk>/delete/', views.dog_delete, name='dog_delete'),  # Добавляем URL для удаления собаки
]