from django  import forms
from . models import Product,Category

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("name",'descr','price','category','image','available','stock')
    # category = forms.ModelChoiceField(queryset=Category.objects.all())
