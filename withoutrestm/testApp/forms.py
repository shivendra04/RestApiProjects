from django import forms
from testApp.models import employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        input_sal=self.cleaned_data['esal']
        if input_sal<5000:
            raise forms.ValidationError('The Minimum salary should be 5000.')
        return input_sal

    class Meta:
        model=employee
        fields='__all__'
