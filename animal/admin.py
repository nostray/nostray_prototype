# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Animals


class AnimalsAdmin(admin.ModelAdmin):
	pass


admin.site.register(Animals, AnimalsAdmin)