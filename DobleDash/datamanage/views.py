from django.shortcuts import render
from .models import Risk, CveInfo, Vendor, Product
from django.views import generic

# Create your views here.

def index(request):
    """
    View Function for Home Page of site
    """
    num_products = Product.objects.all().count()
    num_Vendors = Vendor.objects.all().count()
    num_Cve = CveInfo.objects.all().count()

    context={
            'num_products': num_products, 'num_Vendors':num_Vendors, 'num_Cve': num_Cve,
        }

    return render(
        request,
        'index.html',
        context= context
    )

class ProductListView(generic.ListView):
    """Generic class-based view for a list of products."""
    model = Product
    paginate_by = 10

class ProductDetailView(generic.DetailView):
    model = Product

class VendorListView(generic.ListView):
    model = Vendor
    paginate_by = 10

class VendorDetailView(generic.DetailView):
    model = Vendor
    