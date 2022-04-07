from django.contrib import admin
from . models import User,Product
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','address')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('shape','size','location','price')