from django.urls import path
from .views import HomeView, DetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),

]
