from django import forms

from gallery.models import Photo


class PhotoForm(forms.ModelForm):
    title = forms.CharField()
    subtitle = forms.CharField()
    date = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = Photo
        fields = [
            'title',
            'subtitle',
            'date',
            'image',
        ]
