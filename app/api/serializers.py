from django.contrib.auth.models import User
from rest_framework import serializers
from webapp.models import Image




class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['id', 'image', 'sign', 'users', 'created_at', 'updated_at']
