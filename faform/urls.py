# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:13:45 2021

@author: the eye informatique
"""

from django.urls import path
from .views import clerk, download

urlpatterns = [
    path('', clerk, name='clerk'),
    path('download-file', download, name='download'),
]