from django.contrib import admin
from .models import Tasklist
# Register your models here.

class TastListAdmin(admin.ModelAdmin):
    list_filter = ('done',)

admin.site.register(Tasklist, TastListAdmin)