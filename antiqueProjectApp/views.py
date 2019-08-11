from django.shortcuts import render, HttpResponse

# Create your views here.

from antiqueProjectApp.models import Antique, Creator, AntiqueType

def index(request):

    numAntiques = Antique.objects.all().count()
    numCreators = Creator.objects.count()

    numVisits = request.session.get('numVisits', 0)
    request.session['numVisits'] = numVisits + 1
    
    context = {
        'numAntiques': numAntiques,
        'numCreators': numCreators,
        'numVisits': numVisits,
    }

    return render(request, 'index.html', context=context)

from django.views import generic

class AntiqueListView(generic.ListView):
    model = Antique
    paginate_by = 2

class AntiqueDetailView(generic.DetailView):
    model = Antique

class CreatorListView(generic.ListView):
    model = Creator
    paginate_by = 2

class CreatorDetailView(generic.DetailView):
    model = Creator
    paginate_by = 2
