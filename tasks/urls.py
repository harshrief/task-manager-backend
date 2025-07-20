from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
from django.urls import path
from .views import (
    RegisterView,
    CategoryListCreateView, CategoryRetrieveUpdateDestroyView,
    TaskListCreateView, TaskRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    # Category routes
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    # Task routes
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]
