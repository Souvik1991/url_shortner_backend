from rest_framework import serializers

from .models import Urls

class GetURLSerializer(serializers.Serializer):
	page = serializers.IntegerField(required = True)


class UrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Urls
		fields = ['uuid', 'short_name', 'original_url']