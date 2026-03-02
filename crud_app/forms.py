from django import forms
from .models import Student
import re

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Standard'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '100', 'placeholder': 'Percentage'}),
        }

    # Custom validation for percentage
    def clean_percentage(self):
        percentage = self.cleaned_data.get('percentage')
        if percentage is None:
            raise forms.ValidationError("Percentage is required.")
        if percentage < 0 or percentage > 100:
            raise forms.ValidationError("Percentage must be between 0.00 and 100.00.")
        # Optional: round to 2 decimal places
        return round(percentage, 2)
    
    # Mobile number validation
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile:
            raise forms.ValidationError("Mobile number is required.")
        # Remove spaces or dashes
        mobile_digits = re.sub(r'\D', '', mobile)
        if len(mobile_digits) != 10:
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        if not mobile_digits.isdigit():
            raise forms.ValidationError("Mobile number must contain only digits.")
        return mobile_digits