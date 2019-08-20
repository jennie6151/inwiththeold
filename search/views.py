from django.shortcuts import render
from antiqueProjectApp.models import Antique, Creator
from django.db.models import Q

# Create your views here.

def do_search(request):
    Creators = Creator.objects.filter(Q(CreatorName__icontains=request.GET['q']))
    Antiques = Antique.objects.filter(Q(AntiqueName__icontains=request.GET['q'])| Q(Creator__in=Creators))
    return render(request, "antique_list.html", {"antique_list": Antiques})