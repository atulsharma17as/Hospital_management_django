from base.models import patient
from django import forms

#create Form instead of html Forms.

class PatientForm(forms.Form):
  name=forms.CharField(max_length=100)
  age=forms.IntegerField()
  gender=forms.CharField(max_length=100)
  contact=forms.IntegerField(min_value=0)
  consulting=forms.CharField(max_length=100)

#connect forms and models
class PatientModelForms(forms.ModelForm):
    class Meta:
        model=patient
        fields=['name','age','gender','contact','consulting']
