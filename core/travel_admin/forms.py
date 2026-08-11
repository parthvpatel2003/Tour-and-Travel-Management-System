from django import forms
from .models import PackageType, PlanManagement, Destination, Role_Master

class PackageTypeForm(forms.ModelForm):
    class Meta:
        model = PackageType
        fields = ['destination','package_type','plan_management']
        widgets = {
            'destination': forms.Select(attrs={'class':'form-select'}),
            'package_type': forms.TextInput(attrs={'class':'form-control'}),
            'plan_management': forms.TextInput(attrs={'class':'form-control'}),
        }

class PlanManagementForm(forms.ModelForm):
    class Meta:
        model = PlanManagement
        fields = ["plan_name","duration","nights_days","status",]
        widgets = {
            "plan_name": forms.TextInput(attrs={"class": "form-control"}),
            "duration": forms.TextInput(attrs={"class": "form-control"}),
            "nights_days": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.TextInput(attrs={"class": "form-control"}),
        }

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['destination', 'description','displaylogo', 'displaybanner']

class Role_MasterForm(forms.ModelForm):
    class Meta:
        model = Role_Master
        fields = ['rolename','description']
        widgets = {
            'rolename': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }