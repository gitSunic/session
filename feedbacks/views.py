from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

from maths.views import get_client_ip

from datetime import datetime
import threading


def index(request):
    fbs = Feedback.objects.all()
    form = FeedbackForm()
    return render(request, 'feedbacks/index.html', {'form': form, 'fbs': fbs})


def f_add(request):
    threading.Thread(target=get_client_ip, args=(request, 'new feedback')).start()
    if request.POST:
        print(datetime.now())
        FeedbackForm(request.POST).save()
        return redirect('/feedback/')
    return redirect('/feedback/')
