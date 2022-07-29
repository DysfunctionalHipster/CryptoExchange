from django.contrib import admin
from . import models


# Register your models here.

class WireAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'owner', 'withdrawal')

admin.site.register(models.Wire, WireAdmin)