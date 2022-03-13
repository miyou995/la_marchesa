from django.contrib.sitemaps import Sitemap
from .models import Product, Category
from django.urls import reverse


class ProductSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9
    
    def items(self):
        return Product.objects.filter(actif=True)

    def lastmod(self, obj):
        return obj.updated



class CategorySitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9
    
    def items(self):
        return Category.objects.filter(actif=True)

    def lastmod(self, obj):
        return obj.updated




class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['core:index', "core:about", "core:virement-bancaire", "core:paiement-especes", "core:echange", "core:livraison", "core:retour", "core:contact" ]

    def location(self, item):
        return reverse(item)
 