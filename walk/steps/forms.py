""" Steps form module """
from django import forms
from . models import Target


class GoalsForm(forms.Form):
    """ Creates the Goal form for taking users weekly step goals """
    goals = forms.IntegerField(label='Weekly Goal', min_value=1,
                               max_value=250000,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Weekly Goal'
                                   }
                                   )
                               )
    first_name = Target
    user = Target

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['goals'].widget.attrs['autofocus'] = True
        self.fields['goals'].widget.attrs['class'] = 'form-control my-3'
        self.fields['goals'].label = False


class StepsForm(forms.Form):
    """ Creates the steps form for taking users steps """
    steps = forms.IntegerField(label='Steps', min_value=1, max_value=250000,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Log Steps'
                                   }
                                   )
                               )
    first_name = Target
    user = Target

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['steps'].widget.attrs['autofocus'] = True
        self.fields['steps'].widget.attrs['class'] = 'form-control my-3'
        self.fields['steps'].label = False
