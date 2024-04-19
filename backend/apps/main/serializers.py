from rest_framework import serializers
from .models import (
    Language
)


# Serializers define the API representation.
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"