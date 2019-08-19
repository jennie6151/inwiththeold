from django.views import generic
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.utils import timezone
from antiqueProjectApp.models import Antique, Creator, AntiqueType, AntiqueSale
from antiqueProjectApp.forms import AntiquePurchaseForm, MakePaymentForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_SECRET


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

    # {"antiqueProjectApp": antiqueProjectApp})
    return render(request, 'index.html', context=context)

# def all_antiques(request):
    # all_antiques = Antique.object.all
    # return render (request, "all_antiques.html", {"all-antiques": all_antiques})


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


def GetAllSales(request):
    sales = AntiqueSale.objects.order_by('-saleDate')
    return render(request, "sales_list.html", {'sales': sales})


def IndividualSaleDetails(request, pk):
    sale = get_object_or_404(AntiqueSale, pk=pk)
    return render(request, "antique_sale_detail.html", {'sale': sale})


# def PurchaseAnItem(request, pk=None):
    # sale = None#get_object_or_404(AntiqueSale, pk=pk) if pk else None
    # if request.method == "POST":
        # form = AntiquePurchaseForm(request.POST, request.FILES, instance=sale)
        # if form.is_valid():
            # sale = form.save()
            # rediretcto stripe passing the price
            # return redirect(SaleSuccess, sale.pk)

 # else:
        # sale = AntiqueSale()
        # sale.antique = Antique(pk=pk)
        # sale.save()
        # form = AntiquePurchaseForm(instance=sale)
    # return render(request, 'antique_purchase_form.html', {'form': form, 'sale':sale})


@login_required()
def PurchaseAnItem(request, pk=None):
    sale = None  # get_object_or_404(AntiqueSale, pk=pk) if pk else None
    if request.method == "POST":
        form = AntiquePurchaseForm(request.POST, request.FILES, instance=sale)
        if form.is_valid():
            sale = form.save()
            return redirect(SaleSuccess, sale.pk)
    else:
        form = AntiquePurchaseForm(instance=sale)
    return render(request, 'antique_purchase_form.html', {'form': form})

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='GDP',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')



