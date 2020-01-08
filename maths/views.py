from django.shortcuts import render, redirect
from .models import Ticket, MathImg
from .forms import TicketForm, MathImgForm

import datetime
import threading


def get_client_ip(request, name='main'):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if ip != open('myip.txt', 'r').read():
        f = open('history.txt', 'a')
        f.write(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S") + ' - ' + ip + ' - ' + name + '\n')
        f.close()


def m_start(request):
    threading.Thread(target=get_client_ip, args=(request, 'maths')).start()
    tickets = []
    for t in Ticket.objects.all():
        tickets.append({'id': t.num, 'str': str(t)})
    form = TicketForm()
    return render(request, 'maths/list.html', {'tickets': tickets, 'form': form})


def ticket_view(request, id):
    threading.Thread(target=get_client_ip, args=(request, 'maths_ticket')).start()
    pages = MathImg.objects.filter(ticket__num=id).order_by('pos')
    form = MathImgForm()
    return render(request, 'maths/watch.html', {'pages': pages, 'form': form, 'id': Ticket.objects.get(num=id).id})


def ticket_add(request):
    if request.POST:
        form = TicketForm(request.POST)
        form.save()
    return redirect('/')


def page_add(request):
    if request.POST:
        form = MathImgForm(request.POST, request.FILES)
        page = form.save(commit=False)
        pages = MathImg.objects.filter(ticket__num=page.ticket.num).order_by('pos')
        if page.pos < len(pages):
            for p in pages:
                if p.pos >= page.pos:
                    p.pos = p.pos + 1
                    p.save()
        page.save()
        return redirect('/maths/'+str(page.ticket.num))
    return redirect('/maths/')

