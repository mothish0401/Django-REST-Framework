from dataclasses import field
from rest_framework import serializers

from home.models import University


class UniversitySerializer(serializers.ModelSerializer):


    class Meta:
        model= University
        fields='__all__'
        