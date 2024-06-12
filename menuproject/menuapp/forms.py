from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

        label = {
            'item_name' : 'Name',
            'item_desc' : 'Description',
            'item_price': 'Price',
            'item_image' : 'Image'
        }

        widgets = {
            'item_name' : forms.TextInput(attrs={'placeholder':'Eg: Chicken Lasagna'}),
            'item_desc' : forms.TextInput(attrs={'placeholder':'Eg: Chicken, cheese, bread'}),
            'item_price' : forms.NumberInput(attrs={'placeholder':'Eg: 500'}),
            'item_image' : forms.TextInput(attrs={'placeholder':'Eg: Enter Image URL'})
        }