# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:22:08 2021

@author: the eye informatique
"""

from django import forms
from .models import FaClerkInformation
from .department import DEPARTMENTS


class FaClerkInformationForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        # self.initial_client = kwargs.pop("initial_department")
        self.DEPT_CHOICES = [('--------', "-----Select your Department-----")]


        for dept in DEPARTMENTS:
            d_t = (dept, f'{dept} - {DEPARTMENTS[dept]}')
            self.DEPT_CHOICES.append(d_t)
            
        self.DEPT_CHOICES.append(('000', "NA - Not found in the list"))

        super(FaClerkInformationForm,self).__init__(*args,**kwargs)

        self.fields['dept_number'] = forms.ChoiceField(
                                        label='Choose Your department',
                                        choices = self.DEPT_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    class Meta:
        model = FaClerkInformation
        fields = ['name', 'dept_number', 'phone_number', 'email']
    