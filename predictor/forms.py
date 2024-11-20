# forms.py
from django import forms
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class LaptopPricePredictionForm(forms.Form):
    brand_choices = [
        ('Apple', 'Apple'),
        ('Dell', 'Dell'),
        ('HP', 'HP'),
        ('Lenovo', 'Lenovo'),
        ('Asus', 'Asus'),
        ('Acer', 'Acer'),
        ('MSI', 'MSI'),
        ('Razer', 'Razer'),
        ('Microsoft', 'Microsoft'),
        ('Samsung', 'Samsung'),
    ]

    model_choices = [
        ('MacBook', 'MacBook'),
        ('XPS', 'XPS'),
        ('Pavilion', 'Pavilion'),
        ('ThinkPad', 'ThinkPad'),
        ('ZenBook', 'ZenBook'),
        ('Predator', 'Predator'),
        ('Razer Blade', 'Razer Blade'),
        ('Surface', 'Surface'),
        ('Galaxy Book', 'Galaxy Book'),
    ]

    defect_choices = [
        ('None', 'None'),
        ('Minor Scratches', 'Minor Scratches'),
        ('Damaged Screen', 'Damaged Screen'),
        ('Broken Keyboard', 'Broken Keyboard'),
        ('Battery Issue', 'Battery Issue'),
    ]

    brand = forms.ChoiceField(choices=brand_choices)
    model = forms.ChoiceField(choices=model_choices)
    purchase_price = forms.DecimalField(decimal_places=2, max_digits=10)
    years_used = forms.IntegerField(min_value=0)
    condition = forms.ChoiceField(choices=[('New', 'New'), ('Good', 'Good'), ('Fair', 'Fair'), ('Poor', 'Poor')])
    defects = forms.ChoiceField(choices=defect_choices)
