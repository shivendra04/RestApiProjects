from django import forms
from testApp.models import student

class StudentForm(forms.ModelForm):
    def clean_esal(self):
        input_marks=self.cleaned_data['marks']
        if input_marks<35:
            raise forms.ValidationError('Marks should be >=35')
        return input_marks

    class Meta:
        model=student
        fields='__all__'
