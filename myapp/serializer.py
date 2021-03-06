from rest_framework import serializers

from posts.models import Posts
from posts.serializer import PostSerializer
from .models import Profiles
import re
from rest_framework.exceptions import ValidationError





class ProfileSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(many=True, read_only=True)
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post = PostSerializer(write_only=True)

    class Meta:
        model = Profiles
        fields = '__all__'

    def validate_phone_number(selfs, value):
        phone_number_pattern = re.compile("^09\d{9}$")
        if phone_number_pattern.match(value):
            return value

        raise ValidationError('your phone number pattern in not correct')

    def create(self, validated_data):
        posts = validated_data.pop('post')
        profile = Profiles.objects.create(**validated_data)
        my_post = Posts.objects.create(**posts, author=profile)
        return profile

# توجه شود فیلدهای که فقط خواندنی هستند در خروجی نمایش داده می شوند
# توجه کنید اسم posts باید با related_name یکی باشد توجه شود فیلد
# فقط نوشتی در خروجی نمایش داده نمی شود و فقط در ورودی دریافت می شود
# وفیلدهای معمولی هم درورودی و هم در خروجی نمایش داده می شود


