from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

from datetime import datetime


def index(request):
    fbs = Feedback.objects.all()
    form = FeedbackForm()
    return render(request, 'feedbacks/index.html', {'form': form, 'fbs': fbs})


def f_add(request):
    if request.POST:
        print(datetime.now())
        FeedbackForm(request.POST).save()
        return redirect('/feedback/')
    return redirect('/feedback/')
