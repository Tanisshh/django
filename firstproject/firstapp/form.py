from django import forms
from firstapp.models import Signed_User

class NewUser(forms.ModelForm):
    class Meta():
        model = Signed_User
        fields = '__all__'
        widgets = {
            'Password': forms.PasswordInput(),
        }
