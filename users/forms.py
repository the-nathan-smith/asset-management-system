from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms


class RegisterUserForm(UserCreationForm):
    alphanumericValidator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    email = forms.EmailField()
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'Enter Alphanumeric Characters Only '})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'Enter Alphanumeric Characters Only '})
    )

    # We have two password fields here so that we can
    # get the user to validate that they know their
    # password by typing it in twice and then checking
    # those two values match
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


# We only want the user to be able to edit first_name,
# last_name and email as username is what they use to
# login and would bring added complexity to editting this field
class EditProfileForm(forms.ModelForm):
    alphanumericValidator = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", 'pattern': '[A-Za-z ]+', 'title': 'Enter Alphanumeric Characters Only '}),
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", 'pattern': '[A-Za-z ]+', 'title': 'Enter Alphanumeric Characters Only '}),

    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
