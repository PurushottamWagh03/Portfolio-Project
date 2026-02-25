from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "tech_stack",
                  "github_link", "live_demo"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "w-full border rounded-lg px-4 py-2 text-black"
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full border rounded-lg px-4 py-2 text-black",
                "rows": 5
            }),
            "tech_stack": forms.TextInput(attrs={
                "class": "w-full border rounded-lg px-4 py-2 text-black"
            }),
            "github_link": forms.URLInput(attrs={
                "class": "w-full border rounded-lg px-4 py-2 text-black"
            }),
            "live_demo": forms.URLInput(attrs={
                "class": "w-full border rounded-lg px-4 py-2 text-black"
            }),
        }