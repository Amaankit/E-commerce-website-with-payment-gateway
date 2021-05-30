from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.
from .models import Product,Cart,OrderPlaced,UserProfile
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= [field.name for field in Product._meta.fields ]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display= [field.name for field in Cart._meta.fields ]

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
        list_display= [field.name for field in OrderPlaced._meta.fields ]
        list_display.append('customerInfo')
        list_display.append('productInfo')
        #show customer details in admin panel
        def customerInfo(self,obj):
            link=reverse("admin:app_userprofile_change",args=[obj.userprofile.pk])
            return format_html('<a href="{}">{}</a>',link,obj.userprofile.name)
        #show product details in admin panel
        def productInfo(self,obj):
            link=reverse("admin:app_product_change",args=[obj.product.pk])
            return format_html('<a href="{}">{}</a>',link,obj.product.title)

@admin.register(UserProfile)
class OrderPlacedAdmin(admin.ModelAdmin):
        list_display= [field.name for field in UserProfile._meta.fields ]