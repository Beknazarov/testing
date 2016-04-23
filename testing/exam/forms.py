from django.forms import ModelForm
from .models import Test,Category

# Create the form class.


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = 'title instruction category'.split()


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
