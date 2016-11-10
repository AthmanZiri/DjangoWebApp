# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class post(models.Model):
	title=models.CharField(max_length=140)
	body=models.TextField(max_length=1500)
	date=models.DateTimeField()

	def __str__(self):
		return self.title


