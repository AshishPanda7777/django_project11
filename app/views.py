from django.shortcuts import render

# Create your views here.
def source(request):
    return render(request,'style.html')