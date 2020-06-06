# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from .serializer import GetURLSerializer, UrlSerializer

# Create your views here.
class UrlShortner(APIView):
	permission_classes = (AllowAny,)
	def get(self, request):
		url_serializer = GetURLSerializer(data = request.GET)
		if url_serializer.is_valid():
			page = url_serializer.data['page']

			start_index = (page - 1) * 15
			end_index = page * 15

			urls = UrlSerializer(Urls.objects.all()[start_index:end_index])
			
			return Response({"status": True, "data": urls})
		return Response({"status": False, "reason": "page number not passed"})
