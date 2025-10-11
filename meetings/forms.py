from django.forms import DateInput, ModelForm, TextInput, TimeInput

from meetings.models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start_time': TimeInput(attrs={"type": "time"}),  
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "4"})
        }