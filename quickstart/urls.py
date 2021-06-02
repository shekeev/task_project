from django.urls import path
from . import views
urlpatterns = [
    path('',views.api_overview_links),
    path('users/<int:pk>/', views.UserViewSet.as_view()),
    path('groups/' , views.GroupViewSet.as_view())
]