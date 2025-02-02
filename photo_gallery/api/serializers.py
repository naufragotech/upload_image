from rest_framework import serializers
from .models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"

    def get_photo_url(self, obj):
        request = self.context.get("request")
        photo_url = obj.fingerprint.url

        return request.build_absolute_uri(photo_url)
