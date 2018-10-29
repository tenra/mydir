from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('article/create/', views.CreateView.as_view(), name='create'),
    path('article/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('article/<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('article/<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('article/help/', views.help, name='help'),
]
