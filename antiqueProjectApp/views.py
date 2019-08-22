from django.views import generic
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.utils import timezone
from antiqueProjectApp.models import Antique, Creator, AntiqueType, AntiqueSale
from antiqueProjectApp.forms import AntiquePurchaseForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_SECRET


def index(request):

    numAntiques = Antique.objects.all().count()
    numCreators = Creator.objects.count()
    numVisits = request.session.get('numVisits', 0)
    request.session['numVisits'] = numVisits + 1

    context = {
        'numAntiques': numAntiques,
        'numCreators': numCreators,
        'numVisits': numVisits,
        'allAntiques': Antique.objects.all().order_by('AntiqueName')
    }

    
    return render(request, 'index.html', context=context)


#This generates the antiques list page
class AntiqueListView(generic.ListView):
    model = Antique
    paginate_by = 12

#This generates the antiques detail page
class AntiqueDetailView(generic.DetailView):
    model = Antique

#This generates the creators list page
class CreatorListView(generic.ListView):
    model = Creator
    paginate_by = 12

#This generates the creators detail page
class CreatorDetailView(generic.DetailView):
    model = Creator
    paginate_by = 12

#To get the Purchase form on the screen. A user must be logged in to purchase.
@login_required()
def PurchaseAnItem(request, pk=None):
    sale = None
    sale = AntiqueSale()
    sale.antique = Antique.objects.get(pk=pk)
    form = AntiquePurchaseForm(instance=sale)
    key  = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'antique_purchase_form.html', {'form': form, 'sale': sale,'key':key})

#To process the payment.
@login_required()
def charge(request):
    sale = None
    if request.method == 'POST':
        form = AntiquePurchaseForm(request.POST, request.FILES, instance=sale)
        if form.is_valid():
            sale = form.save()
            sale.stripeId=request.POST['stripeToken']
            sale.save()
        charge = stripe.Charge.create(
            amount=int(sale.antique.Price * 100),
            currency='gbp',
            description='In with the old payment',
            source=request.POST['stripeToken'],
            
        )
        return render(request, 'charge.html', {'sale': sale})



