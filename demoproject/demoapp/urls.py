from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('register_model/', views.register_model),
    path('table/', views.table),
    path('update_register/<int:id>/', views.update_register),
    path('delete_register/<int:id>/', views.delete_register),
    path('first_data/',views.first_data),
    path('last_data/', views.last_data),
    path('age_calculation/', views.age_calculation),
    path('age_calculate_18/', views.age_calculate_18),
    path('product_details/', views.product_details),
    path('login/', views.login)

    ]