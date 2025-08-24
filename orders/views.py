from django.shortcuts import render

# Create your views here.
def about(request):
    context={"title":"about the restaurant","description":("we're serving fresh and seasonal cuisines.Real taste finds here"),}
    return render(request,"about.html",context)
