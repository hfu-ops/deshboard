from django.db import models
from django.urls import reverse

# Create your models here.
class Risk(models.Model):
    """
    Risk Model represents a risk record
    """
    geneScore = models.FloatField(max_length=200, help_text='This is the general risk score of the product')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.geneScore)

class CveInfo(models.Model):
    """
    CveInfo represents a cve id and its related description
    """
    cve_id = models.CharField(max_length=200, help_text='Enter the cve_id')

    def __str__(self):
        return self.cve_id

class Vendor(models.Model):
    """
    vendor represents a company supplier
    """
    vendorName = models.CharField(max_length=200)
    vendorLink = models.URLField(max_length=200)

    def get_absolute_url(self):
        return reverse('vendor-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.vendorName


class Product(models.Model):
    """
    Product represents a product and detailed info.
    """
    name = models.CharField(max_length=200)
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_NULL, null=True)
    cve_ids = models.ManyToManyField(CveInfo, help_text='Select the cve_id for this cve_id')
    risk = models.ForeignKey('Risk', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular product.
        """
        return reverse('product-detail', args=[str(self.id)])