from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.addFoodView, name='add'),
    path('show/', views.showFoodView, name='show'),
    path('details/<int:f_id>', views.detailedFoodView, name='details'),
    path('update/<int:f_id>', views.updateFoodView, name='update'),
    path('delete/<int:f_id>', views.deleteFoodView, name='delete')
]