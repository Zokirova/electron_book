from django.shortcuts import render
from .models import HomeModels
# Create your views here.
def home(request):
    new = HomeModels.objects.all()
    context = {
        "new": new
    }
    return render(request, 'index.html', context)
