from django.views import generic
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.utils import timezone
from antiqueProjectApp.models import Antique, Creator, AntiqueType, AntiqueSale
from antiqueProjectApp.forms import AntiquePurchaseForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = "sk_test_cQbzKPWU5eKkAYgPecuVIcvo00D1Fr15gu"


def index(request):

    numAntiques = Antique.objects.all().count()
    numCreators = Creator.objects.count()
    numVisits = request.session.get('numVisits', 0)
    request.session['numVisits'] = numVisits + 1
    # antiqueProjectApp = Antique.objects.all

    context = {
        'numAntiques': numAntiques,
        'numCreators': numCreators,
        'numVisits': numVisits,
        'allAntiques': Antique.objects.all(),
    }

    
    return render(request, 'index.html', context=context)



class AntiqueListView(generic.ListView):
    model = Antique
    paginate_by = 12


class AntiqueDetailView(generic.DetailView):
    model = Antique


class CreatorListView(generic.ListView):
    model = Creator
    paginate_by = 12


class CreatorDetailView(generic.DetailView):
    model = Creator
    paginate_by = 12


def GetAllSales(request):
    sales = AntiqueSale.objects.order_by('-saleDate')
    return render(request, "sales_list.html", {'sales': sales})


def IndividualSaleDetails(request, pk):
    sale = get_object_or_404(AntiqueSale, pk=pk)
    return render(request, "antique_sale_detail.html", {'sale': sale})

@login_required()
def PurchaseAnItem(request, pk=None):
    sale = None
    sale = AntiqueSale()
    sale.antique = Antique.objects.get(pk=pk)
    form = AntiquePurchaseForm(instance=sale)
    return render(request, 'antique_purchase_form.html', {'form': form, 'sale': sale})

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
        return render(request, 'charge.html')



