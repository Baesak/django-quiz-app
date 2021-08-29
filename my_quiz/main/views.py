from django.shortcuts import reverse
from .models import Question
from .forms import QuestForm, AnswersForm
from django.views.generic import ListView, CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin

# list for saving randomly generated questions
questions = []


class Quiz(ListView, FormView):

    form_class = AnswersForm
    model = Question
    template_name = 'main/quiz.html'
    context_object_name = 'questions'

    def get_queryset(self):
        global questions
        rand_quests = Question.objects.order_by('?')[:3]
        questions = list(rand_quests)
        return rand_quests

    def get_success_url(self):
        global questions
        correct = 0
        for i in range(3):
            if questions[i].answr == self.request.POST.get('answer' + str(i+1)):
                correct += 1
        return reverse('result', kwargs={'correct': correct})


class NewQuest(SuccessMessageMixin, CreateView):

    form_class = QuestForm
    template_name = 'main/new-quest.html'
    success_url = 'new-quest'
    success_message = 'Question added'
