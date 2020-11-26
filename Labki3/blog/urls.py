from django.urls import path
from . import views

from .views import SignUpView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('signup/', SignUpView.as_view(), name='signup'),
]