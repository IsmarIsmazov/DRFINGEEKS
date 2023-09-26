from django.urls import path
from .views import posts_view, posts_detail_view

urlpatterns = [
    path('', posts_view),
    path('<int:pk>', posts_detail_view),
]
