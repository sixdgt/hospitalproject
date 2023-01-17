from rest_framework import serializers
from hospitals.models import Hospital, Category

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("full_name", "short_name","category", "address", "contact",)
        model = Hospital

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("category", "category_code")
        model = Category