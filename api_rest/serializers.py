from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = School
        fields = ('id', 'name', 'address')