from hospitals.models import Hospital, Category
from django import forms

class HospitalCreateForm(forms.ModelForm):
    class Meta:
        fields = ("full_name", "short_name","category", "address", "contact",)
        model = Hospital

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        fields = ("category", "category_code")
        model = Category