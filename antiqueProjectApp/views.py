from django.views import generic
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.utils import timezone
from antiqueProjectApp.models import Antique, Creator, AntiqueType, AntiqueSale
from antiqueProjectApp.forms import AntiquePurchaseForm, MakePaymentForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe


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

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def PurchaseAnItem(request, pk=None):
    sale = None
    if request.method == "POST":
        purchase_form = AntiquePurchaseForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if purchase_form.is_valid() and payment_form.is_valid():
            sale = purchase_form.save(commit=False)
            saleDate = timezone.now()
            sale.save()

            try:
                customer = stripe.Charge.create(
                    amount=100,#int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=MakePaymentForm.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(MakePaymentform.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        purchase_form = AntiquePurchaseForm()
    
    return render(request, "antique_purchase_form.html", {"purchase_form": purchase_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})

   



