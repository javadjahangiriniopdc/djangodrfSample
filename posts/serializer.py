from rest_framework import serializers

from posts.models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
        extra_kwargs = {'author': {'required': False}}
