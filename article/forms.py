from django import forms
from models import Article, File_Upload, Tram_File_Upload

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
	fields = '__all__' # Or a list of the fields that you want to include in your form


class File_UploadForm(forms.ModelForm):

    class Meta:
        model = File_Upload
	fields = '__all__'	
		
class Tram_File_UploadForm(forms.ModelForm):

    class Meta:
        model = Tram_File_Upload		
	fields = '__all__'
