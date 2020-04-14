from django import forms
from . models import JoinTeamMessages


class MessageCreationForm(forms.ModelForm):
    class Meta:
        model = JoinTeamMessages
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'name'}),
            'surname': forms.TextInput(attrs={'class':'form-control', 'id':'surname'}),
            'age': forms.NumberInput(attrs={'class':'form-control', 'value':14, 'min':11, 'max':25, 'id':'age'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':12, 'id':'desc'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'type':'tel', 'id':'phone', "onchange":"validatePhone();"}),
            'email': forms.TextInput(attrs={'class':'form-control', 'type':'email', 'id':'email', "onchange":"validateEmail();"}),
        }
        