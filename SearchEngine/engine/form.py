from django import forms


class SearchForm(forms.Form):
    search_field = forms.CharField(lable='Search',blank=True, max_length=100)
