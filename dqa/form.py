from django.forms import ModelForm
from django import forms

from dqa.models import DataVerification, Period
from project.models import Facilities


class DataVerificationForm(ModelForm):
    class Meta:
        model = DataVerification
        fields = "__all__"
        exclude = ['created_by', 'quarter_year']

    # This is the constructor method of the form
    def __init__(self, *args, **kwargs):
        # Call the parent constructor method
        super().__init__(*args, **kwargs)
        # Loop through all the fields in the form
        for field in self.fields:
            # Set the label of each field to False
            self.fields[field].label = False




    # def save(self, commit=True):
    #     # Get the instance of the form data but don't commit it yet
    #     instance = super().save(commit=False)
    #
    #     # Get the related DataVerification object, if it exists
    #     data_verification = DataVerification.objects.filter(
    #         quarter_year=instance.quarter_year,
    #         facility_name=instance.facility_name
    #     ).first()
    #
    #     # Check if the related DataVerification object exists and both 'Number tested Positive aged 15+ years' and 'Number tested Positive aged <15 years' are present
    #     if data_verification and data_verification.number_positive_15_plus and data_verification.number_positive_below_15:
    #         # Calculate the 'Number tested Positive _Total' field
    #         instance.number_positive_total = data_verification.number_positive_15_plus + data_verification.number_positive_below_15
    #
    #     # Save the form data
    #     if commit:
    #         instance.save()

class PeriodForm(ModelForm):
    class Meta:
        model = Period
        fields = "__all__"


class QuarterSelectionForm(forms.Form):
    quarter = forms.ChoiceField(
        choices=[
            ('Qtr1', 'Qtr1'),
            ('Qtr2', 'Qtr2'),
            ('Qtr3', 'Qtr3'),
            ('Qtr4', 'Qtr4'),
        ]
    )


class YearSelectionForm(forms.Form):
    YEAR_CHOICES = [(str(x), str(x)) for x in range(2021, 2099)]
    year = forms.ChoiceField(
        choices=YEAR_CHOICES
    )


class FacilitySelectionForm(forms.Form):
    facilities = forms.ModelChoiceField(
        queryset=Facilities.objects.all(),
        empty_label="Select facility",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
