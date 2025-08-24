from django.shortcuts import render

# Create your views here.
def home_page(request):
    restaurant_name="Oy! Ramen"
    return render(request,"home.html",{"restaurant_name":Oy! Ramen})

