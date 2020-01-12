from django.shortcuts import render, redirect
from maths.views import get_client_ip
from .models import Ticket, PhysImg
from .forms import TicketForm, PhysImgForm

import threading


def p_start(request):
    threading.Thread(target=get_client_ip, args=(request, 'physics')).start()
    tickets = []
    for t in Ticket.objects.all():
        tickets.append({'id': t.num, 'str': str(t)})
    form = TicketForm()
    return render(request, 'physics/list.html', {'tickets': tickets, 'form': form})


def min(request):
    threading.Thread(target=get_client_ip, args=(request, 'physics_min')).start()
    return render(request, 'physics/min.html')


def ticket_view(request, id):
    threading.Thread(target=get_client_ip, args=(request, 'physics_ticket')).start()
    pages = PhysImg.objects.filter(ticket__num=id).order_by('pos')
    form = PhysImgForm()
    return render(request, 'maths/watch.html', {'pages': pages, 'form': form, 'id': Ticket.objects.get(num=id).id})


def ticket_add(request):
    if request.POST:
        form = TicketForm(request.POST)
        form.save()
    return redirect('/physics')


def page_add(request):
    if request.POST:
        form = PhysImgForm(request.POST, request.FILES)
        page = form.save(commit=False)
        pages = PhysImg.objects.filter(ticket__num=page.ticket.num).order_by('pos')
        if page.pos < len(pages):
            for p in pages:
                if p.pos >= page.pos:
                    p.pos = p.pos + 1
                    p.save()
        page.save()
        return redirect('/physics/'+str(page.ticket.num))
    return redirect('/physics/')
