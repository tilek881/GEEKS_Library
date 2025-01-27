from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    experience = forms.IntegerField(label="Опыт работы (в годах)")

    class Meta:
        model = User
        fields = ("username", "password", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
