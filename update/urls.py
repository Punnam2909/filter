from django.urls import path
from .views import add

urlpatterns=[
    path("update/",add,name="add"),
]