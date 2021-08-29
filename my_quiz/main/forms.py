from .models import Question
from django.forms import ModelForm, TextInput, RadioSelect, Form, CharField, ChoiceField


class QuestForm(ModelForm):
    class Meta:
        model = Question
        fields = ["text", "answr"]
        choices = [('True', 'True'), ('False', 'False')]
        widgets = {
            "text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'write your question',
                'id': 'question'
                }),
            "answr": RadioSelect(attrs={
                'id': 'correct_answer',
                'default': 'Unspecified'
            }, choices=choices, )
        }


class AnswersForm(Form):
    choices = [('True', 'True'), ('False', 'False')]
    answer1 = ChoiceField(widget=RadioSelect, choices=choices)
    answer2 = ChoiceField(widget=RadioSelect, choices=choices)
    answer3 = ChoiceField(widget=RadioSelect, choices=choices)


