from app.models import Contact
from django import forms

class contactForm(forms.ModelForm):
    class Meta:
        model=Contact  # connect to model
        fields=['first_name','Last_name','email','contect'] # That line tells Django:

#“When you create the form, include only these fields from the model — first_name,last_name,email,content.”