from django import forms
from . import models , parser_litmarket

class LitmarketForms(forms.Form):
    MEDIA_CHOICES = (
        ('litmarket' , 'litmarket'),
        ('ts' , 'ts'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'litmarket':
            file_litmarket = parser_litmarket.parsing()
            for i in file_litmarket:
                models.LitmarketParser.objects.create(**i)