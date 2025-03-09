from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='Posts_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='Posts_detail'),
    path('create/', views.PostCreateView.as_view(), name='Posts_create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='Posts_update'),
    path('<int:pk>/delete/', views.DeletePostView.as_view(), name='Posts_Delete'),



]
