from django import forms
from django.forms import ModelForm
from .models import Trip_info,person,trip3,plans,events,expense

class GroupForm(ModelForm):
    class Meta:
        model=Trip_info
        fields="__all__"
class personForm(ModelForm):
    class Meta:
        model=person
        fields="__all__"
class DateInput(forms.DateInput):
    input_type = 'date'
class tripForm(ModelForm):
    class Meta:
        model=trip3
        fields="__all__"
        widgets = {
            'start_date1': DateInput(),
            'end_date1': DateInput()
        }
class planForm(ModelForm):
    class Meta:
        model=plans
        fields="__all__"
    
class EventsForm(ModelForm):
    class Meta:
        model=events
        fields="__all__"
        widgets = {
            'date': DateInput(),
        
        }
class ExpenseForm(ModelForm):
    class Meta:
        model=expense
        fields="__all__"


