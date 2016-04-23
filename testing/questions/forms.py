from django.forms import ModelForm
from .models import Question, ManyChoiceAnswer, TrueFalseAnswer, CompositionAnswer
from django.forms.models import inlineformset_factory


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = 'text point answer_type'.split()

class TrueFalseAnswerForm(ModelForm):
    class Meta:
        model = TrueFalseAnswer
        fields = 'true false'.split()


class CompositionAnswerForm(ModelForm):
    class Meta:
        model = CompositionAnswer
        fields = 'text'.split()
