from django.db import models
from django.utils.text import slugify

# Create your models here.
from atributes.models import Collection, Taille, Pointure, Couleur
from django.db import models
from django.urls import reverse
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.db.models import F
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.functional import cached_property
from django.utils.html import format_html

STATUS_PRODUIT = (
    ('N', _('Nouveau')),
    ('R', _('Rupture')),
    ('P', _('Promotion')),
)

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(actif=True)

class Category(MPTTModel):
    name  = models.CharField( max_length=150, verbose_name='Nom')
    slug  = models.SlugField( max_length=150, unique= True, verbose_name='URL')
    order  = models.IntegerField(verbose_name='ordre', null=True, blank=True)
    actif = models.BooleanField(verbose_name='actif', default=True)
    icon  = models.ImageField(upload_to='images/categories', null=True, blank=True)
    photo  = models.ImageField(upload_to='images/categories', null=True, blank=True)
    # tree = models.ForeignKey(Tree, verbose_name="Branche de Catégorie",related_name="sub_categories" ,on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    objects = models.Manager()
    published = ActiveManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/produits/?category={self.id}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +'-'+str(self.id))
        return super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:prod-by-cat", args=[self.slug])

    @cached_property
    def display_image(self):
        if self.photo:
            return format_html('<img src="{}" height="150" />'.format(self.photo.url))
        return format_html('<strong>There is no image for this entry.<strong>')
        
    class Meta:
        ordering = [F('order').asc(nulls_last=True)]
        verbose_name = 'Catégorie'
        verbose_name_plural = '- Catégories'

    class MPTTMeta:
        order_insertion_by = ["name"]
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name +'-'+str(self.id))
    #     return super(Category, self).save(*args, **kwargs)



class Product(models.Model):
    name            = models.CharField( max_length=150, verbose_name='Nom')
    slug            = models.SlugField( max_length=150, unique= True, verbose_name='URL')
    category        = models.ForeignKey(Category, verbose_name="Sous Catégorie",related_name="products" ,on_delete=models.CASCADE)
    description     = tinymce_models.HTMLField(verbose_name='Déscription', blank=True, null=True)
    price           = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    old_price       = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ancien prix",blank=True, null=True)
    to_home_page    = models.BooleanField(verbose_name="Affiché dans la page d'accueil", default=False)
    order  = models.IntegerField( verbose_name='ordre', null=True, blank=True)
    stock           = models.IntegerField( default=1,  verbose_name="Stock initial",blank=True, null=True)
   
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="collections", blank=True, null=True)
    taille     = models.ManyToManyField(Taille, blank=True, related_name="tailles")
    pointure   = models.ManyToManyField(Pointure, blank=True, related_name="pointures")
    couleur    = models.ManyToManyField(Couleur, related_name="couleurs")

    actif      = models.BooleanField(verbose_name='actif', default=True)
    new        = models.BooleanField(verbose_name='Nouveau', default=True)
    top        = models.BooleanField(verbose_name='Meilleur vente', default=True)

    status     = models.CharField(choices=STATUS_PRODUIT, max_length=1, default='N', blank=True, null=True, verbose_name='Status')

 
    created = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    
    def __str__(self):
        return self.name

    @property
    def home_products(self):
        products = Product.objects.filter(to_home_page=True, actif=True)
        return products
        
    @property
    def first_image(self):
        image = None
        try:
            image = self.photos.first().fichier.url
        except:
            pass
        return image
    class Meta:
        ordering = [F('order').asc(nulls_last=True)]
        verbose_name = 'Produit'
        verbose_name_plural = '3. Produits'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +'-'+str(self.id))
        return super(Product, self).save(*args, **kwargs)    

    def get_absolute_url(self):
        return reverse("core:productDetail", args=[self.slug])

class PhotoProduct(models.Model):
    fichier   = models.ImageField(upload_to='images/produits') 
    actif   = models.BooleanField(verbose_name='actif', default=True)
    produit = models.ForeignKey(Product, related_name="photos", on_delete=models.CASCADE)



class ContactForm(models.Model):
    name        = models.CharField(verbose_name=_('Nom complet'), max_length=100)
    phone       = models.CharField(verbose_name=_("Téléphone") , max_length=25)
    email       = models.EmailField(verbose_name=_("Email"), null=True, blank = True)
    subject     = models.CharField(verbose_name=_("Sujet"), max_length=50, blank=True)
    message     = models.TextField(verbose_name=_("Message"), blank=True, null=True)
    date_sent = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)

    def __str__(self):
        return self.name


