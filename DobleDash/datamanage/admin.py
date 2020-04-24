from django.contrib import admin
from .models import Risk, CveInfo, Vendor, Product
# Register your models here.

admin.site.register(Risk)
admin.site.register(CveInfo)
#admin.site.register(Vendor)
#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor', )
    pass

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendorName', 'vendorLink', )
    pass