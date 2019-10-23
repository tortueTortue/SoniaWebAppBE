from rest_framework import serializers
from .models import *

class LayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layout
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class ModuleNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

