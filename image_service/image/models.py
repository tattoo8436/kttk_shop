from django.db import models

from django import forms

class ImageModel(models.Model):
    img = models.FileField(upload_to='images/%Y/%m/%d')
    productId = models.CharField(max_length=10, default='')

from django import forms

class ImageForm(forms.Form):
    img = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )