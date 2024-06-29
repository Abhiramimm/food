from django import forms

class FoodForm(forms.Form):

    fname=forms.CharField()

    price=forms.IntegerField()

    