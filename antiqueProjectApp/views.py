from django.views import generic
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.utils import timezone
from antiqueProjectApp.models import Antique, Creator, AntiqueType, AntiqueSale
from antiqueProjectApp.forms import AntiquePurchaseForm


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
    return render(request, "salesList.html", {'sales': sales})


def IndividualSaleDetails(request, pk):
    sale = get_object_or_404(AntiqueSale, pk=pk)
    return render(request, "antiqueSaleDetail.html", {'sale': sale})


def PurchaseAnItem(request, pk=None):
    sale = get_object_or_404(AntiqueSale, pk=pk) if pk else None
    if request.method == "POST":
        form = AntiquePurchaseForm(request.POST, request.FILES, instance=sale)
        if form.is_valid():
            sale = form.save()
            return redirect(SaleSuccess, sale.pk)
    else:
        form = AntiquePurchaseForm(instance=sale)
    return render(request, 'antiquePurchaseForm.html', {'form': form})
