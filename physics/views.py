from django.shortcuts import render
from maths.views import get_client_ip

import threading


def p_start(request):
    threading.Thread(target=get_client_ip, args=(request, 'physics')).start()
    return render(request, 'physics/list.html')


def min(request):
    threading.Thread(target=get_client_ip, args=(request, 'physics_min')).start()
    return render(request, 'physics/min.html')


# def ticket_view(request, id):
#     pages = MathImg.objects.filter(ticket__num=id).order_by('pos')
#     for p in pages:
#         print(p.image.url)
#     return render(request, 'maths/watch.html', {'pages': pages})
