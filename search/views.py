from django.shortcuts import render
from antiqueProjectApp.models import Antique

# Create your views here.

def do_search(request):
    Antiques = Antique.objects.filter(AntiqueName__icontains=request.GET['q'])
    return render(request, "antique_list.html", {"antique_list": Antiques})