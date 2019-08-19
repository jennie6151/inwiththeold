from django.shortcuts import render
from antiqueProjectApp.models import Antique

# Create your views here.

def do_search(request):
    Antiques = Antique.objects.filter(name__icontains=request.GET['q'])
    return render(request, "antique_list.html", {"Antiques": Antiques})