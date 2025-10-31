from rest_framework import serializers
from .models import Voyage

class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyage
        fields = '__all__'  # This tells the serializer to include all fields from the model

