# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import *
from .forms import PupilForm

PAGES_COUNT = 5
TESTS_COUNT = 4

def index(request):
    return render(request, 'transformators/index.html')

def about(request):
    return render(request, 'transformators/about.html')
	
def help(request):
    return render(request, 'transformators/help.html')

def pages(request):
    return render(request, 'transformators/pages.html')


def tests(request):
    return render(request, 'transformators/tests.html')


def page(request, page_number):
    if int(page_number) <= PAGES_COUNT:
        return render(request, 'transformators/theory{}.html'.format(page_number))
    else:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')


def autoriz(request, test_number):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST['test_number'] = test_number
        form = PupilForm(request.POST)

        if form.is_valid():
            pupil = form.save()
            if int(test_number) <= TESTS_COUNT:
                return HttpResponseRedirect(
                    '/test/{}/{}/'.format(test_number, pupil.pk)
                )
            else:
                return HttpResponseNotFound('<h1>404 Not Found</h1>')
        else:
            print form.errors

    if int(test_number) <= TESTS_COUNT:
        return render(request, 'transformators/autoriz.html')
    else:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')


def test(request, test_number, pupil_id):
    part = int(test_number)
    questions = Question.objects.filter(part=part)
    all_questions = questions.count()
    accept_answers = 0
 
    result = Pupil.objects.get(pk=int(pupil_id))
 
    if request.method == 'POST':
        POST = request.POST
        for counter, question in enumerate(questions):
            self_answers = Answer.objects.filter(question=question)
            is_all_correct = True
            for answer in self_answers:
                if POST['{}{}'.format(question.pk, answer.pk)] != answer.answer:
                    is_all_correct = False
            if is_all_correct:
                accept_answers += 1
            else:
                result.wrong_answers += '{}'.format(counter + 1) + '; '
 
        result.mark = int(round((10 * accept_answers) / all_questions))
        result.save()
 
        return HttpResponseRedirect('/result/{}/{}/'.format(test_number, pupil_id))
 
    if part <= TESTS_COUNT:
        context = {
            'questions': questions,
            'answers': Answer.objects.all()
        }
        return render(request, 'transformators/practies.html'.format(test_number), context)
    else:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')


def result(request, test_number, pupil_id):
    context = {
        'results': Pupil.objects.filter(test_number=int(test_number)).order_by('-mark', '-date'),
        'cur_result': get_object_or_404(Pupil, id=int(pupil_id))
    }

    return render(request, 'transformators/result.html', context)
