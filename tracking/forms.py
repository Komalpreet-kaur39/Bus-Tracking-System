from django import forms
from .models import Bus, Driver, Route
import json
# class BusForm(forms.ModelForm):
#     class Meta:
#         model = Bus
#         fields = ['bus_number', 'capacity', 'driver', 'route']

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_number', 'capacity', 'route', 'driver']
        widgets = {
            'bus_number': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'route': forms.Select(attrs={'class': 'form-select'}),
            'driver': forms.Select(attrs={'class': 'form-select'}),
        }


# class RouteForm(forms.ModelForm):
#     stops = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), help_text="Comma-separated stops")
#     timings = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), help_text="Comma-separated timings")

#     class Meta:
#         model = Route
#         fields = ['name', 'stops', 'timings']

#     def clean_stops(self):
#         return [s.strip() for s in self.cleaned_data['stops'].split(',')]

#     def clean_timings(self):
#         return [t.strip() for t in self.cleaned_data['timings'].split(',')]


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'stops', 'timings']

    def clean_stops(self):
        """Ensure stops is a list, not a comma-separated string"""
        stops = self.cleaned_data.get('stops')
        if not isinstance(stops, list):
            raise forms.ValidationError("Invalid format for stops.")
        return stops

    def clean_timings(self):
        """Ensure timings is a list, not a comma-separated string"""
        timings = self.cleaned_data.get('timings')
        if not isinstance(timings, list):
            raise forms.ValidationError("Invalid format for timings.")
        return timings



class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'contact_number']
# class RouteForm(forms.ModelForm):
#     class Meta:
#         model = Route
#         fields = ['name', 'stops', 'timings']

