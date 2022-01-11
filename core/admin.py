from django.contrib import admin
from .models import Product, Category, PhotoProduct, ContactForm
from django.contrib.auth.models import Group, User
from django.utils.html import format_html
from django_mptt_admin.admin import DjangoMpttAdmin
from import_export import resources
from django.forms import ModelForm, Textarea
from django.contrib.admin import SimpleListFilter
from mptt.admin import DraggableMPTTAdmin

from import_export.admin import ImportExportModelAdmin

admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.site.unregister(Group)




class CategoryAdmin(DjangoMpttAdmin):

    list_display = ('id', 'name', 'order','actif')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name')
    list_per_page = 40
    list_editable = ['order','actif']
    search_fields = ('id', 'name',)
    exlude = ['slug']
    readonly_fields = ('display_image',)

class PhotosLinesAdmin(admin.TabularInline):
    def image_tag(self):
        return format_html('<img src="{}" height="150"  />'.format(self.fichier.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    model = PhotoProduct
    readonly_fields= (image_tag,)
    extra = 1
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        # exclude = ('confirmer',)
        # widget = ManyToManyWidget(Country, field='name')
        fields = ('id', 'name', 'price', 'reference','category','text','old_price','brand','specifications')
        export_product = ('id', 'name', 'price', 'reference','category','text','old_price','brand','specifications')



class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        widgets = {
            'meta': Textarea(attrs={'cols': 80, 'rows': 2}),
        }


class HasImages(SimpleListFilter):
    title = "Photos" 
    parameter_name = "pic"
        # return Product.objects.filter(photos=True)

    def lookups(self, request, model_admin):
        return (
            ('true', 'Avec Photos'),
            ('false', 'Sans Photos')
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'true':
            products = Product.objects.filter(photos__isnull=False).distinct()
            print('products' , products)
            return products
        elif self.value().lower() == 'false':
            return Product.objects.filter(photos__isnull=True)


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'old_price',  'price', 'new', 'top','to_home_page', 'actif', 'stock','status')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name' )
    list_per_page = 40
    list_filter = ('category',HasImages ,'new')
    list_editable = ['category', 'price','to_home_page', 'new', 'top', 'actif', 'old_price', 'stock','status']
    search_fields = ('name','reference')
    # exclude  = ['reference']
    save_as= True
    resource_class = ProductResource
    form = ProductModelForm
    inlines = [PhotosLinesAdmin]# a comenter pour KAHRABACENTER.com




# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name',  'old_price','price', 'new', 'top', 'actif', 'collection', 'status')
#     prepopulated_fields = {"slug": ("name",)}
#     list_display_links = ('id','name' )
#     list_per_page = 40
#     list_filter = ('name', 'new')
#     list_editable = [ 'price', 'new', 'top', 'actif','collection', 'old_price', 'status']
#     search_fields = ('name',)
#     exlude = ['slug']
#     save_as= True


# Contact
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'subject', 'date_sent')
    list_display_links = ('id',)
    list_per_page = 40
    list_filter = ('name', 'phone', 'email',)
    search_fields = ('id', 'phone', 'email')


admin.site.register(Category, DraggableMPTTAdmin,list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),)

admin.site.register(Product, ProductAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
