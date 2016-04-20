from django.forms import ModelForm
from .models import Test

# Create the form class.
class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = 'title instruction category'.split()
