from django.contrib import admin
from .models import Stockpile,BlendSession


class ItemInline(admin.TabularInline):
    model = Stockpile
'''

@admin.register(Stockpile)
class Item_Admin(admin.ModelAdmin):
    list_display = ('pile_number','rockdescription','kWMT','ni_grade','fe_grade')
'''   
@admin.register(BlendSession)
class Item_Admin(admin.ModelAdmin):
    list_display = ('session_id','blend_date')
    inlines = [ItemInline]
# Register your models here.
