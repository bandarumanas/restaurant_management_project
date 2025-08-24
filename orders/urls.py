from django.urls import path
from .views import *

urlpatterns = [path("restdesc/",views.about,name="about")
    
]