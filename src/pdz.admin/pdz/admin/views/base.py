#coding: utf-8
from django.contrib.admin import ModelAdmin
from django.views.generic import View


class BaseAdminView(View):
    opts = ModelAdmin


