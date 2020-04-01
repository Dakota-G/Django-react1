from rest_framework import serializers
from some_app.models import *

# Serializer to turn Lead Model Objects into JSON

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        