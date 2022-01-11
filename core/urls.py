
from django.urls import path
from .views import IndexView,IndexView, AboutView, ContactView, get_json_view, ProductsView, CategoryProductsView, ProductsView, ProductDetailView, VirementBancaireView, CarteBancaireView ,PaiementView ,PaiementEspecesView ,EchangeView ,LivraisonView ,RetourView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    #  PAIEMENT URLS
    path('virement-bancaire/', VirementBancaireView.as_view(), name='virement-bancaire'),
    path('carte-bancaire/', CarteBancaireView.as_view(), name='crte-bancaire'),
    path('paiement/', PaiementView.as_view(), name='paiement'),
    path('paiement-especes/', PaiementEspecesView.as_view(), name='paiement-especes'),


    #  Livraison URLS
    path('echange/', EchangeView.as_view(), name='echange'),
    path('livraison/', LivraisonView.as_view(), name='livraison'),
    path('retour/', RetourView.as_view(), name='retour'),


    path('contact/', ContactView.as_view(), name='contact'),
    path('produits', ProductsView.as_view(), name='products'),
    path('produits/<slug:slug>/', CategoryProductsView.as_view(), name='prod-by-cat'),
    path('produits/<slug:slug>/', CategoryProductsView.as_view(), name='prod-by-sub-cat'),
    path('produits/produit/<slug:slug>/', ProductDetailView.as_view(), name='productDetail'),

]
