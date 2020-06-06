from rest_framework import serializers

from .models import Urls

class UrlSerializer(serializers.ModelSerializer):
	short_name = serializers.CharField(required=True, allow_blank=False, max_length=250)
	original_url = serializers.CharField(required=True, allow_blank=False)
	
	def create(self, validated_data):
		"""
		Create a return a new `Urls` instance, given the validated data
		"""
		try:
			return Urls.objects.create(**validated_data)
		except Exception as e:
			raise serializers.ValidationError(e)

	class Meta:
		model = Urls
		fields = ("uuid", "short_name", "original_url", "clicked")
