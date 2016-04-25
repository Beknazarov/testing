from django.shortcuts import render, redirect
from .models import *
from questions.models import Question
from .forms import TestForm


def all(request):
    context = {
        "categories": Category.objects.all(),
    }
    return render(request, "tests/test.html", context)


def new(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        test = Test(creator=request.user,
                    title=form.cleaned_data['title'],
                    instruction=form.cleaned_data['instruction'],
                    category=form.cleaned_data['category'])
        test.save()
        return redirect('/test/show/%s/' % test.id)
    return render(request, "tests/add.html", {'form': form})


def show(request, test_id):
    test = Test.objects.get(id=test_id)
    context = {
        'test': test,
        'questions': Question.objects.filter(test = test)
    }
    return render(request, "tests/show.html", context)


def edit(request, test_id):
    instance = Test.objects.get(id=test_id)
    form = TestForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/test/show/%s/' % test_id)
    return render(request, "tests/edit.html", {'form': form, "test": Test.objects.get(id=test_id)})
