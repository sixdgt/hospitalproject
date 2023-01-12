from django.contrib import admin
from .models import Category, Hospital

# Register your models here.
class HospitalAdmin(admin.ModelAdmin):
    list_display = ("full_name", "short_name","category", "address", "contact",)
    search_fields = ("short_name", "address",)
    list_filter = ("short_name", "address",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "category_code")
    search_fields = ("category", "category_code")
    list_filter = ("category", "category_code")
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Hospital, HospitalAdmin)

admin.site.site_header = "HOSPITAL"
admin.site.index_title = "HMS"
admin.site.site_title = "Admin Panel"