from django.shortcuts import render # type: ignore

# Create your views here.
def first(request):
    return render(request,'first.html')
