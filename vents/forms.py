from django import forms
from .models import Vents

class VentForm(forms.ModelForm):

    title = forms.CharField(label='Vent Title', widget=forms.TextInput(attrs={
        'class': 'w-full bg-transparent border-none focus:ring-0 text-deep-forest-950 font-[Inter] text-lg resize-none placeholder:text-lavender-grey-300', 'placeholder': 'Title Here'
    }))

    class Meta:
        model = Vents
        fields = ['title', 'content', 'category', 'mood', 'tension_level', 'is_anonymous']

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full bg-transparent border-none focus:ring-0 text-deep-forest-950 font-[Inter] text-lg resize-none min-h-[50px] placeholder:text-lavender-grey-300', 'placeholder': 'What\'s stressing you right now? Don\'t hold back', 'rows': '3',
            }),
            'category': forms.Select(attrs={
                'class': 'w-full bg-transparent border-none focus:ring-0 text-deep-forest-950 font-[Inter] text-lg resize-none',
            }, choices=['', 'Select any Category'] + Vents.CATEGORY_CHOICES),
            'mood': forms.Select(attrs={
                'class': 'w-full bg-transparent border-none focus:ring-0 text-deep-forest-950 font-[Inter] text-lg resize-none',
            }, choices=['', 'Select any Mood'] + Vents.MOOD_CHOICES),
            'tension_level': forms.NumberInput(attrs={
                'placeholder': 'Enter any number from 1-100',
                'min': '1',
                'max': '100',
                'type': 'range',
                'class': 'w-full bg-transparent px-4 py-3 text-deep-forest-950 outline-none placeholder:text-lavender-grey-300 font-[inter] text-sm'
            }),
            'is_anonymous': forms.CheckboxInput(attrs={
                'class': 'peer sr-only'
            }),
        }