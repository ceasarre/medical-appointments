from .models import Person
from django.forms import ModelForm, RadioSelect, SelectDateWidget

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # view in the form
        widgets = {
        'gender' : RadioSelect(),
        'date_of_appointment': SelectDateWidget(years=range(2020, 2040)),
        'date_of_set_appointment' : SelectDateWidget(years=range(2020, 2040))
        }