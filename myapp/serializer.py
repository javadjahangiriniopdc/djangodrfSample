from rest_framework import serializers
from .models import Profiles
import re
from rest_framework.exceptions import ValidationError


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'

    def validate_phone_number(selfs, value):
        phone_number_pattern = re.compile("^09\d{9}$")
        if phone_number_pattern.match(value):
            return value

        raise ValidationError('your phone number pattern in not correct')
