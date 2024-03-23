from django import forms
from django.forms import ModelForm
from .models import Trip_info,person,trip3,plans,events,expense,locations,User

class GroupForm(ModelForm):
    class Meta:
        model=Trip_info
        fields="__all__"
    def __init__(self, *args, **kwargs):
        
        trips = kwargs.pop('trips', None)
        super().__init__(*args, **kwargs)
        if trips is not None:
            self.fields['trip'].queryset =trip3.objects.filter(pk__in=trips)
class personForm(ModelForm):
    class Meta:
        model=person
        fields="__all__"
class DateInput(forms.DateInput):
    input_type = 'date'
class tripForm(ModelForm):
    place=forms.ModelChoiceField(queryset=locations.objects.all(), to_field_name='location')
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
        fields=['trip_id','id_plan','owner','description']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get the username instance (assuming it's pre-populated)
        if 'initial' in kwargs and 'owner' in kwargs['initial']:
            username_instance = kwargs['initial']['owner']
        else:
            # Handle the case where initial value is not provided
            username_instance = None  # Or set a default username instance

        # Make the username field read-only
        self.fields['owner'].widget = forms.widgets.Select(choices=[(username_instance.pk, str(username_instance))])
        self.fields['owner'].disabled = True  # D
        if 'initial' in kwargs and 'trip' in kwargs['initial']:
            username_instance = kwargs['initial']['trip']
        else:
            # Handle the case where initial value is not provided
            username_instance = None  # Or set a default username instance

        # Make the username field read-only
        self.fields['trip_id'].widget = forms.widgets.Select(choices=[(username_instance.pk, str(username_instance))])
        self.fields['trip_id'].disabled = True  # D
    
class EventsForm(ModelForm):
    class Meta:
        model=events
        fields="__all__"
        widgets = {
            'date': DateInput(),
        
        }
    def __init__(self, *args, **kwargs):
        
      
        super().__init__(*args, **kwargs)
 
        # Get the username instance (assuming it's pre-populated)
        if 'initial' in kwargs and 'owner' in kwargs['initial']:
            username_instance = kwargs['initial']['owner']
        else:
            # Handle the case where initial value is not provided
            username_instance = None  # Or set a default username instance

        # Make the username field read-only
        self.fields['owner'].widget = forms.widgets.Select(choices=[(username_instance.pk, str(username_instance))])
        self.fields['owner'].disabled = True
class ExpenseForm(ModelForm):
    class Meta:
        model=expense
        fields="__all__"
    def __init__(self, *args, **kwargs):
        users = kwargs.pop('users', None)
        
      
        super().__init__(*args, **kwargs)
        if users is not None:
            self.fields['user'].queryset =Trip_info.objects.filter(pk__in=users)
 
        # Get the username instance (assuming it's pre-populated)
        if 'initial' in kwargs and 'trip' in kwargs['initial']:
            username_instance = kwargs['initial']['trip']
        else:
            # Handle the case where initial value is not provided
            username_instance = None  # Or set a default username instance

        # Make the username field read-only
        self.fields['trip_id1'].widget = forms.widgets.Select(choices=[(username_instance.pk, str(username_instance))])
        self.fields['trip_id1'].disabled = True



