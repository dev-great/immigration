from django import forms
from .models import I90Application


class I90ApplicationForm(forms.ModelForm):
    class Meta:
        model = I90Application
        fields = '__all__'
        widgets = {
            'date_of_signature': forms.SelectDateWidget,
            'date_of_admission': forms.SelectDateWidget,
            'dob': forms.SelectDateWidget,
            'interpreter_date_of_signature': forms.SelectDateWidget,
        }

    # Override __init__ to add custom widgets or initial values if needed
    def __init__(self, *args, **kwargs):
        super(I90ApplicationForm, self).__init__(*args, **kwargs)

        # Example: Adding custom classes to fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
