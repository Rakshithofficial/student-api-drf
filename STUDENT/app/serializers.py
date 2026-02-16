from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    def validate_age(self, value):
        if value <= 5:
            raise serializers.ValidationError("Age must be greater than 5")
        return value

    class Meta:
        model = Student
        fields = '__all__'
