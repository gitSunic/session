from django.shortcuts import render, redirect
from .models import Ticket, MathImg
from .forms import TicketForm, MathImgForm


def m_start(request):
    tickets = []
    for t in Ticket.objects.all():
        tickets.append({'id': t.num, 'str': str(t)})
    form = TicketForm()
    return render(request, 'maths/list.html', {'tickets': tickets, 'form': form})


def ticket_view(request, id):
    pages = MathImg.objects.filter(ticket__num=id).order_by('pos')
    form = MathImgForm()
    print(form)
    return render(request, 'maths/watch.html', {'pages': pages, 'form': form, 'id': Ticket.objects.get(num=id).id})


def ticket_add(request):
    if request.POST:
        form = TicketForm(request.POST)
        form.save()
    return redirect('/')


def page_add(request):
    if request.POST:
        print(request.POST)
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

