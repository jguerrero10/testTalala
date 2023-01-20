from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class OfficerForm(UserCreationForm):
    badge = forms.IntegerField()

    def __init__(self, *arg, **kwargs):
        super(OfficerForm, self).__init__(*arg, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'badge', 'username']


class OfficerUpdateForm(UserChangeForm):
    badge = forms.IntegerField()

    def __init__(self, *arg, **kwargs):
        super(OfficerUpdateForm, self).__init__(*arg, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'badge', 'username']
