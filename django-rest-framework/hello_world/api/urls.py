from django.urls import path
from . import views


urlpatterns = [
    path('api/hello-world/', views.HelloWorldAPIView.as_view(), name='hello_world'),
]
