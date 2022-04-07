
from django import forms
from .models import User,Product

class UserReg(forms.ModelForm):
    class Meta :
        model = User
        fields = '__all__'


class ProdReg(forms.ModelForm):
    class Meta :
        model = Product
        fields = '__all__'     