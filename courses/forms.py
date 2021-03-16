from django import forms
from django.forms.models import inlineformset_factory

from .models import Course, Module

# Allows you to build a model formset dynamically for the Module objects related to a Course object.
ModuleFormSet = inlineformset_factory(
    parent_model=Course,
    model=Module,
    fields=["title", "description"],
    extra=2,
    can_delete=True,
)
