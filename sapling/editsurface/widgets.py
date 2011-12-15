from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class EditSurface(forms.HiddenInput):
    def render(self, name, value, attrs=None, **kwargs):
        rendered = super(EditSurface, self).render(name, value, attrs)
        context = {
            'name': name,
            'value': value,
        }
        return rendered + mark_safe(render_to_string(
            'editsurface/editsurface.html', context
        ))
