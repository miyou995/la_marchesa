from django.db import models
from tinymce import models as tinymce_models
from django.utils.html import format_html
# from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
# Create your models here.
# from django.db.models.signals import pre_init
from solo.models import SingletonModel
from django.db.models import F

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(actif=True)



class Business(SingletonModel):
    name        = models.CharField(verbose_name="Nom de l'entreprise", max_length=100)
    logo        = models.ImageField(upload_to='images/logos', verbose_name='Logo')
    logo_negatif= models.ImageField(upload_to='images/slides', verbose_name="Logo négatif")
    title       = models.CharField(verbose_name="Titre", max_length=50, blank=True)
    adress      = models.CharField(verbose_name="Adresse", max_length=50, blank=True)
    email       = models.EmailField(verbose_name="email de l'entreprise", max_length=50, blank=True)
    email2      = models.EmailField(verbose_name="2eme email de l'entreprise", max_length=50, blank=True)
    phone       = models.CharField(verbose_name="numéro de téléphone de l'entreprise", max_length=50, blank=True)
    phone2      = models.CharField(verbose_name="2eme numéro de téléphone de l'entreprise", max_length=50, blank=True)
    about       = tinymce_models.HTMLField(verbose_name='Text a propos', blank=True, null=True)
    mini_about  = models.TextField(verbose_name="Petit texte a propos de l'entreprise ( bas de page)", blank=True, null=True)
    about_photo = models.ImageField(verbose_name="Photo A propos 440 X 275 px", upload_to='slides/', blank=True, null=True)
    facebook    = models.URLField(verbose_name="Lien page Facebook", max_length=300, blank=True, null=True)
    insta       = models.URLField(verbose_name="Lien page Instagram", max_length=300, blank=True, null=True)
    twitter     = models.URLField(verbose_name="Lien Compte Twitter", max_length=300, blank=True, null=True)
    google_plus = models.URLField(verbose_name="Lien Compte Google plus", max_length=300, blank=True, null=True)
    youtube     = models.URLField(verbose_name="Lien Chaine Youtube", max_length=300, blank=True, null=True)
    chat_code   = models.TextField(verbose_name="Script messagerie instantané", blank=True, null=True)
    pixel       = models.TextField(verbose_name="Script Facebook pixel", blank=True, null=True)
    analytics   = models.TextField(verbose_name="Script Analytics", blank=True, null=True)
    contact_message = models.TextField(verbose_name="Contact message", blank=True, null=True)
    google_maps = models.TextField(verbose_name="iframe google maps", blank=True, null=True)
    # actif  = models.BooleanField(verbose_name='Active', default=False)
    # is_big  = models.BooleanField(verbose_name='Grande photo (1920 x 570)', default=False)
    # is_small  = models.BooleanField(verbose_name='Medium photo (720 x 540)', default=False)

    def image_tag(self):
        return format_html('<img src="{}" height="150"  />'.format(self.logo.url))
    image_tag.allow_tags = True
    class Meta:
        verbose_name = ' Infomation'
        verbose_name_plural = ' Infomations'

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Vous ne pouvez pas rajouter d'entreprise")


class Media(models.Model):
    PAGE= [
        ('HO', 'Home page'),
        ('AB', 'About page'),
        ('CN', 'Contact page'),
    ]
    big_slide = models.ImageField(upload_to='images/slides', height_field=None, width_field=None, max_length=None, verbose_name='URL image ')
    order = models.IntegerField(verbose_name='Ordre de la photo',blank=True, null=True )
    actif  = models.BooleanField(verbose_name='Active', default=False)
    is_big  = models.BooleanField(verbose_name='Grande photo Home (1920 x 570) / About (1900 x 240)', default=False)
    is_small  = models.BooleanField(verbose_name='Medium photo (720 x 540)', default=False)
    page  = models.CharField(verbose_name='page de la photo', choices=PAGE,max_length=2,default='HO')
    objects = models.Manager()
    published = ActiveManager()
    class Meta:
        ordering = [F('order').asc(nulls_last=True)]
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'