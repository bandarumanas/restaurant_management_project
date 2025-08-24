from django.urls import path
from .views import *

urlpatterns = [ path('homie',views.home_page,name="home")
    
]