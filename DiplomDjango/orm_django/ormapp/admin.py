from django.contrib import admin
from .models import UserProfile


# Register your models here.

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'age')
    search_fields = ('username', 'lastname',)
    list_filter = ('firstname', 'lastname', 'age')

    readonly_fields = ('created_at',)


