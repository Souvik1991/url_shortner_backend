# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models

# Create your models here.
class Urls(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	short_name = models.CharField(max_length = 255, db_index=True, unique=True)
	original_url = models.TextField()
	clicked = models.BigIntegerField(default=0)

	class Meta:
		db_table = 'urls'

	def __str__(self):
		return "%s" % (self.original_url)
