""" Steps form module """
from django import forms


class Goals_form(forms.Form):
    """ Creates the Goal form for taking users weekly step goals """
    goals = forms.IntegerField(label='Weekly Goal', min_value=1, max_value=250000)


class Steps(forms.Form):
    """ Creates the steps form for taking users steps """
    steps = forms.IntegerField(label='Steps', min_value=1, max_value=250000)
