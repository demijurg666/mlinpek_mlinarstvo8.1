from django.contrib import admin
from .models import *
#from modeltranslation.admin import TranslationAdmin


#class ProductAdmin(TranslationAdmin):
 #   model = Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Izdavastvo)
admin.site.register(proizvodnjaPsenicnogBrasnaInfo)
admin.site.register(Kurs)
admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(Video)
