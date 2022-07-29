from django.contrib import admin
from . import models


# Register your models here.

class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'quantity', 'open_price', 'close_price')

admin.site.register(models.Trade, TradeAdmin)