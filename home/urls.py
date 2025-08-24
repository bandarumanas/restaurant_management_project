from django.urls import path
from .views import home_page

urlpatterns = [ path('homie',views.home_page,name="home"),
    

]
