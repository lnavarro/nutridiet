#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models

class Dieta(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_dieta')
    nome = models.CharField(verbose_name=u'Nome', max_length=45, null=False)
    descricao = models.CharField(verbose_name=u'descricao', max_length=200, null=False)
    calorias = models.FloatField(verbose_name=u'Calorias', blank=False)
    carboidratos = models.FloatField(verbose_name=u'Carboidratos', blank=False)
    gorduras = models.FloatField(verbose_name=u'Gorduras', blank=False)
    proteinas = models.FloatField(verbose_name=u'Proteinas', blank=False)
    fibra_alimentar = models.FloatField(verbose_name=u'Fibra alimentar', blank=False)
    sodio = models.FloatField(verbose_name=u'Sódio', blank=False)
    calcio = models.FloatField(verbose_name=u'Cálcio', blank=False)
    pontos = models.FloatField(verbose_name=u'Pontos', blank=False)
    tipo_dieta = models.ForeignKey('TipoDieta', db_column='id_tipo_dieta', null=False, blank=False)

    class Meta:
        db_table = 'dieta'



class TipoDieta(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_tipo_dieta')
    nome = models.CharField(verbose_name=u'Nome', max_length=45, null=False)
    descricao = models.CharField(verbose_name=u'descricao', max_length=200, null=False)

    class Meta:
        db_table = 'tipo_dieta'