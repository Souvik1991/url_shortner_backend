# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.pagination import LimitOffsetPagination

from .models import Urls
from .serializer import UrlSerializer

from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
class UrlShortner(generics.GenericAPIView):
	permission_classes = (AllowAny,)
	serializer_class = UrlSerializer
	queryset = Urls.objects.all()

	def get(self, request):
		queryset = self.get_queryset()
		page = self.request.query_params.get('page')
		# If the page is there
		if page is not None:
			paginate_queryset = self.paginate_queryset(queryset)
			serializer = self.serializer_class(paginate_queryset, many=True)
			return self.get_paginated_response(serializer.data)

		# If the page is not present
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def post(self, request):
		serializer = UrlSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def url_redirector(request, short_code):
	try:
		url = Urls.objects.get(short_name=short_code)
		url.clicked = url.clicked + 1
		url.save()

		return redirect(url.original_url)

	except Urls.DoesNotExist:
		return HttpResponse(json.dumps({"reason":"bad"}), content_type="application/json")
		# return Response({"reason": "bad_url"}, status=status.HTTP_400_BAD_REQUEST)

