from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):

    username = forms.CharField(max_length=150, required=True, label='Username', widget=forms.TextInput(attrs={
        'class': 'w-full bg-lavender-grey-50 text-deep-forest-950 px-4 py-3.5 rounded-xl border-2 border-transparent focus:border-sage-500 focus:bg-white outline-none transition-all placeholder:text-lavender-grey-400 font-[inter]', 'placeholder': 'johndoe123'
    }))

    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={
        'class': 'w-full bg-lavender-grey-50 text-deep-forest-950 px-4 py-3.5 rounded-xl border-2 border-transparent focus:border-sage-500 focus:bg-white outline-none transition-all placeholder:text-lavender-grey-400 font-[inter]', 'placeholder': '********'
    }))

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class' : 'w-full bg-transparent border-none px-6 py-4 text-deep-forest-950 placeholder:text-lavender-grey-300 focus:ring-0 outline-none font-[inter]', 'placeholder' : '********'
        }
    ))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class' : 'w-full bg-transparent border-none px-6 py-4 text-deep-forest-950 placeholder:text-lavender-grey-300 focus:ring-0 outline-none font-[inter]', 'placeholder' : 'Password again'
        }
    ))

    fullname = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={
        'class': 'w-full bg-transparent border-none px-6 py-4 text-deep-forest-950 placeholder:text-lavender-grey-300 focus:ring-0 outline-none font-[inter]', 'placeholder': 'John Doe'
    }))

    username = forms.CharField(required=True, max_length=200, widget=forms.TextInput(attrs={
        'class': 'w-full bg-transparent border-none px-6 py-4 text-deep-forest-950 placeholder:text-lavender-grey-300 focus:ring-0 outline-none font-[inter]', 'placeholder': 'johndoe123'
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full bg-transparent border-none px-6 py-4 text-deep-forest-950 placeholder:text-lavender-grey-300 focus:ring-0 outline-none font-[inter]'
            })

        self.fields['email'].widget.attrs['placeholder'] = 'johndoe@mail.com'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 
        # We can't have fullname in Meta because it doesn't come from django by default


        # Because we are having fullname which doesn't come with django by default, we'll have to have a save function to handle saving the fullname manually
    def save(self, commit=True):
        user = super().save(commit=False)

        user.fullname = self.cleaned_data['fullname']
        # parts = fullname.split()

        # user.first_name = parts[0]
        # user.last_name = " ".join(parts[1]) if len(parts) > 1 else ""
        if commit:
            user.save()
        return user