from django import forms
from models import Data, JSONModel, JSONModel_Tram

class DataForm(forms.ModelForm):

    class Meta:
        model = Data
	fields = '__all__'

class JSONModelForm(forms.ModelForm):

    class Meta:
        model = JSONModel
	fields = '__all__'		
class JSONModel_Tram_Form(forms.ModelForm):

    class Meta:
        model = JSONModel_Tram		
	fields = '__all__'
