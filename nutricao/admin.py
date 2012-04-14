#!/usr/bin/env python

from django.contrib import admin

from models import Dieta
from models import TipoDieta

admin.site.register(Dieta)
admin.site.register(TipoDieta)