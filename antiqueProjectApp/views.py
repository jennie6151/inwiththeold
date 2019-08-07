from django.shortcuts import render, HttpResponse

# Create your views here.

from antiqueProjectApp.models import Antique, Creator, AntiqueType

def index(request):

    numAntiques = Antique.objects.all().count()
    numCreators = Creator.objects.count()
    
    context = {
        'numAntiques': numAntiques,
        'numCreators': numCreators,
    }

    return render(request, 'index.html', context=context)

from django.views import generic

class AntiqueListView(generic.ListView):
    model = Antique

class AntiqueDetailView(generic.DetailView):
    model = Antique

class AntiqueListView(generic.ListView):
    model = Antique
    paginate_by = 2