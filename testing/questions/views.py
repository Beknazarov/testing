# coding=utf-8
from django.shortcuts import render,redirect, render_to_response
from django.forms.models import inlineformset_factory
from .forms import QuestionForm, TrueFalseAnswerForm, CompositionAnswerForm
from exam.models import Test
from .models import *

# Create your views here.

def new(request, test_id):
    test = Test.objects.get(id = test_id)
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = Question(text = form.cleaned_data['text'],
                        point = form.cleaned_data['point'],
                        answer_type = form.cleaned_data['answer_type'],
                        test = test)
        question.save()
        return redirect('/question/show/%s/' %(question.id))
    return render(request, "questions/new.html", {'form': form, 'test':test})


def show(request, question_id):
    question = Question.objects.get(id=question_id)
    if question.answer_type == 'Many':
        AnswerFormSet = inlineformset_factory(Question,ManyChoiceAnswer, can_delete = True, extra = 1, fields = ('text','right'))
        if request.method == "POST":
            formset = AnswerFormSet(request.POST,request.FILES, instance=question)
            if formset.is_valid():
                formset.save()
            return redirect('/question/show/%s'%question_id)
        else:
            formset = AnswerFormSet(instance = question)
            return render(request,"questions/show.html", {'question':question,'formset':formset})
    elif question.answer_type == 'TrueFalse':
        answer = TrueFalseAnswer.objects.filter(question_id = question_id)[0]
        form = TrueFalseAnswerForm(request.POST or None, instance = answer)
    else:
        answer = CompositionAnswer.objects.filter(question_id = question_id)[0]
        form = CompositionAnswerForm(request.POST or None, instance = answer)
    if form.is_valid():
        form.save()
        return redirect('/question/show/%s/' % question_id)
    return render(request,"questions/show.html", {'question':question,'form':form})


def edit(request, question_id):
    instance = Question.objects.get(id=question_id)
    form = QuestionForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/question/show/%s/' % question_id)
    return render(request, "questions/edit.html", {'form': form, "question": instance})
