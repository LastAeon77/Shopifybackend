from django import forms
from .models import Inventory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
import collections


# This is the "form"
class InventoryMakerForm(forms.Form):

    inventory_name = forms.CharField(
        max_length=30, help_text="Please keep characters below 50!"
    )
    inventory_description = forms.CharField(widget=forms.Textarea)
    # Checks validity of inputted data
    def clean(self):
        N = self.cleaned_data.get("inventory_name")
        J = Inventory.objects.filter(name=N)
        if J:
            raise forms.ValidationError("That name is taken!")
        if len(str(N)) > 30:
            raise forms.ValidationError("Your name is too long!")

    # A simple modifier to align the Form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "inventory_name",
            "inventory_description",
            Submit("submit", "Submit", css_class="btn-success"),
        )


# This is the "form" for the edit
class InventoryEditForm(forms.Form):

    inventory_name = forms.CharField(
        max_length=30, help_text="Please keep characters below 30!"
    )
    inventory_description = forms.CharField(widget=forms.Textarea)
    # Checks validity of inputted data
    def clean(self):
        N = self.cleaned_data.get("inventory_name")
        if len(str(N)) > 30:
            raise forms.ValidationError("Your name is too long!")

    # A simple modifier to align the Form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "inventory_name",
            "inventory_description",
            Submit("submit", "Submit", css_class="btn-success"),
        )

