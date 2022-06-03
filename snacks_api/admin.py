from django.contrib import admin
from .models import Snack

@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    list_display = ('title', 'calories', 'owner')
    list_filter = ('owner', 'updated_at')
    search_fields = ('title', 'owner', 'id')
