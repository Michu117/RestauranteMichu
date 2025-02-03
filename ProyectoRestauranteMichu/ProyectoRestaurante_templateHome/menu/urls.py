from django.urls import path
from .views import categories_view, meals_view, meal_detail_view

urlpatterns = [
    path('categorias/', categories_view, name='categories'),
    path('categorias/<str:category_name>/', meals_view, name='meals_by_category'),
    path('menus/<str:meal_id>/', meal_detail_view, name='meal_detail'),
]
